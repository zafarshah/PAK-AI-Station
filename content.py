"""All content for PAK-AI Station v0.1. Replace SAMPLE items with department-approved data."""

# id, icon, English name, Urdu name (DRAFT - please have a native speaker review), tile colours, ready?
MODULES = [
    dict(id="info",   icon="🧭", en="Public information",        ur="عوامی معلومات",        c=("#2563eb", "#06b6d4"), ready=True,  tip="Weather, places to visit", tip_ur="موسم، دیکھنے کی جگہیں اور مفید معلومات۔"),
    dict(id="story",  icon="📖", en="Grandma stories",           ur="دادی کی کہانیاں",       c=("#f59e0b", "#ef4444"), ready=True,  tip="Short stories, scene by scene", tip_ur="مختصر کہانیاں، منظر بہ منظر۔"),
    dict(id="kids",   icon="🎒", en="Kids learning",             ur="بچوں کی تعلیم",         c=("#10b981", "#84cc16"), ready=False, tip="Lessons and study help", tip_ur="سبق اور پڑھائی میں مدد۔"),
    dict(id="quran",  icon="🕌", en="Holy Quran",                ur="قرآنِ پاک",             c=("#0f766e", "#14b8a6"), ready=False, tip="Recitation and Tajweed (scholar-reviewed)", tip_ur="تلاوت اور تجوید (علماء کی نظرِ ثانی کے ساتھ)۔"),
    dict(id="util",   icon="⚡", en="Utilities and roads",       ur="بجلی اور سڑکیں",        c=("#6366f1", "#a855f7"), ready=False, tip="Electricity, winter shortfall, roads", tip_ur="بجلی، سردیوں کی قلت اور سڑکوں کی صورتحال۔"),
    dict(id="env",    icon="🌍", en="Environment and disasters", ur="ماحول اور آفات",        c=("#0284c7", "#6366f1"), ready=False, tip="Climate, floods, safety", tip_ur="موسمیاتی تبدیلی، سیلاب اور حفاظتی مشورے۔"),
    dict(id="forest", icon="🌲", en="Forest and wildlife",       ur="جنگلات اور جنگلی حیات", c=("#15803d", "#65a30d"), ready=False, tip="Forests, rangelands, wildlife", tip_ur="جنگلات، چراگاہیں اور جنگلی حیات۔"),
    dict(id="agri",   icon="🍎", en="Agriculture and orchards",  ur="زراعت اور باغات",       c=("#dc2626", "#f97316"), ready=False, tip="Farming and orchard advice", tip_ur="کاشتکاری اور باغات کے مشورے۔"),
]

MODULES.extend([
    dict(id="tourism", icon="🏔️", en="Foreigners & Tourism", ur="سیاحت اور غیر ملکی مہمان", c=("#164c73","#20a0b0"), ready=False, tip="Hotels, guides, transport, camping and local attractions", tip_ur="ہوٹل، رہنما، سفر اور سیاحتی مقامات"),
    dict(id="fishery", icon="🐟", en="Fisheries & Aquaculture", ur="ماہی گیری اور آبی پرورش", c=("#13678a","#2cb4ad"), ready=False, tip="Trout, hatcheries, fish health and water quality", tip_ur="ٹراؤٹ، مچھلی کی افزائش اور پانی کا معیار"),
    dict(id="markets", icon="🛍️", en="Local Markets & Entrepreneurship", ur="مقامی بازار اور کاروبار", c=("#a45720","#e1a84c"), ready=False, tip="Fruit, dry fruits, handicrafts and small businesses", tip_ur="پھل، خشک میوہ جات اور مقامی کاروبار")
])

TEXT = {
    "en": dict(welcome="Welcome to", brand="PAK-AI Station.",
               tag="A place to try AI for learning, travel and daily life in Gilgit-Baltistan.",
               tryit="Try it  →", choose="Welcome! Choose a topic.", soon="Coming soon",
               soon_note="This topic is being prepared with the department that owns the information.",
               weather="Today's weather", places="Places to visit", choose_town="Choose a town",
               type_="Type", all_="All", scene="Scene", read="🔊 Read aloud"),
    "ur": dict(welcome="خوش آمدید", brand="پاک اے آئی اسٹیشن",
               tag="گلگت بلتستان میں سیکھنے، سفر اور روزمرہ زندگی کے لیے اے آئی آزمانے کی جگہ۔",
               tryit="شروع کریں  ←", choose="خوش آمدید! اپنا موضوع منتخب کریں۔", soon="جلد آ رہا ہے",
               soon_note="یہ موضوع متعلقہ محکمے کے ساتھ مل کر تیار کیا جا رہا ہے۔",
               weather="آج کا موسم", places="دیکھنے کی جگہیں", choose_town="شہر منتخب کریں",
               type_="قسم", all_="سب", scene="منظر", read="🔊 سنیں"),
}

# Coordinates are approximate town centres, used only for the weather lookup.
TOWNS = {
    "Gilgit": (35.92, 74.31),
    "Skardu": (35.30, 75.63),
    "Karimabad (Hunza)": (36.32, 74.66),
}

