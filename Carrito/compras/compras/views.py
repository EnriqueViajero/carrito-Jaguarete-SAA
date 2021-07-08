from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import productos, producto
from .forms import FormProductosCustom

# Create your views here.
def index(request):
    return render(request,"productos/index.html", {
        "lista_productos": productos.objects.all()
    })

def productos(request, id_producto):
    producto= productos.objects.get(id=id_producto)
    id_producto = productos.productos.all()
    nombre = productos.productos.all()
    no_son_productos = productos.objects.exclude(productos=productos).all()
    return render(request, "productos/productos.html", {
        "id_producto": id_producto,
        "nombre": nombre,
        "no_son_productos": no_son_productos
    })


def producto_alta(request):
   
    if request.method == "POST":
        form = FormProductosCustom(request.POST)
        if form.is_valid():
            form.save()
        return render(request,"productos/index.html", {
            "lista_productos": productos.objects.all()
        })
    else:
        form = FormProductosCustom()
        return render(request, "productos/vuelo_alta.html", {
            "form": form
        })


def producto_modificar(request, id_producto):
    un_producto = get_object_or_404(producto, id=id_producto)
    
    if request.method == "POST":     
        form = FormProductosCustom(request.POST, instance = un_producto) 
        if form.is_valid():
            form.save()
            return render(request,"productos/index.html", {
                "lista_productos": productos.objects.all()
            })
    else:
        form = FormProductosCustom(instance = un_producto)
        return render(request, 'productos/vuelo_modificar.html', {
            "un_producto": un_producto,
            "form": form
        })


def producto_eliminar(request, producto_id):
    un_producto = get_object_or_404(productos, id=producto_id)
    un_producto.delete()
    return render(request,"productos/index.html", {
        "lista_productos": productos.objects.all()
    })


def apartar(request, vuelo_id):
    if request.method == "POST":
        producto = productos.objects.get(pk=id_producto)
        id_producto = int(request.POST["producto"])
        producto = productos.objects.get(pk=id_producto)
        producto.producto.add(producto)
        return HttpResponseRedirect(reverse("compras:producto", args=(id_producto,)))

