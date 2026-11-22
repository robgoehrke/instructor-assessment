import streamlit as st
import streamlit.components.v1 as components
import time
import re
import requests
import threading
import uuid
from datetime import datetime
from fpdf import FPDF
from questions import QUESTIONS
from locations import LOCATIONS

# Ensure a stable session ID per user attempt
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())[:8]

# --- 1. Cached Data & Text Helpers ---
@st.cache_data
def get_available_instruments():
    return sorted(list(set(q["inst"] for q in QUESTIONS)))

def highlight_keywords(text):
    """Bolds key music theory terms and musical symbols for rapid visual scannability."""
    patterns = [
        r'\b(major|minor|diminished|augmented|dominant|pentatonic|blues|chromatic|modal|modes|ionian|dorian|phrygian|lydian|mixolydian|aeolian|locrian)\b',
        r'\b(triad|triads|chord|chords|progression|interval|intervals|scale|scales|arpeggio|arpeggios|octave|octaves|unison|root|inversion|inversions)\b',
        r'\b(sharp|sharps|flat|flats|natural|key signature|tempo|rhythm|time signature|syncopation|triplet|triplets|staccato|legato|vibrato|melisma|clave|onset)\b',
        r'\b(perfect fifth|perfect fourth|major third|minor third|major seventh|minor seventh|tritone|half step|whole step|semitone|tone)\b',
        r'\b([A-G][#b♯♭]?(?:maj|min|m|dim|aug|sus|add)?[0-9]?)\b'
    ]
    for pat in patterns:
        text = re.sub(pat, r'**\1**', text, flags=re.IGNORECASE)
    # Clean up any accidental double-bolding
    text = text.replace('****', '**')
    return text

# --- 2. Branded PDF Generation Function ---
def create_pdf(name, location, instrument, rec, score, q_count, asked_qs, responses, choices):
    def clean_text(text):
        if not isinstance(text, str):
            text = str(text)
        replacements = {
            '\u00be': '3/4', '\u00bd': '1/2', '\u00bc': '1/4',
            '\u215e': '7/8', '\u215b': '1/8', '\u215c': '3/8', '\u215d': '5/8',
            '\u2153': '1/3', '\u2154': '2/3',
            '\u266d': 'b', '\u266f': '#', '♭': 'b', '♯': '#',
            '\u2018': "'", '\u2019': "'", '\u201c': '"', '\u201d': '"',
            '`': "'",
            '\u2013': '-', '\u2014': '-', '\u2026': '...'
        }
        for k, v in replacements.items():
            text = text.replace(k, v)
        return text.encode('latin-1', 'replace').decode('latin-1')

    pdf = FPDF()
    pdf.add_page()
    
    # --- HEADER ---
    pdf.set_fill_color(0, 0, 0)
    pdf.rect(0, 0, 210, 40, 'F')
    
    pdf.set_y(12)
    pdf.set_font("Arial", 'B', 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, "SCHOOL OF ROCK", ln=True, align="C")
    
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(220, 20, 60)
    pdf.cell(0, 10, "INSTRUCTOR ASSESSMENT RESULTS", ln=True, align="C")
    
    # --- CANDIDATE DETAILS ---
    pdf.set_y(55)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "CANDIDATE DETAILS", ln=True)
    
    pdf.set_draw_color(220, 20, 60)
    pdf.set_line_width(1)
    pdf.line(10, 65, 200, 65)
    pdf.ln(5)
    
    pdf.set_font("Arial", '', 12)
    pdf.cell(40, 8, "Name:", 0, 0)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, clean_text(name), 0, 1)
    
    pdf.set_font("Arial", '', 12)
    pdf.cell(40, 8, "Location:", 0, 0)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, clean_text(f"School of Rock - {location}"), 0, 1)
    
    pdf.set_font("Arial", '', 12)
    pdf.cell(40, 8, "Instrument:", 0, 0)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, clean_text(instrument), 0, 1)
    
    date_str = datetime.now().strftime("%B %d, %Y")
    pdf.set_font("Arial", '', 12)
    pdf.cell(40, 8, "Date:", 0, 0)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, date_str, 0, 1)
    
    pdf.ln(15)
    
    # --- SUMMARY RESULTS ---
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "OFFICIAL RESULTS", ln=True)
    y_line = pdf.get_y()
    pdf.line(10, y_line, 200, y_line)
    pdf.ln(5)
    
    pdf.set_fill_color(245, 245, 245)
    pdf.rect(10, pdf.get_y(), 190, 20, 'F')
    
    pdf.set_y(pdf.get_y() + 5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(75, 10, "RECOMMENDED LEVEL:", 0, 0)
    pdf.set_text_color(220, 20, 60)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, clean_text(f" {rec}"), 0, 1)
    
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)
    
    pdf.set_font("Arial", '', 12)
    pdf.cell(50, 8, "Highest Level Passed:", 0, 0)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, f"{score:.0f}" if score >= 2 else "None", 0, 1)
    
    pdf.set_font("Arial", '', 12)
    pdf.cell(50, 8, "Questions Answered:", 0, 0)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, str(q_count), 0, 1)

    # --- DETAILED QUESTION LOG ---
    pdf.add_page()
    pdf.set_fill_color(0, 0, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, " DETAILED QUESTION LOG", ln=True, fill=True)
    pdf.ln(5)
    
    pdf.set_text_color(0, 0, 0)
    for i, (q, r, choice) in enumerate(zip(asked_qs, responses, choices)):
        correct_ans_text = q['opts'][q['ans']]
        
        if r > 0:
            status = "Correct"
        else:
            status = "Incorrect"
            
        pdf.set_font("Arial", 'B', 11)
        pdf.multi_cell(0, 6, clean_text(f"Q{i+1} (Level {int(q['diff'])}): {q['q']}"))
        
        pdf.set_font("Arial", '', 10)
        pdf.multi_cell(0, 6, clean_text(f"Candidate Answer: {choice}"))
        pdf.multi_cell(0, 6, clean_text(f"Correct Answer: {correct_ans_text}"))
        
        if r > 0:
            pdf.set_text_color(34, 139, 34)
        else:
            pdf.set_text_color(220, 20, 60)
            
        pdf.cell(0, 6, f"Result: {status}", ln=True)
        
        pdf.set_text_color(0, 0, 0)
        pdf.set_draw_color(200, 200, 200)
        pdf.set_line_width(0.5)
        pdf.line(10, pdf.get_y() + 2, 200, pdf.get_y() + 2)
        pdf.ln(6)
    
    # --- FOOTER ---
    pdf.ln(10)
    pdf.set_font("Arial", 'I', 10)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 10, "Generated securely by the Instructor Assessment System.", align="C")
    
    pdf_output = pdf.output(dest='S')
    if isinstance(pdf_output, str):
        return pdf_output.encode('latin-1')
    return bytes(pdf_output)

