from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views import View
from .excel import excel_to_db
import pandas as pd
from .models import Match
from django.core.paginator import Paginator
from django.shortcuts import render


def listing(request, matches):
    # match_list = Match.objects.all()
    paginator = Paginator(matches, 10)
    page = request.GET.get('page')
    matches = paginator.get_page(page)
    return matches


def index(request):
    ctx = {}
    return render(request, 'index.html', ctx)


def add_match(request):
    return redirect('/admin/matches/match/add/')


def all_matches(request):
    ctx = {}
    matches = Match.objects.all()
    ctx['matches'] = listing(request, matches)
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
        if country not in 'all' and winner not in 'all':
            ctx['matches'] = Match.objects.filter(champ=country, result=winner)
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
