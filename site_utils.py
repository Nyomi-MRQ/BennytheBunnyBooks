from pathlib import Path
import base64
import html
import mimetypes
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


def asset_data_uri(path: Path) -> str:
    if not path.exists():
        return ""
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


def benny_uri() -> str:
    return asset_data_uri(ASSETS / "benny_character.png")


def sun_uri() -> str:
    return asset_data_uri(ASSETS / "benny_sun.png")


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

        header[data-testid="stHeader"] { background: rgba(0,0,0,0); }
        #MainMenu, footer { visibility: hidden; }
        .block-container { max-width: 1180px; padding-top: 1.15rem; padding-bottom: 5rem; }

        /* BENNY BRAND HERO */
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
            box-shadow:
                0 14px 0 rgba(65,53,74,.07),
                0 28px 55px rgba(56,77,91,.15);
            margin-bottom: 2rem;
            isolation: isolate;
        }

        .brand-hero::after {
            content: "🌼   🌸   🌷   🌼   🌸";
            position: absolute;
            left: 34px;
            bottom: 14px;
            font-size: 1.65rem;
            letter-spacing: 5px;
            z-index: 0;
        }

        .hero-grid {
            position: relative;
            z-index: 2;
            display: grid;
            grid-template-columns: minmax(0, 1.08fr) minmax(300px, .92fr);
            align-items: center;
            gap: clamp(1.6rem, 4vw, 4rem);
            min-height: 470px;
        }

        .hero-copy-column {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            justify-content: center;
            min-width: 0;
            padding-right: .5rem;
        }

        .speech-bubble {
            display: inline-block;
            max-width: 620px;
            background: #ffffff;
            border: 4px solid var(--benny-ink);
            border-radius: 24px;
            padding: .72rem 1.05rem;
            font-weight: 900;
            font-size: 1rem;
            line-height: 1.35;
            box-shadow: 5px 6px 0 var(--benny-ink);
            margin-bottom: 1.25rem;
            text-align: left;
        }

        .rainbow-title {
            font-size: clamp(3.6rem, 7.2vw, 6.6rem);
            line-height: .86;
            letter-spacing: -.06em;
            margin: 0 0 1.15rem;
            font-weight: 1000;
            -webkit-text-stroke: 3px #241e2a;
            paint-order: stroke fill;
            text-shadow:
                0 5px 0 rgba(255,255,255,.98),
                0 9px 0 rgba(47,41,54,.13);
            text-align: left;
        }

        .rainbow-title .r { color: var(--benny-red); }
        .rainbow-title .o { color: var(--benny-orange); }
        .rainbow-title .y { color: var(--benny-yellow); }
        .rainbow-title .g { color: var(--benny-green); }
        .rainbow-title .b { color: var(--benny-blue); }
        .rainbow-title .p { color: var(--benny-purple); }

        .hero-copy-box {
            width: min(100%, 650px);
            background: rgba(255,255,255,.95);
            border: 4px solid white;
            border-radius: 24px;
            padding: 1.05rem 1.2rem;
            font-size: 1.06rem;
            line-height: 1.55;
            font-weight: 750;
            color: #51475a;
            box-shadow: 0 7px 0 rgba(57,45,66,.08);
            text-align: left;
        }

        .hero-character-column {
            display: flex;
            align-items: center;
            justify-content: center;
            min-width: 0;
            padding-top: 2.2rem;
        }

        .benny-frame {
            width: min(100%, 385px);
            aspect-ratio: 4 / 5;
            border: 6px solid white;
            border-radius: 38px;
            overflow: hidden;
            background: rgba(255,255,255,.28);
            box-shadow:
                0 14px 0 rgba(65,53,74,.08),
                0 24px 36px rgba(43,62,66,.18);
        }

        .hero-benny-img {
            display: block;
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center top;
        }

        .hero-sun-img {
            position: absolute;
            top: 18px;
            right: 28px;
            width: 124px;
            height: 124px;
            object-fit: contain;
            z-index: 3;
            filter: drop-shadow(0 8px 10px rgba(0,0,0,.10));
        }

        .section-title {
            font-size: 2.45rem;
            font-weight: 1000;
            letter-spacing: -.045em;
            margin: 2.5rem 0 .25rem;
            color: var(--benny-ink);
        }
        .sub { color:#6b6171; font-size:1.06rem; margin-bottom:1.25rem; font-weight:700; }

        /* HOME ADVENTURE CARDS */
        .adventure-card {
            position: relative;
            overflow: hidden;
            min-height: 330px;
            border-radius: 32px;
            border: 6px solid white;
            padding: 1.4rem 1.2rem 1.1rem;
            text-align: center;
            box-shadow: 0 10px 0 rgba(65,53,74,.08), 0 19px 35px rgba(56,77,91,.12);
        }
        .adventure-card:before {
            content: "☁️          ☁️";
            position: absolute;
            top: 10px;
            left: 0;
            right: 0;
            font-size: 1.9rem;
            opacity: .85;
        }
        .books-card { background: linear-gradient(180deg,#ffd957 0%,#ffb95a 45%,#9cde76 46%,#68bf57 100%); }
        .garden-card { background: linear-gradient(180deg,#72d7ff 0%,#c6f1ff 46%,#9ee37a 47%,#63bb55 100%); }
        .theater-card { background: linear-gradient(180deg,#855bff 0%,#bd92ff 43%,#ff90c9 62%,#664099 100%); }

        .card-benny-img {
            display:block;
            width:124px;
            height:124px;
            object-fit:cover;
            object-position:center top;
            margin:1.8rem auto .2rem;
            border:4px solid white;
            border-radius:50%;
            box-shadow:0 7px 0 rgba(62,48,74,.10), 0 12px 18px rgba(42,61,70,.14);
            background:white;
        }

        .card-scene { font-size: 5.6rem; line-height: 1; margin: 2rem 0 .3rem; filter: drop-shadow(0 8px 4px rgba(0,0,0,.10)); }
        .adventure-card h2 { font-size:1.75rem; line-height:1.05; margin:.3rem 0 .5rem; font-weight:1000; }
        .theater-card h2 { color:white; text-shadow:0 3px 0 rgba(58,38,84,.35); }
        .adventure-card p {
            background:rgba(255,255,255,.92);
            border-radius:19px;
            padding:.8rem .85rem;
            min-height:102px;
            color:#5e5366;
            font-weight:750;
            line-height:1.45;
        }

        div[data-testid="stPageLink"] a {
            border-radius: 18px !important;
            border: 4px solid white !important;
            background: #6f4cff !important;
            color: white !important;
            font-size: 1.03rem !important;
            font-weight: 900 !important;
            padding: .78rem 1rem !important;
            box-shadow: 0 5px 0 #4d34b4 !important;
            justify-content: center !important;
        }

        .card, .premium, .parent-note, .score, .word {
            border: 4px solid white;
            box-shadow: 0 8px 0 rgba(71,55,84,.07), 0 16px 28px rgba(71,76,93,.08);
        }
        .card { background:rgba(255,255,255,.95); border-radius:25px; padding:1.35rem; height:100%; }
        .premium { background:linear-gradient(135deg,#fff8dd,#ffe9f5); border-radius:26px; padding:1.35rem; }
        .parent-note { background:#eef9ff; border-radius:22px; padding:1.2rem; }
        .score { background:#fff; border-radius:19px; padding:.85rem 1rem; font-weight:900; text-align:center; }
        .word { background:#fff; border-radius:25px; padding:1.3rem; text-align:center; font-size:2.4rem; font-weight:1000; }


        /* ---------- MOBILE / DARK-MODE BUTTON VISIBILITY FIX ---------- */
        .stButton > button,
        .stButton > button:focus,
        .stButton > button:active {
            background: #ffffff !important;
            color: #33283b !important;
            border: 4px solid #6f4cff !important;
            border-radius: 18px !important;
            font-weight: 950 !important;
            font-size: 1.05rem !important;
            box-shadow: 0 5px 0 #d7cdfc !important;
            min-height: 58px !important;
            opacity: 1 !important;
            -webkit-text-fill-color: #33283b !important;
        }

        .stButton > button:hover {
            background: #fff4a8 !important;
            color: #2f2636 !important;
            border-color: #ffb93f !important;
            -webkit-text-fill-color: #2f2636 !important;
        }

        .stButton > button p,
        .stButton > button span,
        .stButton > button div {
            color: #33283b !important;
            -webkit-text-fill-color: #33283b !important;
            font-weight: 950 !important;
        }

        /* Disabled shop buttons can stay muted but readable */
        .stButton > button:disabled {
            background: #f1eef6 !important;
            color: #746a7b !important;
            border-color: #d8d0df !important;
            -webkit-text-fill-color: #746a7b !important;
            opacity: 1 !important;
        }

        /* READING GARDEN */
        .reading-garden-hero {
            position: relative;
            overflow: hidden;
            min-height: 390px;
            border-radius: 38px;
            border: 6px solid white;
            padding: 2.7rem 2.6rem 2rem;
            background:
                radial-gradient(circle at 86% 14%, #ffe76d 0 65px, transparent 68px),
                linear-gradient(180deg,#6ed3ff 0%,#d0f3ff 48%,#ace984 49%,#67bf56 100%);
            box-shadow: 0 15px 0 rgba(65,53,74,.08), 0 27px 52px rgba(56,77,91,.15);
            margin-bottom: 1.5rem;
        }
        .reading-garden-hero:before {
            content: "☁️      🌈      ☁️";
            position:absolute;
            top:22px;
            left:30px;
            font-size:2.4rem;
        }
        .reading-garden-hero:after {
            content:"🌼 🌷 🌸 🌼 🌷 🌸";
            position:absolute;
            bottom:10px;
            left:28px;
            font-size:1.9rem;
            letter-spacing:8px;
        }
        .garden-copy { position: relative; z-index: 3; max-width: 650px; }
        .garden-title {
            font-size:clamp(2.8rem,6vw,4.6rem);
            font-weight:1000;
            line-height:.95;
            color:#fff;
            -webkit-text-stroke:2px #2d2734;
            paint-order:stroke fill;
            text-shadow:0 5px 0 rgba(47,41,54,.16);
            margin:0 0 .7rem;
        }
        .garden-intro {
            background:rgba(255,255,255,.94);
            border:4px solid white;
            border-radius:22px;
            padding:.95rem 1.05rem;
            font-weight:750;
            color:#51475a;
            line-height:1.5;
            max-width:620px;
        }
        .garden-benny-img {
            position:absolute;
            z-index:2;
            right:28px;
            bottom:16px;
            width:min(36%,320px);
            max-height:340px;
            object-fit:cover;
            object-position:center top;
            border:5px solid white;
            border-radius:32px;
            box-shadow:0 15px 28px rgba(45,67,70,.18);
            background:rgba(255,255,255,.16);
        }
        .benny-says {
            position:relative;
            background:#fffdf5;
            border:4px solid #2f2936;
            border-radius:23px;
            padding:.9rem 1.1rem;
            font-weight:900;
            color:#51475a;
            box-shadow:5px 6px 0 #2f2936;
            margin:1rem 0 1.2rem;
        }
        .garden-path {
            background:rgba(255,255,255,.91);
            border:4px dashed #d3c5df;
            border-radius:23px;
            padding:1rem 1.1rem;
            margin-bottom:1rem;
            font-weight:750;
        }
        .lesson-note {
            background:#fff;
            border:4px solid #eef0f5;
            border-radius:19px;
            padding:.8rem 1rem;
            margin-bottom:.8rem;
            font-weight:800;
        }

        @media (max-width: 800px) {
            .block-container {
                padding-left: .65rem;
                padding-right: .65rem;
                padding-top: .75rem;
            }

            .brand-hero {
                padding: 1.25rem 1rem 1.35rem;
                border-radius: 30px;
            }

            .hero-grid {
                display: flex;
                flex-direction: column;
                gap: .85rem;
                min-height: auto;
            }

            .hero-copy-column {
                width: 100%;
                align-items: center;
                padding-right: 0;
            }

            .speech-bubble {
                max-width: 100%;
                width: auto;
                margin: 0 auto .9rem;
                font-size: .98rem;
                text-align: center;
                box-shadow: 4px 5px 0 var(--benny-ink);
            }

            .rainbow-title {
                font-size: clamp(3rem, 14vw, 4.7rem);
                line-height: .88;
                text-align: center;
                margin-bottom: .8rem;
            }

            .hero-character-column {
                order: 2;
                width: 100%;
                padding-top: 0;
            }

            .benny-frame {
                width: min(88vw, 355px);
                aspect-ratio: 4 / 4.7;
                border-radius: 32px;
            }

            .hero-copy-box {
                order: 3;
                width: 100%;
                max-width: 100%;
                margin-top: .15rem;
                font-size: 1rem;
                text-align: center;
            }

            .hero-sun-img {
                top: 12px;
                right: 12px;
                width: 80px;
                height: 80px;
            }

            .brand-hero::after {
                left: 50%;
                transform: translateX(-50%);
                bottom: 8px;
                width: 100%;
                text-align: center;
                font-size: 1.35rem;
                letter-spacing: 2px;
            }

            .reading-garden-hero {
                padding: 1.5rem 1rem 1.25rem;
                min-height: auto;
            }

            .garden-copy {
                max-width: 100%;
            }

            .garden-benny-img {
                position: relative;
                right: auto;
                bottom: auto;
                width: min(84%, 320px);
                max-height: none;
                display: block;
                margin: 1.1rem auto .2rem;
                transform: none;
                object-fit: cover;
                object-position: center top;
            }

            .card-benny-img {
                width: 132px;
                height: 132px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


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
