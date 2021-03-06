# Generated by Django 3.1 on 2020-09-21 19:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                            related_name='varieties', to='plants.plant')),
            ],
        ),
    ]
