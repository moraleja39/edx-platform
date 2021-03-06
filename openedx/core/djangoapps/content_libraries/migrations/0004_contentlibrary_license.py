# Generated by Django 2.2.16 on 2020-09-16 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_libraries', '0003_contentlibrary_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentlibrary',
            name='license',
            field=models.CharField(choices=[('', 'All Rights Reserved.'), ('CC:4.0:BY', 'Creative Commons Attribution 4.0'), ('CC:4.0:BY:NC', 'Creative Commons Attribution-NonCommercial 4.0'), ('CC:4.0:BY:NC:ND', 'Creative Commons Attribution-NonCommercial-NoDerivatives 4.0'), ('CC:4.0:BY:NC:SA', 'Creative Commons Attribution-NonCommercial-ShareAlike 4.0'), ('CC:4.0:BY:ND', 'Creative Commons Attribution-NoDerivatives 4.0'), ('CC:4.0:BY:SA', 'Creative Commons Attribution-ShareAlike 4.0')], default='', max_length=25),
        ),
    ]
