from django.contrib import admin
from .models import (Chapter, Section, AlgChapter, AlgSection,
                     LAChapter, LASection, CalcChapter, CalcSection, DMChapter,
                     DMSection, StatsSection, StatsChapter)
# Register your models here.
admin.site.register(Chapter)
admin.site.register(Section)
admin.site.register(AlgSection)
admin.site.register(AlgChapter)
admin.site.register(CalcSection)
admin.site.register(CalcChapter)
admin.site.register(DMSection)
admin.site.register(DMChapter)
admin.site.register(StatsSection)
admin.site.register(StatsChapter)
admin.site.register(LASection)
admin.site.register(LAChapter)