# Generated by Django 2.2.4 on 2019-10-16 19:02
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0009_auto_20191015_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='protectedclass',
            name='form_order',
            field=models.IntegerField(blank=True, null=True),
        )
    ]