function simpanData() {
            // Ambil nilai input
            const nik = document.getElementById("nik").value;
            const nama = document.getElementById("nama").value;
            const tempat_lahir = document.getElementById("tempat_lahir").value;
            const tanggal_lahir = document.getElementById("tanggal_lahir").value;
            const jenis_kelamin = document.getElementById("jenis_kelamin").value;
            const alamat = document.getElementById("alamat").value;
            const agama = document.getElementById("agama").value;

            // Validasi input kosong
            if (!nik || !nama || !tempat_lahir || !tanggal_lahir || !jenis_kelamin || !alamat || !agama) {
                alert("Harap isi semua field!");
                return;
            }

            // Tambahkan baris ke tabel
            const table = document.getElementById("biodataTable").getElementsByTagName('tbody')[0];
            const newRow = table.insertRow();

            newRow.innerHTML = `
                <td>${nik}</td>
                <td>${nama}</td>
                <td>${tempat_lahir}</td>
                <td>${tanggal_lahir}</td>
                <td>${jenis_kelamin}</td>
                <td>${alamat}</td>
                <td>${agama}</td>
                <td>
                    <button class="edit" onclick="editRow(this)">Edit</button>
                    <button class="delete" onclick="hapusRow(this)">Hapus</button>
                </td>
            `;

            // Reset form setelah input
            document.getElementById("biodataForm").reset();
        }

        function hapusRow(button) {
            // Hapus baris yang sesuai
            const row = button.parentNode.parentNode;
            row.parentNode.removeChild(row);
        }

        function editRow(button) {
            // Edit data dalam form
            const row = button.parentNode.parentNode;
            document.getElementById("nik").value = row.cells[0].innerText;
            document.getElementById("nama").value = row.cells[1].innerText;
            document.getElementById("tempat_lahir").value = row.cells[2].innerText;
            document.getElementById("tanggal_lahir").value = row.cells[3].innerText;
            document.getElementById("jenis_kelamin").value = row.cells[4].innerText;
            document.getElementById("alamat").value = row.cells[5].innerText;
            document.getElementById("agama").value = row.cells[6].innerText;

            // Hapus baris setelah mengedit
            row.parentNode.removeChild(row);
        }