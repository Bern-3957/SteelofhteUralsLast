# Generated by Django 4.1.3 on 2022-12-10 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("UralsSteelStore", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="good",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="UralsSteelStore.goods",
                verbose_name="Изображение",
            ),
        ),
    ]
