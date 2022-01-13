"""Removing unmanaged view created in migration #95"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0140_swap_out_new_email_count'),
    ]

    operations = [
        migrations.RunSQL("""
            DROP MATERIALIZED VIEW email_report_count CASCADE;
        """)
    ]