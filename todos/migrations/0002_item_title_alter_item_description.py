# Generated by Django 4.1.7 on 2023-02-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(default='Test Item', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(),
        ),
    ]
