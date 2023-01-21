from django.urls import path,include
from.import views
app_name='home'

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('trophies',views.trophies,name='trophies'),
    path('players',views.players,name='players'),
    path('formexm',views.formexm,name='formexm'),
    path('loginexm',views.loginexm,name='loginexm'),
    path('homeexm',views.homeexm,name='homeexm'),



    

    
    
]