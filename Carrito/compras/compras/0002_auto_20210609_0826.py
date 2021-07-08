from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('muebles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id_nombre', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=3)),
                ('precio', models.CharField(max_length=64)),
                ('cantidad_existente', models.CharField(max_length=64)),
                ('fecha_ingreso', models.CharField(max_length=3)),
                
            ],
        ),
       
    ]
