# Generated by Django 3.2.10 on 2022-03-19 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinema', '0003_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('des', models.TextField()),
            ],
        ),
    ]