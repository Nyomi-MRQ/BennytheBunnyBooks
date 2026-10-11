import random
import streamlit as st
from site_utils import page_setup, speak_button, benny_uri
from data import COLORS, PHONICS, RHYMES, SIGHT_WORDS

page_setup("Reading Garden")
benny = benny_uri()

st.markdown(
    f"""
    <div class="reading-garden-hero">
      <div class="garden-copy">
        <div class="garden-title">Benny's Reading Garden</div>
        <div class="garden-intro">
          Welcome to my garden! We'll practice colors, letters, sounds, rhymes,
          sight words, and sentences together. Every try helps your reading grow! 🌱
        </div>
      </div>
      <img class="garden-benny-img" src="{benny}" alt="Benny the Bunny">
    </div>
    """,
    unsafe_allow_html=True,
)

if "stars" not in st.session_state:
    st.session_state.stars = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0

st.markdown(
    f'<div class="score">⭐ Benny Stars: {st.session_state.stars} &nbsp;&nbsp; 🔥 Reading Streak: {st.session_state.streak}</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="benny-says">🐰 Benny says: “You can do it! Listen, try, and celebrate every word you learn!”</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="garden-path">
      <strong>🌈 Choose a garden path:</strong><br>
      🎨 Colors &nbsp; • &nbsp; 🔤 Phonics &nbsp; • &nbsp; 🎵 Rhymes &nbsp; • &nbsp;
      👀 Sight Words &nbsp; • &nbsp; 📖 Sentences
    </div>
    """,
    unsafe_allow_html=True,
)

tabs = st.tabs(["🎨 Colors", "🔤 Phonics", "🎵 Rhymes", "👀 Sight Words", "📖 Sentences"])

with tabs[0]:
    st.markdown('<div class="lesson-note">🐰 “Let’s find a color together!”</div>', unsafe_allow_html=True)
    idx = st.session_state.get("color_idx", 0) % len(COLORS)
    word, emoji, sentence = COLORS[idx]
    st.markdown(f'<div class="word">{emoji}<br>{word}</div>', unsafe_allow_html=True)
    speak_button(word, f"🔊 Hear the word {word}", key=f"color_word_{idx}")
    speak_button(sentence, "🔊 Hear Benny's sentence", key=f"color_sentence_{idx}")

    choices = [word]
    rng = random.Random(idx + 100)
    while len(choices) < 3:
        candidate = rng.choice(COLORS)[0]
        if candidate not in choices:
            choices.append(candidate)
    rng.shuffle(choices)

    st.write("Which word matches the picture?")
    cols = st.columns(3)
    for i, choice in enumerate(choices):
        if cols[i].button(choice, use_container_width=True, key=f"color_choice_{idx}_{choice}"):
            if choice == word:
                st.session_state.stars += 1
                st.session_state.streak += 1
                st.success("⭐ Great job! Benny knew you could do it!")
                st.balloons()
            else:
                st.session_state.streak = 0
                st.warning("Almost! Benny says listen again and give it another try.")

    if st.button("Next color ➡️", use_container_width=True):
        st.session_state.color_idx = idx + 1
        st.rerun()

with tabs[1]:
    st.markdown('<div class="lesson-note">🐰 “Let’s make the letter sound together!”</div>', unsafe_allow_html=True)
    pidx = st.session_state.get("phonic_idx", 0) % len(PHONICS)
    letter, sound, example, emoji = PHONICS[pidx]
    st.markdown(f'<div class="word">{letter} = {sound} = {example} {emoji}</div>', unsafe_allow_html=True)
    speak_button(f"{letter}. {example}. {letter} is for {example}.", "🔊 Hear the letter & word", key=f"phonics_{pidx}")
    st.write(f"Say it with Benny: **{letter} — {example}**")
    if st.button("I said it! ⭐", key=f"said_{pidx}", use_container_width=True):
        st.session_state.stars += 1
        st.success("Awesome sound practice!")
    if st.button("Next sound ➡️", key="next_phonic", use_container_width=True):
        st.session_state.phonic_idx = pidx + 1
        st.rerun()

with tabs[2]:
    st.markdown('<div class="lesson-note">🐰 “Listen closely. Which words sound alike?”</div>', unsafe_allow_html=True)
    ridx = st.session_state.get("rhyme_idx", 0) % len(RHYMES)
    base, answer, options = RHYMES[ridx]
    speak_button(base, f"🔊 Hear: {base}", key=f"rhyme_base_{ridx}")
    st.write(f"Which word rhymes with **{base}**?")
    cols = st.columns(3)
    for i, option in enumerate(options):
        if cols[i].button(option, use_container_width=True, key=f"rhyme_{ridx}_{option}"):
            if option == answer:
                st.session_state.stars += 1
                st.success(f"⭐ Yes! {base} and {answer} rhyme!")
            else:
                st.warning("Not that one. Benny says try another word!")
    if st.button("Next rhyme ➡️", key="next_rhyme", use_container_width=True):
        st.session_state.rhyme_idx = ridx + 1
        st.rerun()

with tabs[3]:
    st.markdown('<div class="lesson-note">🐰 “Tap each word and hear me read it!”</div>', unsafe_allow_html=True)
    st.write("Tap a button to hear an early-reading sight word.")
    cols = st.columns(5)
    for i, word in enumerate(SIGHT_WORDS):
        with cols[i % 5]:
            speak_button(word, f"🔊 {word}", key=f"sight_{i}")

with tabs[4]:
    st.markdown('<div class="lesson-note">🐰 “Try the sentence first, then listen to me!”</div>', unsafe_allow_html=True)
    sentences = [
        "I see a red apple.",
        "Benny sees blue water.",
        "The little bunny can hop.",
        "I see a yellow sun.",
        "Benny can run and play.",
    ]
    sidx = st.session_state.get("sentence_idx", 0) % len(sentences)
    sentence = sentences[sidx]
    st.markdown(f'<div class="word" style="font-size:1.8rem">{sentence}</div>', unsafe_allow_html=True)
    speak_button(sentence, "🔊 Hear the whole sentence", key=f"sentence_{sidx}")
    st.write("Read it by yourself first. Then listen and compare.")
    if st.button("🐰 I read it!", use_container_width=True, key=f"read_{sidx}"):
        st.session_state.stars += 2
        st.success("⭐ +2 Benny Stars! Wonderful reading!")
    if st.button("Next sentence ➡️", use_container_width=True, key="next_sentence"):
        st.session_state.sentence_idx = sidx + 1
        st.rerun()

if st.session_state.stars >= 10:
    st.info("🏅 Badge unlocked: Benny Reading Explorer!")
if st.session_state.stars >= 20:
    st.info("🏆 Badge unlocked: Benny Super Reader!")

st.markdown(
    """
    <div class="parent-note">
      <strong>👨‍👩‍👧 Grown-up tip:</strong> Let the child try first, then use the audio button for support.
      Keep sessions playful and celebrate effort as much as correct answers.
    </div>
    """,
    unsafe_allow_html=True,
)
