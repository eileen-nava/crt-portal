# Generated by Django 2.2.25 on 2021-12-16 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0135_materialize_email_count_view'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='opened',
            new_name='read',
        ),
    ]