# Benny's Learning World

The public Streamlit website for **Benny the Bunny Books**.

## Pages
- **Home** — Benny hero, three adventures, bookshelf. QR codes can open `?book=colors`, `?book=counting`, `?book=abcs` or `?book=senses` for a book-specific welcome.
- **Books** (Book Burrow) — every book with buy link + its matching game.
- **Games** (Reading Garden) — Colors, Counting 1–10, Letters A–Z, 5 Senses, Rhymes, Sight Words, Sentences. Benny Stars, streaks and badges. Open a game directly with `?game=colors` etc.
- **Story Theater** — read-along for each book.
- **Grown-Ups** — tips, which game goes with which book, safety info.

## Where to change things
| What | File |
|---|---|
| Buy links, read-along links, TikTok/Instagram/Amazon/email footer links | `site_utils.py` (top of the file — paste links between the quotes; empty ones stay hidden) |
| Books, game words, colors, letters, sentences | `data.py` |
| Colors and styling | `site_utils.py` → `add_css()` |

## Adding a new book
1. Add the cover to `assets/covers/` (portrait, about 600×800 JPG keeps the site fast).
2. Add an entry to `BOOKS` in `data.py`.
3. Add its title to `PURCHASE_LINKS` and `READALONG_LINKS` in `site_utils.py`.

## Run it on your computer
```
pip install -r requirements.txt
streamlit run app.py
```

Do not put passwords, payment keys, or other secrets in this public repo.
