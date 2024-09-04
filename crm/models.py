from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=255) 
    email = models.EmailField(unique=True, max_length=255)
    numero_de_telephone = models.CharField(max_length=20)  
    type_de_bien_consulte = models.CharField(max_length=255)
    date_de_consultation = models.DateField()
    simulation_de_credit = models.TextField()
    agence = models.CharField(max_length=255, default='biat')
    est_client_biat = models.BooleanField(default=False)  
    montant_du_credit_simule = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    statut_du_contact = models.CharField(max_length=255)
    source_du_lead = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

        
class Simulation(models.Model):
    nom_sim = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)  
    email = models.EmailField(unique=True, max_length=255)
    pays_de_residence = models.CharField(max_length=255)
    revenu = models.CharField(max_length=255)
    client_biat = models.BooleanField()
    type_du_bien = models.CharField(max_length=255)
    valeur_de_votre_projet = models.CharField(max_length=255)
    montant_maximum_de_credit = models.CharField(max_length=255)
    votre_auto_financement = models.CharField(max_length=255)
    credit_sollicite = models.CharField(max_length=255)
    duree_de_Remboursement_souhaitee = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_sim


