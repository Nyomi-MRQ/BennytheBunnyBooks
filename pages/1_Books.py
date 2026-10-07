import streamlit as st
from site_utils import page_setup, book_card
from data import BOOKS

page_setup("Books")
st.title("📚 Benny's Bookstore")
st.write("Explore the Benny the Bunny learning collection. Purchase links can be connected when your storefront is ready.")

cols = st.columns(2, gap="large")
for i, book in enumerate(BOOKS):
    with cols[i % 2]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        book_card(book["title"], book["cover"], book["description"], "book")
        st.caption("Skills: " + " • ".join(book["skills"]))
        st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.info("💡 Next: connect each Buy button to your preferred checkout/store listing. Keep payment credentials private and out of GitHub.")
