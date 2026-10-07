import streamlit as st
from site_utils import page_setup, COVERS
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

st.markdown("""
<div class="benny-hero">
  <div class="benny-bubble">Hi, friend! Come learn with me! 🌈</div>
  <h1>Benny Learning World</h1>
  <p>
    Hop into Benny's world of books, reading games, sounds, colors,
    letters, stories, and playful learning adventures.
  </p>
  <div class="hero-benny">🐰</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<h2 class="section-title">🌟 Where should Benny take you?</h2>', unsafe_allow_html=True)
st.markdown('<div class="sub">Choose an adventure. Every path leads to something fun to read, hear, watch, or learn.</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.markdown("""
    <div class="adventure-card books-card">
      <div class="card-clouds">☁️ &nbsp;&nbsp; ☁️</div>
      <div class="adventure-emoji">🐰📚</div>
      <h2>Benny's Book Burrow</h2>
      <p>Snuggle into Benny's book nook! Meet every Benny adventure, explore colorful covers, and choose a story to learn with.</p>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/1_Books.py", label="📚 Hop to the Books!", use_container_width=True)

with c2:
    st.markdown("""
    <div class="adventure-card garden-card">
      <div class="card-clouds">☁️ &nbsp;&nbsp; ☀️ &nbsp;&nbsp; ☁️</div>
      <div class="adventure-emoji">🐰🌈</div>
      <h2>Benny's Reading Garden</h2>
      <p>Play with colors, letters, sounds, rhymes, sight words, and reading challenges while you earn Benny Stars.</p>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/2_Reading_Garden.py", label="🎮 Let's Play & Learn!", use_container_width=True)

with c3:
    st.markdown("""
    <div class="adventure-card theater-card">
      <div class="card-clouds">✨ &nbsp;&nbsp; ⭐ &nbsp;&nbsp; ✨</div>
      <div class="adventure-emoji">🐰🎬</div>
      <h2>Benny's Story Theater</h2>
      <p>Watch Benny's stories come alive with narration, highlighted words, sounds, and interactive pauses.</p>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/3_Read_Alongs.py", label="🎬 Enter the Story Theater!", use_container_width=True)

st.markdown("<h2 class=\"section-title\">📖 Benny's Bookshelf</h2>", unsafe_allow_html=True)
st.markdown('<div class="sub">Pick a book and discover what Benny is learning today.</div>', unsafe_allow_html=True)

cols = st.columns(4, gap="medium")
for col, book_item in zip(cols, BOOKS):
    with col:
        cover = COVERS / book_item["cover"]
        if cover.exists():
            st.image(str(cover), use_container_width=True)
        st.markdown(f"**{book_item['title']}**")
        st.caption(" • ".join(book_item["skills"]))

st.markdown("""
<div class="premium">
  <h3>🐰 Keep the adventure going!</h3>
  <p>Benny's books, games, and read-alongs all live together here. Future QR codes inside the books can bring kids straight back to their matching Benny learning adventure.</p>
</div>
""", unsafe_allow_html=True)
