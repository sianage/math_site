from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    #path("<int:chapter_id>/", views.page1, name="page1"),
    path("Alg_section_page/", views.Alg_section_page, name="section"),
    path("LA_section_page/", views.LA_section_page, name="section"),
    path("Calc_section_page/", views.Calc_section_page, name="section"),
    path("DM_section_page/", views.DM_section_page, name="section"),
    path("Stats_section_page/", views.Stats_section_page, name="section"),
    path("DP_section_page/", views.DP_section_page, name="section"),
    path("<int:chapter_id>/<int:section_id>/", views.section_page, name="section"),
    path("<int:chapter_id>/<int:section_id>/", views.LA_section_page, name="section"),
    path("<int:chapter_id>/<int:section_id>/", views.Stats_section_page, name="section"),
    path("<int:chapter_id>/<int:section_id>/", views.Calc_section_page, name="section"),
    path("<int:chapter_id>/<int:section_id>/", views.DM_section_page, name="section"),
    path("<int:chapter_id>/<int:section_id>/", views.DP_section_page, name="section"),
    path("Alg_section_page/<int:algchapter_id>/<int:algsection_id>/", views.Alg_section_page2, name="algsection")
]