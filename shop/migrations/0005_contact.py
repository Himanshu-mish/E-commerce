# Generated by Django 4.1.3 on 2023-01-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_delete_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('phone', models.IntegerField(default='', max_length=50)),
                ('Message', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
