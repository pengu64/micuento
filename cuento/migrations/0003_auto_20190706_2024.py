# Generated by Django 2.2.2 on 2019-07-07 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuento', '0002_auto_20190703_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuento',
            name='ventas',
            field=models.ManyToManyField(null=True, to='cuento.Ventas'),
        ),
    ]
