# Generated by Django 2.2.4 on 2019-11-20 01:01

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('key', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('request_name', models.TextField(default='something')),
                ('request_owner', models.TextField(default='something')),
                ('request_status', models.TextField(default='unassigned')),
                ('request_pid', models.IntegerField(default=0)),
                ('request_issued_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('request_completed_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('file_path', models.TextField(default='/')),
            ],
        ),
        migrations.CreateModel(
            name='requestResult',
            fields=[
                ('key', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('requestName', models.TextField(default='something')),
                ('userEmail', models.TextField(default='something')),
                ('vaderConfusionMatrix', models.CharField(default='SOME STRING', max_length=200)),
                ('vaderPrecise', models.FloatField(default=150.0)),
                ('vaderRecall', models.FloatField(default=150.0)),
                ('vaderF1Score', models.FloatField(default=150.0)),
                ('textblobConfusionMatrix', models.CharField(default='SOME STRING', max_length=200)),
                ('textblobPrecise', models.FloatField(default=150.0)),
                ('textblobRecall', models.FloatField(default=150.0)),
                ('textblobF1Score', models.FloatField(default=150.0)),
                ('sentiWordNetConfusionMatrix', models.CharField(default='SOME STRING', max_length=200)),
                ('sentiWordNetPrecise', models.FloatField(default=150.0)),
                ('sentiWordNetRecall', models.FloatField(default=150.0)),
                ('sentiWordNetF1Score', models.FloatField(default=150.0)),
                ('stanfordNLPConfusionMatrix', models.CharField(default='SOME STRING', max_length=200)),
                ('topFrequentWords', models.CharField(default='SOME STRING', max_length=200)),
                ('wordCounter', models.IntegerField(default=0)),
                ('wordCloudFileName', models.CharField(default='SOME STRING', max_length=200)),
                ('hashtagFrequent', models.CharField(default='SOME STRING', max_length=200)),
                ('positiveTopFrequentHashtag', models.CharField(default='SOME STRING', max_length=200)),
                ('negativeTopFrequentHashtag', models.CharField(default='SOME STRING', max_length=200)),
                ('positiveTopFrequentWords', models.CharField(default='SOME STRING', max_length=200)),
                ('positiveWordcounter', models.IntegerField(default=0)),
                ('positiveWordCloudFilename', models.CharField(default='SOME STRING', max_length=200)),
                ('negativeTopFrequentWords', models.CharField(default='SOME STRING', max_length=200)),
                ('negativeWordcounter', models.IntegerField(default=0)),
                ('negativeWordCloudFilename', models.CharField(default='SOME STRING', max_length=200)),
                ('sortedF1ScoreList', models.CharField(default='SOME STRING', max_length=200)),
                ('vaderCountpol', models.CharField(default='SOME STRING', max_length=10000000)),
                ('textblobCountpol', models.CharField(default='SOME STRING', max_length=10000000)),
                ('sentiWordNetCountpol', models.CharField(default='SOME STRING', max_length=10000000)),
                ('stanfordNLPCountpol', models.CharField(default='SOME STRING', max_length=10000000)),
                ('vaderCountpol_sentence', models.CharField(default='SOME STRING', max_length=10000000)),
                ('textblobCountpol_sentence', models.CharField(default='SOME STRING', max_length=10000000)),
                ('sentiWordnetCountpol_sentence', models.CharField(default='SOME STRING', max_length=10000000)),
                ('stanfordNLPCountpol_sentence', models.CharField(default='SOME STRING', max_length=10000000)),
            ],
        ),
        migrations.CreateModel(
            name='sentenceResult',
            fields=[
                ('key', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('requestName', models.TextField(default='something')),
                ('userEmail', models.TextField(default='something')),
                ('tweet_id', models.TextField(default='tweet_id')),
                ('sentenceID', models.IntegerField(default=0)),
                ('vaderScores', models.FloatField(default=150.0)),
                ('vaderPolarity', models.CharField(default='SOME STRING', max_length=200)),
                ('textblobScores', models.FloatField(default=150.0)),
                ('textblobPolarity', models.CharField(default='SOME STRING', max_length=200)),
                ('sentiWordNetScores', models.FloatField(default=150.0)),
                ('sentiWordNetPolarity', models.CharField(default='SOME STRING', max_length=200)),
                ('stanfordNLPPolarity', models.CharField(default='SOME STRING', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tasklist',
            fields=[
                ('key', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('userEmail', models.TextField(default='something')),
                ('requestName', models.TextField(default='something')),
                ('toolName', models.TextField(default='something')),
                ('toolStatus', models.TextField(default='something')),
                ('tool_pid', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='tweet',
            fields=[
                ('key', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('requestName', models.TextField(default='something')),
                ('userEmail', models.TextField(default='something')),
                ('tweet_id', models.TextField(default='tweet_id')),
                ('tweet_content', models.TextField(default='tweet_content')),
                ('tweet_annotation', models.TextField(default='tweet_annotation')),
                ('vaderScores', models.FloatField(default=150.0)),
                ('vaderPolarity', models.CharField(default='SOME STRING', max_length=200)),
                ('textblobScores', models.FloatField(default=150.0)),
                ('textblobPolarity', models.CharField(default='SOME STRING', max_length=200)),
                ('sentiWordNetScores', models.FloatField(default=150.0)),
                ('sentiWordNetPolarity', models.CharField(default='SOME STRING', max_length=200)),
                ('stanfordNLPPolarity', models.CharField(default='SOME STRING', max_length=200)),
                ('kappa', models.FloatField(default=150.0)),
                ('vaderAverage', models.FloatField(default=150.0)),
                ('vaderMajority', models.TextField(default='something')),
                ('textblobAverage', models.FloatField(default=150.0)),
                ('textblobMajority', models.TextField(default='something')),
                ('sentiWordnetAverage', models.FloatField(default=150.0)),
                ('sentiWordnetMajority', models.TextField(default='something')),
                ('stanfordNLPMajority', models.TextField(default='something')),
                ('sentenceKappa', models.FloatField(default=150.0)),
            ],
        ),
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt'])])),
            ],
        ),
    ]
