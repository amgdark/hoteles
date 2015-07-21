from django.shortcuts import render, redirect, get_object_or_404
from hoteles.models import Ciudad
from hoteles.forms import CiudadForm

def hola_mundo(request):
	nombre = 'Alex'
	return render(request, 'hoteles/hola.html', {'nombre':nombre})

def ciudades(request):
	ciudades = Ciudad.objects.all()
	return render(request, 'hoteles/ciudades.html',{'ciudades':ciudades})

def ciudadNueva(request, pk):
	ciudad = get_object_or_404(Ciudad, pk=pk)
	if request.method == "POST":
		form = CiudadForm(request.POST, instance=ciudad)
		if form.is_valid():
			ciudad = form.save()
			ciudad.save()
			return redirect('hoteles.views.ciudades', pk=ciudad.pk)
	else:
		form = CiudadForm(instance=ciudad)
	return render(request, 'hoteles/ciudad_edit.html',{'form':form})
