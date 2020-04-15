# Generated by Django 3.0.4 on 2020-04-13 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('style', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('abv', models.FloatField()),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('image_url', models.TextField()),
                ('brewery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Brewery')),
            ],
        ),
    ]