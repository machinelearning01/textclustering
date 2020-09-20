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
import gensim
import nltk
import numpy as np
import math
import time as t

class Cosine_Sim:
	def __init__(self):
		self.clusts = {}
		self.clust_no = 1
		self.model = ""
		self.sim_matrix=""

	def get_word_vector(self, word):
		vec = 0
		try:
			vec = self.model[word] #np.array(outputvariable[word])*tf_idf[word]
		except:
			vec = 0
		return (vec)

	def get_phrase_vector(self, phrase):
		vec = 0
		length = len(phrase.split(' '))
		for word in phrase.split(' '): 
			vec = vec + self.get_word_vector(word)
		vec = vec/length
		return vec.reshape(1, -1)

	def gensim_wtv(self, cleaned_array):
		print("gensim w2v...")
		tokenzied_words=[nltk.word_tokenize(sent) for sent in cleaned_array]
		self.model = gensim.models.Word2Vec(tokenzied_words, min_count=1, size=32, sg=1)
		sent_embedding=[]
		for sent in cleaned_array:
			sent_embedding.append((self.get_phrase_vector(sent))[0])
		csim=cosine_similarity(sent_embedding)
		# print("gensim csim", csim)
		return csim

	def vectize(self, cleaned_array):
		print("sklrn vec...")
		vectorizer = CountVectorizer().fit_transform(cleaned_array)
		vectors = vectorizer.toarray()
		csim = cosine_similarity(vectors)
		return csim

	def asort(self):
		l = self.sim_matrix.shape[0]
		print("shape - ",l)
		t1 = t.time()
		r = np.arange(l)
		mask = r[:, None] > r
		inds = list(zip(*np.where(mask)))
		print("inds in - ", (t.time() - t1))
		t2 = t.time()
		idx = self.sim_matrix[mask].argsort()[::-1]
		# print(idx)
		print("sorted in - ", (t.time() - t2))
		return idx, inds

	def truncate(self, f, n):
		return math.floor(f * 10 ** n) / 10 ** n

	def cluster(self, s, inds):
		t1 = t.time()
		clusts = {}
		ct=1
		for i in s:
			per = self.truncate(self.sim_matrix[inds[i]], 1)
			if per > 0.0:
				ct=ct+1
				idx = list(inds[i])  # 0.5
				# print(idx, per, clusts)
				done = False
				for key, values in clusts.items():
					if idx[0] in values:
						done = True
						if key.split('_')[0] == str(per) and idx[1] not in values:
							clusts[key].append(idx[1])
						else:
							break
					elif idx[1] in values:
						done = True
						if key.split('_')[0] == str(per) and idx[0] not in values:
							clusts[key].append(idx[0])
						else:
							break
				if done == False:
					mtchs = [int(key.split('_')[1]) for key in clusts.keys() if key.startswith(str(per))]
					if mtchs:
						clusts[str(per) + '_' + str(int(max(mtchs)+1))] = idx
					else:
						clusts[str(per) + '_1'] = idx
		print("clusterd in - ", (t.time() - t1))
		return clusts

	def clusters(self, slot_replaced_sentences, original_sentences, min_length_clusters, max_similarity, min_similarity):
		# self.sim_matrix=np.array(self.gensim_wtv(slot_replaced_sentences))
		self.sim_matrix=np.array(self.vectize(slot_replaced_sentences))
		# print(self.sim_matrix)

		s, inds = self.asort()
		clus = self.cluster(s, inds)
		# print(clus)
		for k, v in clus.items():
			c=[]
			for i in v:
				c.append(original_sentences[int(i)])
			self.clusts[k]=c
		return self.clusts


