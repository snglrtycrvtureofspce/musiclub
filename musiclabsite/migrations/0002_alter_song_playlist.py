# Generated by Django 4.1.1 on 2022-10-10 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musiclabsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='playlist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='musiclabsite.playlist'),
        ),
    ]