# https://www.youtube.com/watch?v=Otde6VGvhWM
# https://github.com/krishnaik06/Natural-Language-Processing/blob/master/word2vec.py
from gensim.models import Word2Vec

def word2vec(corpus, find_syn):
    sentences = [x.split() for x in corpus]
    
    # Training the Word2Vec model
    model = Word2Vec(sentences, min_count=4)
    words = model.wv.vocab
    # Finding Word Vectors
    # vector = model.wv['enroll']
    # print(vector)
    # Most similar words
    similar = model.wv.most_similar(find_syn)
    return similar
