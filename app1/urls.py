from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:chapter_id>/", views.page1, name="page1"),
    path("<int:chapter_id>/<int:section_id>/", views.section_page, name="section_page")
]