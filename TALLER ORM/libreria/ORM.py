from .models import Libro, Autor,  Editorial, LibroCronica
from django.db.models import Min, Max, Avg, Count, Sum
from django.db.models.functions import Left, Concat, Replace
from django.db.models import Value as V
from django.db.models import F,Q
# funciones para manejo de texto del orm de django
# exact (coincidencia exacta), 
# iexact (coincidencia exacta sin distinguir mayúsculas/minúsculas), 
# contains (contiene el contenido), 
# icontains (contiene el contenido sin distinguir mayúsculas/minúsculas), 
# startswith (comienza con el contenido), 
# istartswith (comienza con el contenido sin distinguir mayúsculas/minúsculas), 
# endswith (termina con el contenido), 
# iendswith (termina con el contenido sin distinguir mayúsculas/minúsculas), 
# regex (coincide con expresión regular), 
# iregex (coincide con expresión regular sin distinguir mayúsculas/minúsculas)

# funciones de fecha del orm
# year: fecha__year=2024  o # (fecha__year__in=[2022, 2023, 2024]
# month: fecha__month=10 (para octubre)
# day: fecha__day=15
# week_day: fecha__week_day=1 (para domingo)
# quarter: fecha__quarter=2 (para el segundo trimestre)
# isnull: fecha__isnull=True (para comprobar si es NULL)
# gt: fecha__gt='2024-01-01' (mayor que una fecha específica)
# lt: fecha__lt='2024-01-01' (menor que una fecha específica)
# gte: fecha__gte='2024-01-01' (mayor o igual que una fecha específica)
# lte: fecha__lte='2024-01-01' (menor o igual que una fecha específica)
# range: fecha__range=['2024-01-01', '2024-12-31'] (dentro de un rango específico)

editorial1 = Editorial.objects.create("e1")

# Inserción básica de datos en la tabla Autor
Autor.objects.create(nombre='Autor desde el ORM')

# Inserción básica de datos en la tabla Autor con el método save
autor1 = Autor.objects.create(nombre='Paula Suárez')
autor2 = Autor.objects.create(nombre='bryan Martinez')
autor1.save()
autor2.save()

# Inserción básica de datos en la tabla Autor con el método bulk_create
autores = [
    Autor(nombre='Autor A'),
    Autor(nombre='Autor B'),
    Autor(nombre='Autor C'),
    Autor(nombre='Autor D'),    
    Autor(nombre='Autor E'),
    Autor(nombre='Autor F'),
]
Autor.objects.bulk_create(autores)

# Consulta básica de datos en la tabla Autor con el método all
autores = Autor.objects.all()

# Inserción básica de datos a la tabla Editorial con el método create
Editorial.objects.create(nombre='Ediciones Julio')

# Obtener la editorial creada con el método get que solo trae un registro.
e1 = Editorial.objects.get(nombre='Ediciones Santillana')

# Inserción básica de datos en la tabla Libro
libro1 = Libro.objects.create(
    isbn='9876543210123',
    titulo='La Fe',
    paginas=250,
    fecha_publicacion='2022-05-15',
    imagen='http://example.com/imagen1.jpg',
    desc_corta='Una epopeya clásica',
    estatus='M',
    categoria='Clásicos',
    editorial=e1
)
libro1.save()

# Inserción básica de datos en la tabla Libro con el método bulk_create
libros = [
    Libro(
        isbn='9784567890123',
        titulo='La Fe',
        paginas=300,
        fecha_publicacion='2020-09-01',
        imagen='http://example.com/imagen2.jpg',
        desc_corta='Novela sobre la decadencia y el hedonismo',
        estatus='B',
        categoria='Literatura',
        editorial=e1
    )
    # Libro(
    #     isbn='9654567890123',
    #     titulo='Matar a un Ruiseñor',
    #     paginas=320,
    #     fecha_publicacion='2018-04-21',
    #     imagen='http://example.com/imagen3.jpg',
    #     desc_corta='Historia de justicia y prejuicio',
    #     estatus='M',
    #     categoria='Literatura',
    #     editorial=e1
    # )
]

Libro.objects.bulk_create(libros)

