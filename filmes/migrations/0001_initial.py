# Generated by Django 4.2.7 on 2023-11-12 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='filmes',
            fields=[
                ('nome_filme', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('criador_filme', models.CharField(max_length=100)),
                ('ano_filme', models.IntegerField()),
                ('criado', models.DateField(auto_now_add=True)),
            ],
        ),
    ]