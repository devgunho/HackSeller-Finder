#%%
from collections import Counter
import gensim
corpus_path = 'merged_text.txt'


class Documents:
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path, encoding='utf-8') as f:
            for doc in f:
                yield doc.strip().split()


documents = Documents(corpus_path)
# %%

dictionary = gensim.corpora.Dictionary(documents)
print('dictionary size : %d' % len(dictionary))
#%%

min_count = 40
word_counter = Counter((word for words in documents for word in words))
removal_word_idxs = {
    dictionary.token2id[word] for word, count in word_counter.items()
    if count < min_count
}

dictionary.filter_tokens(removal_word_idxs)
dictionary.compactify()
print('dictionary size : %d' % len(dictionary))

# %%


class Corpus:
    def __init__(self, path, dictionary):
        self.path = path
        self.dictionary = dictionary
        self.length = 0

    def __iter__(self):
        with open(self.path, encoding='utf-8') as f:
            for doc in f:
                yield self.dictionary.doc2bow(doc.split())

    def __len__(self):
        if self.length == 0:
            with open(self.path, encoding='utf-8') as f:
                for i, doc in enumerate(f):
                    continue
            self.length = i + 1
        return self.length


corpus = Corpus(corpus_path, dictionary)
for i, doc in enumerate(corpus):
    if i >= 5:
        break
    print(doc)
# %%
f = open("ouput.txt", 'w')
NUM_TOPICS = 20
ldamodel = gensim.models.ldamodel.LdaModel(
    corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)
topics = ldamodel.print_topics(num_words=100)
for topic in topics:
    f.write(str(topic))
    f.write('\n')
f.close()
