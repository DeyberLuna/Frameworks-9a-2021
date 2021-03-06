# Generated by Django 3.1.7 on 2021-04-27 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tipos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=100)),
                ('abreviatura', models.CharField(max_length=50)),
                ('estado', models.BooleanField()),
                ('fecha_creacion', models.DateTimeField()),
                ('fecha_modificacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='razas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=100)),
                ('abreviatura', models.CharField(max_length=50)),
                ('estado', models.BooleanField()),
                ('fecha_creacion', models.DateTimeField()),
                ('fecha_modificacion', models.DateTimeField()),
                ('id_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.tipos')),
            ],
        ),
        migrations.CreateModel(
            name='mascotas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=100)),
                ('tiene_vacunas', models.BooleanField()),
                ('estado', models.BooleanField()),
                ('fecha_creacion', models.DateTimeField()),
                ('fecha_modificacion', models.DateTimeField()),
                ('id_raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.razas')),
                ('id_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.tipos')),
            ],
        ),
    ]
