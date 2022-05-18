# Generated by Django 3.1.1 on 2022-05-16 08:26

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20220516_0822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tuman',
            old_name='viloyat_id',
            new_name='viloyat',
        ),
        migrations.AlterField(
            model_name='pasport',
            name='doimiy_tuman',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='Viloyat', chained_model_field='viloyat', on_delete=django.db.models.deletion.CASCADE, to='myapp.tuman'),
        ),
    ]
