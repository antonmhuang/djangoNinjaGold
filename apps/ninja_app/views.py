from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['text'] = ""
    return render(request, 'index.html')
    
def process(request):
    if 'farm' in request.POST:
        rand = random.randrange(10,21)
        request.session['gold'] = request.session['gold'] + rand
        request.session['text'] = "<p class='newgold'>Earned "+ str(rand) + " gold from the farm!</p>"  + request.session['text']
    if 'cave' in request.POST:
        rand = random.randrange(5,11)
        request.session['gold'] = request.session['gold'] + rand
        request.session['text'] = "<p class='newgold'>Earned "+ str(rand) + " gold from the cave!</p>" + request.session['text']
    if 'house' in request.POST:
        rand = random.randrange(2,6)
        request.session['gold'] = request.session['gold'] + rand
        request.session['text'] = "<p class='newgold'>Earned "+ str(rand) + " gold from the house!</p>" + request.session['text']
    if 'casino' in request.POST:
        rand = random.randrange(-50,51)
        if rand > 0:
            request.session['gold'] = request.session['gold'] + rand
            request.session['text'] = "<p class='newgold'>Earned "+ str(rand) + " gold from the casino!</p>" + request.session['text']
        else:
            request.session['gold'] = request.session['gold'] - rand
            request.session['text'] = "<p class='lostgold'>Lost "+ str(rand) + " gold from the casino!</p>" + request.session['text']
    
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
      
