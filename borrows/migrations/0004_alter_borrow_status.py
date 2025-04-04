# Generated by Django 5.1.6 on 2025-03-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrows', '0003_alter_borrow_borrow_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Borrowed', 'Borrowed'), ('Overdue', 'Overdue'), ('Returned', 'Returned'), ('Lost', 'Lost'), ('Canceled', 'Canceled')], default='PENDING', max_length=255),
        ),
    ]
