from pathlib import Path
from functools import lru_cache
import base64
import html
import json
import mimetypes
import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
COVERS = ASSETS / "covers"

# ---------------------------------------------------------------------------
# LINKS — paste your real links between the quotes. Anything left empty
# simply stays hidden (or shows "coming soon") on the website.
# ---------------------------------------------------------------------------
PURCHASE_LINKS = {
    "Benny's Colors": "",
    "Benny's Counting Adventure": "",
    "Benny's ABC's": "",
    "The 5 Senses": "",
}

READALONG_LINKS = {
    "Benny's Colors": "",
    "Benny's Counting Adventure": "",
    "Benny's ABC's": "",
    "The 5 Senses": "",
}

# Shown as buttons in the footer of every page (this is what replaces Linktree).
SOCIAL_LINKS = {
    "📚 All Benny books on Amazon": "",
    "🎵 Benny on TikTok": "",
    "📸 Benny on Instagram": "",
    "✉️ Email Benny's team": "",  # use the form  mailto:you@example.com
}

PAGES = [
    ("app.py", "Home", "🏡"),
    ("pages/1_Books.py", "Books", "📚"),
    ("pages/2_Reading_Garden.py", "Games", "🌼"),
    ("pages/3_Read_Alongs.py", "Story Theater", "🎬"),
    ("pages/4_Grown_Ups.py", "Grown-Ups", "💗"),
]


