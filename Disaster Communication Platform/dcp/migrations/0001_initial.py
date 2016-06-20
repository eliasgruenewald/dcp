# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-20 21:17
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Bump_Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Catastrophe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Location', models.CharField(max_length=100)),
                ('PubDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
            ],
            options={
                'permissions': (('EditCatastrophe', 'Kann eine Katastrophe editieren/löschen'), ('CreateCatastrophe', 'Kann eine Katastrophe erstellen')),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Comment_Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receiver', to=settings.AUTH_USER_MODEL)),
                ('Starter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Starter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Government',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_short', models.CharField(max_length=3)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('location_x', models.FloatField()),
                ('location_y', models.FloatField()),
                ('radius', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)])),
            ],
        ),
        migrations.CreateModel(
            name='Invite_Government',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp.Government')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invite_Ngo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.TextField(max_length=5000)),
                ('SendTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('Conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Conversation', to='dcp.Conversation')),
                ('From', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='From', to=settings.AUTH_USER_MODEL)),
                ('To', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='To', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MissedPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=5000)),
                ('gender', models.CharField(max_length=1)),
                ('age', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('name', models.CharField(max_length=100)),
                ('size', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(250)])),
                ('eyeColor', models.CharField(max_length=50)),
                ('hairColor', models.CharField(max_length=50)),
                ('characteristics', models.CharField(max_length=500)),
                ('picture', models.ImageField(null=True, upload_to='media/upload/people/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ngo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_short', models.CharField(max_length=3)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Ngo_Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('location_x', models.FloatField()),
                ('location_y', models.FloatField()),
                ('radius', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp.Ngo')),
            ],
        ),
        migrations.CreateModel(
            name='Offer_Immaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500, null=True)),
                ('location_x', models.FloatField(null=True)),
                ('location_y', models.FloatField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('visibility', models.BooleanField(default=True)),
                ('timeline_badge_color', models.CharField(default='red', max_length=100)),
                ('timeline_glyphicon', models.CharField(default='glyphicon-transfer', max_length=100)),
                ('bumps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcp.Bump_Relation')),
                ('catastrophe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp.Catastrophe')),
                ('comments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcp.Comment_Relation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Offer_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500, null=True)),
                ('location_x', models.FloatField(null=True)),
                ('location_y', models.FloatField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('visibility', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('1', 'Lebensmittel'), ('2', 'Infrastruktur'), ('3', 'Werkzeug'), ('4', 'Medizin'), ('5', 'Sonstiges')], max_length=1)),
                ('image', models.ImageField(upload_to='upload/')),
                ('timeline_badge_color', models.CharField(default='red', max_length=100)),
                ('timeline_glyphicon', models.CharField(default='glyphicon-transfer', max_length=100)),
                ('bumps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcp.Bump_Relation')),
                ('catastrophe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp.Catastrophe')),
                ('comments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcp.Comment_Relation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_organization_admin', models.BooleanField(default=False)),
                ('date_joined_organization', models.DateTimeField(default=django.utils.timezone.now)),
                ('currentCatastrophe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='currentCatastrophe', to='dcp.Catastrophe')),
                ('government', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcp.Government')),
                ('ngo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcp.Ngo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Report_Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Search_Immaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500, null=True)),
                ('location_x', models.FloatField(null=True)),
                ('location_y', models.FloatField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('visibility', models.BooleanField(default=True)),
                ('radius', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('timeline_badge_color', models.CharField(default='blue', max_length=100)),
                ('timeline_glyphicon', models.CharField(default='glyphicon-search', max_length=100)),
                ('bumps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcp.Bump_Relation')),
                ('catastrophe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp.Catastrophe')),
                ('comments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcp.Comment_Relation')),
                ('reports', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcp.Report_Relation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Search_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500, null=True)),
                ('location_x', models.FloatField(null=True)),
                ('location_y', models.FloatField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('visibility', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('1', 'Lebensmittel'), ('2', 'Infrastruktur'), ('3', 'Werkzeug'), ('4', 'Medizin'), ('5', 'Sonstiges')], max_length=1)),
                ('image', models.ImageField(upload_to='upload/')),
                ('radius', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('timeline_badge_color', models.CharField(default='blue', max_length=100)),
                ('timeline_glyphicon', models.CharField(default='glyphicon-search', max_length=100)),
                ('bumps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcp.Bump_Relation')),
                ('catastrophe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp.Catastrophe')),
                ('comments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcp.Comment_Relation')),
                ('reports', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcp.Report_Relation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='report',
            name='relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp.Report_Relation'),
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='offer_material',
            name='reports',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcp.Report_Relation'),
        ),
        migrations.AddField(
            model_name='offer_material',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='offer_immaterial',
            name='reports',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dcp.Report_Relation'),
        ),
        migrations.AddField(
            model_name='offer_immaterial',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invite_ngo',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp.Ngo'),
        ),
        migrations.AddField(
            model_name='invite_ngo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp.Comment_Relation'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='catastrophe',
            unique_together=set([('Title', 'Location')]),
        ),
        migrations.AddField(
            model_name='bump',
            name='relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcp.Bump_Relation'),
        ),
        migrations.AddField(
            model_name='bump',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='conversation',
            unique_together=set([('Starter', 'Receiver')]),
        ),
    ]
