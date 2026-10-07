import random
import streamlit as st
from site_utils import page_setup, speak_button
from data import COLORS, PHONICS, RHYMES, SIGHT_WORDS

page_setup("Reading Garden")
st.title("🎮 Benny's Reading Garden")
st.write("Free early-reading games for kids. Tap, listen, match, read, and earn Benny Stars. ⭐")

if "stars" not in st.session_state:
    st.session_state.stars = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0

st.markdown(f'<div class="score">⭐ Stars: {st.session_state.stars} &nbsp;&nbsp; 🔥 Streak: {st.session_state.streak}</div>', unsafe_allow_html=True)

tabs = st.tabs(["🎨 Colors", "🔤 Phonics", "🎵 Rhymes", "👀 Sight Words", "📖 Sentences"])

with tabs[0]:
    st.subheader("Find the Color")
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
                st.success("⭐ Great reading!")
                st.balloons()
            else:
                st.session_state.streak = 0
                st.warning("Almost! Listen to the word and try again.")

    if st.button("Next color ➡️", use_container_width=True):
        st.session_state.color_idx = idx + 1
        st.rerun()

with tabs[1]:
    st.subheader("Learn the Sound")
    pidx = st.session_state.get("phonic_idx", 0) % len(PHONICS)
    letter, sound, example, emoji = PHONICS[pidx]
    st.markdown(f'<div class="word">{letter} = {sound} = {example} {emoji}</div>', unsafe_allow_html=True)
    speak_button(f"{letter}. {example}. {letter} is for {example}.", "🔊 Hear the letter & word", key=f"phonics_{pidx}")
    st.write(f"Say it with Benny: **{letter} — {example}**")
    if st.button("I said it! ⭐", key=f"said_{pidx}", use_container_width=True):
        st.session_state.stars += 1
        st.success("Nice sound practice!")
    if st.button("Next sound ➡️", key="next_phonic", use_container_width=True):
        st.session_state.phonic_idx = pidx + 1
        st.rerun()

with tabs[2]:
    st.subheader("Which Words Rhyme?")
    ridx = st.session_state.get("rhyme_idx", 0) % len(RHYMES)
    base, answer, options = RHYMES[ridx]
    speak_button(base, f"🔊 Hear: {base}", key=f"rhyme_base_{ridx}")
    st.write(f"Which word rhymes with **{base}**?")
    cols = st.columns(3)
    for i, option in enumerate(options):
        if cols[i].button(option, use_container_width=True, key=f"rhyme_{ridx}_{option}"):
            if option == answer:
                st.session_state.stars += 1
                st.success(f"⭐ {base} and {answer} rhyme!")
            else:
                st.warning("Listen again and try another word.")
    if st.button("Next rhyme ➡️", key="next_rhyme", use_container_width=True):
        st.session_state.rhyme_idx = ridx + 1
        st.rerun()

with tabs[3]:
    st.subheader("Tap & Hear Sight Words")
    st.write("Tap a button to hear a useful early-reading word.")
    cols = st.columns(5)
    for i, word in enumerate(SIGHT_WORDS):
        with cols[i % 5]:
            speak_button(word, f"🔊 {word}", key=f"sight_{i}")

with tabs[4]:
    st.subheader("Read With Benny")
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
    st.write("Try reading it by yourself. Then listen and compare.")
    if st.button("🐰 I read it!", use_container_width=True, key=f"read_{sidx}"):
        st.session_state.stars += 2
        st.success("⭐ +2 Benny Stars! Wonderful reading.")
    if st.button("Next sentence ➡️", use_container_width=True, key="next_sentence"):
        st.session_state.sentence_idx = sidx + 1
        st.rerun()

if st.session_state.stars >= 10:
    st.info("🏅 Badge unlocked: **Benny Reading Explorer!**")
if st.session_state.stars >= 20:
    st.info("🏆 Badge unlocked: **Benny Super Reader!**")

st.markdown("""
<div class="parent-note">
<strong>👨‍👩‍👧 Grown-up tip:</strong> Keep play sessions short and positive.
Let the child try first, then use the audio button for support.
</div>
""", unsafe_allow_html=True)
