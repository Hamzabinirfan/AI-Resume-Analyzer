from sklearn.feature_extraction.text import TfidfVectorizer

def get_similarity_scores(resume_texts, job_description):
    vectorizer = TfidfVectorizer(stop_words='english')
    try:
        # Convert resumes and job description to TF-IDF vectors
        vectors = vectorizer.fit_transform(resume_texts + [job_description])
        similarity_scores = []
        
        # Calculate cosine similarity for each resume
        for i in range(len(resume_texts)):
            score = (vectors[i] @ vectors[-1].T).toarray()[0][0]
            similarity_scores.append(score * 100)  # Multiply by 100 for percentage
            print(f"Resume {i} score: {similarity_scores[-1]}")  # Debugging print

        return similarity_scores
    except Exception as e:
        print(f"Error in similarity calculation: {e}")
        return []
