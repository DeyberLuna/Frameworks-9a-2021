from django.db import models

# Create your models here.
class Brand(models.Model):
    marca=models.CharField(max_length=50 , blank=False)
    modelo_marca=models.CharField(max_length=50, blank=False)
    create_at=models.DateTimeField()
    update_at=models.DateTimeField()

    def __str__(self):
        return self.marca

class BrandReference(models.Model):
    reference=models.CharField(max_length=150, blank=False)
    brand_id=models.ForeignKey(Brand, on_delete=models.CASCADE)
    create_at=models.DateTimeField()
    update_at=models.DateTimeField()
    delete_at=models.DateTimeField()

    def __str__(self):
        return self.reference

class Auto(models.Model):
    brand_id=models.ForeignKey(Brand, on_delete=models.CASCADE)
    reference_id=models.ForeignKey(BrandReference, on_delete=models.CASCADE)
    modelo=models.IntegerField()
    color=models.CharField(max_length=150, blank=False)
    clase=models.CharField(max_length=150, blank=False)
    numero_chasis=models.CharField(max_length=150, blank=False)
    numero_motor=models.CharField(max_length=150, blank=False)
    tipo=models.CharField(max_length=150, blank=False)
    placa=models.CharField(max_length=150, blank=False)
    kilometraje=models.IntegerField()
    cilindraje=models.IntegerField()
    tipo_combustible=models.CharField(max_length=150, blank=False)
    create_at=models.DateTimeField()
    update_at=models.DateTimeField()
    delete_at=models.DateTimeField()

    def __str__(self):
        return self.modelo


