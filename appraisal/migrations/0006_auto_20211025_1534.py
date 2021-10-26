# Generated by Django 3.2.8 on 2021-10-25 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appraisal', '0005_vehicle_chasis_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='pic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appraisal.pic', verbose_name='Brand Image'),
        ),
        migrations.AddField(
            model_name='pic',
            name='title',
            field=models.CharField(default='Image', max_length=50, verbose_name='Image Title'),
            preserve_default=False,
        ),
    ]