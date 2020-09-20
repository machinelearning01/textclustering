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

	def similarity_gensim(self, cleaned_array):
		tokenzied_words=[nltk.word_tokenize(sent) for sent in cleaned_array]
		self.model = gensim.models.Word2Vec(tokenzied_words, min_count=1, size=32, sg=1)
		sent_embedding=[]
		for sent in cleaned_array:
			sent_embedding.append((self.get_phrase_vector(sent))[0])
		csim=cosine_similarity(sent_embedding)
		print("gensim csim", csim)
		return csim

	def similarity_matrix(self, cleaned_array):
		vectorizer = CountVectorizer().fit_transform(cleaned_array)
		vectors = vectorizer.toarray()
		csim = cosine_similarity(vectors)
		return csim

	def truncate(self, f, n):
		return math.floor(f * 10 ** n) / 10 ** n

	def clusters(self, slot_replaced_sentences, original_sentences, min_length_clusters, max_similarity, min_similarity, others_limit):
		# similarity_matrx = self.similarity_gensim(slot_replaced_sentences)
		similarity_matrx=self.similarity_matrix(slot_replaced_sentences)
		# print(similarity_matrx)

		print("*************** ----- ***********")
		t1 = t.time()
		alen = len(original_sentences)
		dict={}
		for i in range(1, alen):
			for j in range(i):
				rval = round(similarity_matrx[i][j],8)
				if rval > 0.0:
					dict[str(i)+","+str(j)] = rval

		listofTuples = sorted(dict.items(), reverse=True, key=lambda x: x[1])
		# print("ordered similar grouping", listofTuples)
		clust_dict={}
		for elem in listofTuples:
			per=self.truncate(elem[1],1)  #0.5
			indexes = elem[0].split(',')  #[5,9]
			# print(elem[0], ":", elem[1], per)
			done=False
			for key, values in clust_dict.items():
				if indexes[0] in values:
					done=True
					if key == per and indexes[1] not in values:
						clust_dict[per].append(indexes[1])
					else:
						break
				elif indexes[1] in values:
					done=True
					if key == per and indexes[0] not in values:
						clust_dict[per].append(indexes[0])
					else:
						break
			if done == False:
				if per in clust_dict.keys():
					clust_dict[per] = indexes
				else:
					clust_dict[per] = indexes
			# print(clust_dict)
		# print(clust_dict)
		print("clusterd in - ", (t.time() - t1))

		for v in clust_dict.values():
			c=[]
			for i in v:
				c.append(original_sentences[int(i)])
			# print(c)

		# print("similarity_matrx", str(similarity_matrx))
		# self.traverse(similarity_matrx)

		# other_solos = []
		# dct=[]
		# other_solos_slot_replaced_sents = []
		# for arr in similarity_matrx:
		# 	temp = []
		# 	other_temp=[]
		# 	for i in range(len(arr)):
		# 		if arr[i] >= max_similarity:
		# 			if original_sentences[i] not in dct:
		# 				dct.append(original_sentences[i])
		# 				temp.append(original_sentences[i])
		# 				other_temp.append(slot_replaced_sentences[i])
		#
		# 	if len(temp) < min_length_clusters:
		# 		other_solos.extend(temp)
		# 		other_solos_slot_replaced_sents.extend(other_temp)
		# 	else:
		# 		self.clusts["C" + str(self.clust_no) + "_" + str(max_similarity) + "_" + str(len(temp))] = temp
		# 		self.clust_no = self.clust_no + 1
		#
		# print("others_count_"+str(len(other_solos)))
		# if len(other_solos) >= (others_limit + min_length_clusters + 1) and max_similarity > min_similarity:
		# 	self.clusters(other_solos_slot_replaced_sents, other_solos, min_length_clusters, round(max_similarity - 0.1, 1), min_similarity, others_limit)
		# else:
		# 	self.clusts["Others_" + str(max_similarity) + "_" + str(len(other_solos))] = other_solos

		return self.clusts


	def traverse(self, similarity_matrx):
		clust_dict={}
		for arr in similarity_matrx:
			for i in range(len(arr)):
				if i not in clust_dict.values():
					clust_dict[arr[i].toFixed(1)]=[]
					clust_dict[arr[i].toFixed(1)].append(i)
				else:
					clust_dict[arr[i].toFixed(1)].append(i)
		print(clust_dict)

