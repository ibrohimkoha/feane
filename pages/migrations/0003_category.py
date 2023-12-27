# Generated by Django 5.0 on 2023-12-27 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_commentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]