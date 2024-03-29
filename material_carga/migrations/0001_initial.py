# Generated by Django 4.1.6 on 2024-02-08 03:21

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("matricula", models.CharField(max_length=7)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="ArquivoEntrada",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file_data", models.FileField(blank=True, default="", upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Cautela",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "observacao",
                    models.CharField(default=None, max_length=100, null=True),
                ),
                ("data_emissao", models.DateField(auto_now_add=True)),
                ("data_baixa", models.DateField(null=True)),
                ("data_recebimento", models.DateField(null=True)),
                (
                    "cautelado",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "permissions": [("gerenciar", "Can create, update, delete cautela")],
            },
        ),
        migrations.CreateModel(
            name="Conferencia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_owner", models.BooleanField(default=False)),
                ("observacao", models.CharField(default="", max_length=100)),
                (
                    "estado",
                    models.IntegerField(
                        choices=[
                            (1, "Em Uso"),
                            (2, "Inutilizado Danificado"),
                            (3, "Ocioso"),
                        ]
                    ),
                ),
                ("created", models.DateField(auto_now=True)),
                (
                    "conferente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Conta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("numero", models.CharField(max_length=10, unique=True)),
                ("nome", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Setor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sigla", models.CharField(max_length=10, unique=True)),
                ("nome", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Processo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=50)),
                ("nup", models.CharField(max_length=50)),
                (
                    "tipo",
                    models.IntegerField(
                        choices=[
                            (1, "Conferencia Interna"),
                            (2, "Conferencia Anual"),
                            (3, "Inventario"),
                        ]
                    ),
                ),
                ("data_inicio", models.DateField()),
                ("data_fim", models.DateField()),
                ("is_open", models.BooleanField(default=True)),
                (
                    "conferencias",
                    models.ManyToManyField(to="material_carga.conferencia"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Material",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("n_bmp", models.IntegerField(unique=True)),
                ("nomenclatura", models.CharField(max_length=1000)),
                ("n_serie", models.CharField(max_length=100)),
                ("vl_atualizado", models.FloatField()),
                ("vl_liquido", models.FloatField()),
                ("situacao", models.CharField(default=None, max_length=50)),
                ("imagem", models.FileField(blank=True, default="", upload_to="")),
                (
                    "conta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="material_carga.conta",
                    ),
                ),
                (
                    "setor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="material_carga.setor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Emprestimo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_devolucao", models.DateField(blank=True, null=True)),
                (
                    "cautela",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="emprestimos",
                        to="material_carga.cautela",
                    ),
                ),
                (
                    "material",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="material_carga.material",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="conferencia",
            name="localizacao",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="material_carga.setor",
            ),
        ),
        migrations.AddField(
            model_name="conferencia",
            name="material",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="material_carga.material",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="setor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="material_carga.setor",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
