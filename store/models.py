from django.db import models
from django.contrib.auth.models import User


class Utilisateur(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    nom = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom


class Category(models.Model):
    nomCat = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nomCat


class Produit(models.Model):
    nom_pro = models.CharField(max_length=200, null=True)
    cat_produit = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    prix = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nom_pro

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    utilisateur = models.ForeignKey(
        Utilisateur, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordre = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    id_transition = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        elements = self.element_set.all()
        total = sum([item.get_total for item in elements])
        return total

    @property
    def get_cart_item(self):
        elements = self.element_set.all()
        total = sum([item.quantite for item in elements])
        return total


class Element(models.Model):
    produit = models.ForeignKey(
        Produit, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantite = models.IntegerField(default=0, null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
  
    @property
    def get_total(self):
        total = self.produit.prix * self.quantite
        return total


class AdresseCourse(models.Model):
    utilisateur = models.ForeignKey(
        Utilisateur, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    adresse = models.CharField(max_length=200, null=True)
    ville = models.CharField(max_length=200, null=True)
    quartier = models.CharField(max_length=200, null=True)
    codeEntrer = models.CharField(max_length=200, null=True)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adresse
