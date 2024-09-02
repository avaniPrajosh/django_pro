# Generated by Django 5.0.6 on 2024-06-25 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
                ('priority', models.IntegerField(default=0)),
                ('delete_status', models.IntegerField(choices=[(1, 'live'), (0, 'Delete')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updatad_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]