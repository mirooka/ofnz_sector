# Generated by Django 4.0.1 on 2022-04-13 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_name_shoes_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hat',
            name='type',
            field=models.CharField(choices=[('Straw hat', 'Straw hat'), ('Cylinder', 'Cylinder'), ('Winter hat', 'Winter hat'), ('Cap', 'Cap')], max_length=10),
        ),
        migrations.AlterField(
            model_name='jacket',
            name='type',
            field=models.CharField(choices=[('Winter jacket', 'Winter jacket'), ('Summer jacket', 'Summer jacket'), ('Leather jacket', 'Leather jacket'), ('VEST', 'VEST')], max_length=14),
        ),
        migrations.AlterField(
            model_name='pants',
            name='type',
            field=models.CharField(choices=[('JEANS', 'JEANS'), ('SHORTS', 'SHORTS'), ('TRACKSUIT', 'TRACKSUIT'), ('PANTS', 'PANTS'), ('SKIRT', 'SKIRT')], max_length=9),
        ),
        migrations.AlterField(
            model_name='shirt',
            name='type',
            field=models.CharField(choices=[('T-SHIRT', 'T-SHIRT'), ('SWEATSHIRT', 'SWEATSHIRT'), ('SWEATER', 'SWEATER'), ('SHIRT', 'SHIRT'), ('TANK TOP', 'TANK TOP')], max_length=10),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='type',
            field=models.CharField(choices=[('BOOTS', 'BOOTS'), ('HEELS', 'HEELS'), ('SPORT_SHOES', 'SPORT_SHOES'), ('FLIP_FLOPS', 'FLIP_FLOPS')], max_length=11),
        ),
        migrations.AlterField(
            model_name='socks',
            name='type',
            field=models.CharField(choices=[('Sports socks', 'Sports socks'), ('Casual socks', 'Casual socks'), ('Winter socks', 'Winter socks'), ('Tights', 'Tights')], max_length=12),
        ),
        migrations.AlterField(
            model_name='underwear',
            name='type',
            field=models.CharField(choices=[('BRIEFS', 'BRIEFS'), ('BOXERS', 'BOXERS'), ('BRA', 'BRA'), ('Thong bikini', 'Thong bikini'), ('BIKINI', 'BIKINI'), ('Corset', 'Corset')], max_length=12),
        ),
    ]
