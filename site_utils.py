from pathlib import Path
import html
import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
COVERS = ASSETS / "covers"

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

def page_setup(title: str):
    st.set_page_config(
        page_title=f"{title} | Benny the Bunny Books",
        page_icon="🐰",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    add_css()

def add_css():
    st.markdown("""
    <style>
    .stApp {
        background:
          radial-gradient(circle at 12% 10%, rgba(255,255,255,.96) 0 42px, transparent 44px),
          radial-gradient(circle at 18% 8%, rgba(255,255,255,.96) 0 56px, transparent 58px),
          radial-gradient(circle at 84% 10%, rgba(255,255,255,.94) 0 48px, transparent 50px),
          linear-gradient(180deg,#bcecff 0%,#e9faff 38%,#fffaf3 64%,#e8ffd9 100%);
        color:#352d3b;
    }
    header[data-testid="stHeader"] { background:rgba(0,0,0,0); }
    #MainMenu, footer { visibility:hidden; }
    .block-container { max-width:1160px; padding-top:1.2rem; padding-bottom:5rem; }

    .benny-hero {
        position:relative;
        overflow:hidden;
        background:
          radial-gradient(circle at 84% 14%, #fff79a 0 66px, transparent 68px),
          linear-gradient(180deg,#8bdcff 0%,#cff2ff 58%,#8fd36f 59%,#62b957 100%);
        border:5px solid #fff;
        border-radius:38px;
        padding:3rem 2.8rem;
        min-height:350px;
        box-shadow:0 11px 0 rgba(84,68,102,.08), 0 24px 48px rgba(70,91,108,.16);
        margin-bottom:1.6rem;
    }
    .benny-hero:before {
        content:"☁️   ☁️";
        position:absolute; top:28px; right:90px;
        font-size:3rem; letter-spacing:30px; opacity:.95;
    }
    .benny-hero:after {
        content:"🌼  🌷  🌼  🌸  🌼";
        position:absolute; bottom:14px; right:25px;
        font-size:1.9rem; letter-spacing:4px;
    }
    .benny-bubble {
        display:inline-block;
        background:#fff;
        border:3px solid #3c3445;
        border-radius:22px;
        padding:.62rem .95rem;
        font-weight:900;
        box-shadow:4px 5px 0 #3c3445;
        margin-bottom:1rem;
    }
    .benny-hero h1 {
        font-size:clamp(3rem,7vw,5.7rem);
        line-height:.9; letter-spacing:-.055em;
        margin:.25rem 0 1rem;
        max-width:730px;
        color:#fff;
        text-shadow:0 4px 0 #574a67, 3px 6px 0 rgba(0,0,0,.08);
    }
    .benny-hero p {
        background:rgba(255,255,255,.91);
        border:3px solid #fff;
        border-radius:20px;
        padding:1rem 1.15rem;
        font-size:1.08rem;
        font-weight:750;
        line-height:1.55;
        max-width:650px;
        color:#594e60;
    }
    .hero-benny {
        position:absolute; right:7%; bottom:45px;
        font-size:9rem;
        filter:drop-shadow(0 13px 8px rgba(60,55,60,.16));
        transform:rotate(4deg);
    }

    .section-title { font-size:2.45rem; font-weight:950; letter-spacing:-.045em; margin:2.4rem 0 .3rem; color:#493f55; }
    .sub { color:#6e6475; font-size:1.05rem; margin-bottom:1.3rem; font-weight:650; }

    .adventure-card {
        border-radius:30px;
        padding:1.3rem 1.2rem 1.15rem;
        min-height:312px;
        border:5px solid #fff;
        box-shadow:0 9px 0 rgba(76,60,92,.10), 0 18px 32px rgba(62,70,90,.12);
        position:relative; overflow:hidden; text-align:center;
        transition:transform .18s ease, box-shadow .18s ease;
    }
    .adventure-card:hover { transform:translateY(-7px) rotate(-.4deg); box-shadow:0 14px 0 rgba(76,60,92,.08), 0 25px 38px rgba(62,70,90,.16); }
    .books-card { background:linear-gradient(180deg,#ffd87f 0%,#ffbd62 58%,#8ed16f 59%,#69bb59 100%); }
    .garden-card { background:linear-gradient(180deg,#b8ebff 0%,#dff7ff 55%,#96da77 56%,#69bf5b 100%); }
    .theater-card { background:linear-gradient(180deg,#dac8ff 0%,#bfa7ff 58%,#68499f 59%,#4f367f 100%); }
    .card-clouds { position:absolute; top:10px; left:0; right:0; font-size:1.8rem; opacity:.82; }
    .adventure-emoji { font-size:6.2rem; line-height:1; margin:1.8rem 0 .35rem; filter:drop-shadow(0 8px 5px rgba(0,0,0,.10)); }
    .adventure-card h2 { font-size:1.72rem; line-height:1.05; color:#352c3b; margin:.35rem 0 .55rem; font-weight:950; letter-spacing:-.03em; }
    .theater-card h2 { color:#fff; text-shadow:0 2px 0 rgba(0,0,0,.12); }
    .adventure-card p { background:rgba(255,255,255,.9); border-radius:18px; padding:.72rem .85rem; font-size:.94rem; font-weight:700; line-height:1.45; color:#62566a; min-height:90px; margin-bottom:.4rem; }

    div[data-testid="stPageLink"] a {
        border-radius:18px !important;
        border:3px solid #fff !important;
        background:#6d4aff !important;
        color:#fff !important;
        font-size:1.02rem !important;
        font-weight:900 !important;
        padding:.78rem 1rem !important;
        box-shadow:0 5px 0 #4c32b3 !important;
        text-align:center !important;
        justify-content:center !important;
        transition:transform .15s ease !important;
    }
    div[data-testid="stPageLink"] a:hover { transform:translateY(-2px); background:#7d5cff !important; }

    .card { background:rgba(255,255,255,.94); border:3px solid #fff; border-radius:24px; padding:1.35rem; box-shadow:0 9px 0 rgba(85,60,95,.06), 0 18px 30px rgba(82,56,90,.07); height:100%; }
    .card h3 { margin:.4rem 0 .3rem; }
    .card p { color:#6f6674; line-height:1.55; }
    .gamebox { background:linear-gradient(135deg,#fff4cf,#f3eaff,#e8f7ff); border:3px solid #fff; border-radius:26px; padding:1.35rem; }
    .score { background:#fff; border-radius:18px; padding:.8rem 1rem; font-weight:900; border:3px solid #eee3ef; text-align:center; margin:.5rem 0 1rem; }
    .word { background:#fff; border-radius:24px; padding:1.3rem; text-align:center; font-size:2.4rem; font-weight:950; letter-spacing:.02em; border:4px solid #fff; box-shadow:0 8px 0 rgba(70,54,85,.08); }
    .parent-note { background:#eef8ff; border-radius:22px; padding:1.2rem; border:3px solid #fff; }
    .premium { background:linear-gradient(135deg,#fff7de,#ffeaf4); border-radius:26px; padding:1.35rem; border:4px solid #fff; box-shadow:0 8px 0 rgba(85,60,95,.06); }

    @media (max-width:760px) {
        .benny-hero { padding:2rem 1.35rem 7rem; min-height:420px; }
        .hero-benny { font-size:6.4rem; right:8%; bottom:12px; }
        .benny-hero:before { right:5px; font-size:2rem; }
        .adventure-card { min-height:280px; }
    }
    </style>
    """, unsafe_allow_html=True)

def speak_button(text: str, label: str = None, key: str = "speak"):
    safe_text = html.escape(text, quote=True)
    label = label or f"🔊 Hear: {text}"
    safe_label = html.escape(label)
    components.html(
        f"""
        <button id="{key}" onclick="speak_{key}()" style="
            width:100%; padding:12px 16px; border:0; border-radius:14px;
            font-weight:800; font-size:16px; cursor:pointer;
            background:#6d4aff; color:white;">
            {safe_label}
        </button>
        <script>
        function speak_{key}() {{
            window.speechSynthesis.cancel();
            const u = new SpeechSynthesisUtterance("{safe_text}");
            u.rate = 0.82;
            u.pitch = 1.08;
            window.speechSynthesis.speak(u);
        }}
        </script>
        """,
        height=58,
    )

def book_card(title, cover_path, description, product_type="book"):
    cover = COVERS / cover_path
    if cover.exists():
        st.image(str(cover), use_container_width=True)
    st.markdown(f"### {title}")
    st.write(description)
    link = PURCHASE_LINKS.get(title, "") if product_type == "book" else READALONG_LINKS.get(title, "")
    if link:
        st.link_button("Buy now", link, use_container_width=True)
    else:
        st.button("🛍️ Purchase link coming soon", disabled=True, use_container_width=True, key=f"{product_type}_{title}")
