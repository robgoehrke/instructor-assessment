import streamlit as st
import math
import tempfile
import time
from fpdf import FPDF
from questions import QUESTIONS # <--- This pulls your list from the other file!

# --- 1. IRT Probability & Estimation Models (Book-Scaled) ---
def irt_probability(theta, b):
    try:
        return 1.0 / (1.0 + math.exp(-(theta - b)))
    except OverflowError:
        return 0.0 if (theta - b) < 0 else 1.0

def estimate_ability(administered_b, responses, prior_mean):
    best_theta = prior_mean 
    max_ll = -float('inf')
    
    for t in range(0, 81):
        theta = t / 10.0
        ll = 0
        for b, r in zip(administered_b, responses):
            p = irt_probability(theta, b)
            p = max(min(p, 1.0 - 1e-10), 1e-10) 
            ll += r * math.log(p) + (1 - r) * math.log(1 - p)
            
        prior = -0.5 * ((theta - prior_mean)**2)
        ll += prior
        
        if ll > max_ll:
            max_ll = ll
            best_theta = theta
            
    return best_theta

# --- 2. PDF Generation Function ---
def create_pdf(name, location, instrument, rec, score, q_count):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Instructor Assessment Results", ln=True, align="C")
    pdf.ln(10)
    
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Candidate Name: {name}", ln=True)
    pdf.cell(0, 10, f"Interviewing at: School of Rock {location}", ln=True)
    pdf.cell(0, 10, f"Instrument: {instrument}", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, f"Recommended Level: {rec}", ln=True)
    
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Estimated Score: {score:.2f}", ln=True)
    pdf.cell(0, 10, f"Total Questions Answered: {q_count}", ln=True)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        pdf.output(tmp.name)
        with open(tmp.name, "rb") as f:
            return f.read()

# --- 3. Web Interface UI ---
st.set_page_config(page_title="Instructor Assessment", page_icon="🎸")
st.title("Instructor Assessment")

if 'step' not in st.session_state:
    st.session_state.step = 'candidate_info'
    st.session_state.initial_theta = 4.0 
    st.session_state.theta = 4.0 
    st.session_state.admin_b = []
    st.session_state.responses = []
    st.session_state.pool = []
    st.session_state.asked_questions = []
    st.session_state.phase = 'adaptive'
    st.session_state.verification_queue = []
    st.session_state.q_count = 0
    st.session_state.show_feedback = False 
    st.session_state.pending_choice = None
    st.session_state.question_start_time = 0
    st.session_state.time_taken = 0
    st.session_state.timed_out = False

# Screen 1: Candidate Info
if st.session_state.step == 'candidate_info':
    st.write("Please enter your information to begin the assessment.")
    co_locations = ["Aurora", "Boulder", "Broomfield", "Centennial", "Colorado Springs", "Denver", "Littleton", "Longmont"]
    name = st.text_input("Full Name")
    location = st.selectbox("Which School of Rock are you interviewing with?", co_locations)
    
    if st.button("Continue", use_container_width=True):
        if name:
            st.session_state.candidate_name = name
            st.session_state.location = location
            st.session_state.step = 'choose_instrument'
            st.rerun()
        else:
            st.error("Please enter your name.")

# Screen 2: Choose Instrument & Self-Assessment
elif st.session_state.step == 'choose_instrument':
    st.write(f"Hi {st.session_state.candidate_name}! Let's set up your assessment.")
    
    instruments = sorted(list(set(q["inst"] for q in QUESTIONS)))
    selected_inst = st.selectbox("Which instrument are you assessing?", instruments)
    
    st.write("---")
    st.write("**Self-Assessment**")
    self_estimate = st.slider(
        "On a scale of 1 to 6, how would you rate your teaching ability on this instrument? (1 = Beginner, 6 = Advanced)", 
        min_value=1, max_value=6, value=4
    )
    
    if st.button("Start Assessment", use_container_width=True):
        st.session_state.instrument = selected_inst
        st.session_state.initial_theta = float(self_estimate)
        st.session_state.theta = float(self_estimate)
        st.session_state.pool = [q for q in QUESTIONS if q['inst'] == selected_inst]
        st.session_state.step = 'testing'
        st.session_state.question_start_time = time.time()
        st.rerun()

