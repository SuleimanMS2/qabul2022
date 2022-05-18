# Generated by Django 3.1.1 on 2022-05-16 09:49

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20220516_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasport',
            name='talim_turi',
            field=smart_selects.db_fields.ChainedManyToManyField(auto_choose=True, chained_field='talim_shakli', chained_model_field='talim_shakllari', to='myapp.TalimTuri', verbose_name='Ta`lim turi'),
        ),
    ]
