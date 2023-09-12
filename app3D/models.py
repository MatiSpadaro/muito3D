from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=30)
 

class Productos(models.Model):
    claseProducto = models.CharField(max_length=40)
    nombreProducto = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.claseProducto} - {self.nombreProducto}"
    
class Pedidos(models.Model):
    modelo3D = models.CharField(max_length=40)
    filamento = models.CharField(max_length=40)
    
