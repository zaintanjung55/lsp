from django.shortcuts import render, redirect, get_object_or_404
from .models import Mahasiswa
from django.http import HttpResponse

def hello(request):
    return render(request, 'data/hello.html')

# 1. Read (Display list of Mahasiswa)
def form(request):
    # mahasiswa = Mahasiswa.objects.all()
    return render(request, 'data/formtambah.html')

# # 2. Create (Tambah data Mahasiswa)
# def mahasiswa_create(request):
#     if request.method == 'POST':
#         npm = request.POST['npm']
#         nama = request.POST['nama']
#         tempat_lahir = request.POST['tempat_lahir']
#         tanggal_lahir = request.POST['tanggal_lahir']
#         prodi = request.POST['prodi']

#         Mahasiswa.objects.create(
#             npm=npm,
#             nama=nama,
#             tempat_lahir=tempat_lahir,
#             tanggal_lahir=tanggal_lahir,
#             prodi=prodi
#         )
#         return redirect('mahasiswa_list')

#     return render(request, 'data/mahasiswa_form.html')

# # 3. Update (Edit data Mahasiswa)
# def mahasiswa_update(request, id):
#     mahasiswa = get_object_or_404(Mahasiswa, id=id)
#     if request.method == 'POST':
#         mahasiswa.npm = request.POST['npm']
#         mahasiswa.nama = request.POST['nama']
#         mahasiswa.tempat_lahir = request.POST['tempat_lahir']
#         mahasiswa.tanggal_lahir = request.POST['tanggal_lahir']
#         mahasiswa.prodi = request.POST['prodi']
#         mahasiswa.save()
#         return redirect('mahasiswa_list')

#     return render(request, 'data/mahasiswa_form.html', {'mahasiswa': mahasiswa})

# # 4. Delete (Hapus data Mahasiswa)
# def mahasiswa_delete(request, id):
#     mahasiswa = get_object_or_404(Mahasiswa, id=id)
#     if request.method == 'POST':
#         mahasiswa.delete()
#         return redirect('mahasiswa_list')

#     return render(request, 'data/mahasiswa_confirm_delete.html', {'mahasiswa': mahasiswa})
