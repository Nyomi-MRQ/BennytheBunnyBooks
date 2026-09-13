# Benny the Bunny Website

A mobile-friendly Python website for the Benny the Bunny children's book series.

## Files

- `app.py` — the website
- `requirements.txt` — Python dependency list

## Run it on your Mac

Open Terminal inside this folder, then run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Your browser should open the local site.

## Customize these first

At the top of `app.py`, replace:

- `TIKTOK_URL`
- `INSTAGRAM_URL`
- `BOOK_1_URL`
- `BOOK_2_URL`
- `CONTACT_EMAIL`

You can also change:
- the tagline
- book names/descriptions
- activity ideas
- the colors in the CSS

## Publish for free with Streamlit Community Cloud

1. Create a GitHub repository, for example `benny-the-bunny`.
2. Upload `app.py` and `requirements.txt`.
3. Sign in to Streamlit Community Cloud with GitHub.
4. Choose **Create app**.
5. Select your repository and `app.py`.
6. Choose an available `streamlit.app` subdomain.
7. Deploy.

## Suggested brand structure

Home
- Hero / latest book
- The books
- Meet Benny
- Play & Learn
- Follow Benny
- Parent/teacher resources later

## Suggested future upgrades

- Real Benny artwork and book covers
- Downloadable coloring pages
- Email signup
- Shop / Amazon / Etsy / Gumroad buttons
- Embedded TikTok/YouTube clips
- Printable activity PDFs
- Interactive "Find the Color" game
- Analytics
- Custom domain such as `bennythebunnybooks.com`
