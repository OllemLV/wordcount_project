from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.wordcountpage, name='wordcountpage'),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about'),
]
