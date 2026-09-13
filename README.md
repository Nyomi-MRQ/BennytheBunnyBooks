# Benny Learning World v1

Public Streamlit website for the Benny the Bunny children's book series.

## Included

- Public bookstore
- Benny Reading Garden
- Tap-to-hear browser speech
- Color learning game
- Phonics
- Rhyming
- Sight words
- Sentence reading
- Benny Stars / badges
- Read-Along storefront structure
- Free-preview placeholders
- Book + Read-Along bundle placeholders
- QR-ready query links
- Parent / grown-up information page
- Actual cover images extracted from the current Benny PDFs

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## GitHub / Streamlit

Upload the contents of this folder to your public `BennytheBunnyBooks` repo.

Important:
- Do not upload private payment credentials.
- Do not upload full paid read-along video files.
- Purchase URLs can be added later in `site_utils.py`.
- Audio currently uses the visitor's browser speech synthesis, so no private API key is needed.

## Purchase links

Edit `PURCHASE_LINKS` and `READALONG_LINKS` in `site_utils.py`.

## Future QR links

After the permanent public site URL is known, use:

- `https://YOURDOMAIN/?book=colors`
- `https://YOURDOMAIN/?book=counting`
- `https://YOURDOMAIN/?book=abcs`
- `https://YOURDOMAIN/?book=senses`

These links can be turned into QR codes for the updated books.
