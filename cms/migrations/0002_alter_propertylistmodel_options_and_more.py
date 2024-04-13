# Generated by Django 4.1.13 on 2024-04-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propertylistmodel',
            options={'verbose_name_plural': 'Property Listings'},
        ),
        migrations.AddField(
            model_name='propertylistmodel',
            name='show_on_home_page',
            field=models.CharField(choices=[('SHOW_ON_HOME_PAGE', 'Show_on_home_page'), ('DO_NOT_SHOW_ON_HOME_PAGE', 'Do_not_show_on_home_page')], default='DO_NOT_SHOW_ON_HOME_PAGE', max_length=512),
        ),
    ]