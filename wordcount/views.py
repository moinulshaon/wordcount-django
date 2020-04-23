from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
from operator import itemgetter

def home(req):
    return render(req, 'home.html')

def counts(req):
    text = req.GET['fulltext']
    cnt = len(text.split())

    counter = Counter()
    for word in text.split():
        counter[word]+=1

    sortedWords = sorted(counter.items(), key=itemgetter(1), reverse=True)

    return render(req, 'counts.html', {
        'fulltext': text,
        'cnt': cnt,
        'sortedWords': sortedWords,
    })