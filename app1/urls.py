from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:chapter_id>/", views.page1, name="page1"),
    path("<int:chapter_id>/<int:section_id>/", views.section_page, name="section"),
    path("Alg_section_page/", views.Alg_section_page, name="algorithms"),
    path("Calc_section_page/", views.Calc_section_page, name="section"),
    path("DM_section_page/", views.DM_section_page, name="section"),
    path("Stats_section_page/", views.Stats_section_page, name="section"),
    path("LA_section_page/", views.LA_section_page, name="section")
]