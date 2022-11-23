from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404
from .models import (Chapter, Section, AlgChapter, AlgSection,
                     LAChapter, LASection, CalcChapter, CalcSection, DMChapter,
                     DMSection, StatsSection, StatsChapter, DPChapter, DPSection)
from django.http import HttpResponse
#index for euler
def index(request):
    all_chapters = Chapter.objects.all()
    print("--------------------------------Index being accessed---------------------------------")
    return render(request, 'app1/index.html', {'all_chapters': all_chapters})
'''def page1(request, chapter_id):
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    return render(request, 'app1/page1.html', {'chapter': chapter})'''
def section_page(request, chapter_id, section_id):
    section = get_object_or_404(Section, pk=section_id)
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    print("--------------------------------index section page being accessed---------------------------------")
    return render(request, 'app1/section_page.html', {'section': section, 'chapter': chapter})
'''def Hanoi(request, chapter_id, section_id):
    section = get_object_or_404(Section, pk=section_id)
    print("--------------------------------Multiples3or5.html being rendered---------------------------------")
    return render(request, 'app1/Multiples3or5.html', {'section': section})'''
#-----------------------------------------------------------------------------------------------------------------------
#index for algorithms
def Alg_section_page(request):
    all_Alg_chapters = AlgChapter.objects.all()
    print("--------------------------------Alg Index being accessed---------------------------------")
    return render(request, 'app1/Alg_section_page.html', {'all_Alg_chapters': all_Alg_chapters})
#section page for algs
def Alg_section_page2(request, algchapter_id, algsection_id):
    algsection = get_object_or_404(AlgSection, pk=algsection_id)
    algchapter = get_object_or_404(AlgChapter, pk=algchapter_id)
    print("--------------------------------alg section page being accessed---------------------------------")
    return render(request, 'app1/Alg_section_page2.html', {'algsection': algsection, 'algchapter': algchapter})


def Alg_code_page(request, chapter_id, section_id):
    section = get_object_or_404(Section, pk=section_id)
    print("--------------------------------algorithms section page being accessed---------------------------------")
    return render(request, 'app1/section_page.html', {'algsection': section})
def UniqueChar(request, chapter_id, section_id):
    section = get_object_or_404(Section, pk=section_id)
    return render(request, 'app1/UniqueChar.html', {'section': section})
#-----------------------------------------------------------------------------------------------------------------------
def lines_plane(request, chapter_id, section_id):
    section = get_object_or_404(Section, pk=section_id)
    return render(request, 'app1/lines_plane.html.html', {'section': section})
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
def DP_section_page(request):
    all_DP_chapters = DPChapter.objects.all()
    return render(request, 'app1/DP_section_page.html', {'all_DP_chapters': all_DP_chapters})
