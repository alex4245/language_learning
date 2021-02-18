# Generated by Django 3.0.5 on 2021-01-27 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lang_learning', '0006_auto_20210126_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lang_learning.Language'),
            preserve_default=False,
        ),
    ]
