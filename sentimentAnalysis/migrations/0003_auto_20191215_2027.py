# Generated by Django 2.2.6 on 2019-12-16 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentAnalysis', '0002_requestresult_wordgraphfilename'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestresult',
            name='neg_f1score_max',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='neu_f1score_max',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='pos_f1score_max',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='sentiWord_neg_f1score',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='sentiWord_neu_f1score',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='sentiWord_pos_f1score',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='stanfordNLP_neg_f1score',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='stanfordNLP_neu_f1score',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='stanfordNLP_pos_f1score',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='textblob_neg_f1score',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='textblob_neu_f1score',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='textblob_pos_f1score',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='vader_neg_f1score',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='vader_neu_f1score',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='requestresult',
            name='vader_pos_f1score',
            field=models.FloatField(default=150.0),
        ),
    ]