# Generated by Django 3.2.5 on 2021-07-07 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_requestevent_requestrole'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('organizerID', models.AutoField(primary_key=True, serialize=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.event')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]