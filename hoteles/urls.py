from django.conf.urls import include, url
from hoteles import views

urlpatterns = [
    url(r'^hola/', views.hola_mundo),
    url(r'^ciudades/$', views.ciudades),
    url(r'^ciudades/nueva/$', views.ciudadNueva),

]