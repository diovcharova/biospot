# Generated by Django 3.0.2 on 2020-02-10 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_category_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='package',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='producer',
            field=models.CharField(default='', max_length=254),
        ),
    ]