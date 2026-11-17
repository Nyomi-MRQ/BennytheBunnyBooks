import streamlit as st
from site_utils import page_setup, footer, PURCHASE_LINKS, benny_uri, sun_uri, cover_html, pills
from data import BOOKS

page_setup("Book Burrow")

benny = benny_uri()
sun = sun_uri()

st.html(
    f"""
<section class="brand-hero">
  <img class="hero-sun-img" src="{sun}" alt="">
  <div class="hero-grid" style="min-height:340px">
    <div class="hero-copy-column">
      <div class="speech-bubble">🐰 Welcome to my Book Burrow!</div>
      <h1 class="rainbow-burrow-title"><span class="y">Book</span><br><span class="b">Burrow</span></h1>
      <div class="hero-copy-box">
        Snuggle into Benny's colorful bookshelf! Every book comes with a free matching
        game in the Reading Garden.
      </div>
    </div>
    <div class="hero-character-column">
      <div class="benny-frame" style="width:min(100%,280px)">
        <img class="hero-benny-img" src="{benny}" alt="Benny the Bunny">
      </div>
    </div>
  </div>
</section>
<h2 class="section-title">📚 Benny's Story Shelf</h2>
<div class="sub">Tap a book's game button to practice what's inside.</div>
"""
)

for i, book in enumerate(BOOKS):
    if i % 2 == 0:
        cols = st.columns(2, gap="large")  # new row every two books (keeps order on phones)
    with cols[i % 2]:
        with st.container(key=f"bookcard_{i}"):
            left, right = st.columns([1, 1.25], gap="medium")
            with left:
                st.html(cover_html(book))
            with right:
                st.html(
                    f'<div class="book-title">{book["title"]}</div>'
                    f'<div class="book-desc">{book["description"]}</div>'
                    + pills([book["ages"]], "skill-pill age-pill")
                    + pills(book["skills"])
                )
                link = PURCHASE_LINKS.get(book["title"], "")
                if link:
                    st.link_button("🛍️ Bring this book home", link, width="stretch")
                else:
                    st.button("🛍️ Coming soon to buy", disabled=True, width="stretch", key=f"book_{i}")
                st.page_link(
                    "pages/2_Reading_Garden.py",
                    label="Play the game",
                    icon="🎮",
                    query_params={"game": book["slug"]},
                    width="stretch",
                )

st.html(
    """
<div class="premium">
  <strong>🐰 Benny says:</strong> “Every book in my burrow has its own game and read-along. Let's keep learning!”
</div>
"""
)

footer()
