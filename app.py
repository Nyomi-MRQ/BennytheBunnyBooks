import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Benny the Bunny | Children's Book Series",
    page_icon="🐰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- BRAND SETTINGS ----------
SITE_NAME = "Benny the Bunny"
TAGLINE = "Little adventures. Big imagination."
TIKTOK_URL = "https://www.tiktok.com/"
INSTAGRAM_URL = "https://www.instagram.com/"
LINKTREE_URL = "https://linktr.ee/bennythebunnybooks"

# Replace these when your books are published / listed.
BOOK_1_URL = "#"
BOOK_2_URL = "#"
CONTACT_EMAIL = "your@email.com"

st.markdown("""
<style>
    .stApp {
        background:
          radial-gradient(circle at 10% 10%, rgba(255,221,237,.65), transparent 28%),
          radial-gradient(circle at 90% 15%, rgba(216,236,255,.75), transparent 30%),
          linear-gradient(180deg, #fffdf8 0%, #fff7fb 50%, #f7fbff 100%);
        color: #352d3b;
    }

    header[data-testid="stHeader"] { background: rgba(0,0,0,0); }
    div[data-testid="stToolbar"] { visibility: hidden; height: 0%; position: fixed; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }

    .block-container {
        max-width: 1120px;
        padding-top: 1.2rem;
        padding-bottom: 4rem;
    }

    .nav {
        display:flex;
        justify-content:space-between;
        align-items:center;
        gap:1rem;
        padding:.6rem 0 1.4rem 0;
        flex-wrap:wrap;
    }
    .brand {
        font-size:1.3rem;
        font-weight:900;
        letter-spacing:-.02em;
    }
    .navlinks a {
        text-decoration:none;
        color:#52485a !important;
        font-weight:700;
        margin-left:1rem;
        font-size:.92rem;
    }

    .hero {
        background: rgba(255,255,255,.84);
        border: 2px solid rgba(255,255,255,.9);
        box-shadow: 0 20px 60px rgba(108,77,121,.10);
        border-radius: 34px;
        padding: 3.2rem 2.6rem;
        margin-bottom: 2rem;
        overflow:hidden;
        position:relative;
    }
    .hero:after {
        content:"🐰";
        position:absolute;
        right:5%;
        top:6%;
        font-size:9rem;
        transform: rotate(7deg);
        filter: drop-shadow(0 12px 14px rgba(0,0,0,.08));
    }
    .eyebrow {
        display:inline-block;
        background:#ffe5f0;
        color:#7c3a5c;
        border-radius:999px;
        padding:.45rem .85rem;
        font-size:.82rem;
        font-weight:800;
        margin-bottom:1rem;
    }
    .hero h1 {
        font-size:clamp(3rem, 7vw, 5.5rem);
        line-height:.92;
        letter-spacing:-.055em;
        margin:.2rem 0 1rem 0;
        max-width:700px;
    }
    .hero p {
        font-size:1.18rem;
        max-width:620px;
        line-height:1.65;
        color:#655b6b;
        margin-bottom:1.6rem;
    }

    .btn {
        display:inline-block;
        background:#6d4aff;
        color:white !important;
        padding:.9rem 1.25rem;
        border-radius:14px;
        font-weight:800;
        text-decoration:none;
        margin-right:.55rem;
        margin-bottom:.55rem;
        box-shadow:0 8px 20px rgba(109,74,255,.22);
    }
    .btn.secondary {
        background:white;
        color:#4f3f58 !important;
        border:1px solid #eadfec;
        box-shadow:none;
    }

    .section-title {
        font-size:2.25rem;
        letter-spacing:-.04em;
        margin:2.6rem 0 .4rem 0;
    }
    .section-sub {
        color:#766d7b;
        font-size:1.04rem;
        margin-bottom:1.35rem;
    }

    .card {
        background:rgba(255,255,255,.92);
        border:1px solid #eee5ef;
        border-radius:24px;
        padding:1.5rem;
        height:100%;
        box-shadow:0 10px 30px rgba(80,57,87,.07);
    }
    .card .emoji { font-size:3.4rem; }
    .card h3 {
        margin:.5rem 0 .35rem 0;
        font-size:1.35rem;
    }
    .card p {
        color:#706675;
        line-height:1.55;
    }
    .mini-link {
        font-weight:800;
        text-decoration:none;
        color:#6d4aff !important;
    }

    .benny-panel {
        background:linear-gradient(135deg,#ede8ff,#ffeaf3);
        border-radius:30px;
        padding:2rem;
        margin-top:1.2rem;
    }
    .benny-panel h2 { margin-top:0; }

    .activity {
        background:#fff;
        border-radius:20px;
        border:1px dashed #d7c9dc;
        padding:1.2rem;
        margin-bottom:.8rem;
    }

    .quote {
        text-align:center;
        font-size:1.8rem;
        font-weight:900;
        letter-spacing:-.03em;
        padding:3rem 1rem;
    }

    .footer {
        text-align:center;
        color:#877c8b;
        font-size:.9rem;
        padding-top:2rem;
    }

    @media (max-width: 760px) {
        .block-container { padding-left:1rem; padding-right:1rem; }
        .hero { padding:2rem 1.4rem 8rem 1.4rem; }
        .hero:after {
            font-size:6rem;
            right:8%;
            top:auto;
            bottom:.5rem;
        }
        .navlinks { display:none; }
    }
</style>
""", unsafe_allow_html=True)

