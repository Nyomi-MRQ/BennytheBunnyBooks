import streamlit as st
from site_utils import page_setup, COVERS, PURCHASE_LINKS, benny_uri, sun_uri
from data import BOOKS

page_setup("Book Burrow")

benny = benny_uri()
sun = sun_uri()

st.markdown(f"""
<style>
.book-burrow-hero {{
    position: relative;
    overflow: hidden;
    min-height: 380px;
    border-radius: 40px;
    border: 6px solid white;
    padding: 2.5rem 2.2rem 2.2rem;
    background:
        radial-gradient(circle at 18% 18%, rgba(255,255,255,.95) 0 44px, transparent 46px),
        radial-gradient(circle at 26% 14%, rgba(255,255,255,.96) 0 60px, transparent 62px),
        linear-gradient(180deg, #73d7ff 0%, #d8f4ff 52%, #b2e988 53%, #6ec459 100%);
    box-shadow: 0 15px 0 rgba(65,53,74,.08), 0 28px 55px rgba(56,77,91,.16);
    margin-bottom: 1.7rem;
}}
.book-burrow-hero:after {{
    content: "🌼  🌸  🌷  🌼  🌸  🌷";
    position: absolute;
    left: 26px;
    bottom: 8px;
    font-size: 1.9rem;
    letter-spacing: 8px;
}}
.book-sun {{
    position: absolute;
    top: 18px;
    right: 28px;
    width: 126px;
    height: 126px;
    object-fit: contain;
}}
.book-benny {{
    position: absolute;
    right: 28px;
    bottom: 18px;
    width: min(36%, 330px);
    max-height: 335px;
    object-fit: cover;
    object-position: center top;
    border-radius: 34px;
    border: 5px solid white;
    background: rgba(255,255,255,.14);
    box-shadow: 0 16px 28px rgba(40,57,65,.18);
}}
.burrow-copy {{
    max-width: 58%;
    position: relative;
    z-index: 2;
}}
.burrow-bubble {{
    display:inline-block;
    background:#fff;
    border:4px solid #2f2936;
    border-radius:24px;
    padding:.65rem 1rem;
    font-weight:900;
    box-shadow:5px 6px 0 #2f2936;
    margin-bottom:1rem;
}}
.rainbow-burrow-title {{
    font-size: clamp(2.8rem, 7vw, 5.2rem);
    line-height: .9;
    letter-spacing: -.055em;
    margin: .2rem 0 1rem;
    font-weight: 1000;
    -webkit-text-stroke: 3px #241e2a;
    paint-order: stroke fill;
    text-shadow: 0 5px 0 rgba(255,255,255,.95), 0 9px 0 rgba(47,41,54,.13);
}}
.rainbow-burrow-title .y {{ color:#ffd735; }}
.rainbow-burrow-title .b {{ color:#4ca9f7; }}
.rainbow-burrow-title .r {{ color:#ff5545; }}
.rainbow-burrow-title .o {{ color:#ff9d3b; }}
.rainbow-burrow-title .g {{ color:#62c64a; }}
.rainbow-burrow-title .p {{ color:#a65cc7; }}
.burrow-copy-box {{
    max-width: 620px;
    background: rgba(255,255,255,.94);
    border: 4px solid white;
    border-radius: 24px;
    padding: 1rem 1.2rem;
    font-size: 1.04rem;
    line-height: 1.55;
    font-weight: 750;
    color: #51475a;
    box-shadow: 0 7px 0 rgba(57,45,66,.08);
}}
.bookshelf-wrap {{
    margin-top: .8rem;
    background: linear-gradient(180deg,#fff8df 0%,#fff9ef 100%);
    border: 6px solid white;
    border-radius: 34px;
    padding: 1.2rem;
    box-shadow: 0 12px 0 rgba(65,53,74,.06), 0 24px 40px rgba(56,77,91,.10);
}}
.bookshelf-top {{
    background: linear-gradient(90deg,#ffde79,#ffc974,#ffb0c6,#b6e7ff,#c5f2a1);
    color:#2f2936;
    border-radius: 22px;
    padding: .85rem 1rem;
    font-weight: 900;
    font-size: 1.15rem;
    margin-bottom: 1rem;
    border:4px solid white;
}}
.book-card {{
    position:relative;
    background: linear-gradient(180deg,#e9f8ff 0%,#fffdf8 55%,#f0ffd9 100%);
    border: 5px solid white;
    border-radius: 28px;
    padding: 1rem;
    box-shadow: 0 8px 0 rgba(65,53,74,.06), 0 14px 25px rgba(56,77,91,.10);
    height: 100%;
}}
.book-card:before {{
    content:"☁️   ☁️";
    position:absolute;
    top:10px;
    left:0;
    right:0;
    text-align:center;
    opacity:.8;
}}
.book-card h3 {{
    margin:.55rem 0 .3rem;
    font-size:1.45rem;
    line-height:1.05;
}}
.book-card p {{
    color:#5d5365;
    line-height:1.45;
    font-weight:700;
}}
.skill-pill {{
    display:inline-block;
    margin:.2rem .25rem .15rem 0;
    padding:.33rem .6rem;
    border-radius:999px;
    border:3px solid white;
    background:#fff;
    font-weight:800;
    font-size:.82rem;
    box-shadow: 0 4px 0 rgba(65,53,74,.06);
}}
.note-box {{
    margin-top: 1rem;
    background: linear-gradient(135deg,#fff7de,#ffeaf4);
    border-radius: 24px;
    border:4px solid white;
    padding: 1.1rem 1.2rem;
    box-shadow:0 8px 0 rgba(71,55,84,.07);
}}
@media (max-width: 800px) {{
    .book-burrow-hero {{ padding:1.5rem 1rem 1.25rem; min-height:auto; }}
    .burrow-copy {{ max-width:100%; }}
    .book-benny {{
        position:relative;
        right:auto;
        bottom:auto;
        display:block;
        width:min(84%,320px);
        margin:1rem auto .2rem;
    }}
    .book-sun {{ width:88px; height:88px; top:12px; right:12px; }}
}}
</style>

<div class="book-burrow-hero">
  <img class="book-sun" src="{sun}" alt="Benny smiling sun">
  <div class="burrow-copy">
    <div class="burrow-bubble">🐰 Welcome to Benny's Book Burrow!</div>
    <div class="rainbow-burrow-title">
      <span class="y">Book</span> <span class="b">Burrow</span>
    </div>
    <div class="burrow-copy-box">
      Snuggle into Benny's colorful bookshelf! Explore each book, spot favorite covers,
      and choose the next learning adventure you want to hop into.
    </div>
  </div>
  <img class="book-benny" src="{benny}" alt="Benny the Bunny">
</div>

<div class="bookshelf-wrap">
  <div class="bookshelf-top">📚 Benny's Story Shelf</div>
</div>
""", unsafe_allow_html=True)

cols = st.columns(2, gap="large")
for i, book in enumerate(BOOKS):
    with cols[i % 2]:
        cover = COVERS / book["cover"]
        st.markdown('<div class="book-card">', unsafe_allow_html=True)
        if cover.exists():
            st.image(str(cover), use_container_width=True)
        st.markdown(f"### {book['title']}")
        st.write(book["description"])
        for skill in book["skills"]:
            st.markdown(f'<span class="skill-pill">{skill}</span>', unsafe_allow_html=True)
        st.markdown("<div style='height:.45rem'></div>", unsafe_allow_html=True)
        link = PURCHASE_LINKS.get(book["title"], "")
        if link:
            st.link_button("🛍️ Bring this book home", link, use_container_width=True)
        else:
            st.button("🛍️ Book link coming soon", disabled=True, use_container_width=True, key=f"book_{i}")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="note-box">
  <strong>🐰 Benny says:</strong> “Every book in my burrow can connect to games, read-alongs,
  and fun learning adventures!”
</div>
""", unsafe_allow_html=True)
