# Generated by Django 4.1.1 on 2022-11-22 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_calcchapter_dmchapter_lachapter_statschapter_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DPChapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DPSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.dpchapter')),
            ],
        ),
    ]