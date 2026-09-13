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
<div class="hero">
  <span class="pill">🐰 Books • Games • Read-Alongs</span>
  <h1>Benny Learning World</h1>
  <p>
    Welcome to the online home of <strong>Benny the Bunny Books</strong>.
    Read with Benny, practice early-learning skills, play free reading games,
    and discover premium read-along adventures.
  </p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="large")
with c1:
    st.markdown("""<div class="card"><h3>📚 Explore the Books</h3><p>Meet the growing Benny collection and choose your next learning adventure.</p></div>""", unsafe_allow_html=True)
    st.page_link("pages/1_📚_Books.py", label="Go to Books →", use_container_width=True)
with c2:
    st.markdown("""<div class="card"><h3>🎮 Reading Garden</h3><p>Free tap-to-hear words, colors, phonics, rhymes, sight words, and reading games.</p></div>""", unsafe_allow_html=True)
    st.page_link("pages/2_🎮_Reading_Garden.py", label="Play & Learn →", use_container_width=True)
with c3:
    st.markdown("""<div class="card"><h3>🎬 Read-Alongs</h3><p>Watch free previews and discover full premium narrated learning adventures.</p></div>""", unsafe_allow_html=True)
    st.page_link("pages/3_🎬_Read_Alongs.py", label="See Read-Alongs →", use_container_width=True)

st.markdown('<h2 class="section-title">📖 Meet the Collection</h2>', unsafe_allow_html=True)
st.markdown('<div class="sub">Four learning adventures already have a home in Benny Learning World.</div>', unsafe_allow_html=True)

cols = st.columns(4, gap="medium")
for col, book in zip(cols, BOOKS):
    with col:
        cover = COVERS / book["cover"]
        if cover.exists():
            st.image(str(cover), use_container_width=True)
        st.markdown(f"**{book['title']}**")
        st.caption(" • ".join(book["skills"]))

st.markdown("""
<div class="premium">
  <h3>✨ One Benny world, online and in every book</h3>
  <p>
  Future QR codes inside the books can lead children and grown-ups back here for
  free companion activities, previews, and the matching read-along.
  </p>
</div>
""", unsafe_allow_html=True)
