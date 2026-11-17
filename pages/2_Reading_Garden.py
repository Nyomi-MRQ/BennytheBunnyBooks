import random
import streamlit as st
from site_utils import page_setup, footer, speak_button, speak_buttons, benny_uri
from data import BOOKS_BY_SLUG, COLORS, COUNTING, PHONICS, SENSES, RHYMES, SIGHT_WORDS, SENTENCES

page_setup("Reading Garden")
benny = benny_uri()

ss = st.session_state
ss.setdefault("stars", 0)
ss.setdefault("streak", 0)
ss.setdefault("celebrate", False)

BADGES = [(5, "🌱", "Seedling"), (10, "🌼", "Reading Explorer"), (20, "🏆", "Super Reader"), (40, "👑", "Benny Champion")]
CHEERS = ["⭐ Great job!", "🌟 You got it!", "🎉 Hooray!", "🐰 Benny is so proud!", "✨ Super!"]


# ---------------------------------------------------------------------------
# Shared game helpers (callbacks run BEFORE the page redraws, so the star
# counter is always up to date)
# ---------------------------------------------------------------------------
def answer(game, choice, correct, right_msg=None, stars=1):
    if choice == correct:
        before = ss.stars
        ss.stars += stars
        ss.streak += 1
        ss[f"{game}_fb"] = ("ok", right_msg or random.choice(CHEERS))
        if any(before < need <= ss.stars for need, _, _ in BADGES) or ss.streak % 5 == 0:
            ss.celebrate = True
    else:
        ss.streak = 0
        ss[f"{game}_fb"] = ("try", "Almost! Listen again and try another one. 💪")


def next_item(game):
    ss[f"{game}_idx"] = ss.get(f"{game}_idx", 0) + 1
    ss[f"{game}_fb"] = None


def give_star(game, msg, stars=1):
    ss.stars += stars
    ss.streak += 1
    ss[f"{game}_fb"] = ("ok", msg)


def current(game, items):
    i = ss.get(f"{game}_idx", 0) % len(items)
    return i, items[i]


def options_for(correct, pool, seed, n=3):
    rng = random.Random(seed)
    opts = [correct] + rng.sample([p for p in pool if p != correct], n - 1)
    rng.shuffle(opts)
    return opts


def choice_buttons(game, idx, options, correct, fmt=str, right_msg=None):
    cols = st.columns(len(options))
    for col, opt in zip(cols, options):
        col.button(
            fmt(opt), key=f"{game}_{idx}_{opt}", width="stretch",
            on_click=answer, args=(game, opt, correct, right_msg),
        )


def feedback_and_next(game, label):
    fb = ss.get(f"{game}_fb")
    if fb:
        (st.success if fb[0] == "ok" else st.warning)(fb[1])
    st.button(f"{label} ➡️", key=f"next_{game}", type="primary", width="stretch", on_click=next_item, args=(game,))


# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.html(
    f"""
    <div class="reading-garden-hero">
      <div class="garden-copy">
        <h1 class="garden-title">Benny's Reading Garden</h1>
        <div class="garden-intro">
          Welcome to my garden! Pick a game below. Tap 🔊 to hear me say the words.
          Every try helps your reading grow! 🌱
        </div>
      </div>
      <img class="garden-benny-img" src="{benny}" alt="Benny the Bunny">
    </div>
    """
)

if ss.celebrate:
    st.balloons()
    ss.celebrate = False

badges_html = "".join(
    f'<span class="badge {"" if ss.stars >= need else "locked"}">{icon} {name}<br><small>{need} ⭐</small></span>'
    for need, icon, name in BADGES
)
st.html(
    f'<div class="score">⭐ Benny Stars: {ss.stars} &nbsp;&nbsp; 🔥 Streak: {ss.streak}</div>'
    f'<div class="badge-row">{badges_html}</div>'
)

TAB_NAMES = ["🎨 Colors", "🔢 Counting", "🔤 Letters", "👀 Senses", "🎵 Rhymes", "💬 Sight Words", "📖 Sentences"]
start = BOOKS_BY_SLUG.get(st.query_params.get("game", ""), {}).get("game_tab")
tabs = st.tabs(TAB_NAMES, default=start if start in TAB_NAMES else None)

# ---- Colors ---------------------------------------------------------------
with tabs[0]:
    st.html('<div class="lesson-note">🐰 “Let’s find a color together! Which word matches?”</div>')
    idx, (word, emoji, sentence, hexcol) = current("color", COLORS)
    st.html(f'<div class="word"><div class="swatch" style="background:{hexcol}"></div>{emoji}</div>')
    speak_buttons([(f"🔊 Hear the color", word), ("🔊 Hear Benny's sentence", sentence)])
    choice_buttons("color", idx, options_for(word, [c[0] for c in COLORS], idx + 100), word,
                   right_msg=f"⭐ Yes! That's {word.lower()}! {sentence}")
    feedback_and_next("color", "Next color")

