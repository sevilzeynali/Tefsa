
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import gensim
from gensim import corpora, models, similarities
from gensim.models import ldamodel, lsimodel
import codecs
import string
import nltk
FILE_IN_PATH='corpus_mixe_1_article_1_ligne.txt'
STOP_WORD_PATH='stop_word.txt'
FILE_OUT_PATH='resultat_lda_corpus_mixe.txt'

fileIN=open(FILE_IN_PATH,'r').readlines()
fileStop=open(STOP_WORD_PATH,'r').readlines()
stop=list()
fileOut=codecs.open(FILE_OUT_PATH,'w','utf-8')

for i in fileStop:
  i=i.strip()
  stop.append(i)
#lemmatizing our fileIn
lemm = nltk.WordNetLemmatizer()
txt=[[lemm.lemmatize(unicode(word, 'utf-8')) for word in d.lower().split() if (word not in stop and len(word)>3) ] for d in fileIN]

#Calulate the frequencies of the words in fileIN
all_tokens=sum(txt,[])
#do a set of all tokens in our fileIn who has the frequencies less than 2
tokens_once=set(word for word in set(all_tokens) if all_tokens.count(word)<2)
#To delet the duplicated words
texts=[[word for word in text if word not in tokens_once] for text in txt]

dictionary=corpora.Dictionary(texts)
corpus=[dictionary.doc2bow(text) for text in texts]
lda=ldamodel.LdaModel(corpus,id2word=dictionary,num_topics=20)

if len(fileIN)>1:
  tfidf=models.TfidfModel(corpus)
  doctfidf=tfidf[corpus]
  ldat=ldamodel.LdaModel(doctfidf,id2word=dictionary,num_topics=10)
#writing topics in a file
dd=dict()
for i in range(0,lda.num_topics):
  fileOut.write(lda.print_topic(i)+'\n')
  dd[i]=lda.print_topic(i)



  
