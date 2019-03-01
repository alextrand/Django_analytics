from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    context = {}
    context['key'] = 'value'
    context['four'] = 2 + 2
    return render(request, 'index.html', context)


def upload2(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        if fs.exists(uploaded_file.name):
            fs.delete(uploaded_file.name)
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'action/action.html')


def calc(request):
    # if request.method == 'GET':
    return render(request, 'action/calc.html', {})





