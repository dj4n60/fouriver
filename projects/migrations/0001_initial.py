

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=20)),
                ('jobtype', models.CharField(max_length=20)),
                ('paymentmethod', models.CharField(max_length=20)),
                ('jobdescription', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'projects',
            },
        ),
    ]
