# Generated by Django 5.0.6 on 2024-06-26 07:02

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ontology_auth', '0004_rdf_type_object_rdf_type_ontology_rdf_type_subject'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ontology',
            name='access',
            field=models.CharField(choices=[('Global', 'Общедоступная'), ('Private', 'Приватная')], default='Global', max_length=50, verbose_name='Доступность'),
        ),
        migrations.AlterField(
            model_name='ontology',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='ontology',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование онтологии'),
        ),
        migrations.AlterField(
            model_name='ontology',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ontology', to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
