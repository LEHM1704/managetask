from django.db import models

# Create your models here.


class Task(models.Model):
    title=models.CharField(max_length=100, verbose_name='Titulo')
    description=models.TextField(blank=True, null=True, verbose_name='Descripcion')
    is_completed=models.BooleanField(default=False, verbose_name='completo')
    created=models.DateTimeField(auto_now=True,verbose_name='Fecha de creación')
    
    class Meta:
        ordering=['-created']
        
    def __str__(self):
        return self.title