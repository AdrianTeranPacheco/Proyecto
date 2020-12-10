from django.db import models
from django.urls import reverse # Se utilizaran para direccionar los path de nuestro  proyecto  asociado.
import uuid                     # Se utlizara para relacionar los objetos.


# Create your models here.
 
class Jugete(models.Model):
     idJugete = models.UUIDField(primary_key=True, default=uuid.uuid4)
     nombreJugete = models.CharField(max_length=200)
     marca = models.CharField(max_length=200)
     precio = models.TextField(max_length=1000)
     stock = models.URLField(max_length=100, default='')
    
     def get_absolute_url(self):
		    return reverse('jugete-detail', args=[str(self.idJugete)])

     def __str__(self):
		    return self.nombreJugete
		


class Usuario(models.Model):
     idUsu = models.UUIDField(primary_key=True, default=uuid.uuid4)
     nombreUsu = models.CharField(max_length=200)
     apellido = models.CharField(max_length=200)
     pais = models.TextField(max_length=1000)
     mail = models.URLField(max_length=100, default='')
    
     def __str__(self):
        
          return self.nombreUsu
    
     def get_absolute_url(self):
        
          return reverse('Usario-detail', args=[str(self.idUsu)])


