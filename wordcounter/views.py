from django.http import HttpResponse
from django.shortcuts import render
import operator

def hi(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET["fulltext"]

    splitted = fulltext.split()

    worddictionary = {}

    for word in splitted:

        if word in worddictionary:

            worddictionary[word] += 1

        else:

            worddictionary[word] = 1


        wordlist = worddictionary.items()

        sortedlist = sorted(wordlist, key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext': fulltext, 'length': len(splitted), 'sortedlist': sortedlist})

def about(request):
    return render(request, 'about.html')
