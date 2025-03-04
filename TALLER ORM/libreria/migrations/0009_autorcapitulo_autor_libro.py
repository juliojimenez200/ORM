# Generated by Django 5.1.2 on 2024-10-27 21:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0008_libro_editorial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutorCapitulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_capitulos', models.IntegerField(default=0)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libreria.autor')),
                ('libro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libreria.libro')),
            ],
        ),
        migrations.AddField(
            model_name='autor',
            name='libro',
            field=models.ManyToManyField(related_name='libros_autores', through='libreria.AutorCapitulo', to='libreria.libro'),
        ),
    ]
