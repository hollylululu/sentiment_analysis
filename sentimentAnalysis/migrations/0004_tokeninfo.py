# Generated by Django 2.2.6 on 2019-11-19 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentAnalysis', '0003_auto_20191108_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.TextField(default='something')),
                ('email', models.TextField(default='something')),
                ('token', models.TextField(default='something')),
                ('state', models.TextField(default='1')),
            ],
        ),
    ]