# ---------- TOP NAV ----------
st.markdown(f"""
<div class="nav">
  <div class="brand">🐰 {SITE_NAME}</div>
  <div class="navlinks">
    <a href="#books">Books</a>
    <a href="#meet-benny">Meet Benny</a>
    <a href="#activities">Activities</a>
    <a href="#follow">Follow</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown(f"""
<div class="hero">
  <span class="eyebrow">Children's Book Series</span>
  <h1>{SITE_NAME}</h1>
  <p><strong>{TAGLINE}</strong><br>
  Follow Benny through colorful stories made for curious little readers,
  family reading time, imagination, and fun.</p>
  <a class="btn" href="#books">Explore the Books</a>
  <a class="btn secondary" href="#follow">Follow Benny</a>
</div>
""", unsafe_allow_html=True)

# ---------- BOOKS ----------
st.markdown('<div id="books"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">📚 The Benny Books</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-sub">Build the series here as each Benny adventure is released.</p>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.markdown(f"""
    <div class="card">
      <div class="emoji">🌈</div>
      <h3>Benny the Bunny: Colors</h3>
      <p>A playful first adventure for learning and finding colors with Benny.</p>
      <a class="mini-link" href="{BOOK_1_URL}">View book →</a>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
      <div class="emoji">🔎</div>
      <h3>Find the Color</h3>
      <p>An interactive companion idea where little readers can spot, point, and discover.</p>
      <a class="mini-link" href="{BOOK_2_URL}">Coming soon →</a>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
      <div class="emoji">✨</div>
      <h3>More Adventures</h3>
      <p>New Benny stories, printable activities, and surprises can grow right here.</p>
      <span class="mini-link">In development</span>
    </div>
    """, unsafe_allow_html=True)

# ---------- MEET BENNY ----------
st.markdown('<div id="meet-benny"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="benny-panel">
  <h2>🐇 Meet Benny</h2>
  <p>Benny is a curious little bunny who loves discovering the world one small adventure at a time.
  His stories are designed to make learning feel playful, colorful, and easy to share together.</p>
  <p><strong>Benny loves:</strong> colors, exploring, asking questions, spotting little details,
  and turning everyday moments into adventures.</p>
</div>
""", unsafe_allow_html=True)

# ---------- ACTIVITIES ----------
st.markdown('<div id="activities"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">🎨 Play & Learn</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-sub">This can become the part of the website parents and kids come back to.</p>', unsafe_allow_html=True)

a1, a2 = st.columns(2, gap="large")
with a1:
    st.markdown("""
    <div class="activity"><strong>🖍️ Coloring Pages</strong><br>
    Free Benny pages can be added as PDF downloads.</div>
    <div class="activity"><strong>🔍 Find-the-Color Game</strong><br>
    Turn the book idea into a simple web game later.</div>
    """, unsafe_allow_html=True)
with a2:
    st.markdown("""
    <div class="activity"><strong>📖 Read-Along Videos</strong><br>
    Embed your TikTok or YouTube storytelling clips.</div>
    <div class="activity"><strong>🐰 Bunny Club</strong><br>
    Later, collect parent emails for new-book updates and freebies.</div>
    """, unsafe_allow_html=True)

# ---------- SOCIAL ----------
st.markdown('<div id="follow"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">📱 Follow Benny</h2>', unsafe_allow_html=True)
st.markdown("""
<p class="section-sub">Use TikTok to show the books coming to life — drawing pages, reading clips,
color challenges, behind-the-scenes creation, and new-book reveals.</p>
""", unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)
with s1:
    st.link_button("🎵 TikTok", TIKTOK_URL, use_container_width=True)
with s2:
    st.link_button("📸 Instagram", INSTAGRAM_URL, use_container_width=True)
with s3:
    st.link_button("🔗 Current Linktree", LINKTREE_URL, use_container_width=True)

st.markdown("""
<div class="quote">“Every little discovery can become a big adventure.” 🐰</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="footer">
  © Benny the Bunny / MO.Ent · Made with imagination 💗<br>
  Contact: {CONTACT_EMAIL}
</div>
""", unsafe_allow_html=True)
