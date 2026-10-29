# questions.py

QUESTIONS = [
    # ---------------- GUITAR ----------------
    {"inst": "Guitar", "diff": 2.0, "ans": 3, "q": "The Circle of Fifths shows:", "opts": ["The number of sharps in a key signature.", "The number of flats in a key signature.", "The relative minor for each key signature.", "All of the above."]},
    {"inst": "Guitar", "diff": 2.0, "ans": 1, "q": "A sus4 chord would contain the following values:", "opts": ["1, 2, 5", "1, 4, 5", "1, 2, 3, 5", "1, 3, 4, 7"]},
    {"inst": "Guitar", "diff": 2.0, "ans": 0, "q": "To play the minor blues scale, you add this note to the minor pentatonic scale:", "opts": ["b5", "2", "b6", "7"]},
    {"inst": "Guitar", "diff": 2.0, "ans": 1, "q": "There are typically _____ major scale patterns:", "opts": ["4", "5", "6", "7"]},
    {"inst": "Guitar", "diff": 2.0, "ans": 2, "q": "If a triad is said to be inverted:", "opts": ["There is no root note.", "The root note is lower than the other notes in the triad.", "The root note is higher than at least one of the other notes in the triad.", "The triad is played as a descending arpeggio."]},
    
    {"inst": "Guitar", "diff": 3.0, "ans": 1, "q": "A double stop is:", "opts": ["Two rests in a row.", "Two notes played together creating a partial chord.", "Picking something twice.", "Two accents played in a row."]},
    {"inst": "Guitar", "diff": 3.0, "ans": 0, "q": "A diminished triad contains these intervals:", "opts": ["1, b3, b5", "1, 2, b5", "1, 3, b5", "1, 3, 5"]}, 
    {"inst": "Guitar", "diff": 3.0, "ans": 1, "q": "Hybrid pentatonic scales are made by:", "opts": ["Subtracting notes from the minor pentatonic scale.", "Adding notes from the minor and major pentatonic scales together.", "Adding a b2.", "Subtracting the 5."]},
    {"inst": "Guitar", "diff": 3.0, "ans": 2, "q": "There are ______ modes of the major scale;", "opts": ["5", "6", "7", "8"]},
    {"inst": "Guitar", "diff": 3.0, "ans": 2, "q": "A major 9th chord contains what intervals?", "opts": ["1, 3, 5, b7, 9", "1, b3, 5, 7, 9", "1, 3, 5, 7, 9", "1, 3, 5, 6, 9"]},
    
    {"inst": "Guitar", "diff": 4.0, "ans": 1, "q": "What is a dom 7 chord?", "opts": ["A minor triad with a major 7", "A major triad with a minor 7", "A major triad with a major 7", "A minor triad with a minor 7"]},
    {"inst": "Guitar", "diff": 4.0, "ans": 0, "q": "In open G major tuning, if you barre all the strings at the 5th fret you produce a _____ chord:", "opts": ["C", "B", "A", "G"]},
    {"inst": "Guitar", "diff": 4.0, "ans": 1, "q": "An altered chord contains:", "opts": ["An octave of the root note.", "An additional chromatic note not from the corresponding diatonic scale.", "Stacked fifths.", "An additional note from the corresponding diatonic scale."]},
    {"inst": "Guitar", "diff": 4.0, "ans": 2, "q": "Which of the following Pink Floyd songs is mostly in 'odd' time?", "opts": ["Dark Side of the Moon", "Another Brick in the Wall pt 2", "Money", "Time"]},
    {"inst": "Guitar", "diff": 4.0, "ans": 1, "q": "Hybrid picking is a technique where:", "opts": ["You pick alternately up and down.", "You use one or more fingers in addition to your flat pick.", "You use fingerpicks.", "You pick using only your thumb."]},
    
    {"inst": "Guitar", "diff": 5.0, "ans": 3, "q": "Modal interchange occurs when a chord is introduced to a progression from:", "opts": ["The same key.", "Another key.", "The relative minor.", "A parallel key."]},
    {"inst": "Guitar", "diff": 5.0, "ans": 0, "q": "What are the intervals of the harmonic minor scale?", "opts": ["1, 2, b3, 4, 5, b6, 7", "1, 2, b3, 4, 5, b6, b7", "1, b2, b3, 4, 5, b6, b7", "1, 2, 3, 4, 5, b6, b7"]},
    {"inst": "Guitar", "diff": 5.0, "ans": 2, "q": "What is an open triad voicing?", "opts": ["A chord with some open strings.", "A chord with all the notes in the same octave.", "A chord with the second note of the triad raised an octave.", "A chord with all open strings."]},
    {"inst": "Guitar", "diff": 5.0, "ans": 1, "q": "Slash chords are:", "opts": ["Chords made famous by the guitarist Slash.", "Chords that have an additional bass note that is not the root note.", "Chords that have an inverted root note.", "Chords that have two names like C#/Db."]},
    {"inst": "Guitar", "diff": 5.0, "ans": 1, "q": "The fourth mode of the Melodic Minor scale is:", "opts": ["Lydian Augmented", "Lydian Dominant", "Lydian #4", "Super Lydian"]},
    
    {"inst": "Guitar", "diff": 6.0, "ans": 0, "q": "A tresillo groove can best be described as:", "opts": ["123-123-12", "12-123-12", "1234-1234", "123-12-123"]},
    {"inst": "Guitar", "diff": 6.0, "ans": 3, "q": "Travis Picking describes a picking style that features:", "opts": ["The thumb playing the melody in the bass", "The fingers 'rolling' through descending patterns", "The pinky always playing the highest string", "The thumb playing a rhythmic pattern while the fingers play the melody"]},
    {"inst": "Guitar", "diff": 6.0, "ans": 2, "q": "Open A Tuning is primarily used for:", "opts": ["Metal", "Experimental music", "Slide guitar", "Acoustic guitar"]},
    {"inst": "Guitar", "diff": 6.0, "ans": 1, "q": "Which of the following is a common Phrygian mode chord progression?", "opts": ["I-♭V", "I-♭II", "I-vi-ii-V", "ii-V-I"]},
    {"inst": "Guitar", "diff": 6.0, "ans": 0, "q": "Harmonizing a scale in fourths is often called:", "opts": ["Quartal harmony", "Stacking tritones", "Augmented cadence", "Contrary motion"]},

    # ---------------- BASS ----------------
    {"inst": "Bass", "diff": 2.0, "ans": 1, "q": "What are the intervals of the natural minor scale?", "opts": ["1, 2, b3, 4, 5, 6, b7", "1, 2, b3, 4, 5, b6, b7", "1, 2, b3, 4, 5, b6, 7", "1, 2, b3, 4, 5, 6, 7"]},
    {"inst": "Bass", "diff": 2.0, "ans": 2, "q": "What intervals are in an augmented triad?", "opts": ["1, 3, 5", "1, 3, 7", "1, 3, 5#", "1, b3, 5#"]},
    {"inst": "Bass", "diff": 2.0, "ans": 1, "q": "Which of these chord progressions describes a I-vi-ii-V in the key of A?", "opts": ["A-Bm-F#m-D", "A-E-F#m-D", "E-C#m-F#m-B", "A-F#m-Bm-E"]},
    {"inst": "Bass", "diff": 2.0, "ans": 1, "q": "A common form of bass syncopation places some notes on the _______?", "opts": ["Downbeat.", "The 'and'.", "One.", "Kick drum."]},
    {"inst": "Bass", "diff": 2.0, "ans": 0, "q": "Which of these bass players exclusively played with a pick:", "opts": ["Carol Kaye and Lemmy", "Chris Squire and John Paul Jones", "John Entwhistle and Geddy Lee", "Les Claypool and Paul McCartney"]},
    
    {"inst": "Bass", "diff": 3.0, "ans": 1, "q": "What is the relative minor of Fmaj?", "opts": ["Cm", "Dm", "Bm", "Fm"]},
    {"inst": "Bass", "diff": 3.0, "ans": 2, "q": "How many sharps in A major?", "opts": ["None", "2", "3", "4"]},
    {"inst": "Bass", "diff": 3.0, "ans": 3, "q": "How many eighth note triplets can be in a bar of 4/4?", "opts": ["8", "3", "2", "4"]},
    {"inst": "Bass", "diff": 3.0, "ans": 2, "q": "Who is considered the inventor of the electric bass slap and pop technique?", "opts": ["Flea", "Bootsy Collins", "Larry Graham", "Victor Wooten"]},
    {"inst": "Bass", "diff": 3.0, "ans": 0, "q": "When playing a shuffle groove, beats ____ and ______ are accented:", "opts": ["2, 4", "1, 3", "And of 2, and of 4", "And of 1, and of 3"]},
    
    {"inst": "Bass", "diff": 4.0, "ans": 3, "q": "What notes are in a dom 7 arpeggio?", "opts": ["1, 3, 5, 7", "1, b3, 5, b7", "1, b3, 5, 7", "1, 3, 5, b7"]},
    {"inst": "Bass", "diff": 4.0, "ans": 0, "q": "What are the intervals of the Phrygian mode?", "opts": ["1, b2, b3, 4, 5, b6, b7", "1, b2, 3, 4, 5, 6, b7", "1, 2, b3, 4, 5, b6, b7", "1, b2, b3, 4, 5, b6, 7"]},
    {"inst": "Bass", "diff": 4.0, "ans": 1, "q": "What is a reverse gallop?", "opts": ["eighth note followed by two 16ths notes.", "Two sixteenth notes followed by an eighth note.", "Three sixteenth notes followed by a rest.", "Three eighth note triplets."]},
    {"inst": "Bass", "diff": 4.0, "ans": 1, "q": "Odd time refers to_____?", "opts": ["The bottom number of the time signature being an odd number.", "The top number of the time signature being an odd number.", "The top number being divisible by two.", "The bottom number being divisible by two."]},
    {"inst": "Bass", "diff": 4.0, "ans": 2, "q": "The second inversion of the C major chord is:", "opts": ["C, G, E", "C, E, G", "G, C, E", "E, C, G"]},
    
    {"inst": "Bass", "diff": 5.0, "ans": 2, "q": "For compound time signatures, the top number is divisible by____:", "opts": ["2", "4", "3", "5"]},
    {"inst": "Bass", "diff": 5.0, "ans": 0, "q": "The 'blue third' occurs when you_____:", "opts": ["Add a minor third to the major pentatonic.", "Add a b5 to the minor pentatonic.", "Add a b5 to the major pentatonic.", "Add a major third to the minor pentatonic."]},
    {"inst": "Bass", "diff": 5.0, "ans": 0, "q": "The double thumb technique involves______:", "opts": ["Using your thumb to play a downstroke followed by an upstroke.", "Playing two notes in a row with your thumb.", "Popping two notes in row.", "Slapping notes in double time."]},
    {"inst": "Bass", "diff": 5.0, "ans": 3, "q": "In 5/4 time, the quarter note can be counted as _____:", "opts": ["A group of 3 and a group of 2.", "A group of 2 and a group of 3.", "1, 2, 3, 4, 5.", "All of the above."]},
    {"inst": "Bass", "diff": 5.0, "ans": 1, "q": "Linear tapping uses what techniques in the fretting hand:", "opts": ["Vibrato and slides", "Hammer ons and pull offs", "Slap and pop", "String skipping and muting"]},
    
    {"inst": "Bass", "diff": 6.0, "ans": 2, "q": "Sixteenth-note swing is often used in what style of music:", "opts": ["Metal", "Punk", "Funk", "Indie Rock"]},
    {"inst": "Bass", "diff": 6.0, "ans": 0, "q": "A tresillo groove can best be described as:", "opts": ["123-123-12", "12-123-12", "1234-1234", "123-12-123"]},
    {"inst": "Bass", "diff": 6.0, "ans": 1, "q": "Pinch harmonics are achieved by:", "opts": ["Pinching the string with your second finger", "Using your thumb and finger to pluck the string simultaneously", "Pushing really hard on the fretboard", "Tapping the string 12 frets away from the fretted note"]},
    {"inst": "Bass", "diff": 6.0, "ans": 0, "q": "What are the most common extensions used over a major chord?", "opts": ["1, 3, 5, 7, 9, #11, 13", "1, 3, 5, ♭7, 9, 11, 13", "1, 3, 5, 7, #9, 11, ♭13", "1, 3, 5, 7, 9, 11, #13"]},
    {"inst": "Bass", "diff": 6.0, "ans": 1, "q": "Jaco Pastorius is known for his work with:", "opts": ["Return to Forever", "Weather Report", "Mahavishnu Orchestra", "Snarky Puppy"]},

    # ---------------- DRUMS ----------------
    {"inst": "Drums", "diff": 2.0, "ans": 2, "q": "The upbeat occurs on______:", "opts": ["The one", "The 'e'", "The 'and'", "The 'ah'"]},
    {"inst": "Drums", "diff": 2.0, "ans": 1, "q": "How do you count eighth notes?", "opts": ["One-two-three-four", "One-and-Two-and", "One-ta-Two-ta", "One-plus-Two-plus"]},
    {"inst": "Drums", "diff": 2.0, "ans": 0, "q": "What is the difference between half time and double time?", "opts": ["Halftime makes the feel slower, Double Time makes the feel faster", "Halftime makes the feel faster, Double Time makes the feel slower", "There is no difference", "They are in different time signatures"]},
    {"inst": "Drums", "diff": 2.0, "ans": 1, "q": "How many beats does a dotted eighth note represent?", "opts": ["½", "¾", "1", "1 ½"]},
    {"inst": "Drums", "diff": 2.0, "ans": 3, "q": "What is a “ghost note”?", "opts": ["A note that is written but not played", "An echo of another played note", "A note that is played much louder than the others", "A note that is played much softer than the others"]},
    
    {"inst": "Drums", "diff": 3.0, "ans": 1, "q": "Eighth note triplets are counted _______:", "opts": ["Tri-pl-et, Tri-pl-et, Tri-pl-et", "One-Trip-let, Two-Trip-let", "One-and-ah, Two-and-ah", "Ti-ti-ta, Ti-ti-ta"]},
    {"inst": "Drums", "diff": 3.0, "ans": 0, "q": "Shuffles are derived from what rhythm?", "opts": ["Triplets", "Eighth Notes", "Sixteenth Notes", "Quarter Notes"]},
    {"inst": "Drums", "diff": 3.0, "ans": 2, "q": "An example of an inverted paradiddle would be:", "opts": ["R L R L R R L R L R L L", "R R R L R R R L", "R L L R L R R L", "R R L L L L R R"]},
    {"inst": "Drums", "diff": 3.0, "ans": 2, "q": "In a ¾ Waltz, the snare is played on which two beats?", "opts": ["1 & 2", "1 & 3", "2 & 3", "It’s only played on beat 3"]},
    {"inst": "Drums", "diff": 3.0, "ans": 3, "q": "What is the difference between 4/4 time and ⅞ time?", "opts": ["Three 8th notes", "Three ¼ notes", "No difference", "One 8th note"]},
    
    {"inst": "Drums", "diff": 4.0, "ans": 0, "q": "When playing 16th note double bass grooves, your ‘footing’ typically follows this pattern:", "opts": ["R L R L", "R R L L", "R L L R R L L R", "R L R R L R L L"]},
    {"inst": "Drums", "diff": 4.0, "ans": 2, "q": "Steve Gadd played a groove that was a variation of the Mozambique rhythm on which Paul Simon song?", "opts": ["50 Ways to Leave Your Lover", "Graceland", "Late in The Evening", "The Boxer"]},
    {"inst": "Drums", "diff": 4.0, "ans": 1, "q": "The African 3/2 Clave rhythm was the inspiration for this famous beat:", "opts": ["Train Beat", "Bo-Diddley Beat", "Purdie Shuffle", "New Jack Swing"]},
    {"inst": "Drums", "diff": 4.0, "ans": 3, "q": "This influential drummer was one of the first rock drummers to heavily incorporate reggae and Latin influences in his playing.", "opts": ["Keith Moon", "Ginger Baker", "Neil Peart", "Stewart Copeland"]},
    {"inst": "Drums", "diff": 4.0, "ans": 2, "q": "What rhythm is best used for counting 32nd notes?", "opts": ["Quarter notes", "Eighth notes", "Sixteenth notes", "Triplets"]},
    
    {"inst": "Drums", "diff": 5.0, "ans": 1, "q": "What is Linear Drumming?", "opts": ["When you play grooves or fills where your limbs line up", "When you play grooves or fills where your limbs do not line up", "When you play grooves or fills based on second-line drumming", "When you play grooves or fills that line up with the bassist"]},
    {"inst": "Drums", "diff": 5.0, "ans": 0, "q": "“Break On Through (To The Other Side)” is a famous example of a rock song in which the drummer is playing this Latin beat:", "opts": ["Bossa Nova", "Samba", "Baiao", "Cha Cha Cha"]},
    {"inst": "Drums", "diff": 5.0, "ans": 2, "q": "What is an ostinato?", "opts": ["A funk groove", "A syncopated fill-in", "A repeated rhythmic pattern", "A short drum solo"]},
    {"inst": "Drums", "diff": 5.0, "ans": 1, "q": "A hemiola is when", "opts": ["You play in an odd time signature", "You play a 3 over 2 pattern", "You play a linear groove", "A repeated rhythmic pattern"]},
    {"inst": "Drums", "diff": 5.0, "ans": 0, "q": "The drum solo in “Packard Goose” by Frank Zappa is a:", "opts": ["Vamp in 6/4 time", "Vamp in 6/8 time", "Call & Response", "Open solo"]},
    
    {"inst": "Drums", "diff": 6.0, "ans": 0, "q": "Quadruplets might be typically found in which of these time signatures:", "opts": ["4/4", "2/2", "7/4", "12/8"]},
    {"inst": "Drums", "diff": 6.0, "ans": 1, "q": "A tresillo groove can best be described as:", "opts": ["123-123-12", "12-123-12", "1234-1234", "123-12-123"]},
    {"inst": "Drums", "diff": 6.0, "ans": 2, "q": "Six patterns describe what concept?", "opts": ["Six stroke rolls", "Sextuplet hi hat patterns", "Six-note groupings between hands and feet", "Measures of 6/4"]},
    {"inst": "Drums", "diff": 6.0, "ans": 1, "q": "Salidor, tres golpes, and quinto are all types of what?", "opts": ["Handheld bells", "Styles of dance", "Afro-Cuban 6/8 beats", "Conga drums"]},
    {"inst": "Drums", "diff": 6.0, "ans": 3, "q": "Two different time signatures played together is referred to as:", "opts": ["A polyrhythm", "A polymeter", "A hybrid beat", "A complex time signature"]},

    # ---------------- KEYS ----------------
    {"inst": "Keys", "diff": 2.0, "ans": 1, "q": "What are the intervals of the minor scale?", "opts": ["1, 2, b3, 4, 5, 6, b7", "1, 2, b3, 4, 5, b6, b7", "1, 2, b3, 4, 5, b6, 7", "1, 2, 3, 4, 5, b6, b7"]},
    {"inst": "Keys", "diff": 2.0, "ans": 0, "q": "How many sharps are in the key signature of D major?", "opts": ["2", "3", "None", "1"]},
    {"inst": "Keys", "diff": 2.0, "ans": 2, "q": "For compound time signatures, the top number is divisible by____:", "opts": ["2", "4", "3", "5"]},
    {"inst": "Keys", "diff": 2.0, "ans": 2, "q": "What is an inverted chord?", "opts": ["There is no root note.", "The root note is lower than the other notes in the triad.", "The root note is higher than at least one of the other notes in the triad.", "The triad is played as a descending arpeggio."]},
    {"inst": "Keys", "diff": 2.0, "ans": 2, "q": "What intervals are in a dom 7th chord?", "opts": ["1, b3, 5, b7", "1, 3, 5, 7", "1, 3, 5, b7", "1, b3, 5, 7"]},
    
    {"inst": "Keys", "diff": 3.0, "ans": 1, "q": "What interval is added to the minor pentatonic scale to get the Blues scale?", "opts": ["6", "b5", "4", "b3"]},
    {"inst": "Keys", "diff": 3.0, "ans": 0, "q": "How many flats are in the key of Ab?", "opts": ["4", "3", "5", "2"]},
    {"inst": "Keys", "diff": 3.0, "ans": 2, "q": "What is the relative minor of E maj?", "opts": ["G", "A", "C#", "B"]},
    {"inst": "Keys", "diff": 3.0, "ans": 3, "q": "What intervals are in a Sus2 chord?", "opts": ["1, 3, 5", "1, 4, 5", "1, b3, 5", "1, 2, 5"]},
    {"inst": "Keys", "diff": 3.0, "ans": 1, "q": "What is a passing chord?", "opts": ["A chord you skip when playing a chord progression.", "A chord that you play between two diatonic chords.", "A chord that you play for a whole measure.", "A rootless chord."]},
    
    {"inst": "Keys", "diff": 4.0, "ans": 1, "q": "A diminished 7th chord contains these intervals:", "opts": ["1, 3, b5, b7", "1, b3, b5, bb7", "1, b3, 5, b7", "1, 3, b5, 7"]},
    {"inst": "Keys", "diff": 4.0, "ans": 0, "q": "The Phrygian mode contains these intervals:", "opts": ["1, b2, b3, 4, 5, b6, b7", "1, b2, 3, 4, 5, 6, b7", "1, 2, b3, 4, 5, b6, b7", "1, b2, b3, 4, 5, 6, b7"]},
    {"inst": "Keys", "diff": 4.0, "ans": 2, "q": "Chord extensions are:", "opts": ["When you add a 7.", "When you add the root an octave higher.", "When you extend the chord beyond the 7 into the next octave.", "When you add a non diatonic note."]},
    {"inst": "Keys", "diff": 4.0, "ans": 3, "q": "The second note name in a slash chord contains:", "opts": ["The chord you play with your right hand.", "The chord substitution.", "The passing chord.", "The lowest note in the chord voicing."]},
    {"inst": "Keys", "diff": 4.0, "ans": 0, "q": "An open chord voicing contains:", "opts": ["Notes in more than one octave.", "Just the root and the 5.", "A b5.", "No root note."]},
    
    {"inst": "Keys", "diff": 5.0, "ans": 1, "q": "Which of the following progressions contains a functional dominant chord:", "opts": ["C7, D7, C7, D7", "Dm, G7, C, C", "C, F, C, C", "C7, F7, C7, F7"]},
    {"inst": "Keys", "diff": 5.0, "ans": 0, "q": "What is unique about the ascending melodic minor scale?", "opts": ["When ascending it has a b3, descending it has a b3, b6, b7.", "When ascending it has a b3, b6, b7 and descending it has b3, b6.", "When ascending it has b3 and a b7 and descending it has b3, b7.", "When ascending it is major, when descending it is minor."]},
    {"inst": "Keys", "diff": 5.0, "ans": 3, "q": "The lydian dominant scale is which of the following?", "opts": ["An 'altered scale'", "An 'exotic scale'", "A mode of the melodic minor scale.", "All of the above"]},
    {"inst": "Keys", "diff": 5.0, "ans": 1, "q": "What is mixed meter?", "opts": ["A part that has different rhythmic accents in each hand", "A passage that moves between different time signatures", "A time signature where the numbers are different, such as 3/4.", "A melody that uses dotted notes."]},
    {"inst": "Keys", "diff": 5.0, "ans": 0, "q": "When playing a guide tone voicing, what intervals are used in the chord?", "opts": ["3, 7", "5, 7", "3, 5", "4, 7"]},
    
    {"inst": "Keys", "diff": 6.0, "ans": 0, "q": "A tresillo groove can best be described as:", "opts": ["123-123-12", "12-123-12", "1234-1234", "123-12-123"]},
    {"inst": "Keys", "diff": 6.0, "ans": 2, "q": "Contrary Motion in voice leading refers to:", "opts": ["Melodic lines moving at different tempos", "Melodic lines moving at different intervals", "Melodic lines moving in different directions", "Melodic lines moving through different scales"]},
    {"inst": "Keys", "diff": 6.0, "ans": 3, "q": "Quadruplets might be typically found in which of these time signatures:", "opts": ["4/4", "2/2", "7/4", "12/8"]},
    {"inst": "Keys", "diff": 6.0, "ans": 3, "q": "“Slip Notes” refers to which technique?", "opts": ["Portamento bending on synths", "Multi-octave glissando", "Slipping in and out of a song’s key center", "Tasteful grace notes that add excitement to chord comping"]},
    {"inst": "Keys", "diff": 6.0, "ans": 1, "q": "What is a symmetrical scale?", "opts": ["A scale that is derived from the diatonic scale.", "A scale based on a pattern of intervals instead such as the whole tone scale.", "A scale that incorporates passing tones.", "A scale that has six notes."]},

    # ---------------- VOCALS ----------------
    {"inst": "Vocals", "diff": 2.0, "ans": 0, "q": "True or False: Singers need less support when singing in falsetto/head voice vs full voice since the sound is higher.", "opts": ["False", "True"]},
    {"inst": "Vocals", "diff": 2.0, "ans": 3, "q": "What muscles in the body engage with proper diaphragmatic support?", "opts": ["back/ rib cage", "gluteal/ buttocks", "pelvic/ stomach", "All of the above"]},
    {"inst": "Vocals", "diff": 2.0, "ans": 0, "q": "How many notes are in the major Pentatonic scale?", "opts": ["5", "7", "6", "8"]},
    {"inst": "Vocals", "diff": 2.0, "ans": 0, "q": "Common vocal harmonies that complete a major triad are ___", "opts": ["3rds & 5ths", "b3rds and 5ths", "Root and 5ths", "3rds and 7ths"]},
    {"inst": "Vocals", "diff": 2.0, "ans": 0, "q": "Syncopation is when the ___ is stressed.", "opts": ["offbeat/ upbeat", "One", "Two and Four", "Onbeat"]},
    
    {"inst": "Vocals", "diff": 3.0, "ans": 0, "q": "What are the 5 vocal resonators?", "opts": ["Head, mouth, chest, nasal cavity & sinus/ mask", "Diaphragm, head, chest, nasal cavity, mouth", "Head, mouth, chest, throat, sinus/mask", "Mouth, chest, nasal cavity, diaphragm, nasal cavity"]},
    {"inst": "Vocals", "diff": 3.0, "ans": 0, "q": "What is staccato vs legato?", "opts": ["Staccato is short or disconnected and legato is long and connected", "Staccato is fast and legato is slow", "Staccato is loud and legato is soft", "Staccato is half time, legato is double time"]},
    {"inst": "Vocals", "diff": 3.0, "ans": 0, "q": "All major triads consist of ___", "opts": ["1, 3 & 5 degrees", "1, 3, b5", "1, 4, 5", "1, b3, 5"]},
    {"inst": "Vocals", "diff": 3.0, "ans": 0, "q": "How do you best count in your band for a song in ¾?", "opts": ["Give the band 2 measures “1, 2, 3; 2, 2, 3”", "1, 2, 3", "1, 2, 3, 4", "1, and 2, and 3, and 4"]},
    {"inst": "Vocals", "diff": 3.0, "ans": 0, "q": "True or False: Triplets always need to have 3 notes in them?", "opts": ["False: the notes of the triplet just need to add up to three of whatever value there would normally be two of", "True"]},
    
    {"inst": "Vocals", "diff": 4.0, "ans": 2, "q": "When you sing you want to move your larynx", "opts": ["Up", "Down", "As little as possible", "Quickly"]},
    {"inst": "Vocals", "diff": 4.0, "ans": 0, "q": "True or False: Vibrato is naturally occurring when you are breathing deeply with loosened support muscles.", "opts": ["False: vibrato occurs when you are relaxed and supporting your voice correctly.", "True"]},
    {"inst": "Vocals", "diff": 4.0, "ans": 0, "q": "What chord progression is I-vi-IV-V in the Key of C?", "opts": ["C-Am- F- G", "C-Bm-F-G", "C-Am-F#-G", "C-A-F-G"]},
    {"inst": "Vocals", "diff": 4.0, "ans": 0, "q": "When transposing a song from the Key of C to the Key of G, by what interval might you be moving each note?", "opts": ["Perfect fifth higher", "Perfect fourth higher", "Perfect fifth lower", "None of the above"]},
    {"inst": "Vocals", "diff": 4.0, "ans": 3, "q": "What are some of the biggest contributors to vocal health?", "opts": ["Hydration", "Rest", "Not smoking/ Vaping", "All of the above"]},
    
    {"inst": "Vocals", "diff": 5.0, "ans": 1, "q": "One way to make singing notes at the top of your range easier is to_____:", "opts": ["Use your chest voice.", "Use a more closed vocal position for vowel sounds.", "Use your diaphragm.", "Use a more open vocal position for vowel sounds."]},
    {"inst": "Vocals", "diff": 5.0, "ans": 2, "q": "What is vocal onset?", "opts": ["The beginning of your vocal range.", "When the hard sound from a t.", "When you move from breath to sound.", "The point at which your voice cracks."]},
    {"inst": "Vocals", "diff": 5.0, "ans": 2, "q": "The fourth mode of the C Major Scale is:", "opts": ["C Aeolian", "G Mixolydian", "F Lydian", "G Dorian"]},
    {"inst": "Vocals", "diff": 5.0, "ans": 0, "q": "Lip trills are designed to _____:", "opts": ["Help you develop even breath flow.", "Help you sing faster.", "Help projection.", "Help you find your range."]},
    {"inst": "Vocals", "diff": 5.0, "ans": 3, "q": "What element of a song will help you determine if a song is in a comfortable range?", "opts": ["They key.", "The highest note.", "The lowest note.", "The entire melody."]},
    
    {"inst": "Vocals", "diff": 6.0, "ans": 0, "q": "A 3:2 Clave is a syncopated rhythm featuring:", "opts": ["Three beats in the first measure and two beats in the second measure", "A 3 over 2 polyrhythm", "Two consecutive triplets", "Three consecutive duplets"]},
    {"inst": "Vocals", "diff": 6.0, "ans": 2, "q": "Contrary Motion in voice leading refers to:", "opts": ["Melodic lines moving at different tempos", "Melodic lines moving at different intervals", "Melodic lines moving in different directions", "Melodic lines moving through different scales"]},
    {"inst": "Vocals", "diff": 6.0, "ans": 2, "q": "A melisma refers to:", "opts": ["A frequently repeated rhythmic idea.", "A breathing technique where the breath is drawn in from the nose.", "An ornamental technique where one vowel sound is stretched over multiple notes.", "A melody sung at half vocal power."]},
    {"inst": "Vocals", "diff": 6.0, "ans": 0, "q": "What are the most common extensions used over a major chord?", "opts": ["1, 3, 5, 7, 9, #11, 13", "1, 3, 5, ♭7, 9, 11, 13", "1, 3, 5, 7, #9, 11, ♭13", "1, 3, 5, 7, 9, 11, #13"]},
    {"inst": "Vocals", "diff": 6.0, "ans": 2, "q": "Vocalese is a style of signing where:", "opts": ["The vocal parts are totally improvised.", "It is always acapella.", "The vocal parts are actual transcriptions of solos and sung note for note using lyrics.", "Nonsensical words are sung."]}
]
