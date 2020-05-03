"""
Text Clustering: Cosine_Sim

Author: Jinraj K R <jinrajkr@gmail.com>
Created Date: 1-Apr-2020
Modified Date: 1-May-2020
===================================

``similarity_matrix`` method takes array of utterances as parameter
> convert a collection of text documents to a matrix of token counts
> compute cosine similarity between samples in X and Y, where X and Y are the arrays
So, similarities identified from one utterance against all other utterances

``clusters`` method takes array of cleaned up utterances as parameter with other required parameters
> based on the min_similarity score cluster them together
and returns clustered utterances

"""

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
					if original_sentences[i] not in dct:
						dct.append(original_sentences[i])
						temp.append(original_sentences[i])
						other_temp.append(slot_replaced_sentences[i])

			if len(temp) < min_length_clusters:
				other_solos.extend(temp)
				other_solos_slot_replaced_sents.extend(other_temp)
			else:
				self.clusts["C" + str(self.clust_no) + "_" + str(max_similarity) + "_" + str(len(temp))] = temp
				self.clust_no = self.clust_no + 1

		print("others_count_"+str(len(other_solos)))
		if len(other_solos) >= (others_limit + min_length_clusters + 1) and max_similarity > min_similarity:
			self.clusters(other_solos_slot_replaced_sents, other_solos, min_length_clusters, round(max_similarity - 0.1, 1), min_similarity, others_limit)
		else:
			self.clusts["Others_" + str(max_similarity) + "_" + str(len(other_solos))] = other_solos

		return self.clusts
