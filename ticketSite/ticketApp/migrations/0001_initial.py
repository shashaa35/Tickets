# Generated by Django 4.2.2 on 2023-07-14 17:53

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
            name='ProblemSubtype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
                ('location_type', models.CharField(choices=[('Quarter', 'Quarter'), ('Building', 'Building'), ('Other', 'Other')], default='Quarter', max_length=1000)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Created', 'Created'), ('Approved by RW Officer', 'Approved By Rw Officer'), ('To Do', 'To Do'), ('In Progress', 'In Progress'), ('In Review', 'In Review'), ('Done', 'Done')], default='Created', max_length=1000)),
                ('hours_spent', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignee', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('problemSubtype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticketApp.problemsubtype')),
                ('problemType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticketApp.problemtype')),
            ],
        ),
        migrations.AddField(
            model_name='problemsubtype',
            name='problem_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticketApp.problemtype'),
        ),
    ]