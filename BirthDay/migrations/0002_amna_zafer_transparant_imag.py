# Generated by Django 2.2.16 on 2020-09-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BirthDay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='amna_zafer',
            name='Transparant_Imag',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
