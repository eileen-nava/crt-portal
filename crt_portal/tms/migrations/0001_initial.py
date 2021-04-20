# Generated by Django 2.2.19 on 2021-04-16 16:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cts_forms', '0106_donotemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='TMSEmail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tms_id', models.BigIntegerField(unique=True)),
                ('recipient', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('new', 'New'), ('sending', 'Sending'), ('sent', 'Sent'), ('failed', 'Failed'), ('inconclusive', 'Inconclusive')], max_length=32)),
                ('report', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='cts_forms.Report')),
            ],
        ),
    ]
