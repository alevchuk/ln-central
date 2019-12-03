# Generated by Django 2.1.7 on 2019-11-26 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceListCheckpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkpoint_name', models.CharField(default='__DEFAULT__', max_length=255, verbose_name='Checkpoint name')),
                ('add_index', models.IntegerField(default=0, verbose_name='LN Invoice add_index')),
            ],
        ),
        migrations.CreateModel(
            name='LightningInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_hash', models.CharField(default='__DEFAULT__', max_length=255, verbose_name='LN Invoice r_hash')),
                ('pay_req', models.CharField(max_length=255, verbose_name='LN Invoice pay_req')),
                ('add_index', models.IntegerField(default=-1, verbose_name='LN Invoice add_index')),
            ],
        ),
        migrations.CreateModel(
            name='LightningNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity_pubkey', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='LN Identity Pubkey')),
                ('rpcserver', models.CharField(default='localhost:10009', max_length=255, verbose_name='host:port of ln daemon')),
            ],
        ),
        migrations.AddField(
            model_name='invoicelistcheckpoint',
            name='lightning_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lner.LightningNode'),
        ),
    ]