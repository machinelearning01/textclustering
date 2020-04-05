
# https://www.youtube.com/watch?v=i3Opb3-QNX4
# https://medium.com/@mishra.thedeepak/doc2vec-simple-implementation-example-df2afbbfbad5
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

def doctovec_model(arr_clean_sentences):
    tagged_data = [TaggedDocument(words=_d, tags=[str(i)]) for i, _d in enumerate(arr_clean_sentences)]
    max_epochs = 100
    vec_size = 20
    alpha = 0.025

    model = Doc2Vec(size=vec_size,
                    alpha=alpha,
                    min_alpha=0.00025,
                    min_count=5,
                    dm=1)

    model.build_vocab(tagged_data)

    for epoch in range(max_epochs):
        print('iteration {0}'.format(epoch))
        model.train(tagged_data,
                    total_examples=model.corpus_count,
                    epochs=model.iter)
        # decrease the learning rate
        model.alpha -= 0.0002
        # fix the learning rate, no decay
        model.min_alpha = model.alpha
    model.save("saved_doc2vec_model")

def generate_clusters(arr_clean_sentences, fresh_model):
    if fresh_model:
        doctovec_model(arr_clean_sentences)
    model = Doc2Vec.load('saved_doc2vec_model')

    new_sentence = arr_clean_sentences[0].split(" ")
    print(new_sentence)
    similar_doc=model.docvecs.most_similar(positive=[model.infer_vector(new_sentence)],topn=10)
    print(similar_doc)

# v1 = model.infer_vector(new_sentence)
# print("V1_infer", v1)

# to find most similar doc using tags
# similar_doc = model.docvecs.most_similar('1')
# print(similar_doc)
