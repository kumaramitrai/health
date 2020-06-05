# Generated by Django 2.2.12 on 2020-06-02 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=12)),
                ('condition', models.CharField(choices=[('b', 'Bad'), ('g', 'Good')], max_length=1)),
                ('status', models.BooleanField()),
            ],
        ),
    ]
