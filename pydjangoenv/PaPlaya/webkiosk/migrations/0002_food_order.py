# Generated by Django 3.2.5 on 2021-07-16 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webkiosk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderdatetime', models.DateTimeField(auto_now_add=True)),
                ('paymentmode', models.CharField(choices=[('CH', 'Cash'), ('CD', 'Card')], max_length=2)),
                ('quantity', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webkiosk.customer')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webkiosk.food')),
            ],
        ),
    ]
