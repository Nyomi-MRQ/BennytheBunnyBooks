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
          radial-gradient(circle at 8% 8%, rgba(255,223,239,.72), transparent 28%),
          radial-gradient(circle at 92% 8%, rgba(213,238,255,.78), transparent 30%),
          linear-gradient(180deg,#fffdf8 0%,#fff8fc 52%,#f7fbff 100%);
        color:#332b39;
    }
    header[data-testid="stHeader"] { background:rgba(0,0,0,0); }
    #MainMenu, footer { visibility:hidden; }
    .block-container { max-width:1160px; padding-top:1.2rem; padding-bottom:4rem; }

    .hero {
        border-radius:34px;
        padding:3rem;
        background:rgba(255,255,255,.88);
        box-shadow:0 18px 55px rgba(85,54,96,.11);
        border:2px solid rgba(255,255,255,.95);
        margin-bottom:1.5rem;
    }
    .hero h1 { font-size:clamp(2.8rem,7vw,5.4rem); line-height:.95; letter-spacing:-.055em; margin:.4rem 0 1rem; }
    .hero p { font-size:1.13rem; line-height:1.65; color:#685f6e; max-width:720px; }
    .pill {
        display:inline-block; padding:.45rem .8rem; border-radius:999px;
        background:#ffe4f1; color:#7e3f61; font-weight:800; font-size:.83rem;
    }
    .section-title { font-size:2.25rem; letter-spacing:-.04em; margin:2.2rem 0 .4rem; }
    .sub { color:#746a79; font-size:1.03rem; margin-bottom:1.25rem; }
    .card {
        background:rgba(255,255,255,.94); border:1px solid #eee5ef; border-radius:24px;
        padding:1.35rem; box-shadow:0 10px 30px rgba(82,56,90,.07); height:100%;
    }
    .card h3 { margin:.4rem 0 .3rem; }
    .card p { color:#6f6674; line-height:1.55; }
    .gamebox {
        background:linear-gradient(135deg,#fff4cf,#f3eaff,#e8f7ff);
        border:1px solid #eadced; border-radius:26px; padding:1.35rem;
    }
    .score {
        background:white; border-radius:16px; padding:.8rem 1rem; font-weight:800;
        border:1px solid #eee3ef; text-align:center; margin:.5rem 0 1rem;
    }
    .word {
        background:#fff; border-radius:22px; padding:1.3rem; text-align:center;
        font-size:2.4rem; font-weight:900; letter-spacing:.02em; border:1px solid #eee5ef;
    }
    .parent-note {
        background:#eef8ff; border-radius:20px; padding:1.2rem; border:1px solid #d8eaf7;
    }
    .premium {
        background:linear-gradient(135deg,#fff7de,#ffeaf4); border-radius:24px;
        padding:1.35rem; border:1px solid #f0dfd8;
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
