# Generated by Django 2.1.1 on 2018-09-22 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('Content', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]