# Generated by Django 2.0 on 2018-05-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alarm_id', models.CharField(max_length=100, verbose_name='警情ID')),
                ('first_type', models.CharField(max_length=100, verbose_name='警情一级类型')),
                ('second_type', models.CharField(max_length=100, verbose_name='警情二级类型')),
                ('third_type', models.CharField(max_length=100, verbose_name='警情三级类型')),
                ('fourth_type', models.CharField(max_length=100, verbose_name='警情四级类型')),
                ('content', models.CharField(max_length=100, verbose_name='警情描述')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-date_time'],
            },
        ),
    ]
