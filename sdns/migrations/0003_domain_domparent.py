# Generated by Django 3.1.3 on 2021-06-10 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sdns', '0002_auto_20210206_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='domParent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='domParet', to='sdns.domain'),
        ),
    ]
