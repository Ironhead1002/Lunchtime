# Generated by Django 3.2.12 on 2022-04-02 06:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('reviews_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('menu_rev_star', models.FloatField(blank=True, null=True)),
                ('menu_rev_comment', models.TextField(blank=True, null=True)),
                ('menu_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menu')),
            ],
        ),
    ]
