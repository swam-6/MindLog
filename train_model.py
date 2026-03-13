from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib, os

positives = [
    "Feeling great today, had a wonderful time with friends",
    "So happy and energetic, accomplished a lot at work",
    "Woke up refreshed, life feels good right now",
    "Had a productive day, feeling motivated and optimistic",
    "Grateful for everything, enjoying the little moments",
    "Excited about upcoming plans, feeling cheerful",
    "Great workout today, feeling strong and positive",
    "Spent quality time with family, feeling loved",
    "Everything is going smoothly, in a great mood",
    "Feeling confident and ready to take on challenges",
    "Laughed a lot today, life is good and bright",
    "Received great news, feeling on top of the world",
    "Enjoying my hobbies, feeling at peace with myself",
    "Had a fulfilling day, feeling truly satisfied",
    "Feeling hopeful about the future ahead",
    "Celebrated a small win today, feeling proud",
    "Morning walk was refreshing, full of energy",
    "Connected with an old friend, feeling warm inside",
    "Finished a big project, feeling accomplished and proud",
    "Sunny day lifted my mood, feeling joyful and alive",
    "Amazing day full of laughter and good moments",
    "Feeling blessed and content with my life",
    "Best day in a long time, feeling fantastic",
    "Full of energy and love for life today",
    "Super motivated and energized this morning",
    "Life is beautiful today, feeling deeply grateful",
    "Radiant mood, everything clicked perfectly today",
    "Smiling all day without any specific reason",
    "Thriving and happy, mood is excellent",
    "Feeling unstoppable, positive about everything",
]

neutrals = [
    "Today was okay, nothing special happened",
    "Regular day at work, feeling neither good nor bad",
    "Did my routine tasks, mood is stable today",
    "Nothing exciting but nothing bad either today",
    "Average day, just going through the motions",
    "Feeling fine, just a normal uneventful day",
    "Work was okay, came home and relaxed a bit",
    "Had a decent meal, watched some TV tonight",
    "Not much to report, feeling neutral and calm",
    "Day was unremarkable, mood is steady and flat",
    "Completed tasks as usual, no strong feelings today",
    "Just existing today, not feeling much at all",
    "Routine day, nothing to complain or cheer about",
    "Moderate energy, did some chores around the house",
    "Feeling okay overall, just tired from long work",
    "Ordinary day, nothing really to write home about",
    "Stayed home most of the day, feeling quite calm",
    "Not sad not happy, just in the middle today",
    "Mild day overall, did some reading before bed",
    "Feeling blank, just going with the flow easily",
    "Got through the day, nothing special to note",
    "Feeling neither here nor there about today",
    "Day passed quietly without any excitement",
    "Mood is steady, nothing interesting to report",
    "Just another day, feeling okay and stable",
    "Things are normal, no real complaints today",
    "Quiet day at home, feeling reasonably stable",
    "Middle of the road kind of day overall",
    "Calm and unbothered by anything today",
    "Not much going on, feeling fine enough",
]

anxious = [
    "Really worried about my exam tomorrow, can't stop thinking",
    "Feeling very anxious and stressed about upcoming deadlines",
    "Heart racing constantly, can't seem to calm down today",
    "Overwhelmed with work pressure, feeling nervous all day",
    "So much on my mind, can't focus on anything at all",
    "Panic attack earlier today, still shaking from it",
    "Scared about the future, constant unrelenting worry",
    "Restless and on edge all day, can't sit still",
    "Catastrophizing everything, my mind just won't stop",
    "Feeling tense and irritable, snapped at everyone today",
    "Chest feels tight and anxious, worried about health",
    "Can't sleep at all because my brain won't stop",
    "Dreading tomorrow, feels like everything will go wrong",
    "Feeling jittery and uneasy for absolutely no reason",
    "Social anxiety hit hard today, avoided all people",
    "Worried about money endlessly and can't let it go",
    "Feeling completely overwhelmed and totally out of control",
    "Nervous energy all day long, couldn't relax at all",
    "Hyperventilating earlier, feel completely drained now",
    "Everything feels uncertain and I really can't cope",
    "Constant worry about what might happen next",
    "Stomach in knots for most of the day today",
    "Can't shake this terrible feeling of dread at all",
    "Overthinking every single little thing obsessively",
    "On edge and very irritable, unable to relax",
    "Mind is racing nonstop and I can't stop it",
    "Feeling trapped and totally overwhelmed today",
    "Sweating and shaking anxiously for no clear reason",
    "Scared something very bad will happen soon",
    "Anxiety is through the roof today, feel awful",
]

depressed = [
    "Don't see the point in anything anymore at all",
    "Feeling completely empty and utterly hopeless today",
    "Cried for most of the day, don't even know why",
    "No energy to get out of bed, everything feels heavy",
    "Feel like a complete burden to everyone around me",
    "Nothing brings me joy, even things I once loved",
    "Deep persistent sadness that just won't go away",
    "Feeling completely worthless and like I'm failing",
    "Can't stop having dark thoughts about everything",
    "Isolated myself all day, didn't want to face anyone",
    "Feeling numb and totally disconnected from the world",
    "Lost interest in everything, just barely existing now",
    "Crying for no reason, feeling completely lost inside",
    "Hopelessness is overwhelming, can't see any way out",
    "Very low mood all day, struggled to do basic things",
    "Feeling like absolutely nothing will ever get better",
    "Exhausted emotionally and completely spiritually drained",
    "Withdrawing from everyone I know, feel so utterly alone",
    "Mood is rock bottom today, truly cannot function",
    "Dark heavy cloud over me all day, feeling broken",
    "Woke up deeply sad and went to bed even sadder",
    "All motivation is completely and totally gone now",
    "Very hard to find any reason to keep going today",
    "Everything feels pointless, grey, and utterly meaningless",
    "Stayed in bed all day today, just couldn't move",
    "Feeling invisible, like nobody even notices I exist",
    "Deep emptiness inside that absolutely nothing will fill",
    "Skipped meals, have absolutely no appetite at all",
    "Feel like I'm watching my life from far outside",
    "Broken inside and struggling badly to function today",
]

texts = positives + neutrals + anxious + depressed
labels = ["Positive"]*30 + ["Neutral"]*30 + ["Anxious"]*30 + ["Depressed"]*30

X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.2, random_state=42, stratify=labels
)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=3000, ngram_range=(1,2), stop_words="english", sublinear_tf=True)),
    ("clf", SVC(kernel="linear", C=1.0, probability=True, random_state=42))
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("=== Model Training Complete ===")
print(classification_report(y_test, y_pred))

os.makedirs("backend/ml", exist_ok=True)
joblib.dump(pipeline, "backend/ml/mood_model.pkl")
print("✓ Model saved to backend/ml/mood_model.pkl")
