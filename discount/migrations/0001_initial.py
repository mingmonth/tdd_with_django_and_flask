# Generated by Django 4.0.3 on 2022-03-02 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=35, unique=True)),
                ('value', models.FloatField()),
                ('description', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ended', models.DateTimeField()),
            ],
        ),
    ]
