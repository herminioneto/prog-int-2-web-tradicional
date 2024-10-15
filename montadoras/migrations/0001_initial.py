import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Montadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=50)),
                ('ano_fundacao', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor_referencia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('motorizacao', models.CharField(max_length=10)),
                ('turbo', models.BooleanField(default=False)),
                ('automatico', models.BooleanField(default=False)),
                ('montadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='montadoras.montadora')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(max_length=50)),
                ('ano_fabricacao', models.IntegerField()),
                ('ano_modelo', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('placa', models.CharField(max_length=7, unique=True)),
                ('vendido', models.BooleanField(default=False)),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='montadoras.modelo')),
            ],
        ),
    ]
