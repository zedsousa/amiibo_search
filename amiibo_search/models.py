from django.db import models
import uuid

class Amiibo(models.Model):
    idAmiibo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serieAmiibo = models.CharField(max_length=255)
    personagem = models.CharField(max_length=15)
    serie = models.CharField(max_length=15)
    nome = models.CharField(max_length=15)
    tipo = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.serieAmiibo}"