from django.db import models

# Create your models here.a
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categoria'

    def __str__(self) -> str:
        return self.categoria
    
class Plato(models.Model):
    id_plato = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, to_field='id_categoria',db_column='id_categoria')
    precio = models.IntegerField(verbose_name='Precio')
    descripcion = models.TextField(blank=True,verbose_name='Descripción')

    class Meta:
        managed = False
        db_table = 'plato'

    def __str__(self) -> str:
        return self.nombre
    

    