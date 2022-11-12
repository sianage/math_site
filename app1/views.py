from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404
from .models import (Chapter, Section, AlgChapter, AlgSection,
                     LAChapter, LASection, CalcChapter, CalcSection, DMChapter,
                     DMSection, StatsSection, StatsChapter)
from django.http import HttpResponse

def index(request):
    all_chapters = Chapter.objects.all()
    return render(request, 'app1/index.html', {'all_chapters': all_chapters})

def page1(request, chapter_id):
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    return render(request, 'app1/page1.html', {'chapter': chapter})

def section_page(request, chapter_id, section_id):
    section = get_object_or_404(Section, pk=section_id)
    return render(request, 'app1/section_page.html', {'section': section})

def Hanoi(request, chapter_id, section_id):
    section = get_object_or_404(Section, pk=section_id)
    return render(request, 'app1/Hanoi.html', {'section': section})

def lines_plane(request, chapter_id, section_id):
    section = get_object_or_404(Section, pk=section_id)
    return render(request, 'app1/lines_plane.html.html', {'section': section})

def Alg_section_page(request):
    all_Alg_chapters = AlgChapter.objects.all()
    return render(request, 'app1/Alg_section_page.html', {'all_Alg_chapters': all_Alg_chapters})

def Calc_section_page(request):
    all_Calc_chapters = CalcChapter.objects.all()
    return render(request, 'app1/Calc_section_page.html', {'all_Calc_chapters': all_Calc_chapters})

def DM_section_page(request):
    all_DM_chapters = DMChapter.objects.all()
    return render(request, 'app1/DM_section_page.html', {'all_DM_chapters': all_DM_chapters})

def Stats_section_page(request):
    all_Stats_chapters = StatsChapter.objects.all()
    return render(request, 'app1/Stats_section_page.html', {'all_Stats_chapters': all_Stats_chapters})

def LA_section_page(request):
    all_LA_chapters = LAChapter.objects.all()
    return render(request, 'app1/LA_section_page.html', {'all_LA_chapters': all_LA_chapters})

