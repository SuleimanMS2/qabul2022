# Generated by Django 3.1.1 on 2022-05-16 08:42

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20220516_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasport',
            name='doimiy_tuman',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='viloyat', chained_model_field='doimiy_viloyat', on_delete=django.db.models.deletion.PROTECT, to='myapp.tuman', verbose_name='Doimiy yashash tumani'),
        ),
    ]
