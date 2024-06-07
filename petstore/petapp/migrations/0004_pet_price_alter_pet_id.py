# Generated by Django 5.0.4 on 2024-05-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0003_alter_pet_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='price',
            field=models.FloatField(default=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
