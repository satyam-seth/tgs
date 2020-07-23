# Generated by Django 3.0.6 on 2020-07-23 06:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0011_mjoin_wjoin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tgsw_join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('cid', models.IntegerField()),
                ('team_name', models.CharField(max_length=50)),
                ('leader_pname', models.CharField(max_length=50)),
                ('second_pname', models.CharField(max_length=50)),
                ('third_pname', models.CharField(max_length=50)),
                ('fourth_pname', models.CharField(max_length=50)),
                ('fifth_pname', models.CharField(max_length=50)),
                ('whats_num', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$')])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('pay_ss', models.ImageField(upload_to='mjoin/pss/')),
                ('team_logo', models.ImageField(blank=True, null=True, upload_to='mjoin/logo/')),
            ],
        ),
        migrations.AlterField(
            model_name='mjoin',
            name='pay_ss',
            field=models.ImageField(upload_to='mjoin/pss/'),
        ),
        migrations.AlterField(
            model_name='mjoin',
            name='team_logo',
            field=models.ImageField(blank=True, null=True, upload_to='mjoin/logo/'),
        ),
        migrations.AlterField(
            model_name='wjoin',
            name='pay_ss',
            field=models.ImageField(upload_to='wjoin/pss/'),
        ),
        migrations.AlterField(
            model_name='wjoin',
            name='team_logo',
            field=models.ImageField(blank=True, null=True, upload_to='wjoin/logo/'),
        ),
    ]