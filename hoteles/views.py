from django.shortcuts import render, redirect, get_object_or_404
from hoteles.models import Ciudad, DatosHotel
from hoteles.forms import CiudadForm,HotelForm

def hoteles(request):
	hoteles = DatosHotel.objects.all()
	return render(request, 'hoteles/hoteles.html',{'hoteles':hoteles})

def hotelNuevo(request):
	if request.method == "POST":
		form = HotelForm(request.POST)
		if form.is_valid():
			hotel = form.save()
			hotel.save()
			return redirect('hoteles.views.hoteles')
	else:
		form = HotelForm()
	return render(request, 'hoteles/hotel_edit.html',{'form':form,'nuevo':'Nuevo'})

def hotelEditar(request, pk):
	hotel = get_object_or_404(DatosHotel, pk=pk)
	if request.method == "POST":
		form = HotelForm(request.POST, instance=hotel)
		if form.is_valid():
			hotel = form.save()
			hotel.save()
			return redirect('hoteles.views.hoteles')
	else:
		form = HotelForm(instance=hotel)
	return render(request, 'hoteles/hotel_edit.html',{'form':form, 'nuevo':'Actualizar'})

def hotelEliminar(request, pk):
	hotel = get_object_or_404(DatosHotel, pk=pk)
	hotel.delete()
	return redirect('hoteles.views.hoteles')

def ciudades(request):
	ciudades = Ciudad.objects.order_by('nombre')
	return render(request, 'hoteles/ciudades.html',{'ciudades':ciudades})

def ciudadNueva(request):
	if request.method == "POST":
		form = CiudadForm(request.POST)
		if form.is_valid():
			ciudad = form.save()
			ciudad.save()
			return redirect('hoteles.views.ciudades')
	else:
		form = CiudadForm()
	return render(request, 'hoteles/ciudad_edit.html',{'form':form,'nuevo':'Nueva'})

def ciudadEditar(request, pk):
	ciudad = get_object_or_404(Ciudad, pk=pk)
	if request.method == "POST":
		form = CiudadForm(request.POST, instance=ciudad)
		if form.is_valid():
			ciudad = form.save()
			ciudad.save()
			return redirect('hoteles.views.ciudades')
	else:
		form = CiudadForm(instance=ciudad)
	return render(request, 'hoteles/ciudad_edit.html',{'form':form, 'nuevo':'Actualizar'})

def ciudadEliminar(request, pk):
	ciudad = get_object_or_404(Ciudad, pk=pk)
	ciudad.delete()
	return redirect('hoteles.views.ciudades')