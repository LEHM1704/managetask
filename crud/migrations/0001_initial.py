# Generated by Django 5.1.4 on 2024-12-17 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('is_completed', models.BooleanField(default=False, verbose_name='completo')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
