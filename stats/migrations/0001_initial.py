# Generated by Django 3.0.3 on 2020-03-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_cases', models.IntegerField()),
                ('new_cases', models.IntegerField()),
                ('total_deaths', models.IntegerField()),
                ('new_deaths', models.IntegerField()),
                ('total_recovered', models.IntegerField()),
                ('active_cases', models.IntegerField()),
                ('serious_critical', models.IntegerField()),
                ('total_cases_per_1m_population', models.IntegerField()),
                ('deaths_per_1m_population', models.IntegerField()),
                ('first_case', models.DateTimeField()),
            ],
        ),
    ]