from django.contrib import admin
from django.urls import path
from base import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name='home'),
    path('index/',views.index,name='index'),
    path('index2/',views.index2,name='index2'),
    path('index3/',views.index3,name='index3'),
    path('index4/',views.index4,name='index4'),
    path('index/result/', views.result, name='result'),
    path('index2/result2/', views.result2, name='result2'),
    path('index3/result3/', views.result3, name='result3'),
    path('index4/result4/', views.result4, name='result4'),
    
]