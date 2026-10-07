import streamlit as st
from site_utils import page_setup, COVERS, READALONG_LINKS
from data import BOOKS

page_setup("Read-Alongs")
st.title("🎬 Benny Read-Alongs")
st.write("Premium narrated learning adventures with free preview space built into the storefront.")

st.markdown("""
<div class="premium">
<h3>What makes a Benny Read-Along special?</h3>
<p>
🎙️ Warm narration &nbsp; • &nbsp;
🔎 Highlighted words &nbsp; • &nbsp;
🎵 Gentle sound effects &nbsp; • &nbsp;
⏸️ Kid-answer pauses &nbsp; • &nbsp;
✨ Page movement & zoom &nbsp; • &nbsp;
🐰 Benny celebrations
</p>
</div>
""", unsafe_allow_html=True)

for i, book in enumerate(BOOKS):
    st.divider()
    left, right = st.columns([1, 2], gap="large")
    with left:
        cover = COVERS / book["cover"]
        if cover.exists():
            st.image(str(cover), use_container_width=True)
    with right:
        st.subheader(book["title"] + " — Read-Along")
        if book["title"] == "Benny's Colors":
            st.write("Follow Benny through color words, repeat the simple sentences, pause to find colors nearby, and finish with a color challenge.")
        elif book["title"] == "Benny's Counting Adventure":
            st.write("Count aloud with Benny from 1 to 10 with pauses for children to count each group before Benny answers.")
        elif book["title"] == "Benny's ABC's":
            st.write("Practice letters, beginning sounds, and picture vocabulary with a call-and-response alphabet adventure.")
        else:
            st.write("Explore sight, sound, touch, taste, and smell with Benny and Teddy through interactive questions and everyday examples.")

        c1, c2, c3 = st.columns(3)
        c1.button("▶️ Free Preview — coming soon", disabled=True, use_container_width=True, key=f"preview_{i}")
        if READALONG_LINKS.get(book["title"]):
            c2.link_button("🎬 Buy Read-Along", READALONG_LINKS[book["title"]], use_container_width=True)
        else:
            c2.button("🎬 Buy Read-Along — coming soon", disabled=True, use_container_width=True, key=f"video_buy_{i}")
        c3.button("✨ Book + Video Bundle — coming soon", disabled=True, use_container_width=True, key=f"bundle_{i}")

st.divider()
st.info("The full paid video files should stay outside the public GitHub repository. The website can host previews and link securely to your checkout/delivery platform.")
