# Generated by Django 3.2.8 on 2021-10-26 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appraisal', '0008_alter_pic_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
