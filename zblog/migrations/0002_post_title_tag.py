# Generated by Django 4.0.6 on 2022-08-02 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='DEYS RAVEZ!', max_length=600),
        ),
    ]