# Screen 3: Three-Phase Testing with Timer & Feedback
elif st.session_state.step == 'testing':
    
    if not st.session_state.show_feedback:
        if st.session_state.phase == 'adaptive' and (st.session_state.q_count >= 7 or not st.session_state.pool):
            st.session_state.phase = 'verification_target'
            
            theta = st.session_state.theta
            if theta < 2.5: target_diff = 2.0
            elif theta < 3.5: target_diff = 3.0
            elif theta < 4.5: target_diff = 4.0
            elif theta < 5.5: target_diff = 5.0
            else: target_diff = 6.0
            
            st.session_state.target_diff = target_diff
            
            asked_texts = [q['q'] for q in st.session_state.asked_questions]
            target_qs = [q for q in QUESTIONS if q['inst'] == st.session_state.instrument and q['diff'] == target_diff]
            
            st.session_state.verification_queue = [q for q in target_qs if q['q'] not in asked_texts]

        if st.session_state.phase == 'verification_target' and not st.session_state.verification_queue:
            st.session_state.phase = 'verification_prior'
            target_diff = st.session_state.target_diff
            second_diff = target_diff - 1.0
            
            queue = []
            if second_diff >= 2.0:
                asked_texts = [q['q'] for q in st.session_state.asked_questions]
                second_qs = [q for q in QUESTIONS if q['inst'] == st.session_state.instrument and q['diff'] == second_diff]
                
                target_correct = sum(r for q, r in zip(st.session_state.asked_questions, st.session_state.responses) if q['diff'] == target_diff)
                target_total = sum(1 for q in st.session_state.asked_questions if q['diff'] == target_diff)
                asked_second_count = sum(1 for q in st.session_state.asked_questions if q['diff'] == second_diff)
                
                if target_total > 0 and (target_correct / target_total) < 0.8:
                    needed = len(second_qs) - asked_second_count
                else:
                    needed = 3 - asked_second_count
                    
                if needed > 0:
                    unasked_second = [q for q in second_qs if q['q'] not in asked_texts]
                    queue.extend(unasked_second[:needed])
                    
            st.session_state.verification_queue = queue

        if st.session_state.phase == 'verification_prior' and not st.session_state.verification_queue:
            st.session_state.step = 'results'
            st.rerun()
            st.stop()
            
    if st.session_state.phase == 'adaptive':
        current_q = min(st.session_state.pool, key=lambda x: abs(x['diff'] - st.session_state.theta))
        status_text = f"Assessment Phase - Question {st.session_state.q_count + 1}"
    else: 
        current_q = st.session_state.verification_queue[0]
        status_text = f"Verification Phase - {len(st.session_state.verification_queue)} left"
        
    st.subheader(status_text)
    
    if not st.session_state.show_feedback:
        
        st.markdown("""
        <style>
        .timer-progress {
            height: 8px; border-radius: 4px;
            animation: countdown 20s linear forwards;
        }
        @keyframes countdown {
            0% { width: 100%; background-color: #28a745; }
            50% { width: 50%; background-color: #ffc107; }
            80% { background-color: #dc3545; }
            100% { width: 0%; background-color: #dc3545; }
        }
        </style>
        <div style="width: 100%; height: 8px; background-color: #ddd; border-radius: 4px; margin-bottom: 20px;">
            <div class="timer-progress"></div>
        </div>
        <p style="font-size: 0.8em; color: gray; margin-top: -15px;">20 seconds to answer (faster = higher score)</p>
        """, unsafe_allow_html=True)
        
        st.write(f"**(Level {int(current_q['diff'])})** {current_q['q']}")
        display_options = current_q['opts'] + ["I don't know"]
        
        for idx, opt in enumerate(display_options):
            if st.button(opt, use_container_width=True):
                time_taken = time.time() - st.session_state.question_start_time
                
                if time_taken > 20:
                    is_correct = 0.0
                    st.session_state.timed_out = True
                else:
                    st.session_state.timed_out = False
                    if idx == current_q['ans']:
                        if time_taken <= 5:
                            is_correct = 1.0
                        else:
                            is_correct = 1.0 - 0.5 * ((time_taken - 5) / 15)
                    else:
                        is_correct = 0.0
                
                st.session_state.pending_b = current_q['diff']
                st.session_state.pending_r = is_correct
                st.session_state.pending_q = current_q
                st.session_state.pending_choice = opt
                st.session_state.correct_text = current_q['opts'][current_q['ans']]
                st.session_state.time_taken = time_taken
                
                st.session_state.show_feedback = True
                st.rerun()
                
    else:
        st.write(current_q['q'])
        
        if st.session_state.timed_out:
            st.error(f"**⏰ Out of Time!** You took longer than 20 seconds. This counts as an incorrect answer.")
            st.info(f"The correct answer was: **{st.session_state.correct_text}**")
        elif st.session_state.pending_r > 0:
            credit_pct = int(st.session_state.pending_r * 100)
            seconds = int(st.session_state.time_taken)
            st.success(f"**Correct!** That was a Level {int(current_q['diff'])} question.")
            if credit_pct == 100:
                st.info(f"⏱️ Lightning fast! You answered in {seconds} seconds and earned **100% credit**.")
            else:
                st.warning(f"⏱️ You answered in {seconds} seconds, earning **{credit_pct}% credit**.")
        elif st.session_state.pending_choice == "I don't know":
            st.warning(f"**No worries.** That was a Level {int(current_q['diff'])} question.")
            st.info(f"For your knowledge, the correct answer is: **{st.session_state.correct_text}**")
        else:
            st.error(f"**Incorrect.** That was a Level {int(current_q['diff'])} question.")
            st.info(f"The correct answer was: **{st.session_state.correct_text}**")
            
        if st.button("Next Question", use_container_width=True):
            st.session_state.admin_b.append(st.session_state.pending_b)
            st.session_state.responses.append(st.session_state.pending_r)
            st.session_state.asked_questions.append(st.session_state.pending_q)
            
            st.session_state.theta = estimate_ability(
                st.session_state.admin_b, 
                st.session_state.responses,
                st.session_state.initial_theta
            )
            
            if st.session_state.phase == 'adaptive':
                st.session_state.pool.remove(st.session_state.pending_q)
            else:
                st.session_state.verification_queue.pop(0)
                
            st.session_state.q_count += 1
            st.session_state.show_feedback = False 
            st.session_state.question_start_time = time.time()
            st.rerun()

