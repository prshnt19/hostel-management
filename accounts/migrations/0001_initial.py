# Generated by Django 2.1.7 on 2019-03-30 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll_no', models.CharField(max_length=10)),
                ('mob_no', models.CharField(max_length=11)),
                ('room_no', models.CharField(max_length=3)),
                ('father_name', models.CharField(max_length=50)),
                ('father_mobile', models.CharField(max_length=11)),
                ('hostel', models.CharField(choices=[('BH1', 'BH1'), ('BH2', 'BH2'), ('BH3', 'BH3'), ('GH1', 'GH1')], default='BH1', max_length=5)),
            ],
        ),
    ]
