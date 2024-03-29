# Generated by Django 4.2.6 on 2023-10-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('content_image', models.ImageField(null=True, upload_to='item_images/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
