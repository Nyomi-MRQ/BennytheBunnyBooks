"""All of the words, books, and game content for Benny's Learning World.

Edit this file to add books or change game words. No other file needs to change.
"""

BOOKS = [
    {
        "slug": "colors",
        "title": "Benny's Colors",
        "cover": "bennys_colors.jpg",
        "description": "Learn colors with Benny through simple sentences, colorful pictures, and a Find the Color challenge.",
        "skills": ["Color words", "Early reading", "Observation"],
        "ages": "Ages 2–5",
        "game_tab": "🎨 Colors",
        "readalong": "Follow Benny through colors, repeat simple sentences, and pause to find colors around you.",
        "readalong_badges": ["Colors", "Listen & Repeat", "Find It"],
    },
    {
        "slug": "counting",
        "title": "Benny's Counting Adventure",
        "cover": "counting_adventure.jpg",
        "description": "Count with Benny from 1 to 10 through a cheerful outdoor adventure.",
        "skills": ["Counting 1–10", "Number sequence", "Read-aloud practice"],
        "ages": "Ages 2–5",
        "game_tab": "🔢 Counting",
        "readalong": "Count with Benny from 1 to 10 with cheerful call-and-response moments.",
        "readalong_badges": ["Counting", "Call & Response", "Numbers"],
    },
    {
        "slug": "abcs",
        "title": "Benny's ABC's",
        "cover": "bennys_abcs.jpg",
        "description": "Explore the alphabet with Benny using friendly pictures and simple A-is-for vocabulary.",
        "skills": ["Alphabet", "Beginning sounds", "Vocabulary"],
        "ages": "Ages 3–6",
        "game_tab": "🔤 Letters",
        "readalong": "Practice letters, beginning sounds, and easy vocabulary in a playful alphabet show.",
        "readalong_badges": ["Alphabet", "Phonics", "Vocabulary"],
    },
    {
        "slug": "senses",
        "title": "The 5 Senses",
        "cover": "five_senses.jpg",
        "description": "Benny and Teddy Bear explore sight, sound, touch, taste, and smell.",
        "skills": ["Five senses", "Vocabulary", "Everyday science"],
        "ages": "Ages 3–6",
        "game_tab": "👀 Senses",
        "readalong": "Explore seeing, hearing, touching, tasting, and smelling with Benny and Teddy.",
        "readalong_badges": ["5 Senses", "Questions", "Everyday Learning"],
    },
]

BOOKS_BY_SLUG = {b["slug"]: b for b in BOOKS}

# (word, picture, Benny's sentence, swatch color)
COLORS = [
    ("RED", "🍓", "Benny sees a red strawberry.", "#ff5545"),
    ("ORANGE", "🍊", "Benny sees an orange fruit.", "#ff9d3b"),
    ("YELLOW", "☀️", "Benny sees a bright yellow sun.", "#ffd735"),
    ("GREEN", "🌿", "Benny sees green grass.", "#62c64a"),
    ("BLUE", "💧", "Benny sees blue water.", "#4ca9f7"),
    ("PURPLE", "🍇", "Benny sees purple grapes.", "#a65cc7"),
    ("PINK", "🐷", "Benny sees a pink pig.", "#ff8fc4"),
    ("GREY", "🐘", "Benny sees a grey elephant.", "#9a9aa5"),
    ("BROWN", "🐴", "Benny sees a brown horse.", "#9b6a43"),
    ("BLACK", "🕷️", "Benny sees a black spider.", "#2f2936"),
    ("WHITE", "☁️", "Benny sees white clouds.", "#ffffff"),
]

# (letter, sound, word, picture)
PHONICS = [
    ("A", "/a/", "Apple", "🍎"),
    ("B", "/b/", "Bunny", "🐰"),
    ("C", "/k/", "Car", "🚗"),
    ("D", "/d/", "Duck", "🦆"),
    ("E", "/e/", "Egg", "🥚"),
    ("F", "/f/", "Flower", "🌸"),
    ("G", "/g/", "Goat", "🐐"),
    ("H", "/h/", "House", "🏠"),
    ("I", "/i/", "Igloo", "🧊"),
    ("J", "/j/", "Juice", "🧃"),
    ("K", "/k/", "Koala", "🐨"),
    ("L", "/l/", "Lion", "🦁"),
    ("M", "/m/", "Moon", "🌙"),
    ("N", "/n/", "Nut", "🥜"),
    ("O", "/o/", "Octopus", "🐙"),
    ("P", "/p/", "Pig", "🐷"),
    ("Q", "/kw/", "Queen", "👑"),
    ("R", "/r/", "Rainbow", "🌈"),
    ("S", "/s/", "Sun", "☀️"),
    ("T", "/t/", "Turtle", "🐢"),
    ("U", "/u/", "Umbrella", "☂️"),
    ("V", "/v/", "Violin", "🎻"),
    ("W", "/w/", "Whale", "🐳"),
    ("X", "/ks/", "Fox", "🦊"),
    ("Y", "/y/", "Yarn", "🧶"),
    ("Z", "/z/", "Zebra", "🦓"),
]

# (number, word, picture)
COUNTING = [
    (1, "one", "🥕"),
    (2, "two", "🌼"),
    (3, "three", "🍎"),
    (4, "four", "🐞"),
    (5, "five", "⭐"),
    (6, "six", "🦋"),
    (7, "seven", "🍓"),
    (8, "eight", "🎈"),
    (9, "nine", "🐣"),
    (10, "ten", "🌷"),
]

# (sense, body part, picture, example question, things that use this sense)
SENSES = [
    ("sight", "eyes", "👀", "Which sense helps Benny see a rainbow?", "🌈"),
    ("hearing", "ears", "👂", "Which sense helps Benny hear a bird sing?", "🐦"),
    ("touch", "hands", "✋", "Which sense helps Benny feel a soft blanket?", "🧸"),
    ("taste", "tongue", "👅", "Which sense helps Benny taste ice cream?", "🍦"),
    ("smell", "nose", "👃", "Which sense helps Benny smell a flower?", "🌸"),
]

RHYMES = [
    ("cat", "hat", ["hat", "dog", "sun"]),
    ("pig", "big", ["big", "red", "car"]),
    ("bee", "tree", ["tree", "book", "ball"]),
    ("sun", "fun", ["fun", "fish", "blue"]),
    ("hop", "top", ["cup", "top", "hen"]),
    ("bug", "rug", ["rug", "map", "bed"]),
    ("cake", "lake", ["leaf", "milk", "lake"]),
    ("star", "car", ["car", "moon", "sock"]),
]

SIGHT_WORDS = ["I", "SEE", "A", "THE", "BIG", "LITTLE", "BUNNY", "PLAY", "RUN", "HOP",
               "CAN", "WE", "LIKE", "YOU", "GO"]

SENTENCES = [
    "I see a red apple.",
    "Benny sees blue water.",
    "The little bunny can hop.",
    "I see a yellow sun.",
    "Benny can run and play.",
    "We like to read books.",
    "Teddy can see a big tree.",
]
