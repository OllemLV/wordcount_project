from django.shortcuts import render

import operator

# Create your views here.
def wordcountpage(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def count(request):
    fulltext = request.POST.get('fulltext', False)
    wordlist = fulltext.split()

    mydict = {}
    for word in wordlist:
        if word in mydict:
            mydict[word] += 1;
        else:
            mydict[word] = 1;

    wordcount = sorted(mydict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'myapp/count.html', {'fulltext':fulltext, 'count': len(wordlist), 'wordcount': wordcount})
