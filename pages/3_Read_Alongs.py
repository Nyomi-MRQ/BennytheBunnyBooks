import streamlit as st
from site_utils import page_setup, footer, READALONG_LINKS, benny_uri, sun_uri, cover_html, pills
from data import BOOKS

page_setup("Story Theater")

benny = benny_uri()
sun = sun_uri()

st.html(f"""
<style>
.theater-hero {{
    position: relative;
    overflow: hidden;
    min-height: 395px;
    border-radius: 40px;
    border: 6px solid white;
    padding: 2.5rem 2.2rem 2.2rem;
    background:
        linear-gradient(180deg,#8a5dff 0%,#bc90ff 30%,#ff9ed2 53%,#74d5ff 54%,#d8f4ff 76%,#9ae27a 77%,#63bb55 100%);
    box-shadow: 0 15px 0 rgba(65,53,74,.08), 0 28px 55px rgba(56,77,91,.16);
    margin-bottom: 1.7rem;
}}
.theater-curtain-left, .theater-curtain-right {{
    position:absolute;
    top:0;
    width:86px;
    height:100%;
    background: linear-gradient(90deg,#d62a4d 0%,#f64f71 45%,#d62a4d 100%);
    z-index:1;
    box-shadow: inset -8px 0 0 rgba(120,19,39,.22), inset 8px 0 0 rgba(255,255,255,.18);
}}
.theater-curtain-left {{ left:0; border-radius: 30px 0 0 30px; }}
.theater-curtain-right {{ right:0; border-radius: 0 30px 30px 0; }}
.theater-sun {{
    position:absolute;
    top:18px;
    right:104px;
    width:120px;
    height:120px;
    object-fit:contain;
    z-index:2;
}}
.theater-benny {{
    position:absolute;
    right:32px;
    bottom:16px;
    width:min(35%,300px);
    max-height:320px;
    object-fit:cover;
    object-position:center top;
    border:5px solid white;
    border-radius:34px;
    background:rgba(255,255,255,.14);
    z-index:2;
}}
.theater-copy {{
    position:relative;
    z-index:3;
    max-width:58%;
}}
.theater-bubble {{
    display:inline-block;
    background:#fff;
    border:4px solid #2f2936;
    border-radius:24px;
    padding:.65rem 1rem;
    font-weight:900;
    box-shadow:5px 6px 0 #2f2936;
    margin-bottom:1rem;
}}
.theater-title {{
    font-size: clamp(2.8rem, 7vw, 5rem);
    line-height: .9;
    letter-spacing: -.055em;
    margin: .2rem 0 1rem;
    font-weight: 1000;
    -webkit-text-stroke: 3px #241e2a;
    paint-order: stroke fill;
    text-shadow: 0 5px 0 rgba(255,255,255,.95), 0 9px 0 rgba(47,41,54,.13);
}}
.theater-title .r {{ color:#ff5545; }}
.theater-title .o {{ color:#ff9d3b; }}
.theater-title .y {{ color:#ffd735; }}
.theater-title .g {{ color:#62c64a; }}
.theater-title .b {{ color:#4ca9f7; }}
.theater-title .p {{ color:#a65cc7; }}
.theater-copy-box {{
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
.feature-marquee {{
    margin-top: .9rem;
    background: rgba(255,255,255,.9);
    border:4px solid white;
    border-radius:22px;
    padding:.8rem 1rem;
    font-weight:900;
    color:#44394f;
}}
.stage-wrap {{
    background: linear-gradient(180deg,#fff7df 0%,#fffdf8 100%);
    border:6px solid white;
    border-radius:34px;
    padding: 1.2rem;
    box-shadow: 0 12px 0 rgba(65,53,74,.06), 0 24px 40px rgba(56,77,91,.10);
}}
.stage-top {{
    background: linear-gradient(90deg,#ff8dbd,#ffcb78,#fff39f,#96e2ff,#cba7ff);
    color:#2f2936;
    border-radius: 22px;
    padding: .85rem 1rem;
    font-weight: 900;
    font-size: 1.15rem;
    margin-bottom: 1rem;
    border:4px solid white;
}}
.read-card {{
    position:relative;
    background: linear-gradient(180deg,#e6f8ff 0%,#fffdf8 55%,#f0ffd9 100%);
    border: 5px solid white;
    border-radius: 28px;
    padding: 1rem;
    box-shadow: 0 8px 0 rgba(65,53,74,.06), 0 14px 25px rgba(56,77,91,.10);
    height: 100%;
}}
.read-card:before {{
    content:"⭐   ✨   ⭐";
    position:absolute;
    top:10px;
    left:0;
    right:0;
    text-align:center;
    opacity:.8;
}}
.read-card h3 {{
    margin:.55rem 0 .35rem;
    font-size:1.4rem;
    line-height:1.05;
}}
.read-card p {{
    color:#5d5365;
    line-height:1.45;
    font-weight:700;
}}
.badge-pill {{
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
.preview-note {{
    margin-top: 1rem;
    background: linear-gradient(135deg,#fff7de,#ffeaf4);
    border-radius: 24px;
    border:4px solid white;
    padding: 1.1rem 1.2rem;
    box-shadow:0 8px 0 rgba(71,55,84,.07);
}}
@media (max-width: 800px) {{
    .theater-hero {{ padding:1.5rem 1rem 1.25rem; min-height:auto; }}
    .theater-copy {{ max-width:100%; }}
    .theater-curtain-left, .theater-curtain-right {{ width:34px; }}
    .theater-sun {{ width:84px; height:84px; top:12px; right:42px; }}
    .theater-benny {{
        position:relative;
        right:auto;
        bottom:auto;
        display:block;
        width:min(82%,300px);
        margin:1rem auto .2rem;
    }}
}}
</style>

<div class="theater-hero">
  <div class="theater-curtain-left"></div>
  <div class="theater-curtain-right"></div>
  <img class="theater-sun" src="{sun}" alt="Benny smiling sun">
  <div class="theater-copy">
    <div class="theater-bubble">🎬 Welcome to Benny's Story Theater!</div>
    <div class="theater-title">
      <span class="b">Story</span> <span class="p">Theater</span>
    </div>
    <div class="theater-copy-box">
      Step into Benny's stage and watch stories come alive! Explore read-alongs with
      narration, highlighted words, sound cues, and fun pauses to join in.
    </div>
    <div class="feature-marquee">🎙️ Narration • ✨ Highlighted words • ⏸️ Pause-and-answer moments • 🐰 Benny fun</div>
  </div>
  <img class="theater-benny" src="{benny}" alt="Benny the Bunny">
</div>

<h2 class="section-title">🍿 Tonight's Benny Features</h2>
<div class="sub">Grab a snack and a cozy spot — the show is about to begin!</div>
""")

for i, book in enumerate(BOOKS):
    with st.container(key=f"readcard_{i}"):
        left, right = st.columns([1, 2], gap="large", vertical_alignment="center")
        with left:
            st.html(cover_html(book))
        with right:
            st.html(
                f'<div class="book-title">{book["title"]} — Read-Along</div>'
                f'<div class="book-desc">{book["readalong"]}</div>'
                + pills(book["readalong_badges"], "badge-pill")
            )
            c1, c2 = st.columns(2)
            link = READALONG_LINKS.get(book["title"], "")
            if link:
                c1.link_button("🎬 Watch the read-along", link, width="stretch")
            else:
                c1.button("🎬 Read-along coming soon", disabled=True, width="stretch", key=f"buy_{i}")
            with c2:
                st.page_link("pages/2_Reading_Garden.py", label="Play the game", icon="🎮",
                             query_params={"game": book["slug"]}, width="stretch")

st.html("""
<div class="preview-note">
  <strong>🐰 Benny says:</strong> “These story shows will help children listen, read along,
  and have fun with each book!”
</div>
""")

footer()