# --- 3. Web Interface UI Configuration & ADHD-Friendly Styling ---
st.set_page_config(page_title="Instructor Assessment", page_icon="🎸")

st.markdown(
    """<style>
/* Anti-cheating: disable text selection and copying */
div[data-testid="stAppViewContainer"] {
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}

/* Generous spacing, larger readable text, and clean click targets for option buttons */
div.stButton > button {
    padding: 0.85rem 1.2rem !important;
    margin-bottom: 0.45rem !important;
    border-radius: 10px !important;
    font-size: 1.08rem !important;
    line-height: 1.45 !important;
    transition: transform 0.08s ease, box-shadow 0.12s ease;
}
div.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
}

/* Visual Level Stepper Banner */
.stepper-container {
    display: flex;
    justify-content: space-between;
    gap: 6px;
    margin: 10px 0 20px 0;
}
.step-pill {
    flex: 1;
    text-align: center;
    padding: 8px 4px;
    border-radius: 8px;
    font-size: 0.85rem;
    font-weight: 600;
    background-color: #f0f2f6;
    color: #6c757d;
    border: 1px solid #dee2e6;
}
.step-pill.done {
    background-color: #d4edda;
    color: #155724;
    border-color: #c3e6cb;
}
.step-pill.active {
    background-color: #dc143c;
    color: #ffffff;
    border-color: #b01030;
    box-shadow: 0 2px 6px rgba(220,20,60,0.25);
}

/* Clean Instruction Callout Cards */
.info-card {
    background-color: #f8f9fa;
    border-left: 4px solid #dc143c;
    padding: 12px 16px;
    border-radius: 6px;
    margin-bottom: 10px;
}
.info-card-title {
    font-weight: 700;
    font-size: 1.05rem;
    margin-bottom: 4px;
    color: #111111 !important;
}
.info-card-body {
    font-size: 0.95rem;
    color: #222222 !important;
}
</style>""",
    unsafe_allow_html=True,
)

