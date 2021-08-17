# Generated by Django 3.2.2 on 2021-08-17 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('stack', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('degree', models.CharField(max_length=4)),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('url', models.URLField()),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.skills')),
            ],
        ),
    ]
