from django.db import models

class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    email = models.EmailField(unique=True, db_index=False)
    numero_de_telephone = models.CharField(max_length=20)
    type_de_bien_consulte = models.CharField(max_length=50)
    date_de_consultation = models.DateField()
    simulation_de_credit = models.CharField(max_length=3, choices=[('Oui', 'Oui'), ('Non', 'Non')])
    montant_du_credit_simule = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    statut_du_contact = models.CharField(max_length=50, choices=[
        ('Contacté', 'Contacté'),
        ('RDV programmé', 'RDV programmé'),
        ('En attente', 'En attente'),
    ])
    source_du_lead = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Simulation(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom_sim = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(unique=True, db_index=False)
    paysDeResidence = models.CharField(max_length=20)
    revenu = models.CharField(max_length=50)
    clientBiat = models.BooleanField()
    typeDuBien = models.CharField(max_length=50)
    valeurDeVotreProjet = models.CharField(max_length=50)
    montantMaximumDeCredit = models.CharField(max_length=50)
    votreAutofinancement = models.CharField(max_length=50)
    creditSollicite = models.CharField(max_length=50)
    dureeDeRemboursementSouhaitee = models.CharField(max_length=2)

    def __str__(self):
        return self.nom_sim
               