# Screen 4: Results & PDF Download
elif st.session_state.step == 'results':
    st.header("Assessment Complete!")
    theta = st.session_state.theta
    
    if theta < 2.5: rec = "Book 2 (or below)"
    elif theta < 3.5: rec = "Book 3"
    elif theta < 4.5: rec = "Book 4"
    elif theta < 5.5: rec = "Book 5"
    else: rec = "Book 6"
    
    st.success(f"**Recommended Level:** {rec}")
    st.write(f"Total Questions Answered: {st.session_state.q_count}")
    st.write("Please download your official results below and send the PDF to your recruiter to complete your application.")
    
    pdf_bytes = create_pdf(
        st.session_state.candidate_name, 
        st.session_state.location, 
        st.session_state.instrument, 
        rec, 
        theta, 
        st.session_state.q_count
    )
    
    st.download_button(
        label="📄 Download Results as PDF",
        data=pdf_bytes,
        file_name=f"{st.session_state.candidate_name}_Assessment_{st.session_state.instrument}.pdf",
        mime="application/pdf",
        use_container_width=True
    )
    
    st.write("---")
    if st.button("Assess Another Instrument", use_container_width=True):
        name_memory = st.session_state.candidate_name
        loc_memory = st.session_state.location
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.session_state.candidate_name = name_memory
        st.session_state.location = loc_memory
        st.session_state.step = 'choose_instrument'
        st.rerun()
