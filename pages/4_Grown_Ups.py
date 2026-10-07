import streamlit as st
from site_utils import page_setup

page_setup("Grown-Ups")
st.title("👨‍👩‍👧 For Grown-Ups")
st.write("Benny Learning World is designed to make early learning playful, repeatable, and easy to share together.")

c1, c2 = st.columns(2, gap="large")
with c1:
    st.markdown("""
    <div class="card">
      <h3>🌱 Skills we practice</h3>
      <p>
      Color vocabulary • alphabet awareness • beginning sounds • rhyming • sight words •
      simple sentences • counting • listening • observation • basic comprehension.
      </p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="card">
      <h3>💗 How to use the games</h3>
      <p>
      Let children try first. Use tap-to-hear as support rather than a test.
      Celebrate attempts, repeat favorite activities, and stop while it is still fun.
      </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<h2 class="section-title">🔒 Child-friendly design</h2>', unsafe_allow_html=True)
st.write("The current Reading Garden does not require a child to create an account or enter personal information.")

st.markdown('<h2 class="section-title">📱 From book to website</h2>', unsafe_allow_html=True)
st.write("""
Updated Benny books can include QR codes that open the matching companion experience.
A permanent website URL can use book-specific links such as:

- `YOURDOMAIN.com/?book=colors`
- `YOURDOMAIN.com/?book=counting`
- `YOURDOMAIN.com/?book=abcs`
- `YOURDOMAIN.com/?book=senses`

Once the final public domain is chosen, those are the links we should encode into the printed QR codes.
""")
