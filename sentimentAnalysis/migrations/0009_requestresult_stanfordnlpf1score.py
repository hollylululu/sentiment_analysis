# Generated by Django 2.2.4 on 2019-12-20 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentAnalysis', '0008_auto_20191218_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestresult',
            name='stanfordNLPF1Score',
            field=models.FloatField(default=150.0),
        ),
    ]