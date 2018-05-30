# Generated by Django 2.0 on 2018-05-30 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180516_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='alarm_id',
            field=models.CharField(max_length=100, null=True, verbose_name='警情ID'),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='content',
            field=models.CharField(max_length=500, verbose_name='警情描述'),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='first_type',
            field=models.CharField(max_length=100, null=True, verbose_name='警情一级类型'),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='fourth_type',
            field=models.CharField(max_length=100, null=True, verbose_name='警情四级类型'),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='second_type',
            field=models.CharField(max_length=100, null=True, verbose_name='警情二级类型'),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='third_type',
            field=models.CharField(max_length=100, null=True, verbose_name='警情三级类型'),
        ),
    ]