from django.urls import re_path
from . import views

app_name = 'leaf_oj'
urlpatterns = [
    re_path(r'^$', views.index_view, name='index'),
    re_path(r'^problems/?$', views.problems_view, name='problems'),
    re_path(r'^problems/(?P<problem_id>P\d+)/?$', views.problem_view, name='problem'),
    re_path(r'^login/?$', views.login_view, name='login'),
]