from .views import *
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# l'entete des importation des fichier piont py 


urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('galerie/',galerie,name='galerie'),
    path('product/',product,name='product'),
    path('apropos/',apropo,name='apropos'),
    path('detail/<int:fruit_id>/', detail, name='detail'),
    path('connexion/',auth_views.LoginView.as_view(template_name = 'pages/connexion.html'),name='connexion'),
    path('deconnexion/',auth_views.LogoutView.as_view(next_page ='home'),name ='deconnexion'),
    path('inscription/',inscription,name='inscription'),
]
