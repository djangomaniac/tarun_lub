from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_catalogue, name='catalogue'),
    path('sulfonates/', views.sulfo_view, name='sulfo_view'),
    path('industrial-lub/', views.indus_view, name='indus_view'),
    path('auto-lub/', views.auto_view, name='auto_view'),
    path('textile-lub/', views.tex_view, name='tex_view'),
]
