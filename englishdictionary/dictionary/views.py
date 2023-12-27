from django.shortcuts import render
from django.http import HttpResponse
from PyDictionary import PyDictionary

# Create your views here.
def home(request):
    return render(request, 'index.html')

def words(request):
    if request.method == "GET":
        wrd = request.GET.get('search')
        dictionary = PyDictionary()
        try:
            context = {
                'word': wrd,
                'noun': dictionary.meaning(wrd)['Noun'][0],
                'synonym': dictionary.synonym(wrd),
                'antonym': dictionary.antonym(wrd),
            }
        except:
            context = {'noun': None}
        return render(request, 'index.html', context)