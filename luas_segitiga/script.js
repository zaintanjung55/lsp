// fungsi untuk menghitung luas segitiga
function hitungLuas() {
    const alas = document.getElementById('alas').value;
    const tinggi = document.getElementById('tinggi').value;
    const luas = 0.5 * alas * tinggi;
    document.getElementById('result').innerText = `Luas Segitiga: ${luas} cm²`;
}