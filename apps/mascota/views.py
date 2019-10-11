from django.shortcuts import render, redirect

from django.http  import HttpResponse

from apps.mascota.forms import MascotaForm

def index (request):
    return render(request, 'mascota/index.html') #Mostrar en la pagina principal el texto index

def mascota_view (request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = MascotaForm() #Renderizar el formulario

    return render (request, 'mascota/mascota_form.html', {'form':form})

