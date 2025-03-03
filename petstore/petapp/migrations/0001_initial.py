# Generated by Django 5.0.4 on 2024-05-02 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('Name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('Breed', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('Description', models.CharField(max_length=100)),
            ],
        ),
    ]