# Obtener un libro con el método get
libro = Libro.objects.get(isbn='9654567890123')
libro=Libro.objects.get(pk='9654567890123')
# Obtener el primer libro con el método first
libroprimero = Libro.objects.first()
# Obtener el último libro con el método last
libroultimo = Libro.objects.last()
# Obtener los primeros n libros
libros2 = Libro.objects.all()[:3]
#Obtener solo el primer resultado
Libro.objects.all().first()
#Obtener solo el utlimo resultado
Libro.objects.all().last()
# Consultas por coincidencia
# Obtener los libros con el isbn que empieza con 97 con el método startswith
libros = Libro.objects.filter(titulo__startswith='La')

# Consultas mayor que con el método gt(>)
# Obtener los libros con más de 200 páginas con el método gt
libros = Libro.objects.filter(paginas__gt=200)


# Consultas con not in con el método exclude
# Consultar los libros que tengan más de 200 páginas y cuyo isbn no sea 9876543210123 es decir qu elo excluya totalmente
libros = Libro.objects.filter(paginas__gt=200).exclude(isbn='9876543210123')


# Consultas mayor o igual que con el método gte(>=)
libros = Libro.objects.filter(paginas__gte=200)
# Ejemplo de los libros que tengan 200 o más páginas pero solo muestra las columnas isbn y las paginas
libros = Libro.objects.filter(paginas__gte=200).values('isbn','paginas')


# Consulta menor que con el método lt(<)
# Consultar los libros que tengan menos de 200 páginas
libros = Libro.objects.filter(paginas__lt=200).values('isbn','paginas')


# Consulta menor o igual que con el método lte(<=)
libros = Libro.objects.filter(paginas__lte=200)
# Consultar los libros que tengan 200 o menos páginas
libros = Libro.objects.filter(paginas__lte=200).values('isbn','paginas')


# Consultas con count
# Contar los libros que tengan menos de 200 páginas
libros = Libro.objects.filter(paginas__lt=200).count()

# Consulta con or forma larga
# Consultar los libros con 200 o 300 páginas
libros1 = Libro.objects.filter(paginas=200)
libros2 = Libro.objects.filter(paginas=300)
consultatotal = (libros1 | libros2).values('isbn','paginas')

# Consulta por fecha con el método year
# Consultar los libros que se publicaron en el 2015
libros = Libro.objects.filter(fecha_publicacion__year=2015).values('isbn','fecha_publicacion')


# Filtrando con expresiones regulares con el método regex
# Consultar cuyo isbn comience con 97 seguido de 8 dígitos
libros = Libro.objects.filter(isbn__regex=r'^97\d{11}$').values('isbn')


# Consulta con unión con el método union
# Consultar el nombre de los autores que contengan 'Karla' con las editoriales que contengan 'Ediciones'
a1 = Autor.objects.filter(nombre__icontains='Karla').values('nombre')
e1 = Editorial.objects.filter(nombre__icontains='Santillana').values('nombre')
union = a1.union(e1)


# Consulta con el método order_by
# Obtener el cuarto libro con más páginas
libro = Libro.objects.values("isbn","paginas").order_by("-paginas")[3]


# Obtener el cuarto y quinto libro con más páginas
libros = Libro.objects.values("isbn","paginas").order_by("-paginas")[3:5]


# Consulta por índice
Libro.objects.filter(paginas__gt=200).explain()


# Consultas de agregación y agrupación
# con las funciones Min, Max, Avg, Count, Sum

# Consultar el número mínimo de páginas de los libros con la función Min
Libro.objects.aggregate(Min('paginas'))

libro = Libro.objects.filter(paginas__gt=0).aggregate(Min('paginas'))


# Consultar el número máximo de páginas de los libros con la función Max
Libro.objects.aggregate(Max('paginas'))

libro = Libro.objects.filter(paginas__gt=0).aggregate(Max('paginas'))


# Consultar el número promedio de páginas de los libros con la función Avg
libro = Libro.objects.filter(paginas__gt=0).aggregate(Avg('paginas'))

# Consultar el número total de páginas de los libros de literatura con la función Sum
libro = Libro.objects.filter(categoria__icontains='literatura').aggregate(Sum('paginas'))


