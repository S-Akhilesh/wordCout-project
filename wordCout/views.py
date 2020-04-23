import operator

from django.shortcuts import render

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    wordDict= {}

    for word in words:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    sortedWords = sorted(wordDict.items(),key=operator.itemgetter(1),reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'noOf': len(words), 'wordDict': sortedWords})
