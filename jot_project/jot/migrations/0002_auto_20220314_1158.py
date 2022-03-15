# Generated by Django 2.2.26 on 2022-03-14 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'verbose_name': 'Admin', 'verbose_name_plural': 'Admins'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'UserProfile', 'verbose_name_plural': 'UserProfiles'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Users', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='book',
            name='book_date_published',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date_written',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.BooleanField(default=False),
        ),
    ]