# SAMPLE list: place names only. Routes, hours and tips must come from the Tourism Department.
PLACES = [
    {"name": "Baltit Fort", "area": "Hunza", "type": "Fort / history", "route": "TO BE FILLED by Tourism Department", "tip": ""},
    {"name": "Altit Fort", "area": "Hunza", "type": "Fort / history", "route": "TO BE FILLED by Tourism Department", "tip": ""},
    {"name": "Attabad Lake", "area": "Hunza", "type": "Lake / picnic", "route": "TO BE FILLED by Tourism Department", "tip": ""},
    {"name": "Kharpocho (Skardu) Fort", "area": "Skardu", "type": "Fort / history", "route": "TO BE FILLED by Tourism Department", "tip": ""},
    {"name": "Deosai National Park", "area": "Skardu", "type": "Park / nature", "route": "TO BE FILLED by Tourism Department", "tip": ""},
    {"name": "Naltar Valley", "area": "Gilgit", "type": "Valley / nature", "route": "TO BE FILLED by Tourism Department", "tip": ""},
]

# A sample original story in the "scene by scene" format. Each scene has narration and a video prompt.
STORIES = [
    {
        "title": "Grandma and the Apricot Tree (SAMPLE)",
        "moral": "Good things grow when we are patient and kind.",
        "scenes": [
            ("Grandma gives a seed",
             "On a sunny morning, Grandma gives little Zara an apricot seed. 'Plant it, and be kind to it,' she says.",
             "A warm 3D cartoon scene in a mountain village. An old grandmother in a soft shawl gives a small apricot seed to a smiling girl. Stone house, terraced fields and snowy peaks in the background. Gentle morning light."),
            ("Zara plants the seed",
             "Zara digs a small hole by the stream and plants the seed. She pours water with her hands.",
             "3D cartoon: a girl kneels by a mountain stream, digging a small hole, planting a seed and pouring water. Green terraces and white peaks behind her. Soft sunlight."),
            ("Winter comes",
             "Snow covers the village. Zara worries. Grandma says, 'The seed is sleeping. Waiting is part of growing.'",
             "3D cartoon: a snowy village at dusk. The girl looks at a snow-covered garden from a window while Grandma smiles beside her, a warm fire glowing inside."),
            ("A tiny green leaf",
             "In spring, a tiny green leaf pushes up through the soil. Zara jumps with joy.",
             "3D cartoon: close-up of a tiny green sprout in dark soil with melting snow. The girl's happy face above it, spring flowers around."),
            ("Helpers in the garden",
             "A bee and a little bird visit the young tree. Grandma says, 'Everyone helps the tree grow, and the tree helps everyone.'",
             "3D cartoon: a young apricot tree with pink blossoms, a bee on a flower and a small bird on a branch. The girl and Grandma smile nearby."),
            ("Sweet apricots",
             "Years later, the tree is full of golden apricots. Zara shares them with all the neighbors.",
             "3D cartoon: a big apricot tree full of golden fruit. A grown-up girl and old Grandma share baskets of apricots with smiling neighbors in the village."),
        ],
    }
]

