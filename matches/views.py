# from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views import View
from .excel import excel_to_db
import pandas as pd
from .models import Match


class Index(View):
    template_name = 'matches/all_matches.html'
    context = {}

    def get(self, request):
        if request.GET.get('delete_btn') == 'Delete':
            Match.objects.all().delete()
        return render(request, self.template_name, self.context)


class Load_excel(View):
    template_name = 'index.html'
    context = {}

    def post(self, request):
        if request.POST.get('upload_btn') == 'Upload':
            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            if fs.exists(uploaded_file.name):
                fs.delete(uploaded_file.name)
            fs.save(uploaded_file.name, uploaded_file)
            df = pd.read_excel(uploaded_file, sheet_name='all')
            excel_to_db(df)
        return render(request, self.template_name, self.context)


def index(request):
    ctx = {}
    return render(request, 'index.html', ctx)


def all_matches(request):
    ctx = {}
    ctx['matches'] = Match.objects.all()
    return render(request, 'matches/all_matches.html', ctx)


def filters(request):
    ctx = {}
    ctx['matches'] = Match.objects.all()
    if request.method == "POST":
        country = request.POST.get('country')
        winner = request.POST.get('winner')
        if country not in 'all':
            ctx['matches'] = Match.objects.filter(champ=country)
        if winner not in 'all':
            ctx['matches'] = Match.objects.filter(result=winner)
        return render(request, 'matches/filters.html', ctx)
    return render(request, 'matches/filters.html', ctx)


def load_excel(request):
    ctx = {}
    if request.POST.get('upload_btn') == 'Upload':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        if fs.exists(uploaded_file.name):
            fs.delete(uploaded_file.name)
        fs.save(uploaded_file.name, uploaded_file)
        df = pd.read_excel(uploaded_file, sheet_name='all')
        excel_to_db(df)
    return render(request, 'matches/load_excel.html', ctx)


def delete(request):
    ctx = {}
    ctx['matches'] = Match.objects.all()
    if request.method == 'GET':
        Match.objects.all().delete()
    return render(request, 'matches/all_matches.html', ctx)

# def upload(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         fs = FileSystemStorage()
#         if fs.exists(uploaded_file.name):
#             fs.delete(uploaded_file.name)
#         fs.save(uploaded_file.name, uploaded_file)
#
#         df = pd.read_excel(uploaded_file, sheet_name='all')
#         excel_to_db(df)
#     return render(request, 'index.html')