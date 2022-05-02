from django.urls import path

from core import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name='logout'),
    path('register', views.registerUser, name='register'),
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('addTopic', views.add_topic, name='addTopic'),
    path('addParticipant', views.add_participant, name='addParticipant'),
    path('github', views.github, name='github'),
    path('linkedin', views.linkedin, name='linkedin'),
    path('about', views.about, name='about'),
    path('delete/<str:pk>/', views.deleteBook, name='delete'),
    path('addBook', views.add_book, name='addBook'),
    path('update/<str:pk>', views.updateBook, name='update')
]
