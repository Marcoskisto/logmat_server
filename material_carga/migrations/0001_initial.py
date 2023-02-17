# Generated by Django 4.1.6 on 2023-02-15 23:43

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
            name='ArquivoEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_data', models.FileField(blank=True, default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10, unique=True)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=10, unique=True)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('saram', models.CharField(max_length=7)),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='material_carga.setor')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_bmp', models.IntegerField(unique=True)),
                ('nomenclatura', models.CharField(max_length=1000)),
                ('n_serie', models.CharField(max_length=100)),
                ('vl_atualizado', models.FloatField()),
                ('vl_liquido', models.FloatField()),
                ('situacao', models.CharField(max_length=5)),
                ('is_pending', models.BooleanField(default=False)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='material_carga.conta')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='material_carga.setor')),
            ],
        ),
        migrations.CreateModel(
            name='Cautela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', models.CharField(default=None, max_length=100, null=True)),
                ('data_emissao', models.DateField()),
                ('data_devolucao', models.DateField(blank=True, null=True)),
                ('materials', models.ManyToManyField(related_name='cautelas', related_query_name='cautela', to='material_carga.material')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]