# tefsa : Topic Extraction For Scientific Articles

tefsa is a program in Python for extract topics from scientific articles in txt format. It uses Python [lda](https://pypi.python.org/pypi/lda) library.

## Installing and requirements

You need Python >= 2.6 or >= 3.3

You must install lda and nltk for using tefsa :

```
$ pip install lda
$ sudo pip install -U nltk
```

## How to use

The input file should be a text file with one article per line without \n in each line.

In the output file you can see the topics for each article and their tfidf.

you can change the number of topics that you want from each article.
