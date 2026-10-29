import streamlit as st
import math
import urllib.parse

# --- 1. IRT Probability & Estimation Models (Book-Scaled) ---
def irt_probability(theta, b):
    try:
        return 1.0 / (1.0 + math.exp(-(theta - b)))
    except OverflowError:
        return 0.0 if (theta - b) < 0 else 1.0

def estimate_ability(administered_b, responses):
    best_theta = 4.0 # Center gravity at Book 4
    max_ll = -float('inf')
    
    for t in range(0, 81):
        theta = t / 10.0
        ll = 0
        for b, r in zip(administered_b, responses):
            p = irt_probability(theta, b)
            p = max(min(p, 1.0 - 1e-10), 1e-10) 
            ll += r * math.log(p) + (1 - r) * math.log(1 - p)
            
        prior = -0.5 * ((theta - 4.0)**2)
        ll += prior
        
        if ll > max_ll:
            max_ll = ll
            best_theta = theta
            
    return best_theta

# --- 2. Full Question Bank (All Instruments & Levels) ---
QUESTIONS = [
    # ---------------- GUITAR ----------------
    # Book 2
    {"inst": "Guitar", "diff": 2.0, "ans": 3, "q": "The Circle of Fifths shows:", "opts": ["The number of sharps in a key signature.", "The number of flats in a key signature.", "The relative minor for each key signature.", "All of the above."]},
    {"inst": "Guitar", "diff": 2.0, "ans": 1, "q": "A sus4 chord would contain the following values:", "opts": ["1, 2, 5", "1, 4, 5", "1, 2, 3, 5", "1, 3, 4, 7"]},
    {"inst": "Guitar", "diff": 2.0, "ans": 0, "q": "To play the minor blues scale, you add this note to the minor pentatonic scale:", "opts": ["b5", "2", "b6", "7"]},
    {"inst": "Guitar", "diff": 2.0, "ans": 1, "q": "There are typically _____ major scale patterns:", "opts": ["4", "5", "6", "7"]},
    {"inst": "Guitar", "diff": 2.0, "ans": 2, "q": "If a triad is said to be inverted:", "opts": ["There is no root note.", "The root note is lower than the other notes in the triad.", "The root note is higher than at least one of the other notes in the triad.", "The triad is played as a descending arpeggio."]},
    # Book 3
    {"inst": "Guitar", "diff": 3.0, "ans": 1, "q": "A double stop is:", "opts": ["Two rests in a row.", "Two notes played together creating a partial chord.", "Picking something twice.", "Two accents played in a row."]},
    {"inst": "Guitar", "diff": 3.0, "ans": 0, "q": "A diminished triad contains these intervals:", "opts": ["1, b3, b5", "1, 2, b5", "1, 3, b5", "1, 3, 5"]}, 
    {"inst": "Guitar", "diff": 3.0, "ans": 1, "q": "Hybrid pentatonic scales are made by:", "opts": ["Subtracting notes from the minor pentatonic scale.", "Adding notes from the minor and major pentatonic scales together.", "Adding a b2.", "Subtracting the 5."]},
    {"inst": "Guitar", "diff": 3.0, "ans": 2, "q": "There are ______ modes of the major scale;", "opts": ["5", "6", "7", "8"]},
    {"inst": "Guitar", "diff": 3.0, "ans": 2, "q": "A major 9th chord contains what intervals?", "opts": ["1, 3, 5, b7, 9", "1, b3, 5, 7, 9", "1, 3, 5, 7, 9", "1, 3, 5, 6, 9"]},
    # Book 4
    {"inst": "Guitar", "diff": 4.0, "ans": 1, "q": "What is a dom 7 chord?", "opts": ["A minor triad with a major 7", "A major triad with a minor 7", "A major triad with a major 7", "A minor triad with a minor 7"]},
    {"inst": "Guitar", "diff": 4.0, "ans": 0, "q": "In open G major tuning, if you barre all the strings at the 5th fret you produce a _____ chord:", "opts": ["C", "B", "A", "G"]},
    {"inst": "Guitar", "diff": 4.0, "ans": 1, "q": "An altered chord contains:", "opts": ["An octave of the root note.", "An additional chromatic note not from the corresponding diatonic scale.", "Stacked fifths.", "An additional note from the corresponding diatonic scale."]},
    {"inst": "Guitar", "diff": 4.0, "ans": 2, "q": "Which of the following Pink Floyd songs is mostly in 'odd' time?", "opts": ["Dark Side of the Moon", "Another Brick in the Wall pt 2", "Money", "Time"]},
    {"inst": "Guitar", "diff": 4.0, "ans": 1, "q": "Hybrid picking is a technique where:", "opts": ["You pick alternately up and down.", "You use one or more fingers in addition to your flat pick.", "You use fingerpicks.", "You pick using only your thumb."]},
    # Book 5
    {"inst": "Guitar", "diff": 5.0, "ans": 3, "q": "Modal interchange occurs when a chord is introduced to a progression from:", "opts": ["The same key.", "Another key.", "The relative minor.", "A parallel key."]},
    {"inst": "Guitar", "diff": 5.0, "ans": 0, "q": "What are the intervals of the harmonic minor scale?", "opts": ["1, 2, b3, 4, 5, b6, 7", "1, 2, b3, 4, 5, b6, b7", "1, b2, b3, 4, 5, b6, b7", "1, 2, 3, 4, 5, b6, b7"]},
    {"inst": "Guitar", "diff": 5.0, "ans": 2, "q": "What is an open triad voicing?", "opts": ["A chord with some open strings.", "A chord with all the notes in the same octave.", "A chord with the second note of the triad raised an octave.", "A chord with all open strings."]},
    {"inst": "Guitar", "diff": 5.0, "ans": 1, "q": "Slash chords are:", "opts": ["Chords made famous by the guitarist Slash.", "Chords that have an additional bass note that is not the root note.", "Chords that have an inverted root note.", "Chords that have two names like C#/Db."]},
    {"inst": "Guitar", "diff": 5.0, "ans": 1, "q": "The fourth mode of the Melodic Minor scale is:", "opts": ["Lydian Augmented", "Lydian Dominant", "Lydian #4", "Super Lydian"]},
    # Book 6
    {"inst": "Guitar", "diff": 6.0, "ans": 0, "q": "A tresillo groove can best be described as:", "opts": ["123-123-12", "12-123-12", "1234-1234", "123-12-123"]},
    {"inst": "Guitar", "diff": 6.0, "ans": 3, "q": "Travis Picking describes a picking style that features:", "opts": ["The thumb playing the melody in the bass", "The fingers 'rolling' through descending patterns", "The pinky always playing the highest string", "The thumb playing a rhythmic pattern while the fingers play the melody"]},
    {"inst": "Guitar", "diff": 6.0, "ans": 2, "q": "Open A Tuning is primarily used for:", "opts": ["Metal", "Experimental music", "Slide guitar", "Acoustic guitar"]},
    {"inst": "Guitar", "diff": 6.0, "ans": 1, "q": "Which of the following is a common Phrygian mode chord progression?", "opts": ["I-♭V", "I-♭II", "I-vi-ii-V", "ii-V-I"]},
    {"inst": "Guitar", "diff": 6.0, "ans": 0, "q": "Harmonizing a scale in fourths is often called:", "opts": ["Quartal harmony", "Stacking tritones", "Augmented cadence", "Contrary motion"]},

    # ---------------- BASS ----------------
    # Book 2
    {"inst": "Bass", "diff": 2.0, "ans": 1, "q": "What are the intervals of the natural minor scale?", "opts": ["1, 2, b3, 4, 5, 6, b7", "1, 2, b3, 4, 5, b6, b7", "1, 2, b3, 4, 5, b6, 7", "1, 2, b3, 4, 5, 6, 7"]},
    {"inst": "Bass", "diff": 2.0, "ans": 2, "q": "What intervals are in an augmented triad?", "opts": ["1, 3, 5", "1, 3, 7", "1, 3, 5#", "1, b3, 5#"]},
    {"inst": "Bass", "diff": 2.0, "ans": 1, "q": "Which of these chord progressions describes a I-vi-ii-V in the key of A?", "opts": ["A-Bm-F#m-D", "A-E-F#m-D", "E-C#m-F#m-B", "A-F#m-Bm-E"]},
    {"inst": "Bass", "diff": 2.0, "ans": 1, "q": "A common form of bass syncopation places some notes on the _______?", "opts": ["Downbeat.", "The 'and'.", "One.", "Kick drum."]},
    {"inst": "Bass", "diff": 2.0, "ans": 0, "q": "Which of these bass players exclusively played with a pick:", "opts": ["Carol Kaye and Lemmy", "Chris Squire and John Paul Jones", "John Entwhistle and Geddy Lee", "Les Claypool and Paul McCartney"]},
    # Book 3
    {"inst": "Bass", "diff": 3.0, "ans": 1, "q": "What is the relative minor of Fmaj?", "opts": ["Cm", "Dm", "Bm", "Fm"]},
    {"inst": "Bass", "diff": 3.0, "ans": 2, "q": "How many sharps in A major?", "opts": ["None", "2", "3", "4"]},
    {"inst": "Bass", "diff": 3.0, "ans": 3, "q": "How many eighth note triplets can be in a bar of 4/4?", "opts": ["8", "3", "2", "4"]},
    {"inst": "Bass", "diff": 3.0, "ans": 2, "q": "Who is considered the inventor of the electric bass slap and pop technique?", "opts": ["Flea", "Bootsy Collins", "Larry Graham", "Victor Wooten"]},
    {"inst": "Bass", "diff": 3.0, "ans": 0, "q": "When playing a shuffle groove, beats ____ and ______ are accented:", "opts": ["2, 4", "1, 3", "And of 2, and of 4", "And of 1, and of 3"]},
    # Book 4
    {"inst": "Bass", "diff": 4.0, "ans": 3, "q": "What notes are in a dom 7 arpeggio?", "opts": ["1, 3, 5, 7", "1, b3, 5, b7", "1, b3, 5, 7", "1, 3, 5, b7"]},
    {"inst": "Bass", "diff": 4.0, "ans": 0, "q": "What are the intervals of the Phrygian mode?", "opts": ["1, b2, b3, 4, 5, b6, b7", "1, b2, 3, 4, 5, 6, b7", "1, 2, b3, 4, 5, b6, b7", "1, b2, b3, 4, 5, b6, 7"]},
    {"inst": "Bass", "diff": 4.0, "ans": 1, "q": "What is a reverse gallop?", "opts": ["eighth note followed by two 16ths notes.", "Two sixteenth notes followed by an eighth note.", "Three sixteenth notes followed by a rest.", "Three eighth note triplets."]},
    {"inst": "Bass", "diff": 4.0, "ans": 1, "q": "Odd time refers to_____?", "opts": ["The bottom number of the time signature being an odd number.", "The top number of the time signature being an odd number.", "The top number being divisible by two.", "The bottom number being divisible by two."]},
    {"inst": "Bass", "diff": 4.0, "ans": 2, "q": "The second inversion of the C major chord is:", "opts": ["C, G, E", "C, E, G", "G, C, E", "E, C, G"]},
    # Book 5
    {"inst": "Bass", "diff": 5.0, "ans": 2, "q": "For compound time signatures, the top number is divisible by____:", "opts": ["2", "4", "3", "5"]},
    {"inst": "Bass", "diff": 5.0, "ans": 0, "q": "The 'blue third' occurs when you_____:", "opts": ["Add a minor third to the major pentatonic.", "Add a b5 to the minor pentatonic.", "Add a b5 to the major pentatonic.", "Add a major third to the minor pentatonic."]},
    {"inst": "Bass", "diff": 5.0, "ans": 0, "q": "The double thumb technique involves______:", "opts": ["Using your thumb to play a downstroke followed by an upstroke.", "Playing two notes in a row with your thumb.", "Popping two notes in row.", "Slapping notes in double time."]},
    {"inst": "Bass", "diff": 5.0, "ans": 3, "q": "In 5/4 time, the quarter note can be counted as _____:", "opts": ["A group of 3 and a group of 2.", "A group of 2 and a group of 3.", "1, 2, 3, 4, 5.", "All of the above."]},
    {"inst": "Bass", "diff": 5.0, "ans": 1, "q": "Linear tapping uses what techniques in the fretting hand:", "opts": ["Vibrato and slides", "Hammer ons and pull offs", "Slap and pop", "String skipping and muting"]},
    # Book 6
    {"inst": "Bass", "diff": 6.0, "ans": 2, "q": "Sixteenth-note swing is often used in what style of music:", "opts": ["Metal", "Punk", "Funk", "Indie Rock"]},
    {"inst": "Bass", "diff": 6.0, "ans": 0, "q": "A tresillo groove can best be described as:", "opts": ["123-123-12", "12-123-12", "1234-1234", "123-12-123"]},
    {"inst": "Bass", "diff": 6.0, "ans": 1, "q": "Pinch harmonics are achieved by:", "opts": ["Pinching the string with your second finger", "Using your thumb and finger to pluck the string simultaneously", "Pushing really hard on the fretboard", "Tapping the string 12 frets away from the fretted note"]},
    {"inst": "Bass", "diff": 6.0, "ans": 0, "q": "What are the most common extensions used over a major chord?", "opts": ["1, 3, 5, 7, 9, #11, 13", "1, 3, 5, ♭7, 9, 11, 13", "1, 3, 5, 7, #9, 11, ♭13", "1, 3, 5, 7, 9, 11, #13"]},
    {"inst": "Bass", "diff": 6.0, "ans": 1, "q": "Jaco Pastorius is known for his work with:", "opts": ["Return to Forever", "Weather Report", "Mahavishnu Orchestra", "Snarky Puppy"]},

    # ---------------- DRUMS ----------------
    # Book 2
    {"inst": "Drums", "diff": 2.0, "ans": 2, "q": "The upbeat occurs on______:", "opts": ["The one", "The 'e'", "The 'and'", "The 'ah'"]},
    {"inst": "Drums", "diff": 2.0, "ans": 1, "q": "How do you count eighth notes?", "opts": ["One-two-three-four", "One-and-Two-and", "One-ta-Two-ta", "One-plus-Two-plus"]},
    {"inst": "Drums", "diff": 2.0, "ans": 0, "q": "What is the difference between half time and double time?", "opts": ["Halftime makes the feel slower, Double Time makes the feel faster", "Halftime makes the feel faster, Double Time makes the feel slower", "There is no difference", "They are in different time signatures"]},
    {"inst": "Drums", "diff": 2.0, "ans": 1, "q": "How many beats does a dotted eighth note represent?", "opts": ["½", "¾", "1", "1 ½"]},
    {"inst": "Drums", "diff": 2.0, "ans": 3, "q": "What is a “ghost note”?", "opts": ["A note that is written but not played", "An echo of another played note", "A note that is played much louder than the others", "A note that is played much softer than the others"]},
    # Book 3
    {"inst": "Drums", "diff": 3.0, "ans": 1, "q": "Eighth note triplets are counted _______:", "opts": ["Tri-pl-et, Tri-pl-et, Tri-pl-et", "One-Trip-let, Two-Trip-let", "One-and-ah, Two-and-ah", "Ti-ti-ta, Ti-ti-ta"]},
    {"inst": "Drums", "diff": 3.0, "ans": 0, "q": "Shuffles are derived from what rhythm?", "opts": ["Triplets", "Eighth Notes", "Sixteenth Notes", "Quarter Notes"]},
    {"inst": "Drums", "diff": 3.0, "ans": 2, "q": "An example of an inverted paradiddle would be:", "opts": ["R L R L R R L R L R L L", "R R R L R R R L", "R L L R L R R L", "R R L L L L R R"]},
    {"inst": "Drums", "diff": 3.0, "ans":
