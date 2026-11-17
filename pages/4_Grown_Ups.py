import streamlit as st
from site_utils import page_setup, footer, benny_uri
from data import BOOKS

page_setup("Grown-Ups")

st.html(
    f"""
<section class="brand-hero" style="padding-bottom:2.2rem">
  <div class="hero-grid" style="min-height:260px">
    <div class="hero-copy-column">
      <div class="speech-bubble">💗 Thank you for reading with me!</div>
      <h1 class="rainbow-title" style="font-size:clamp(2.8rem,6vw,4.8rem)"><span class="p">For</span> <span class="b">Grown-Ups</span></h1>
      <div class="hero-copy-box">
        Benny's Learning World makes early learning playful, repeatable, and easy to share —
        at home, in the classroom, or at grandma's house.
      </div>
    </div>
    <div class="hero-character-column">
      <div class="benny-frame" style="width:min(100%,240px)">
        <img class="hero-benny-img" src="{benny_uri()}" alt="Benny the Bunny">
      </div>
    </div>
  </div>
</section>
"""
)

c1, c2, c3 = st.columns(3, gap="large")
c1.html(
    """<div class="card"><h3>🌱 Skills we practice</h3><p>
    Colors • counting 1–10 • the alphabet • beginning sounds • rhyming • sight words •
    simple sentences • the five senses • listening and observation.</p></div>"""
)
c2.html(
    """<div class="card"><h3>📖 Read, then play</h3><p>
    Read a Benny book together first. Then open the matching game in the Reading Garden
    so your little one can practice what they just heard.</p></div>"""
)
c3.html(
    """<div class="card"><h3>💗 Keep it light</h3><p>
    Let children try first and use 🔊 as support, not a test. Ten playful minutes beats
    a long session — stop while it's still fun!</p></div>"""
)

st.html('<h2 class="section-title">🎯 Which game goes with which book?</h2>')
cols = st.columns(len(BOOKS), gap="medium")
for col, book in zip(cols, BOOKS):
    with col:
        st.page_link(
            "pages/2_Reading_Garden.py",
            label=f"{book['title']} → {book['game_tab'][2:]}",
            icon=book["game_tab"][:1],
            query_params={"game": book["slug"]},
            width="stretch",
        )

st.html(
    """
<h2 class="section-title">🔒 Safe for little ones</h2>
<div class="card" style="height:auto">
  <p style="margin:0">
  Children never need to sign up, log in, or type personal information to play.
  There are no ads and no in-game purchases. The 🔊 read-aloud buttons use your device's
  own built-in voice.
  </p>
</div>
<h2 class="section-title">📱 QR codes in the books</h2>
<div class="card" style="height:auto">
  <p style="margin:0">
  Scan the QR code inside a Benny book with your phone's camera to jump straight to that
  book's welcome page and matching game.
  </p>
</div>
"""
)

footer()