# Consultar el número de libros con la función Count
libro = Libro.objects.filter(paginas__gt=0).aggregate(Count('paginas'))


# Consulta con group by y annotate
# Consultar los libros que son de literatura por categoría y contar cuántos libros hay en cada categoría
libros = Libro.objects.filter(categoria__contains='literatura').values('categoria').annotate(NumeroLibros=Count('*')) 


# Consulta los libros que son de literatura por categoría y contar cuántos hay en cada editorial
libro = Libro.objects.filter(categoria__icontains='literatura').values('categoria','editorial__nombre').annotate(NumeroLibros=Count('*'))  


# Consultas Having (filtrar agrupaciones)
# Filtrar los libros por fecha de publicación y mostrar solo los que tengan más de 2 libros en esa fecha
Consulta_fechas = Libro.objects.values('fecha_publicacion').annotate(cant_fec_pub=Count('fecha_publicacion')).filter(cant_fec_pub__gte=2).values_list('fecha_publicacion', flat=True)

# Para obtener el detalle de los libros que se publicaron en esas fechas
Detalle_libros = Libro.objects.filter(fecha_publicacion__in=Consulta_fechas).values('isbn', 'fecha_publicacion')
print(Detalle_libros)

# Consultas con Distinct
#Devolver valores únicos de una para evitar ver valores duplicados, en este ejemplo usamos distinct sobre paginas ya que muchos libros tienen 0 paginas.
Libro.objects.values('paginas').filter(paginas__lt=200).distinct()

#Consultas LEFT
#Queremos que nuestra desc_corta solo muestre los primeros 15 caracteres
Libro.objects.annotate(desc_resumida=Left('desc_corta',15)).values('isbn','desc_resumida')

#Concat y Value
#Queremos concatenar tres puntos (…) al fina de los valores de nuestra desc_resumida, para poder concatenar usamos la función Concat y para especificar la cadena a concatenar usamos Value.

Libro.objects.annotate(desc_resumida=Concat(Left('desc_corta',15),V('...'))).values('isbn','desc_resumida')

#CASE
#En el ejemplo anterior le pusimos los tres puntos (…) a todas las filas, en este ejemplo solo se los pondremos a las cadenas cuya longitud sea mayor de 15.

# Libro.objects.annotate(longitud = Length('desc_corta')).annotate( desc_resumida = Case( When(longitud__gt=50, then = Concat(Left('desc_corta',15), V('...'))) , default=('desc_corta'), output_field=CharField(), )).values('isbn','desc_resu mida','longitud')

#Comparar columnas del mismo modelo (F)
Libro.objects.annotate(tit50= Left('titulo',50), desc50= Left('desc_corta',50)).filter(tit50 = F('desc50')).values('isbn','tit50','desc50')

#REPLACE
#Queremos quitarle las comillas a los nombres de nuestra categoría y remplazarlas por un *
Libro.objects.annotate(categoria_sin_comillas = Replace('categoria', V('"'),V('*'))).values('isbn','categoria','categoria_sin_comillas')

#CONSULTAS AVANZADAS
#OR mejorado (usando Q) Para poder hacer esto utilizamos el operador Q(consulta) después podemos aplicar el OR y seguir haciendo condiciones.
Libro.objects.filter( (Q(categoria__contains='Literatura') | Q(categoria__contains='clásico') | Q(categoria__contains='deporte')) & ~Q(paginas=0))

#LEFT JOIN
#Queremos hacer una consulta entre el modelo Libro y LibroCronica, nos interesa saber que libros no tienen crónica, recordemos como esta nuestra relación 1 a 1.

Libro.objects.filter(librocronica__descripcion_larga__isnull=True).values('isbn','titulo','librocronica__descripcion_larga')

#LEFT JOIN (usando select_related relaciones 1 a 1)
#Existe otra forma de hacer la relacion uno a uno de Libro y LibroCronica y es usando select_related(modelo_relacion).
Libro.objects.select_related('librocronica').filter(categoria__contains='literatura')

#Beneficios de usar select_related en relaciones 1 a 1
#En el ejemplo anterior hicimos las consultas desde el modelo Libro, que pasaría si lo hiciéramos ahora desde el modelo, vamos a consultar primero nuestro modelo LibroCronica.
LibroCronica.objects.all()[:1]

