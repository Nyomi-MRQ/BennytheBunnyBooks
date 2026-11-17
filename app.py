import streamlit as st
from site_utils import page_setup, footer, benny_uri, sun_uri, cover_html
from data import BOOKS, BOOKS_BY_SLUG

page_setup("Home")

benny = benny_uri()
sun = sun_uri()

# QR codes in the printed books open  YOURSITE/?book=colors  (or counting / abcs / senses)
book_slug = st.query_params.get("book", "")
qr_book = BOOKS_BY_SLUG.get(book_slug)

st.html(
    f"""
<section class="brand-hero">
  <img class="hero-sun-img" src="{sun}" alt="">
  <div class="hero-grid">
    <div class="hero-copy-column">
      <div class="speech-bubble">Hi, friend! I'm Benny! Let's learn together! 🌈</div>
      <h1 class="rainbow-title" aria-label="Benny's Learning World">
        <span class="y">Benny's</span><br>
        <span class="b">Learning</span><br>
        <span class="r">W</span><span class="o">o</span><span class="y">r</span><span class="g">l</span><span class="p">d</span>
      </h1>
      <div class="hero-copy-box">
        Colorful picture books for little readers — plus free games to practice colors,
        counting, letters, and the five senses with Benny. 🐰
      </div>
    </div>
    <div class="hero-character-column">
      <div class="benny-frame">
        <img class="hero-benny-img" src="{benny}" alt="Benny the Bunny holding an apple and a pencil">
      </div>
    </div>
  </div>
</section>
"""
)

# ---- Arrived from a QR code inside a book --------------------------------
if qr_book:
    with st.container(key="bookcard_qr"):
        left, right = st.columns([1, 3], gap="large", vertical_alignment="center")
        with left:
            st.html(cover_html(qr_book))
        with right:
            st.html(
                f'<div class="book-title">🎉 Welcome, {qr_book["title"]} reader!</div>'
                f'<div class="book-desc">Benny made a game just for your book. Tap the big button to start playing.</div>'
            )
            st.page_link(
                "pages/2_Reading_Garden.py",
                label=f"Play the {qr_book['game_tab'][2:]} game ➜",
                icon="🎮",
                query_params={"game": qr_book["slug"]},
                width="stretch",
            )

# ---- Three adventures ---------------------------------------------------------
st.html('<h2 class="section-title">🌟 Choose a Benny Adventure</h2><div class="sub">Pick where you want to hop next!</div>')

cards = [
    ("books-card", "📚🌈", "Benny's Book Burrow",
     "Meet Benny's growing book collection and pick your next story.",
     "pages/1_Books.py", "Hop to the Books!", "📚"),
    ("garden-card", "🌼🔤🔢", "Benny's Reading Garden",
     "Play colors, counting, letters, senses, rhymes, and more — and earn Benny Stars!",
     "pages/2_Reading_Garden.py", "Play & Learn!", "🎮"),
    ("theater-card", "⭐🎬📖", "Benny's Story Theater",
     "Read-along versions of every book with narration and highlighted words.",
     "pages/3_Read_Alongs.py", "Enter the Theater!", "🎬"),
]
cols = st.columns(3, gap="large")
for col, (cls, scene, title, text, page, label, icon) in zip(cols, cards):
    with col:
        st.html(
            f"""
            <div class="adventure-card {cls}">
              <div class="card-scene">{scene}</div>
              <h2>{title}</h2>
              <p>{text}</p>
            </div>
            """
        )
        st.page_link(page, label=label, icon=icon, width="stretch")

# ---- Bookshelf ------------------------------------------------------------
st.html('<h2 class="section-title">📖 Benny\'s Bookshelf</h2><div class="sub">Four bright books, each with its own learning game.</div>')

shelf = "".join(
    '<div class="shelf-item">' + cover_html(book)
    + f'<div class="shelf-title">{book["title"]}</div>'
    + f'<div class="shelf-meta">{book["ages"]} · {" • ".join(book["skills"][:2])}</div></div>'
    for book in BOOKS
)
st.html(f'<div class="shelf-grid">{shelf}</div>')

st.page_link("pages/1_Books.py", label="See all the books", icon="📚", width="stretch")

st.html(
    """
    <div class="premium">
      <h3 style="margin-top:0">💗 For parents, teachers & grandparents</h3>
      <p style="margin-bottom:0">
        Every Benny book connects to a free game here — no sign-ups, no ads. Read the book together,
        then play the matching game to practice what you learned. Visit the <b>Grown-Ups</b> page for
        simple tips on reading with little ones.
      </p>
    </div>
    """
)

footer()
