# Generated by Django 2.2.4 on 2019-12-17 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentAnalysis', '0006_sentenceresult_sentence_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestresult',
            name='frequentHashtagFilename',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='frequentwordFilename',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='negative_frequentHashtagFilename',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='negative_frequentwordFilename',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='positive_frequentHashtagFilename',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='positive_frequentwordFilename',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]
