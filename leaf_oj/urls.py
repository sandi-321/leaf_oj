from django.urls import re_path
from . import views

app_name = 'leaf_oj'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^problems/?$', views.problems, name='problems'),
    re_path(r'^problems/(?P<problem_id>P\d+)/?$', views.problem, name='problem'),
]