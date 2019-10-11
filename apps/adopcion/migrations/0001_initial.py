# Generated by Django 2.2.5 on 2019-10-08 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=70)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('domilicio', models.TextField()),
            ],
        ),
    ]