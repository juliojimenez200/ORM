from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def validar_titulo(titulo): 
    if 'cobol' in titulo: 
        raise ValidationError(f'{titulo} no se vende mucho') 
    return titulo



class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.nombre

    class Meta:
        managed = True
        db_table = 'libreria_editorial'

class Libro(models.Model):
    estatus_libro = (('P','Publish'),('M','Meap'))
    isbn = models.CharField(max_length=13, primary_key=True) 
    titulo = models.CharField(max_length=70, blank=True, validators=[validar_titulo,]) 
    paginas = models.PositiveIntegerField() 
    fecha_publicacion = models.DateField(null=True) 
    imagen = models.URLField(max_length=85, null=True) 
    desc_corta = models.CharField(max_length=2000, default='Sin reseña') 
    estatus= models.CharField(max_length=1, choices=estatus_libro) 
    categoria = models.CharField(max_length=50)
    edicion_ant = models.ForeignKey("self", null=True, default=None, on_delete=models.PROTECT)#Se relaciona con la misma tabla y el PROTECT sirve para que no se borre el libro con el que esta relacionado
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT)
    class Meta: 
        constraints = [models.CheckConstraint(check=~models.Q(titulo='cobol'), name='titulo_no_permitido_chk')]
    
    def __str__(self) -> str:
        return self.isbn
    
    def get_historial_ediciones(self):
        """
        Retorna una lista con todas las ediciones anteriores del libro
        ordenadas de la más reciente a la más antigua
        """
        historial = []
        edicion = self.edicion_anterior
        
        while edicion is not None:
            historial.append(edicion)
            edicion = edicion.edicion_anterior
            
        return historial

class LibroCronica(models.Model): 
    descripcion_larga = models.TextField(null=True) 
    libro = models.OneToOneField(Libro, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self) -> str:
        return "%s Cronica del libro " % self.libro.isbn
    
class Autor(models.Model):
    nombre = models.CharField(max_length=70)
    libro = models.ManyToManyField(
        'Libro',
        through='AutorCapitulo',
        related_name='libros_autores',
        through_fields=('autor','libro')
    )

    def __str__(self) -> str:
        return self.nombre

class AutorCapitulo(models.Model):
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    libro = models.ForeignKey('Libro', on_delete=models.SET_NULL, null=True) 
    numero_capitulos = models.IntegerField(default=0)



