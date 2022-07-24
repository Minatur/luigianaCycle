# Generated by Django 2.2.5 on 2022-07-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('length', models.IntegerField()),
                ('difficulty', models.CharField(choices=[('1', 'Easy'), ('2', 'Medium'), ('3', 'Hard'), ('4', 'Very Hard'), ('5', 'Nightmare')], max_length=1)),
            ],
        ),
    ]