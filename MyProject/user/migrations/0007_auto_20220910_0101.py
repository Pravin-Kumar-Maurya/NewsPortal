# Generated by Django 3.2.4 on 2022-09-09 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20220909_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videonews',
            name='vcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.ncategory'),
        ),
        migrations.AlterField(
            model_name='videonews',
            name='vcity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.city'),
        ),
    ]