STORIES.append({
    "title": "Ant and a mimic-ant trucker spider",
    "moral": "In nature, everyone has a special superpower, and different friends can still be best friends.",
    "scenes": [
        ("Who is that on the leaf?",
         "Come close, my dears. Once, a young red ant named Rusty was walking near his nest. On a dry leaf he saw another ant. 'It looks just like me,' Rusty whispered, 'but something feels funny.'",
         "Funny and stylish 3D Pixar-style animation. Sunny forest floor with soil, pebbles, moss and a busy anthill. A shiny young red ant with big expressive black eyes and twitching antennae tiptoes past a curled dry leaf and freezes when he spots a strange ant sitting on it. He leans in, squints and whispers to himself. The camera slowly pushes in on his suspicious face. Sound effects: tiny footsteps, rustling grass, soft wind, a little 'hmm' sound, antenna twitch. No background music."),
        ("Are you lost?",
         "Rusty was a kind ant. He smiled and asked, 'Hello, friend! Are you lost? Do you need help finding your home?'",
         "3D Pixar-style. The young red ant walks up to the dry leaf with a friendly smile and a small wave, then points toward the anthill. The strange creature wiggles and looks around dramatically as if pretending to be confused. Close-up on their funny blinking eyes. Sound effects: soft tapping feet, a friendly 'pop' for the wave, leaf creak, tiny giggle. No background music."),
        ("Surprise! I am a spider!",
         "The new friend giggled. 'I am not an ant,' it said. 'I am a spider!' Rusty jumped so high in surprise that his antennae spun round and round.",
         "3D Pixar-style, comedy moment. The strange creature suddenly stands tall and reveals it is a spider. The red ant leaps backward with huge eyes and wildly spinning antennae, then lands on his bottom with a bounce. The leaf bends and wobbles. Slow-motion camera orbit around the spider's proud grin. Sound effects: surprised gasp, funny boing, spinning whoosh, little sparkle ping, leaf bounce. No background music."),
        ("You look just like me!",
         "Rusty looked closely. 'You look exactly like me!' he said. The spider smiled like a clever trickster. 'That is my secret,' it said.",
         "3D Pixar-style. Split-screen style close-ups: the ant and the mimic spider stand side by side on the leaf, comparing their shapes with a magnifying glass the ant holds. The spider winks like a magician. The camera swings between their faces. Sound effects: magnifying-glass squeak, cartoon wink 'ting', soft giggles, rustling leaf. No background music."),
        ("Eight legs, two fake antennae",
         "The spider lifted its two front legs high. 'Spiders have eight legs,' it said, 'but I hold two up like antennae, so I look like an ant!' Rusty counted all eight legs, one by one.",
         "3D Pixar-style. The spider raises two front legs like antennae and slowly turns to show all eight legs. The red ant counts each leg with a tiny finger; a bright floating number from 1 to 8 pops in the air with a sparkle each time. The spider strikes funny magician poses. Sound effects: tap for each leg, a little 'ding' per number, sparkle pops, pose swooshes. No background music."),
        ("Where is your home?",
         "'Where do you live?' asked Rusty. The spider showed him two little pictures. In summer it lived on green leaves. In winter it hid safely on the ground, where it was warm and quiet.",
         "3D Pixar-style. The spider pulls out two tiny picture cards. One shows bright summer leaves blowing in the wind; the other shows winter ground, rocks and gently falling snow. The ant holds the cards, amazed, and the camera pans between the cards and their faces while tiny leaves and snowflakes animate on the cards. Sound effects: paper flipping, leaf rustling, light wind, soft snow crunch, amazed 'wow'. No background music."),
        ("Why pretend to be an ant?",
         "'Why do you pretend to be an ant?' asked Rusty. The spider whispered, 'It keeps me safe. Many hungry animals do not like to bother ants.' It showed a funny picture of a confused bird and a puzzled lizard.",
         "3D Pixar-style, comedy. A confused bird and a puzzled lizard peek from behind a rock, tilt their heads, blink and scratch themselves while question marks pop above them. The spider laughs proudly and the red ant falls over laughing on the leaf. Sound effects: silly bird chirps, lizard hiss, confused grunts, giggles, cartoon boings, leaf rustle. No background music."),
        ("Tricksters around the world",
         "'There are ant-mimic spiders in many countries,' said the spider. 'We are famous tricksters everywhere!' Rusty's eyes grew big. 'That is amazing!' he said.",
         "3D Pixar-style. A glowing spinning globe appears on the leaf. Small cartoon ant-mimic spiders in different colors and habitats (forest, grassland, desert, garden) wave from different parts of the world like tiny tourists. The red ant looks up in awe. Sound effects: globe whoosh, sparkle pops, many tiny cheers, amazed gasp. No background music."),
        ("Rusty's big family",
         "Rusty said proudly, 'Come and see my family!' He showed the busy colony with its queen. 'We live together and work as a team,' he said. Some ants carried leaves, some carried seeds, and all of them helped each other.",
         "3D Pixar-style. A cutaway of a big, busy ant colony with underground tunnels. Worker ants carry leaves, seeds and food in a neat line. The camera glides through the tunnels and reveals a gentle queen ant surrounded by helpers. Rusty proudly shows everything to the spider. Sound effects: marching footsteps, tiny carrying grunts, soft chatter, tunnel echoes. No background music."),
        ("A solo explorer",
         "'I live alone,' said the spider. 'I am a solo explorer.' It spun a tiny silk thread that sparkled in the sunlight. Rusty thought it was beautiful.",
         "3D Pixar-style. The mimic spider sits alone on a leaf in warm sunlight and spins a tiny glittering silk thread into the air. The thread shines like a rainbow. The camera makes a gentle slow orbit; the red ant watches with amazement. The contrast between teamwork and solo life feels funny and heartwarming. Sound effects: soft silk-spinning sound, sparkle shimmer, light breeze, tiny 'wow'. No background music."),
        ("Different, but friends",
         "Rusty smiled. 'You live alone and I live in a big family,' he said. 'We are different, but we can still be friends!' The spider smiled back. 'Yes, friends!'",
         "3D Pixar-style. The red ant and the spider sit on the dry leaf. The ant gently pats the spider's shoulder and holds out a tiny leaf-handshake. Little hearts and sparkles float up. The camera moves in close on their happy faces. Sound effects: soft happy giggles, sparkle chimes, gentle leaf rustle, a warm 'aww' sound. No background music."),
        ("Everyone has a superpower",
         "They laughed together on the dry leaf as the sun went down. 'In nature,' said Rusty, 'everyone has a special superpower.' 'And now we have a new friend,' said the spider. And that, my dears, is the end of the story. Remember: look at spiders with your eyes, not with your hands.",
         "3D Pixar-style. Golden sunset over the forest floor, orange and pink sky. The red ant and the spider laugh on the dry leaf as tiny sparkles float around them. The camera slowly pulls back to show the anthill, the leaf and the peaceful forest. Sound effects: soft breeze, happy giggles, sparkle pings, distant insect chirps, gentle leaf rustle. No background music."),
    ],
})
