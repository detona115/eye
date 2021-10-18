# Generated by Django 3.2.8 on 2021-10-12 20:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='element',
        ),
        migrations.AlterField(
            model_name='event',
            name='session_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element', models.CharField(blank=True, max_length=100)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='element', to='api.data')),
            ],
        ),
    ]
