from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class Cosine_Sim:
	def __int__(self):
		self.clusts={}
		self.clust_no=1

	def similarity_matrix(self, cleaned_array):
		vectorizer = CountVectorizer().fit_transform(cleaned_array)
		vectors = vectorizer.toarray()
		csim = cosine_similarity(vectors)
		return csim


	def clusters(self, slot_replaced_sentences, cleanup_sentences, min_length_clusters, min_similarity, others_limit=100):
		similarity_matrx = self.similarity_matrix(slot_replaced_sentences)
		print("others_count_"+str(len(slot_replaced_sentences)))

		other_solos = []
		dct=[]
		other_solos_slot_replaced_sents = []
		for arr in similarity_matrx:
			temp = []
			other_temp=[]
			for i in range(len(arr)):
				if arr[i] >= min_similarity:
					if slot_replaced_sentences[i] not in dct:
						dct.append(slot_replaced_sentences[i])
						temp.append(cleanup_sentences[i])
						other_temp.append(slot_replaced_sentences[i])
			if len(temp) < min_length_clusters:
				other_solos.extend(temp)
				other_solos_slot_replaced_sents.extend(other_temp)
			elif len(temp) >= min_length_clusters:
				self.clusts["C" + str(self.clust_no) + "_" + str(min_similarity) + "_" + str(len(temp))] = temp
				self.clust_no = self.clust_no + 1

		if len(other_solos) >= (others_limit + min_length_clusters + 1) and min_similarity >= 0.2:
			self.clusters(other_solos_slot_replaced_sents, other_solos, min_length_clusters, round(min_similarity - 0.1, 1), others_limit)
		else:
			self.clusts["Others_" + str(min_similarity) + "_" + str(len(other_solos))] = other_solos

		return self.clusts
