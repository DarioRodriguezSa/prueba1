
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from inicio import views as view_m
from actividades import views as views_a
from eventos import views as views_e
from gastos import views as views_g


urlpatterns = [
    
 
    path('', include('auntenticacion.urls')),
    path('', include('miembros.urls')),
    
    path('admin/', admin.site.urls), 
    path('',view_m.home, name="home"),






#------------------------------ACTIVIDADES
    path('actividades/', views_a.actividades, name="actividades"),



#--------------------------------EVENTOS
    path('eventos/', views_e.eventos, name="eventos"),




#---------------------------------GASTOS
    path('gastos/', views_g.gastos, name="gastos"),
    




   



  



    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