st.title("Instructor Assessment")

# Initialize Session State
if 'step' not in st.session_state:
    st.session_state.step = 'candidate_info'
    st.session_state.current_level = 2.0
    st.session_state.level_questions = []
    st.session_state.level_index = 0
    st.session_state.level_score = 0.0
    st.session_state.level_attempts = 0
    st.session_state.highest_passed_level = None
    st.session_state.hide_timer = False
    
    st.session_state.asked_questions = []
    st.session_state.responses = []
    st.session_state.user_choices = []
    st.session_state.q_count = 0
    
    st.session_state.show_feedback = False 
    st.session_state.pending_choice = None
    st.session_state.question_start_time = 0
    st.session_state.time_taken = 0
    st.session_state.timed_out = False

WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbwZ1HRRtZhpSdBvBBnt6Lg_2zthN2hMhku0BasBBn2t9a6KejVPefdYB_fkSMNkTFySlw/exec"

def send_audit_log(status_text):
    audit_data = {
        "session_id": st.session_state.session_id,
        "name": st.session_state.candidate_name,
        "location": st.session_state.location,
        "instrument": st.session_state.instrument,
        "questions_seen": st.session_state.q_count,
        "status": status_text
    }
    def ping_google(url, data):
        try:
            requests.post(url, json=data, timeout=3)
        except:
            pass
    threading.Thread(target=ping_google, args=(WEBHOOK_URL, audit_data)).start()

# Screen 1: Candidate Info
if st.session_state.step == 'candidate_info':
    st.write("Enter your details below to get started.")
    name = st.text_input("Full Name")
    
    location = st.selectbox(
        "Which School of Rock are you interviewing with?", 
        LOCATIONS,
        index=None,
        placeholder="Type state (e.g. 'CO') or city to search..."
    )
    
    if st.button("Continue", type="primary", use_container_width=True):
        if name and location:
            st.session_state.candidate_name = name
            st.session_state.location = location
            st.session_state.step = 'choose_instrument'
            st.rerun()
        else:
            st.error("Please enter your name and select a location.")
            
# Screen 2: Choose Instrument
elif st.session_state.step == 'choose_instrument':
    st.write(f"Hi **{st.session_state.candidate_name}**! Select the instrument you are interviewing to teach.")
    
    instruments = get_available_instruments()
    
    selected_inst = st.selectbox(
        "Instrument", 
        instruments,
        index=None,
        placeholder="Start typing to search..."
    )
    
    if st.button("Continue to Quick Briefing", type="primary", use_container_width=True):
        if selected_inst:
            st.session_state.instrument = selected_inst
            st.session_state.current_level = 2.0
            
            st.session_state.level_questions = [
                q for q in QUESTIONS 
                if q['inst'] == selected_inst and q['diff'] == 2.0
            ]
            st.session_state.level_index = 0
            st.session_state.level_score = 0.0
            st.session_state.level_attempts = 0
            
            st.session_state.step = 'instructions'
            st.rerun()
        else:
            st.error("Please select an instrument to continue.")

# Screen 2.5: Chunked Instructions & Focus Preferences
elif st.session_state.step == 'instructions':
    st.header("Quick Briefing")
    
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🪜 Step-by-Step Levels</div>
        <div class="info-card-body">Everyone starts at <b>Book 2</b> (5 questions). Score <b>80% or higher</b> to unlock the next book level, with a breather screen between every tier.</div>
    </div>
    <div class="info-card">
        <div class="info-card-title">⏱️ 30-Second Pacing</div>
        <div class="info-card-body">You have <b>30 seconds</b> per question. Select <b>"I don't know"</b> anytime to skip without waiting.</div>
    </div>
    <div class="info-card">
        <div class="info-card-title">🔒 Focus & Integrity</div>
        <div class="info-card-body">Copy/paste is disabled. Avoid refreshing or closing this tab while active so your session stays intact.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.session_state.hide_timer = st.toggle(
        "🧘 Hide visual countdown bar (shows only a 10-second heads-up before time expires)",
        value=st.session_state.hide_timer
    )
    
    st.write("")
    if st.button("Start Book 2", type="primary", use_container_width=True):
        st.session_state.step = 'testing'
        st.session_state.question_start_time = time.time()
        send_audit_log("Started / In Progress")
        st.rerun()

