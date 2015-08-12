from django.conf.urls import url
from hoteles import views

urlpatterns = [
    url(r'^$', views.hoteles),
    url(r'^hoteles/nuevo/$', views.hotelNuevo),
    
    url(r'^hoteles/(?P<pk>[0-9]+)/edit/$', views.hotelEditar, name='hotel_edit'),
    url(r'^hoteles/(?P<pk>[0-9]+)/del/$', views.hotelEditar, name='hotel_eliminar'),

	url(r'^ciudades/$', views.ciudades),
    url(r'^ciudades/nueva/$', views.ciudadNueva),
    url(r'^ciudades/(?P<pk>[0-9]+)/edit/$', views.ciudadEditar, name='ciudad_edit'),
    url(r'^ciudades/(?P<pk>[0-9]+)/del/$', views.ciudadEliminar, name='ciudad_eliminar'),

]