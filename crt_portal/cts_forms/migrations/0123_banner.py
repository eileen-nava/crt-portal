# Generated by Django 2.2.24 on 2021-09-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0122_update_spl_tagalog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_banner', models.BooleanField(default=False)),
                ('banner_text', models.CharField(max_length=500)),
                ('button_text', models.CharField(blank=True, max_length=50, null=True)),
                ('button_url', models.URLField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('deploy_date', models.DateTimeField(auto_now_add=True)),
                ('destroy_date', models.DateTimeField()),
            ],
        ),
    ]