# Screen 3.5: Sensory Reset / Level-Up Breather Screen
elif st.session_state.step == 'level_break':
    completed_lvl = int(st.session_state.highest_passed_level)
    next_lvl = int(st.session_state.current_level)
    
    st.success(f"🎉 **Book {completed_lvl} Mastered!** You hit the 80%+ benchmark.")
    st.header(f"Up Next: Book {next_lvl}")
    st.write("Take a deep breath, stretch your shoulders, or grab a sip of water. The clock will not start until you click the button below.")
    
    st.write("")
    if st.button(f"Start Book {next_lvl} (5 Questions) ➔", type="primary", use_container_width=True):
        st.session_state.step = 'testing'
        st.session_state.question_start_time = time.time()
        st.rerun()

# Screen 3: Progressive Benchmark Ladder Testing
elif st.session_state.step == 'testing':

    # Accidental Back/Refresh Guard (Browser beforeunload warning)
    components.html(
        """
        <script>
        window.parent.addEventListener('beforeunload', function (e) {
            e.preventDefault();
            e.returnValue = '';
        });
        </script>
        """,
        height=0,
    )

    # Check if candidate has completed all questions for the current level
    if not st.session_state.show_feedback and st.session_state.level_index >= len(st.session_state.level_questions):
        pass_rate = st.session_state.level_score / max(st.session_state.level_attempts, 1)
        
        if pass_rate >= 0.8:
            st.session_state.highest_passed_level = st.session_state.current_level
            
            if st.session_state.current_level >= 6.0:
                rec = "Book 6"
                st.session_state.recommendation = rec
                send_audit_log(f"Completed - {rec}")
                st.session_state.step = 'results'
                st.rerun()
                st.stop()
            else:
                # Prepare next tier and route to breather screen
                st.session_state.current_level += 1.0
                st.session_state.level_questions = [
                    q for q in QUESTIONS 
                    if q['inst'] == st.session_state.instrument and q['diff'] == st.session_state.current_level
                ]
                st.session_state.level_index = 0
                st.session_state.level_score = 0.0
                st.session_state.level_attempts = 0
                
                send_audit_log(f"In Progress - Passed Book {int(st.session_state.highest_passed_level)}")
                st.session_state.step = 'level_break'
                st.rerun()
                st.stop()
        else:
            if st.session_state.highest_passed_level is None:
                rec = "Not Recommended"
            else:
                rec = f"Book {int(st.session_state.highest_passed_level)}"
                
            st.session_state.recommendation = rec
            send_audit_log(f"Completed - {rec}")
            
            st.session_state.step = 'results'
            st.rerun()
            st.stop()

    # Visual Level Stepper Banner
    cur_lvl = int(st.session_state.current_level)
    pills_html = '<div class="stepper-container">'
    for lvl in [2, 3, 4, 5, 6]:
        if lvl < cur_lvl:
            cls = "step-pill done"
            label = f"✓ Book {lvl}"
        elif lvl == cur_lvl:
            cls = "step-pill active"
            label = f"Book {lvl}"
        else:
            cls = "step-pill"
            label = f"Book {lvl}"
        pills_html += f'<div class="{cls}">{label}</div>'
    pills_html += '</div>'
    st.markdown(pills_html, unsafe_allow_html=True)

    current_q = st.session_state.level_questions[st.session_state.level_index]
    st.subheader(f"Book {cur_lvl} — Question {st.session_state.level_index + 1} of {len(st.session_state.level_questions)}")
    
    if not st.session_state.show_feedback:
        if not st.session_state.hide_timer:
            st.markdown("""
            <style>
            .timer-progress {
                height: 8px; border-radius: 4px;
                animation: countdown 30s linear forwards;
            }
            @keyframes countdown {
                0% { width: 100%; background-color: #28a745; }
                50% { width: 50%; background-color: #28a745; }
                83% { width: 17%; background-color: #ffc107; }
                100% { width: 0%; background-color: #dc3545; }
            }
            </style>
            <div style="width: 100%; height: 8px; background-color: #ddd; border-radius: 4px; margin-bottom: 18px;">
                <div class="timer-progress"></div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <style>
            .ten-sec-warning {
                opacity: 0;
                max-height: 0;
                overflow: hidden;
                background-color: #fff3cd;
                color: #856404;
                border-left: 4px solid #ffc107;
                border-radius: 6px;
                font-weight: 600;
                font-size: 0.95rem;
                animation: showWarning 0.4s ease-out 25s forwards;
            }
            @keyframes showWarning {
                to {
                    opacity: 1;
                    max-height: 60px;
                    padding: 8px 14px;
                    margin-bottom: 16px;
                }
            }
            </style>
            <div class="ten-sec-warning">⏳ 10 seconds remaining — choose your best guess!</div>
            """, unsafe_allow_html=True)
        
        # Render question with keyword highlighting and larger typography
        formatted_q = highlight_keywords(current_q['q'])
        st.markdown(f"<div style='font-size: 1.22rem; line-height: 1.5; margin-bottom: 16px;'>{formatted_q}</div>", unsafe_allow_html=True)
        
        display_options = current_q['opts'] + ["I don't know"]
        
        for idx, opt in enumerate(display_options):
            if st.button(opt, use_container_width=True):
                time_taken = time.time() - st.session_state.question_start_time
                
                if time_taken > 30:
                    is_correct = 0.0
                    st.session_state.timed_out = True
                else:
                    st.session_state.timed_out = False
                    is_correct = 1.0 if idx == current_q['ans'] else 0.0
                
                st.session_state.pending_b = current_q['diff']
                st.session_state.pending_r = is_correct
                st.session_state.pending_q = current_q
                st.session_state.pending_choice = opt
                st.session_state.correct_text = current_q['opts'][current_q['ans']]
                st.session_state.time_taken = time_taken
                
                st.session_state.show_feedback = True
                st.rerun()
                
    else:
        st.markdown(f"<div style='font-size: 1.15rem; margin-bottom: 12px;'>{highlight_keywords(current_q['q'])}</div>", unsafe_allow_html=True)
        
        if st.session_state.timed_out:
            st.error("**⏰ Out of Time!** Over 30 seconds elapsed, so this counts as incorrect.")
            st.info(f"Correct answer: **{st.session_state.correct_text}**")
        elif st.session_state.pending_r > 0:
            seconds = int(st.session_state.time_taken)
            st.success(f"**Correct!** Answered in **{seconds}s**.")
        elif st.session_state.pending_choice == "I don't know":
            st.warning("**Skipped.** Good call moving forward.")
            st.info(f"Correct answer: **{st.session_state.correct_text}**")
        else:
            st.error("**Incorrect.**")
            st.info(f"Correct answer: **{st.session_state.correct_text}**")
            
        st.write("")
        if st.button("Next Question ➔", type="primary", use_container_width=True):
            st.session_state.responses.append(st.session_state.pending_r)
            st.session_state.asked_questions.append(st.session_state.pending_q)

            actual_choice = "Time Out" if st.session_state.timed_out else st.session_state.pending_choice
            st.session_state.user_choices.append(actual_choice)
            
            st.session_state.level_score += st.session_state.pending_r
            st.session_state.level_attempts += 1
            st.session_state.level_index += 1
            st.session_state.q_count += 1
            
            st.session_state.show_feedback = False 
            st.session_state.question_start_time = time.time()
            st.rerun()

