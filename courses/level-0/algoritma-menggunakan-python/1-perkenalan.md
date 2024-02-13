# Perkenalan

Selamat datang pada short course 'Algoritma menggunakan Python' ini! Setelah menyelesaikan course ini, kalian diharapkan sudah memahami dasar-dasar algoritma dan bisa melakukan pemrograman dasar menggunakan Python secara mandiri. Tanpa panjang lebar, yuk langsung ke bagian selanjutnya!

## Apa itu algoritma?

Definisi algoritma itu banyak dan mudah saja dicari di internet. Namun pada dasarnya, algoritma itu adalah sebuah **set instruksi** yang dapat dilakukan untuk menyelesaikan suatu masalah. Dalam konteks ini (dan dalam lingkup yang luas), set instruksi ini dibuat oleh manusia dan diberikan ke komputer untuk kemudian dijalankan atau dilakukan pemrosesan.

## Mengapa belajar algoritma itu penting?

Dalam implementasinya, set instruksi ini bentuknya bisa bermacam tergantung dengan bahasa pemrograman yang dipilih. Sebagai contoh, sintaks dari bahasa C akan berbeda dengan sintaks dari bahasa Python. 

```c
// Bahasa C
#include <stdio.h>

int main(void)
{
    printf("Hello, world!\n");
}
```

```python
# Bahasa python
print('Hello, world!')
```

*Perbedaan sintaks dari bahasa C dan Python untuk melakukan print 'Hello, world!'*

Meskipun demikian, konsep dari set instruksi atau algoritma ini memiliki fundamental yang sama. Sehingga, apabila teman-teman telah memahami dengan benar konsep dari algoritma, belajar bahasa pemrograman baru akan jauh lebih mudah.

Pada course ini, Python dipilih karena bahasanya relatif mudah, fungsi-fungsinya lengkap, dan kegunaannya sangat luas (bisa untuk scripting, data analysis dsb). 

## Input dan output

Mengimplementasikan sebuah algoritma tidak luput dari konsep input dan output.

```mermaid
flowchart LR
    classDef processState stroke-dasharray:3,fill:white
    Input --> Algoritma:::processState
    Algoritma --> Output
```

Suatu algoritma dikatakan berhasil atau menyelesaikan masalah apabila algoritma tersebut dapat menghasilkan output yang dikehendaki sesuai dengan input yang diberikan. Sehingga, masalah yang sama dapat diselesaikan dengan solusi algoritma yang berbeda-beda. Jadi, kalau nanti di bagian exercise kalian memiliki solusi yang berbeda dari kunci jawaban, itu sama sekali tidak menjadi persoalan.

## Instalasi Python

Cara yang paling sederhana untuk melakukan instalasi Python adalah dengan instal langsung dari sumbernya. Pilih salah satu cara berikut ini sesuai dengan OS komputer yang kamu gunakan:

- Windows: Kunjungi https://www.python.org/downloads/ dan klik tombol download disana. Jalankan file `.exe` yang telah di-download, lalu ikuti instruksi pada dialog instalasi hingga selesai.
- MacOS: Buka aplikasi terminal atau iTerm, lalu jalankan perintah `brew update && brew upgrade`. Setelah itu, jalankan perintah `brew install python3`. Tunggu hingga proses instalasi selesai.

Untuk mengetes apakah instalasi program Python kalian sukses, ikuti langkah-langkah berikut:

1. Buat file baru dengan nama `hello-world.py` dan copas kode Python `Hello, world!` dari contoh sebelumnya.
2. Buka aplikasi terminal pada komputer kalian. Ganti direktori ke lokasi dimana kalian menyimpan file `hello-world.py`.
3. Jalan perintah `python hello-world.py`. Apabila tidak muncul error dan tampil teks `Hello, world!` pada terminal, maka instalasi Python kalian telah berhasil!

>[!NOTE] 
> Ada beberapa pengetahuan yang dapat kita ambil dari mengikuti langkah-langkah instalasi Python yang diberikan. 
> 1. Program Python perlu diinstal pada komputer kita agar skrip Python kita bisa dijalankan atau dieksekusi. Hal ini umumnya berlaku pada bahasa pemrograman lain seperti C, C++, R, Ruby, Erlang dsb. Yang membedakan biasanya hanya pada cara instalasinya saja. 
> 2. Setelah menginstal program Python, kita dapat menjalankan perintah `python` pada terminal. Ini juga umumnya berlaku pada bahasa pemrograman lain, dan biasanya cara menjalankan skripnya sama, yaitu dengan menjalankan perintah dengan pola `<bahasa-pemrograman> <nama-file>.<ekstensi>`.