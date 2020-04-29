from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class Cosine_Sim:
	def __init__(self):
		self.clusts = {}
		self.clust_no = 1

	def similarity_matrix(self, cleaned_array):
		vectorizer = CountVectorizer().fit_transform(cleaned_array)
		vectors = vectorizer.toarray()
		csim = cosine_similarity(vectors)
		return csim


	def clusters(self, slot_replaced_sentences, original_sentences, min_length_clusters, max_similarity, min_similarity, others_limit=100):
		similarity_matrx = self.similarity_matrix(slot_replaced_sentences)
		print("max_similarity", str(max_similarity))
		other_solos = []
		dct=[]
		other_solos_slot_replaced_sents = []
		for arr in similarity_matrx:
			temp = []
			other_temp=[]
			for i in range(len(arr)):
				if arr[i] >= max_similarity:
					if slot_replaced_sentences[i] not in dct:
						dct.append(slot_replaced_sentences[i])
						temp.append(original_sentences[i])
						other_temp.append(slot_replaced_sentences[i])
			if len(temp) < min_length_clusters:
				other_solos.extend(temp)
				other_solos_slot_replaced_sents.extend(other_temp)
			elif len(temp) >= min_length_clusters:
				self.clusts["C" + str(self.clust_no) + "_" + str(max_similarity) + "_" + str(len(temp))] = temp
				self.clust_no = self.clust_no + 1

		print("others_count_"+str(len(other_solos)))
		if len(other_solos) >= (others_limit + min_length_clusters + 1) and max_similarity > min_similarity:
			self.clusters(other_solos_slot_replaced_sents, other_solos, min_length_clusters, round(max_similarity - 0.1, 1), min_similarity, others_limit)
		else:
			self.clusts["Others_" + str(max_similarity) + "_" + str(len(other_solos))] = other_solos

		return self.clusts
