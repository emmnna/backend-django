# Generated by Django 5.1 on 2024-08-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('numero_de_telephone', models.CharField(max_length=20)),
                ('type_de_bien_consulte', models.CharField(max_length=100)),
                ('date_de_consultation', models.DateField()),
                ('simulation_de_credit', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], max_length=3)),
                ('montant_du_credit_simule', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('statut_du_contact', models.CharField(choices=[('Contacté', 'Contacté'), ('RDV programmé', 'RDV programmé'), ('En attente', 'En attente')], max_length=50)),
                ('source_du_lead', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
