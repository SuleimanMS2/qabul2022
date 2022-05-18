# Generated by Django 3.1.1 on 2022-05-16 09:39

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_talimturi_talim_turi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talimturi',
            old_name='talim_turi',
            new_name='talim_shakllari',
        ),
        migrations.RemoveField(
            model_name='pasport',
            name='talim_turi',
        ),
        migrations.AddField(
            model_name='pasport',
            name='talim_turi',
            field=smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='talim_shakli', chained_model_field='talim_shakllari', horizontal=True, null=True, to='myapp.TalimTuri', verbose_name='Ta`lim turi'),
        ),
    ]
