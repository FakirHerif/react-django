# Generated by Django 4.2.7 on 2023-11-06 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_event_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='accounts.category'),
        ),
        migrations.DeleteModel(
            name='EventImage',
        ),
        migrations.DeleteModel(
            name='Seat',
        ),
    ]
