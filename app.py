import streamlit as st
from site_utils import page_setup, COVERS, benny_uri, sun_uri
from data import BOOKS

page_setup("Home")

book = st.query_params.get("book", "")
welcome = {
    "colors": "🎨 Welcome back from Benny's Colors!",
    "counting": "🔢 Welcome back from Benny's Counting Adventure!",
    "abcs": "🔤 Welcome back from Benny's ABC's!",
    "senses": "👀 Welcome back from The 5 Senses!",
}
if book in welcome:
    st.success(welcome[book] + " Keep learning with Benny below.")

benny = benny_uri()
sun = sun_uri()

st.markdown(
    f"""
    <section class="brand-hero">
      <img class="hero-sun-img" src="{sun}" alt="Benny smiling sun">

      <div class="hero-grid">
        <div class="hero-copy-column">
          <div class="speech-bubble">
            Hi, friend! I'm Benny! Let's learn together! 🌈
          </div>

          <div class="rainbow-title" aria-label="Benny's Learning World">
            <span class="y">Benny's</span><br>
            <span class="b">Learning</span><br>
            <span class="r">W</span><span class="o">o</span><span class="y">r</span><span class="g">l</span><span class="p">d</span>
          </div>

          <div class="hero-copy-box">
            Explore colorful books, practice sounds and words, play reading games,
            and watch Benny's stories come to life — all in the same cheerful world as the books.
          </div>
        </div>

        <div class="hero-character-column">
          <div class="benny-frame">
            <img class="hero-benny-img" src="{benny}" alt="Benny the Bunny holding an apple and pencil">
          </div>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h2 class="section-title">🌟 Choose a Benny Adventure</h2>', unsafe_allow_html=True)
st.markdown('<div class="sub">Pick where you want to hop next!</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="large")
with c1:
    st.markdown(
        f"""
        <div class="adventure-card books-card">
          <img class="card-benny-img" src="{benny}" alt="Benny the Bunny">
          <div class="card-scene">📚🌈</div>
          <h2>Benny's Book Burrow</h2>
          <p>Meet Benny's growing book collection and choose a colorful learning adventure.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link("pages/1_Books.py", label="📚 Hop to the Books!", use_container_width=True)

with c2:
    st.markdown(
        f"""
        <div class="adventure-card garden-card">
          <img class="card-benny-img" src="{benny}" alt="Benny the Bunny">
          <div class="card-scene">🌼🌈🔤</div>
          <h2>Benny's Reading Garden</h2>
          <p>Practice colors, letter sounds, rhymes, sight words, and sentences while earning Benny Stars.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link("pages/2_Reading_Garden.py", label="🎮 Play & Learn with Benny!", use_container_width=True)

with c3:
    st.markdown(
        f"""
        <div class="adventure-card theater-card">
          <img class="card-benny-img" src="{benny}" alt="Benny the Bunny">
          <div class="card-scene">⭐🎬📖</div>
          <h2>Benny's Story Theater</h2>
          <p>Watch the books become read-along adventures with narration, highlighted words, and learning pauses.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link("pages/3_Read_Alongs.py", label="🎬 Enter the Story Theater!", use_container_width=True)

st.markdown("<h2 class='section-title'>📖 Benny's Bookshelf</h2>", unsafe_allow_html=True)
st.markdown("<div class='sub'>The website now follows the same bright Benny style as the book covers.</div>", unsafe_allow_html=True)

cols = st.columns(4, gap="medium")
for col, book_item in zip(cols, BOOKS):
    with col:
        cover = COVERS / book_item["cover"]
        if cover.exists():
            st.image(str(cover), use_container_width=True)
        st.markdown(f"**{book_item['title']}**")
        st.caption(" • ".join(book_item["skills"]))

st.markdown(
    """
    <div class="premium">
      <h3>🐰 One Benny, one learning world</h3>
      <p>
        Benny keeps the same look and personality across the books, Reading Garden,
        Story Theater, QR experiences, and future learning activities.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)
