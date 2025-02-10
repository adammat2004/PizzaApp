# Generated by Django 5.1.5 on 2025-02-02 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaOrder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cheesetype',
            name='name',
        ),
        migrations.RemoveField(
            model_name='crusttype',
            name='name',
        ),
        migrations.RemoveField(
            model_name='pizzaorder',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='pizzaorder',
            name='user',
        ),
        migrations.RemoveField(
            model_name='pizzasize',
            name='name',
        ),
        migrations.RemoveField(
            model_name='pizzasize',
            name='price',
        ),
        migrations.RemoveField(
            model_name='saucetype',
            name='name',
        ),
        migrations.AddField(
            model_name='cheesetype',
            name='cheese_type',
            field=models.CharField(choices=[('M', 'Mozzarella'), ('V', 'Vegan'), ('L', 'Low fat')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='crusttype',
            name='crust_type',
            field=models.CharField(choices=[('N', 'Normal'), ('T', 'Thin'), ('K', 'Thick'), ('G', 'Gluten Free')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='pizzasize',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='saucetype',
            name='sauce_type',
            field=models.CharField(choices=[('T', 'Tomato'), ('B', 'BBQ')], default='T', max_length=1),
        ),
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(choices=[('P', 'Pepperoni'), ('M', 'Mushroom'), ('O', 'Onion'), ('S', 'Sausage'), ('G', 'Green Pepper'), ('B', 'Black Olive'), ('A', 'Anchovy'), ('H', 'Ham'), ('C', 'Chicken'), ('B', 'Bacon')], default='P', max_length=10),
        ),
    ]
