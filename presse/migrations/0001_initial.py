# Generated by Django 4.2.4 on 2023-10-04 18:18

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
            name="Coursier",
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
                ("solde_compte", models.DecimalField(decimal_places=2, max_digits=10)),
                ("numero", models.CharField(max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RechargeTransaction",
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
                    "montant",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Montant de la recharge en FCFA.",
                        max_digits=10,
                    ),
                ),
                (
                    "numero_compte_a_debiter",
                    models.CharField(
                        help_text="Numéro de compte à débiter.", max_length=20
                    ),
                ),
                (
                    "type_mobile_money",
                    models.CharField(
                        choices=[
                            ("Orange", "Orange Money"),
                            ("MTN", "MTN Mobile Money"),
                            ("Moov", "Moov Money"),
                            ("Wave", "Wave Money"),
                        ],
                        help_text="Type de Mobile Money pour la recharge.",
                        max_length=10,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "coursier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="presse.coursier",
                    ),
                ),
            ],
        ),
    ]