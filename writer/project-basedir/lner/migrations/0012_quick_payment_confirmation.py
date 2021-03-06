# Generated by Django 2.2.9 on 2020-01-11 16:29

import common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lner', '0011_lightninginvoice_checkpoint_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lightninginvoice',
            name='checkpoint_status',
        ),
        migrations.AddField(
            model_name='lightninginvoicerequest',
            name='comment',
            field=models.CharField(default='__DEFAULT__', max_length=255, verbose_name='A copy of comment from InvoiceListCheckpoint for scalability'),
        ),
        migrations.AlterField(
            model_name='invoicelistcheckpoint',
            name='checkpoint_name',
            field=models.CharField(default='__DEFAULT__', max_length=255, unique=True, validators=[common.validators.validate_checkpoint_name], verbose_name='Checkpoint name. Encodes relationships with data such as node pubkey and add_index. This relationship is not in the database for scalability and flexibility.'),
        ),
        migrations.AlterField(
            model_name='invoicelistcheckpoint',
            name='checkpoint_value',
            field=models.IntegerField(default=1, verbose_name='Integer value of the checkpoint (e.g. offset). Zero invalidates checkpoint.'),
        ),
        migrations.AlterField(
            model_name='invoicelistcheckpoint',
            name='comment',
            field=models.CharField(default='__DEFAULT__', max_length=255, verbose_name='Comment. Explanation of reason for checkpoint. E.g. "done", "canceled", "deserialize_failure", or "memo_invalid".'),
        ),
    ]
