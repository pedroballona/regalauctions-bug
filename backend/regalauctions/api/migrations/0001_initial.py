# Generated by Django 2.1.4 on 2018-12-07 23:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('initial_value', models.FloatField()),
                ('is_used', models.BooleanField()),
                ('opening_date', models.DateField()),
                ('ending_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Auction')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
                ('active', models.BooleanField()),
                ('is_admin', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserProfile'),
        ),
        migrations.AddField(
            model_name='auction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='bid',
            unique_together={('user', 'value', 'auction')},
        ),
    ]