# ---- Counting -------------------------------------------------------------
with tabs[1]:
    st.html('<div class="lesson-note">🐰 “Touch each one and count with me! How many?”</div>')
    idx, (num, numword, emoji) = current("count", COUNTING)
    st.html(f'<div class="word"><div class="count-row">{" ".join([emoji] * num)}</div></div>')
    speak_button(", ".join(str(n) for n in range(1, num + 1)) + f"! {numword} in all!",
                 "🔊 Count along with Benny")
    choice_buttons("count", idx, options_for(num, list(range(1, 11)), idx + 200), num,
                   fmt=lambda n: f"{n}", right_msg=f"⭐ Yes! There {'is' if num == 1 else 'are'} {numword}!")
    feedback_and_next("count", "Next number")

# ---- Letters (A to Z) -----------------------------------------------------
with tabs[2]:
    st.html('<div class="lesson-note">🐰 “Let’s make the letter sound! Which picture starts with it?”</div>')
    idx, (letter, sound, example, emoji) = current("letter", PHONICS)
    st.html(f'<div class="word" style="font-size:4rem">{letter}{letter.lower()}</div>')
    hint = f"{letter} is in {example}" if letter == "X" else f"{letter} is for {example}"
    speak_buttons([("🔊 Hear the letter", f"{letter}."), ("🔊 Hear a word", f"{hint}.")])
    if letter == "X":
        st.write("X is a tricky letter — it hides at the **end** of words like **Fox** 🦊!")
        st.button("⭐ I found the X in Fox!", key=f"x_{idx}", width="stretch",
                  on_click=give_star, args=("letter", "⭐ Great looking! F-O-X ends with X!"))
    else:
        pool = [p for p in PHONICS if p[0] != "X"]
        opts = options_for((example, emoji), [(p[2], p[3]) for p in pool], idx + 300)
        choice_buttons("letter", idx, opts, (example, emoji), fmt=lambda o: f"{o[1]} {o[0]}",
                       right_msg=f"⭐ Yes! {hint}!")
    st.caption(f"Letter {idx + 1} of 26")
    feedback_and_next("letter", "Next letter")

# ---- Senses ---------------------------------------------------------------
with tabs[3]:
    st.html('<div class="lesson-note">🐰 “Teddy and I use our senses every day! Which one do we need?”</div>')
    idx, (sense, part, part_emoji, question, thing) = current("sense", SENSES)
    st.html(f'<div class="word">{thing}<br><span style="font-size:1.5rem">{question}</span></div>')
    speak_button(question, "🔊 Hear the question")
    opts = options_for(sense, [s[0] for s in SENSES], idx + 400)
    lookup = {s[0]: s for s in SENSES}
    choice_buttons("sense", idx, opts, sense, fmt=lambda s: f"{lookup[s][2]} {s.title()}",
                   right_msg=f"⭐ Yes! We use our {part} for {sense}!")
    feedback_and_next("sense", "Next question")

# ---- Rhymes ---------------------------------------------------------------
with tabs[4]:
    st.html('<div class="lesson-note">🐰 “Listen closely. Which word sounds like it?”</div>')
    idx, (base, correct, options) = current("rhyme", RHYMES)
    st.html(f'<div class="word">{base}</div>')
    speak_buttons([(f"🔊 Hear “{base}”", base), ("🔊 Hear all the choices", ", ".join(options))])
    choice_buttons("rhyme", idx, options, correct, right_msg=f"⭐ Yes! {base} and {correct} rhyme!")
    feedback_and_next("rhyme", "Next rhyme")

# ---- Sight words ----------------------------------------------------------
with tabs[5]:
    st.html('<div class="lesson-note">🐰 “Tap each word and hear me read it! Can you say it too?”</div>')
    speak_buttons([(w, w.lower()) for w in SIGHT_WORDS], big=True)
    st.button("⭐ I read all the words!", key="sight_done", width="stretch",
              on_click=give_star, args=("sight", "⭐ +3 Benny Stars! What a reader!", 3))
    fb = ss.get("sight_fb")
    if fb:
        st.success(fb[1])

# ---- Sentences ------------------------------------------------------------
with tabs[6]:
    st.html('<div class="lesson-note">🐰 “Try reading the sentence first, then listen to me!”</div>')
    idx, sentence = current("sentence", SENTENCES)
    st.html(f'<div class="word" style="font-size:1.9rem">{sentence}</div>')
    speak_button(sentence, "🔊 Hear the whole sentence")
    st.button("🐰 I read it!", key=f"read_{idx}", width="stretch",
              on_click=give_star, args=("sentence", "⭐ +2 Benny Stars! Wonderful reading!", 2))
    feedback_and_next("sentence", "Next sentence")

st.html(
    """
    <div class="parent-note">
      <strong>👨‍👩‍👧 Grown-up tip:</strong> Let your child try first, then use the 🔊 buttons for support.
      Keep it playful, celebrate effort as much as right answers, and stop while it's still fun.
    </div>
    """
)

footer()
