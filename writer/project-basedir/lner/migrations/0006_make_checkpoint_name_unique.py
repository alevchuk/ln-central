# Generated by Django 2.2.9 on 2019-12-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lner', '0005_auto_20191224_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicelistcheckpoint',
            name='checkpoint_name',
            field=models.CharField(default='__DEFAULT__', max_length=255, unique=True, verbose_name='Checkpoint name'),
        ),
    ]