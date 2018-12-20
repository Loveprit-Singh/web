# Generated by Django 2.1.2 on 2018-12-20 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inbox', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='CTA_Text',
            new_name='cta_text',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='CTA_URL',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='from_user_id',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='to_user_id',
        ),
        migrations.AddField(
            model_name='notification',
            name='cta_url',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='notification',
            name='from_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sent_notification', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='to_user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='received_notification', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='created_on',
            field=models.DateTimeField(db_index=True, default=economy.models.get_time),
        ),
        migrations.AlterField(
            model_name='notification',
            name='message_html',
            field=models.CharField(blank=True, default='NULL', help_text='Html message', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='modified_on',
            field=models.DateTimeField(default=economy.models.get_time),
        ),
    ]