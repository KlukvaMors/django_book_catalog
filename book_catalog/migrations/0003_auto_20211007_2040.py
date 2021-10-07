# Generated by Django 3.2.7 on 2021-10-07 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_catalog', '0002_auto_20211005_1213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['full_name'], 'permissions': (('can_edit', 'User can create, update and delete model'),)},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('can_edit', 'User can create, update and delete model'),)},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'permissions': (('can_edit', 'User can create, update and delete model'),)},
        ),
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]