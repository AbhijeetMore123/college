# Generated by Django 3.1.7 on 2021-09-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Roll_no', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