#Vamos a ver que pasa si utilizamos select_related
LibroCronica.objects.select_related('libro').all()[:1]

#Beneficios de usar select_related en relaciones 1 a muchos
categorias = Libro.objects.all().select_related('editorial').filter(categoria__icontains='deporte')

for libro in categorias: 
    print(libro.editorial.nombre)

#ahora sin usar for
consulta = Libro.objects.all().select_related('editorial').filter(categoria__icontains='literatura')

dic_libros = dict(consulta.values_list('isbn','editorial__nombre')) 
print(dic_libros)

#Forma optima usando prefetch_related
#Vamos a realizar la misma consulta anterior pero ahora usaremos el método prefetch_related para especificarle que Autor tiene una relación con libros, y como veremos ahora solo realizara 2 consultas no importa el numero de autores que consultemos.
autores = Autor.objects.filter(pk__in=(1,2)).prefetch_related('libro')

for autor in autores: 
    print(f'Autor: {autor}') 
    print('Libros escritos:') 
    for libro in autor.libro.all(): 
        print(libro.titulo)

#Consultas muchos a muchos profundas (forma inviable)
autores = Autor.objects.filter(pk__in=(1,2)).prefetch_related('libro')

for autor in autores: 
    print(f'Autor: {autor}') 
    print('Libros escritos:') 
    for libro in autor.libro.all(): 
        print(f'{libro.isbn} Editorial: {libro.editorial.nombre}')
        

#Consultas muchos a muchos profundas (forma viable)
# autores = Autor.objects.filter(pk__in=(398,523)).prefetch_related(libro__editorial)
# for autor in autores: 
#     print(f'Autor: {autor}') 
#     print('Libros escritos:') 
#     for libro in autor.libro.all(): 
#         print(f'{libro.isbn} Editorial: {libro.editorial.nombre}')




#TEST

## 1. Crea 6 autores y relaciónalos con el libro  “La Fe”. (bulk_create)
autores = [
    Autor(nombre='Julio'),
    Autor(nombre='Bryan'),
    Autor(nombre='Antoni'),
    Autor(nombre='Felipe'),
    Autor(nombre='Kevin'),
    Autor(nombre='Mario'),
]
Autor.objects.bulk_create(autores)
libro = Libro.objects.get(isbn='9876543210123')
autores = Autor.objects.filter(nombre__in=['Julio', 'Bryan', 'Antoni', 'Felipe', 'Kevin', 'Mario'])
libro.libros_autores.set(autores)
print("Autores relacionados con el libro 'La Fe':", [autor.nombre for autor in libro.libros_autores.all()])

# 2. Encuentra todos los autores con nombres que contengan la letra "o" y que hayan escrito un libro en la categoría "Referencia".
autores_ref = Autor.objects.filter(nombre__icontains='o', libros_autores__categoria='Referencia')
print("Autores con 'o' y categoría 'Referencia':", [autor.nombre for autor in autores_ref])

# 3. Busca libros publicados entre 2020 y 2024, con más de 250 páginas y categoría distinta de "Referencia"
libros = Libro.objects.filter(fecha_publicacion__range=['2020-01-01', '2024-12-31'], paginas__gt=250).exclude(categoria='Referencia')
print("Libros publicados entre 2020 y 2024 con más de 250 páginas y categoría distinta de 'Referencia':", [libro.titulo for libro in libros])

# 4. Dado el libro “La Fe”, muestra todos sus autores
libro = Libro.objects.get(isbn='9876543210123')
autores_libro = libro.libros_autores.all()
print("Autores del libro 'La Fe':", [autor.nombre for autor in autores_libro])

# 5. Incrementa el número de páginas en 50 para todos los libros que tengan más de 100 páginas y cuyo autor sea “antoni”
from django.db.models import F
autor_antoni = Autor.objects.get(nombre='Antoni')
libros_antoni = Libro.objects.filter(paginas__gt=100, libros_autores=autor_antoni)
libros_antoni.update(paginas=F('paginas') + 50)
print("Libros de 'Antoni' con páginas incrementadas en 50:", [(libro.titulo, libro.paginas) for libro in libros_antoni])