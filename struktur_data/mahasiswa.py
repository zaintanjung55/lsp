from django.db import models

class Mahasiswa(models.Model):
    npm = models.CharField(max_length=10, primary_key=True)
    nama = models.CharField(max_length=50)
    tempat_lahir = models.CharField(max_length=50)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=10)
    alamat = models.TextField()
    prodi = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama} ({self.npm})"