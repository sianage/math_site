from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404
from .models import Chapter, Section
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