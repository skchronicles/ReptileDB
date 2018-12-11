from django.db import models

class Organism(models.Model):
        Author =models.CharField(max_length=200)
        Year =models.CharField(max_length=200)
        Highertaxa =models.CharField(max_length=200)
        Genus =models.CharField(max_length=40)
        Species=models.CharField(max_length=40)
        Reproduction =models.CharField(max_length=30)
        Parentheses =models.CharField(max_length=500)

        def __str__(self):
            return self.Author + " " + self.Year + self.Highertaxa + " " + self.Genus + " " + self.Species + " " + self.Reproduction + " " + self.Parentheses

class CommonName (models.Model):
    CommonName =models.CharField(max_length=50)
    pk_organism_id = models.ForeignKey(Organism, on_delete=models.CASCADE)

    def __str__(self):
        return self.CommonName

class Synonym (models.Model):
     Synonym =models.CharField(max_length=75)
     pk_organism_id = models.ForeignKey(Organism, on_delete=models.CASCADE)

     def __str__(self):
         return self.Synonym


class Links (models.Model):
     Links =models.CharField(max_length=500)
     pk_organism_id = models.ForeignKey(Organism, on_delete=models.CASCADE)

     def __str__(self):
         return self.Links


class Distribution(models.Model):
     Location =models.CharField(max_length=125)
     pk_organism_id = models.ForeignKey(Organism, on_delete=models.CASCADE)

     def __str__(self):
         return self.Location


class Subspecies_Name(models.Model):
     Subspecies =models.CharField(max_length=75)
     pk_organism_id = models.ForeignKey(Organism, on_delete=models.CASCADE)

     def __str__(self):
         return self.Subspecies


class Types(models.Model):
     Type =models.CharField(max_length=200)
     pk_organism_id = models.ForeignKey(Organism, on_delete=models.CASCADE)

     def __str__(self):
         return self.Type


class PhotoURLS(models.Model):
     PhotoURL =models.CharField(max_length=400)
     pk_organism_id = models.ForeignKey(Organism, on_delete=models.CASCADE)

     def __str__(self):
         return self.PhotoURL


class Comments(models.Model):
     Comments =models.CharField(max_length=5000)
     pk_organism_id = models.ForeignKey(Organism, on_delete=models.CASCADE)

     def __str__(self):
         return self.Comments


class BiblioRefer (models.Model):
     ReferenceNumber =models.CharField(max_length=10)
     pk_organism_id = models.ForeignKey(Organism, on_delete=models.CASCADE)

     def __str__(self):
         return self.ReferenceNumber




