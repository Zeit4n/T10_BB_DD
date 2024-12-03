from django.shortcuts import render, redirect
from .models import Plato, Categoria
# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    else:
        return render(request,'index.html')
    
def register(request):
    if request.method == 'GET':
        return render(request,'form.html')
    else:
        categoria = Categoria.objects.get(id_categoria=request.POST['category'])
        plato = Plato.objects.create(nombre=request.POST['name'],
                                     id_categoria=categoria,
                                     precio=request.POST['price'],
                                     descripcion=request.POST['description'])
        plato.save()
        return redirect('show')
    
def show(request):
    if request.method == 'GET':
        platos = Plato.objects.all().order_by('id_plato')
        context = {
            'platos':platos,
        }
        return render(request,'show.html',context)
    else:
        return render(request,'show.html')
    

def update(request,plato_id):
    if request.method == 'GET':
        old_plato = Plato.objects.get(id_plato=plato_id)
        return render(request,'edit_plato.html',{'old_plato':old_plato})
    else:
        categoria = Categoria.objects.get(id_categoria=request.POST['category'])
        new_plato = Plato.objects.get(id_plato=plato_id)
        new_plato.nombre = request.POST['name']
        new_plato.id_categoria = categoria
        new_plato.precio = request.POST['price']
        new_plato.descripcion = request.POST['description']
        new_plato.save()
        return redirect('show')
    
def delete(request,plato_id):
    plato_del = Plato.objects.get(id_plato=plato_id)
    plato_del.delete()
    return redirect(to='show')

