from django.urls import path

from . import views

app_name="wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.lookup_entries, name="lookup_entries"),
    path("search", views.search, name="search"),
    path("random", views.random_search, name="random_search"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("newpage", views.new_page, name="new_page")

]
