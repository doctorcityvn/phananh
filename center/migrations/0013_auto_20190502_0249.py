# Generated by Django 2.2 on 2019-05-02 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0012_auto_20190502_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yeucau',
            name='thanhtoan_v',
            field=models.CharField(blank=True, default='thanh toán bảo hiểm', max_length=100, null=True, verbose_name='thanhtoan'),
        ),
    ]