# Generated by Django 3.1.1 on 2022-05-16 09:55

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20220516_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasport',
            name='talim_yunalishi',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='talim_turi', chained_model_field='talim_turi', null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.yonalishotm', verbose_name='OTM Yo`nalishi'),
        ),
    ]
