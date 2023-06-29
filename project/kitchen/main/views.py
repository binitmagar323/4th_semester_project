from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render (request, 'main/index.html',{
        'cateories' : categories,
        'items' : items,
    })

def contact(request):
    return render(request, 'main/contact.html')

def signup(request):
    if request.method == 'POST':
        form =SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'main/signup.html',{
        'form' : form
    })