# Generated by Django 4.0.6 on 2022-08-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descriptions', models.TextField()),
                ('price', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('group', models.CharField(choices=[('Accessories', 'accessories'), ('shoes', 'shoes'), ('clothes', 'clothes'), ('bags', 'bags')], default='clothes', max_length=20)),
                ('img', models.ImageField(default='no_image.jpg', upload_to='product_image')),
            ],
        ),
    ]