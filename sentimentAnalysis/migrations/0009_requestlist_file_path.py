# Generated by Django 2.2.4 on 2019-10-24 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentAnalysis', '0008_auto_20191008_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlist',
            name='file_path',
            field=models.TextField(default='/'),
        ),
    ]