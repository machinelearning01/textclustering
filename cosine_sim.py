from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def similar(cleaned_array):
	vectorizer = CountVectorizer().fit_transform(cleaned_array)
	vectors = vectorizer.toarray()

	csim = cosine_similarity(vectors)
	return csim