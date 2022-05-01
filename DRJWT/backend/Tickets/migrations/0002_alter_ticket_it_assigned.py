# Generated by Django 4.0.3 on 2022-04-20 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='it_assigned',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_it': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='it_for_ticket', to=settings.AUTH_USER_MODEL),
        ),
    ]