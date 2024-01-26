from django.urls import path,include
from .import views

app_name="home"
urlpatterns=[
    path('',views.home,name="home"),
    path('get_quiz/',views.get_quiz,name="get_quiz"),
    path('quiz/',views.quiz,name='quiz'),
]