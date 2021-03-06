# Generated by Django 3.1.3 on 2020-11-07 07:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Text')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create Time')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log_app.topic')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
