from django.db import models

# Create your models here.

class producto(models.Model):
    id_producto = models.CharField(max_length=3)
    nombre = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.id_producto} ({self.nombre})"

class productos(models.Model):
    idproducto = models.ForeignKey(producto, on_delete=models.CASCADE, related_name="entradas")
    nombre = models.IntegerField()
    precio = models.IntegerField()
    cantidad_existente=models.IntegerField()
    fecha_ingreso=models.CharField(max_length=8)

    def __str__(self):
        return f"{self.idproducto} ({self.nombre}) ({self.precio}) ({self.cantidad})"

