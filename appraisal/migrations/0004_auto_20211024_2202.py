# Generated by Django 3.2.8 on 2021-10-25 02:02

import appraisal.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appraisal', '0003_document_manufacturer_note_pic_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='engine',
            field=models.CharField(blank=True, max_length=255, verbose_name='Engine'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='documents',
            field=models.ManyToManyField(blank=True, to='appraisal.Document', verbose_name='Documents'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='engine_and_trans',
            field=models.CharField(blank=True, max_length=255, verbose_name='Engine and Transmission'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='engine_no',
            field=models.CharField(blank=True, max_length=255, verbose_name='Engine #'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='exterior',
            field=models.CharField(blank=True, max_length=255, verbose_name='Exterior'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='interior',
            field=models.CharField(blank=True, max_length=255, verbose_name='Interior'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='manufacture_year',
            field=models.PositiveSmallIntegerField(blank=True, default=2021, validators=[django.core.validators.MinValueValidator(1900), appraisal.models.max_value_current_year], verbose_name='Year of Manufacture'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appraisal.manufacturer'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='other_features',
            field=models.CharField(blank=True, max_length=255, verbose_name='Other Features'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='pics',
            field=models.ManyToManyField(blank=True, to='appraisal.Pic', verbose_name='Pictures'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='safety',
            field=models.CharField(blank=True, max_length=255, verbose_name='Safety'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='suspension',
            field=models.CharField(blank=True, max_length=255, verbose_name='Suspension'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, default=2021, validators=[django.core.validators.MinValueValidator(1900), appraisal.models.max_value_current_year]),
        ),
    ]
