import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and process the CSV
try:
    df = pd.read_csv("medical_faq.csv", quotechar='"')
    print("✅ CSV Loaded:", df.shape)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['question'].astype(str))
except Exception as e:
    print("❌ Error loading or vectorizing CSV:", e)
    df = pd.DataFrame()
    X = None
    vectorizer = None

def get_bot_response(user_query):
    try:
        user_vec = vectorizer.transform([user_query])
        scores = cosine_similarity(user_vec, X)
        best_idx = scores.argmax()
        confidence = scores[0][best_idx]

        if confidence < 0.3:
            return "I'm not sure how to help with that. Please consult a doctor."

        return df.iloc[best_idx]['answer']
    except Exception as e:
        print("❌ get_bot_response error:", e)
        return "Sorry, something went wrong."
