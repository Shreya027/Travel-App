from django.shortcuts import render

# Create your views here.
from mysite.forms import ContactForm,ListForm
from django.http import HttpResponse
from travel.models import Place,List,Country



def search(request):
    errors = []
    if 'q' in request.GET :
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            travel = Place.objects.filter(name__icontains=q)
            return render(request, 'search_results.html',
                          {'travel': travel, 'query': q})

    full=Place.objects.all()        
    return render(request, 'search_form.html',
              {'errors': errors,'full':full})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST ,request.FILES or None )
        if form.is_valid():
            cd = form.cleaned_data
            Place.objects.create(name=cd['name'],location=cd['location'],notes=cd['notes'],image=request.FILES['image'])
        form = ContactForm()    
        return render(request,'contact_form.html',{'form': form})               
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})    



def list(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            List.objects.create(destination=cd['destination'])
            spot = List.objects.all()
            form = ListForm()
            return render(request, 'list.html',{'form':form ,'spot':spot})

    elif request.method == 'GET':
        if 'q' in request.GET and request.GET['q']!='':
            q = request.GET['q']
            extract = List.objects.filter(destination__icontains=q)
            extract.delete()
            spot = List.objects.all()
            form = ListForm()
            return render(request, 'list.html',{'form':form ,'spot':spot})
                
    form = ListForm()
    spot=List.objects.all()
    return render(request, 'list.html', {'form': form,'spot':spot})  


def map(request):
    return render(request,'gmap.html')


def hotel(request):
    return render(request,'hotel_search.html')


def direction(request):
    return render(request,'direction.html')

def quiz(request):
    return render(request,'quiz.html')

def currency(request):
    return render(request,'currency.html')    

def index(request):
    return render(request,'index.html')     


def country(request):
    full=Country.objects.all()
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 30:
            errors.append('Please enter at most 20 characters.')
        else:
            country = Country.objects.filter(name__icontains=q)
            return render(request, 'country_form.html',
                          {'country': country,'full':full})
        
    return render(request, 'country_form.html',
              {'errors': errors,'full':full})




