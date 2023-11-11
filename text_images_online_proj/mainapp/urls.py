from django.urls import path
from mainapp.views import main_page, gallery_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('gallery/', gallery_page, name='gallery_page'),
]