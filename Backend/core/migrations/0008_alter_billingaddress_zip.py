# Generated by Django 4.2.2 on 2023-09-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_billingaddress_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='zip',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]