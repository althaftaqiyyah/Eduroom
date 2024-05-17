from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'Eduroom'
    }
    return render(request, "User/index.html", context)