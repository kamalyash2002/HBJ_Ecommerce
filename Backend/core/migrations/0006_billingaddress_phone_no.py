# Generated by Django 4.2.2 on 2023-07-13 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_billingaddress_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='phone_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]