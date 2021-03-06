# Generated by Django 3.0.3 on 2020-04-18 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='index1',
            field=models.IntegerField(default=0, verbose_name='主讲教师'),
        ),
        migrations.AddField(
            model_name='comment',
            name='index2',
            field=models.IntegerField(default=0, verbose_name='教学内容'),
        ),
        migrations.AddField(
            model_name='comment',
            name='index3',
            field=models.IntegerField(default=0, verbose_name='教学条件'),
        ),
        migrations.AddField(
            model_name='comment',
            name='index4',
            field=models.IntegerField(default=0, verbose_name='教学方法'),
        ),
        migrations.AddField(
            model_name='comment',
            name='index5',
            field=models.IntegerField(default=0, verbose_name='教学效果'),
        ),
        migrations.AlterField(
            model_name='course',
            name='rate',
            field=models.FloatField(verbose_name='分数'),
        ),
        migrations.AlterField(
            model_name='join',
            name='rate',
            field=models.FloatField(verbose_name='评分'),
        ),
    ]
