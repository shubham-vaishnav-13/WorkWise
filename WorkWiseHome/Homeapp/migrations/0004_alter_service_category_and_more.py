# Generated by Django 5.1.5 on 2025-03-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homeapp', '0003_remove_serviceprovider_rating_service_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.CharField(choices=[('Plumber', 'Plumber'), ('Electrician', 'Electrician'), ('Carpenter', 'Carpenter'), ('Repair Technician', 'Repair Technician'), ('Cleaner', 'Cleaner'), ('Cook', 'Cook')], db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='service_category',
            field=models.CharField(choices=[('Plumber', 'Plumber'), ('Electrician', 'Electrician'), ('Carpenter', 'Carpenter'), ('Repair Technician', 'Repair Technician'), ('Cleaner', 'Cleaner'), ('Cook', 'Cook')], db_index=True, max_length=50),
        ),
    ]