# ---------------------------------------------------------------------------
# Page frame
# ---------------------------------------------------------------------------
def page_setup(title: str):
    st.set_page_config(
        page_title=f"{title} | Benny the Bunny Books",
        page_icon="🐰",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    add_css()
    nav()


def nav():
    with st.container(horizontal=True, key="benny_nav", horizontal_alignment="center", gap="small"):
        for path, label, icon in PAGES:
            st.page_link(path, label=label, icon=icon)


def footer():
    links = {label: url for label, url in SOCIAL_LINKS.items() if url}
    st.html(
        f"""
        <div class="benny-footer-top">
          <img src="{sun_uri()}" alt="" class="footer-sun">
          <div><strong>Benny the Bunny Books</strong><br>
          Bright, gentle picture books and free learning games for little readers.</div>
        </div>
        """
    )
    if links:
        with st.container(horizontal=True, key="benny_footer_links", horizontal_alignment="center"):
            for label, url in links.items():
                st.link_button(label, url)
    st.html('<div class="benny-footer-small">Made with love for little readers 🐰 No sign-ups and no ads — just reading fun.</div>')


# ---------------------------------------------------------------------------
# Images (embedded once, cached so pages load fast)
# ---------------------------------------------------------------------------
@lru_cache(maxsize=32)
def asset_data_uri(path: Path) -> str:
    if not path.exists():
        return ""
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    if path.suffix == ".svg":
        mime = "image/svg+xml"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


def benny_uri() -> str:
    return asset_data_uri(ASSETS / "benny_character.jpg")


def sun_uri() -> str:
    return asset_data_uri(ASSETS / "benny_sun.svg")


def cover_uri(book: dict) -> str:
    return asset_data_uri(COVERS / book["cover"])


def cover_html(book: dict, cls: str = "cover-img") -> str:
    return f'<img class="{cls}" src="{cover_uri(book)}" alt="Cover of {html.escape(book["title"])}">'


def pills(items, cls="skill-pill") -> str:
    return "".join(f'<span class="{cls}">{html.escape(i)}</span>' for i in items)


# ---------------------------------------------------------------------------
# Read-aloud buttons (uses the device's built-in voice, no data sent anywhere)
# ---------------------------------------------------------------------------
_SPEAK_JS = """
<script>
function bennySpeak(t){
  try{
    const s = window.speechSynthesis; s.cancel();
    const u = new SpeechSynthesisUtterance(t);
    u.rate = 0.82; u.pitch = 1.1;
    const v = s.getVoices().find(v => /en(-|_)US/i.test(v.lang) && /female|samantha|google us/i.test(v.name))
           || s.getVoices().find(v => /^en/i.test(v.lang));
    if (v) u.voice = v;
    s.speak(u);
  }catch(e){}
}
</script>
<style>
body{margin:0;font-family:"Source Sans Pro",system-ui,sans-serif}
.row{display:flex;flex-wrap:wrap;gap:10px}
button{flex:1 1 140px;padding:12px 14px;border:4px solid #fff;border-radius:16px;
  font-weight:800;font-size:17px;cursor:pointer;background:#6d4aff;color:#fff;
  box-shadow:0 5px 0 #4d34b4;transition:transform .08s}
button:active{transform:translateY(3px);box-shadow:0 2px 0 #4d34b4}
button.big{font-size:20px;flex-basis:90px}
</style>
"""


def speak_buttons(items, height=None, big=False):
    """items: list of (label, text_to_say). Renders them in one light-weight row."""
    btns = "".join(
        f'<button class="{"big" if big else ""}" onclick=\'bennySpeak({html.escape(json.dumps(text), quote=True)})\'>'
        f"{html.escape(label)}</button>"
        for label, text in items
    )
    if height is None:
        per_row = 4 if big else 2
        height = 66 * max(1, -(-len(items) // per_row)) + 6
    components.html(_SPEAK_JS + f'<div class="row">{btns}</div>', height=height)


def speak_button(text: str, label: str = None, key: str = "speak"):
    speak_buttons([(label or f"🔊 Hear: {text}", text)], height=66)


# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
def add_css():
    st.markdown(
        """
        <style>
        :root {
            --benny-sky: #77d7ff;
            --benny-sky-light: #d9f5ff;
            --benny-grass: #79cf5d;
            --benny-yellow: #ffd735;
            --benny-red: #ff5545;
            --benny-orange: #ff9d3b;
            --benny-green: #62c64a;
            --benny-blue: #4ca9f7;
            --benny-purple: #a65cc7;
            --benny-pink: #ff8fc4;
            --benny-ink: #2f2936;
            --benny-cream: #fffdf8;
        }

        .stApp {
            background:
                radial-gradient(circle at 8% 8%, rgba(255,255,255,.94) 0 46px, transparent 48px),
                radial-gradient(circle at 16% 8%, rgba(255,255,255,.94) 0 58px, transparent 60px),
                radial-gradient(circle at 83% 11%, rgba(255,255,255,.92) 0 50px, transparent 52px),
                linear-gradient(180deg, var(--benny-sky-light) 0%, #f7fcff 44%, #fff9de 70%, #efffdc 100%);
            color: var(--benny-ink);
        }
        .stApp, .stApp p, .stApp li, .stApp h1, .stApp h2, .stApp h3 { color: var(--benny-ink); }

        header[data-testid="stHeader"] { background: rgba(0,0,0,0); }
        #MainMenu, footer, [data-testid="stSidebarCollapsedControl"], [data-testid="stToolbar"] { display: none !important; }
        .block-container { max-width: 1180px; padding-top: 1rem; padding-bottom: 3rem; }

        /* ---------- TOP NAV ---------- */
        .st-key-benny_nav {
            background: rgba(255,255,255,.88);
            border: 4px solid white;
            border-radius: 999px;
            padding: .35rem .5rem;
            box-shadow: 0 6px 0 rgba(65,53,74,.06), 0 12px 24px rgba(56,77,91,.08);
            margin-bottom: 1.1rem;
            position: sticky; top: .4rem; z-index: 50;
            backdrop-filter: blur(6px);
        }
        .st-key-benny_nav div[data-testid="stPageLink"] a {
            background: transparent !important;
            box-shadow: none !important;
            border: 0 !important;
            color: var(--benny-ink) !important;
            padding: .35rem .8rem !important;
            border-radius: 999px !important;
        }
        .st-key-benny_nav div[data-testid="stPageLink"] a p { color: var(--benny-ink) !important; font-weight: 900 !important; font-size: 1rem !important; }
        .st-key-benny_nav div[data-testid="stPageLink"] a:hover { background: #fff4a8 !important; }
        .st-key-benny_nav div[data-testid="stPageLink"] a[aria-current="page"],
        .st-key-benny_nav div[data-testid="stPageLink-NavLink"][aria-current="page"] { background: #efe9ff !important; }

        /* ---------- BENNY BRAND HERO ---------- */
        .brand-hero {
            position: relative;
            overflow: hidden;
            border-radius: 40px;
            border: 6px solid white;
            padding: 2.5rem 2.6rem 2.6rem;
            background:
                radial-gradient(circle at 13% 15%, rgba(255,255,255,.96) 0 42px, transparent 44px),
                radial-gradient(circle at 21% 13%, rgba(255,255,255,.96) 0 58px, transparent 60px),
                linear-gradient(180deg, #67d0ff 0%, #ccefff 55%, #a7e57f 56%, #67bf55 100%);
            box-shadow: 0 14px 0 rgba(65,53,74,.07), 0 28px 55px rgba(56,77,91,.15);
            margin-bottom: 1rem;
            isolation: isolate;
        }
        .brand-hero::after {
            content: "🌼   🌸   🌷   🌼   🌸";
            position: absolute; left: 34px; bottom: 14px;
            font-size: 1.65rem; letter-spacing: 5px; z-index: 0;
        }
        .hero-grid {
            position: relative; z-index: 2;
            display: grid;
            grid-template-columns: minmax(0, 1.08fr) minmax(300px, .92fr);
            align-items: center;
            gap: clamp(1.6rem, 4vw, 4rem);
            min-height: 440px;
        }
        .hero-copy-column { display: flex; flex-direction: column; align-items: flex-start; justify-content: center; min-width: 0; }
        .speech-bubble {
            display: inline-block; max-width: 620px;
            background: #fff; border: 4px solid var(--benny-ink); border-radius: 24px;
            padding: .72rem 1.05rem; font-weight: 900; font-size: 1.05rem; line-height: 1.35;
            box-shadow: 5px 6px 0 var(--benny-ink); margin-bottom: 1.25rem;
            animation: bob 3.2s ease-in-out infinite;
        }
        .rainbow-title, .rainbow-burrow-title, .theater-title {
            font-size: clamp(3.6rem, 7.2vw, 6.6rem);
            line-height: .9; letter-spacing: -.03em;
            margin: 0 0 1.15rem; font-weight: 1000;
            -webkit-text-stroke: 3px #241e2a; paint-order: stroke fill;
            text-shadow: 0 5px 0 rgba(255,255,255,.98), 0 9px 0 rgba(47,41,54,.13);
        }
        .r { color: var(--benny-red); } .o { color: var(--benny-orange); } .y { color: var(--benny-yellow); }
        .g { color: var(--benny-green); } .b { color: var(--benny-blue); } .p { color: var(--benny-purple); }

        .hero-copy-box {
            width: min(100%, 650px);
            background: rgba(255,255,255,.95); border: 4px solid white; border-radius: 24px;
            padding: 1.05rem 1.2rem; font-size: 1.08rem; line-height: 1.55; font-weight: 750;
            color: #51475a; box-shadow: 0 7px 0 rgba(57,45,66,.08);
        }
        .hero-character-column { display: flex; align-items: center; justify-content: center; min-width: 0; padding-top: 2.2rem; }
        .benny-frame {
            width: min(100%, 360px); aspect-ratio: 4 / 5;
            border: 6px solid white; border-radius: 38px; overflow: hidden;
            background: rgba(255,255,255,.28);
            box-shadow: 0 14px 0 rgba(65,53,74,.08), 0 24px 36px rgba(43,62,66,.18);
            transform: rotate(2deg);
        }
        .hero-benny-img { display: block; width: 100%; height: 100%; object-fit: cover; object-position: center top; }
        .hero-sun-img {
            position: absolute; top: 14px; right: 24px; width: 120px; height: 120px; z-index: 3;
            filter: drop-shadow(0 8px 10px rgba(0,0,0,.10));
            animation: spin 40s linear infinite;
        }
        @keyframes bob { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-5px); } }
        @keyframes spin { to { transform: rotate(360deg); } }
        @media (prefers-reduced-motion: reduce) { .speech-bubble, .hero-sun-img { animation: none; } }

        .section-title { font-size: 2.3rem; font-weight: 1000; letter-spacing: -.035em; margin: 2.2rem 0 .2rem; color: var(--benny-ink); }
        .sub { color:#6b6171; font-size:1.08rem; margin-bottom:1rem; font-weight:700; }

        /* ---------- HOME ADVENTURE CARDS ---------- */
        .adventure-card {
            position: relative; overflow: hidden;
            height: 410px;
            display: flex; flex-direction: column; align-items: center;
            border-radius: 32px; border: 6px solid white;
            padding: 1.4rem 1.2rem 1.1rem; text-align: center;
            box-shadow: 0 10px 0 rgba(65,53,74,.08), 0 19px 35px rgba(56,77,91,.12);
            transition: transform .15s;
        }
        .adventure-card:hover { transform: translateY(-4px) rotate(-.5deg); }
        .books-card { background: linear-gradient(180deg,#ffd957 0%,#ffb95a 45%,#9cde76 46%,#68bf57 100%); }
        .garden-card { background: linear-gradient(180deg,#72d7ff 0%,#c6f1ff 46%,#9ee37a 47%,#63bb55 100%); }
        .theater-card { background: linear-gradient(180deg,#855bff 0%,#bd92ff 43%,#ff90c9 62%,#664099 100%); }
        .card-scene { font-size: 4.6rem; line-height: 1; margin: 1.2rem 0 .4rem; filter: drop-shadow(0 8px 4px rgba(0,0,0,.10)); }
        .adventure-card h2 { font-size:1.7rem; line-height:1.05; margin:.3rem 0 .7rem; font-weight:1000; min-height: 2.1em; display:flex; align-items:center; }
        .theater-card h2 { color:white !important; text-shadow:0 3px 0 rgba(58,38,84,.35); }
        .adventure-card p {
            margin-top: auto;
            background:rgba(255,255,255,.93); border-radius:19px; padding:.8rem .85rem;
            color:#5e5366; font-weight:750; line-height:1.45; width: 100%;
        }

        /* Big friendly page-link buttons (outside the nav) */
        div[data-testid="stPageLink"] a {
            border-radius: 18px !important;
            border: 4px solid white !important;
            background: #6f4cff !important;
            padding: .7rem 1rem !important;
            box-shadow: 0 5px 0 #4d34b4 !important;
            justify-content: center !important;
        }
        div[data-testid="stPageLink"] a p, div[data-testid="stPageLink"] a span { color: white !important; font-weight: 900 !important; font-size: 1.05rem !important; }

        /* ---------- BOOK COVERS & CARDS ---------- */
        .cover-img {
            display:block; width:100%; aspect-ratio: 3 / 4; object-fit: cover;
            border-radius: 18px; border: 5px solid white;
            box-shadow: 0 10px 0 rgba(65,53,74,.07), 0 16px 28px rgba(56,77,91,.14);
            transition: transform .15s;
        }
        .cover-img:hover { transform: translateY(-4px) rotate(-1deg); }
        .shelf-grid { display:grid; grid-template-columns: repeat(4, 1fr); gap: 1.2rem; margin-bottom: 1rem; }
        .shelf-title { font-weight: 900; font-size: 1.1rem; margin: .7rem 0 .1rem; }
        .shelf-meta { color:#6b6171; font-size:.92rem; font-weight:700; }

        [class*="st-key-bookcard"], [class*="st-key-readcard"] {
            background: linear-gradient(180deg,#e9f8ff 0%,#fffdf8 55%,#f0ffd9 100%);
            border: 5px solid white; border-radius: 28px; padding: 1.2rem;
            box-shadow: 0 8px 0 rgba(65,53,74,.06), 0 14px 25px rgba(56,77,91,.10);
        }
        [class*="st-key-readcard"] { margin-bottom: 1rem; }
        .skill-pill, .badge-pill {
            display:inline-block; margin:.2rem .3rem .15rem 0; padding:.3rem .7rem;
            border-radius:999px; border:3px solid white; background:#fff;
            font-weight:800; font-size:.85rem; box-shadow: 0 4px 0 rgba(65,53,74,.06);
        }
        .age-pill { background:#fff4a8; }
        .book-desc { color:#5d5365; line-height:1.5; font-weight:700; font-size:1.02rem; margin:.3rem 0 .6rem; }
        .book-title { font-size:1.6rem; font-weight:1000; line-height:1.1; margin:.2rem 0 .3rem; }

        .card, .premium, .parent-note, .score, .word {
            border: 4px solid white;
            box-shadow: 0 8px 0 rgba(71,55,84,.07), 0 16px 28px rgba(71,76,93,.08);
        }
        .card { background:rgba(255,255,255,.95); border-radius:25px; padding:1.35rem; height:100%; }
        .premium { background:linear-gradient(135deg,#fff8dd,#ffe9f5); border-radius:26px; padding:1.35rem 1.5rem; margin-top: 1.5rem; }
        .parent-note { background:#eef9ff; border-radius:22px; padding:1.2rem; margin-top: 1.5rem; }
        .score { background:#fff; border-radius:999px; padding:.7rem 1rem; font-weight:900; text-align:center; font-size:1.15rem; }
        .word { background:#fff; border-radius:25px; padding:1.3rem; text-align:center; font-size:2.4rem; font-weight:1000; margin-bottom:.6rem; }

        /* ---------- BUTTONS (readable on phones in dark mode too) ---------- */
        .stButton > button, .stLinkButton > a,
        .stButton > button:focus, .stButton > button:active {
            background: #ffffff !important;
            color: #33283b !important;
            border: 4px solid #6f4cff !important;
            border-radius: 18px !important;
            font-weight: 950 !important;
            font-size: 1.05rem !important;
            box-shadow: 0 5px 0 #d7cdfc !important;
            min-height: 56px !important;
            opacity: 1 !important;
            -webkit-text-fill-color: #33283b !important;
        }
        .stButton > button:hover, .stLinkButton > a:hover {
            background: #fff4a8 !important; border-color: #ffb93f !important;
        }
        .stButton > button p, .stLinkButton > a p, .stButton > button span, .stButton > button div {
            color: #33283b !important; -webkit-text-fill-color: #33283b !important; font-weight: 950 !important; font-size: 1.15rem !important;
        }
        .stButton > button[kind="primary"] { background: #6f4cff !important; border-color: white !important; box-shadow: 0 5px 0 #4d34b4 !important; }
        .stButton > button[kind="primary"] p { color: white !important; -webkit-text-fill-color: white !important; }
        .stButton > button:disabled {
            background: #f1eef6 !important; color: #746a7b !important; border-color: #d8d0df !important;
            -webkit-text-fill-color: #746a7b !important; box-shadow: none !important;
        }
        .stButton > button:disabled p { color: #746a7b !important; -webkit-text-fill-color: #746a7b !important; }

        /* ---------- TABS (bigger for little fingers) ---------- */
        [role="tablist"] { gap: .45rem !important; flex-wrap: wrap !important; border-bottom: 0 !important; overflow: visible !important; }
        [data-testid="stTab"] {
            background: #fff !important; border: 4px solid white !important; border-radius: 999px !important;
            padding: .45rem 1rem !important; height: auto !important; min-height: 48px;
            box-shadow: 0 4px 0 rgba(65,53,74,.08) !important; margin-bottom: .4rem;
        }
        [data-testid="stTab"] p { font-size: 1.1rem !important; font-weight: 900 !important; color: var(--benny-ink) !important; }
        [data-testid="stTab"][aria-selected="true"] { background: #ffe66e !important; }
        [role="tablist"] .react-aria-SelectionIndicator { display: none !important; }
        .stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] { display: none; }

        /* ---------- READING GARDEN ---------- */
        .reading-garden-hero {
            position: relative; overflow: hidden; min-height: 360px;
            border-radius: 38px; border: 6px solid white;
            padding: 4.4rem 2.6rem 3.2rem;
            background:
                radial-gradient(circle at 86% 14%, #ffe76d 0 65px, transparent 68px),
                linear-gradient(180deg,#6ed3ff 0%,#d0f3ff 48%,#ace984 49%,#67bf56 100%);
            box-shadow: 0 15px 0 rgba(65,53,74,.08), 0 27px 52px rgba(56,77,91,.15);
            margin-bottom: 1.2rem;
        }
        .reading-garden-hero:before { content: "☁️      🌈      ☁️"; position:absolute; top:16px; left:30px; font-size:2.2rem; }
        .reading-garden-hero:after { content:"🌼 🌷 🌸 🌼 🌷 🌸"; position:absolute; bottom:10px; left:28px; font-size:1.9rem; letter-spacing:8px; }
        .garden-copy { position: relative; z-index: 3; max-width: 60%; }
        .garden-title {
            font-size:clamp(2.8rem,6vw,4.6rem); font-weight:1000; line-height:.95; color:#fff !important;
            -webkit-text-stroke:2px #2d2734; paint-order:stroke fill;
            text-shadow:0 5px 0 rgba(47,41,54,.16); margin:0 0 .8rem;
        }
        .garden-intro {
            background:rgba(255,255,255,.94); border:4px solid white; border-radius:22px;
            padding:.95rem 1.05rem; font-weight:750; color:#51475a; line-height:1.5; max-width:620px;
        }
        .garden-benny-img {
            position:absolute; z-index:2; right:28px; bottom:16px;
            width:min(32%,300px); max-height:320px; object-fit:cover; object-position:center top;
            border:5px solid white; border-radius:32px; box-shadow:0 15px 28px rgba(45,67,70,.18);
        }
        .benny-says {
            background:#fffdf5; border:4px solid #2f2936; border-radius:23px;
            padding:.9rem 1.1rem; font-weight:900; color:#51475a;
            box-shadow:5px 6px 0 #2f2936; margin:1rem 0 1.2rem;
        }
        .lesson-note { background:#fff; border:4px solid #eef0f5; border-radius:19px; padding:.8rem 1rem; margin:.6rem 0 .8rem; font-weight:800; font-size:1.1rem; }
        .badge-row { display:flex; gap:.6rem; flex-wrap:wrap; justify-content:center; margin:.8rem 0; }
        .badge { background:#fff; border:4px solid white; border-radius:20px; padding:.6rem .9rem; font-weight:900; box-shadow:0 5px 0 rgba(65,53,74,.08); }
        .badge.locked { opacity:.45; filter: grayscale(1); }
        .count-row { font-size: 3rem; line-height: 1.3; letter-spacing: .15em; text-align:center; }
        .swatch { width: 90px; height: 90px; border-radius: 50%; margin: 0 auto .5rem; border: 5px solid #2f2936; }

        /* ---------- FOOTER ---------- */
        .benny-footer-top {
            margin-top: 3rem; display:flex; gap:1rem; align-items:center; justify-content:center;
            background: rgba(255,255,255,.9); border: 4px solid white; border-radius: 26px;
            padding: 1rem 1.2rem; font-weight: 700; color:#51475a; text-align:left;
            box-shadow: 0 8px 0 rgba(71,55,84,.06);
        }
        .footer-sun { width: 56px; height: 56px; }
        .benny-footer-small { text-align:center; color:#7a7080; font-size:.9rem; font-weight:700; margin-top:.8rem; }
        .st-key-benny_footer_links { margin-top: .8rem; }

        /* ---------- PHONES ---------- */
        @media (max-width: 800px) {
            .block-container { padding-left: .65rem; padding-right: .65rem; padding-top: .6rem; }
            .st-key-benny_nav { border-radius: 24px; }
            .st-key-benny_nav div[data-testid="stPageLink"] a { padding: .25rem .55rem !important; }
            .st-key-benny_nav div[data-testid="stPageLink"] a p { font-size: .92rem !important; }
            .brand-hero { padding: 1.25rem 1rem 2.6rem; border-radius: 30px; }
            .hero-grid { display: flex; flex-direction: column; gap: .85rem; min-height: auto; }
            .hero-copy-column { width: 100%; align-items: center; }
            .speech-bubble { max-width: 100%; margin: 3.6rem auto .9rem; font-size: 1rem; text-align: center; box-shadow: 4px 5px 0 var(--benny-ink); }
            .rainbow-title, .rainbow-burrow-title, .theater-title { font-size: clamp(3rem, 14vw, 4.7rem); text-align: center; margin-bottom: .8rem; }
            .hero-character-column { width: 100%; padding-top: 0; }
            .benny-frame { width: min(78vw, 320px); aspect-ratio: 4 / 4.6; border-radius: 32px; }
            .hero-copy-box { width: 100%; font-size: 1rem; text-align: center; }
            .hero-sun-img { top: 10px; right: 10px; width: 76px; height: 76px; }
            .brand-hero::after { left: 50%; transform: translateX(-50%); bottom: 8px; width: 100%; text-align: center; font-size: 1.35rem; letter-spacing: 2px; }
            .adventure-card { height: auto; min-height: 320px; }
            .reading-garden-hero { padding: 4rem 1rem 3rem; min-height: auto; }
            .garden-copy { max-width: 100%; }
            .garden-benny-img { position: relative; right: auto; bottom: auto; width: min(76%, 300px); display: block; margin: 1.1rem auto .2rem; }
            .word { font-size: 2rem; }
            .shelf-grid { grid-template-columns: repeat(2, 1fr); gap: .9rem; }
            .shelf-title { font-size: 1rem; }
            .count-row { font-size: 2.3rem; }
            .benny-footer-top { flex-direction: column; text-align: center; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
