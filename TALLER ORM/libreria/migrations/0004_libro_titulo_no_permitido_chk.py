# Generated by Django 5.1.2 on 2024-10-27 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_alter_libro_titulo'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='libro',
            constraint=models.CheckConstraint(condition=models.Q(('titulo', 'cobol'), _negated=True), name='titulo_no_permitido_chk'),
        ),
    ]
