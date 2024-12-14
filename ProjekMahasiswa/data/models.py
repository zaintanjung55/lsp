from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    npm = models.CharField(max_length=10, unique=True)  # Nomor Pokok Mahasiswa
    nama = models.CharField(max_length=100)
    tempat_lahir = models.CharField(max_length=50)
    tanggal_lahir = models.DateField()
    prodi = models.CharField(max_length=50)  # Program Studi

    def __str__(self):
        return f"{self.npm} - {self.nama}"