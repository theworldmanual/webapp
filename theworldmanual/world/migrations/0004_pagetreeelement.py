# Generated by Django 2.2.6 on 2019-10-13 16:59

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0003_auto_20191012_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageTreeElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('page', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='world.Page')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='world.PageTreeElement')),
                ('world', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='world.World')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
