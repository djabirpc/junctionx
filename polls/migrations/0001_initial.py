# Generated by Django 3.2.9 on 2023-10-06 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtractedText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('category', models.CharField(choices=[('id', 'ID'), ('passport', 'Passport'), ('invoice', 'Invoice')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
