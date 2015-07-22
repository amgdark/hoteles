from django.conf.urls import url
from hoteles import views

urlpatterns = [
    url(r'^hola/', views.hola_mundo),
    url(r'^ciudades/$', views.ciudades),
    url(r'^ciudades/nueva/$', views.ciudadNueva),
    url(r'^ciudades/(?P<pk>[0-9]+)/edit/$', views.ciudadEditar, name='ciudad_edit'),
    url(r'^ciudades/(?P<pk>[0-9]+)/del/$', views.ciudadEliminar, name='ciudad_eliminar'),

]