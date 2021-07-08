
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id_nombre', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('precio', models.CharField(max_length=64)),
                ('cantidad_existente', models.IntegerField()),
                ('fecha_ingreso', models.CharField(max_length=64)),
                
            ],
        ),
    ]