# Screen 4: Results & PDF Download
elif st.session_state.step == 'results':
    st.header("Assessment Complete!")
    
    rec = st.session_state.get('recommendation', "Not Recommended")
    
    if rec == "Not Recommended":
        st.error(f"**Assessment Outcome:** {rec}")
        st.warning("The candidate did not meet the baseline 80% threshold for Book 2 instruction.")
    else:
        st.success(f"**Recommended Level:** {rec}")
        
    st.write(f"Total Questions Answered: **{st.session_state.q_count}**")
    st.write("Download your official results below and send the PDF to your recruiter to complete your application.")
    
    if 'pdf_bytes' not in st.session_state:
        display_score = float(st.session_state.highest_passed_level) if st.session_state.highest_passed_level else 1.0
        st.session_state.pdf_bytes = create_pdf(
            st.session_state.candidate_name, 
            st.session_state.location, 
            st.session_state.instrument, 
            rec, 
            display_score, 
            st.session_state.q_count, 
            st.session_state.asked_questions, 
            st.session_state.responses, 
            st.session_state.user_choices
        )
    
    st.write("")
    st.download_button(
        label="📄 Download Results as PDF",
        data=st.session_state.pdf_bytes,
        file_name=f"{st.session_state.candidate_name}_Assessment_{st.session_state.instrument}.pdf",
        mime="application/pdf",
        type="primary",
        use_container_width=True
    )
