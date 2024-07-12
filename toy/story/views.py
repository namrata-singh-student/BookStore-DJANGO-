from django.shortcuts import render,redirect
from django.http import HttpResponse
from story.models import * 

# Create your views here.


#Project Functions

def index1(request):
    return render(request,'index1.html')

def form(request):
    return render(request,'form.html')
def userForm(request):
    if request.method == 'POST':
        p = project()
        p.date = request.POST['a1']
        p.bookName = request.POST['a2']
        p.name = request.POST['a3']
        p.city = request.POST['a4']
        p.address = request.POST['a5']
        p.email = request.POST['a6']
        p.phone = request.POST['a7']
        p.save()
        return render(request, 'index1.html')
    else:
       
        return render(request, 'index1.html')
def store(request):
    p = project.objects.all()
    return render(request,'store.html',{'a':p})
def dele(request,id):
    d=project.objects.get(id=id)
    d.delete()
    return redirect('../store')

def loginn(request):
    return render(request, 'loginn.html')

def logcodee(request):
    if request.method == 'POST':
        a = request.POST.get('a1')
        b = request.POST.get('a2')
        remember = request.POST.get('remember')

        
        if a == 'admin' and b == '12345':
            data = project.objects.all()
            
            
            return render(request, 'store.html', {'a': data})
            
            
    
    
    return render(request, 'loginn.html')

def contact(request):
    return render(request,'contact.html')
