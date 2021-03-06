# Generated by Django 2.2.4 on 2019-08-12 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_one', '0002_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='store',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='django_one.Product'),
        ),
    ]
