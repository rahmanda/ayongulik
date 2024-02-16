# Exercises - Part 1

Selamat datang di chapter 'Exercises - Part 1'! Pada exercises ini, kamu akan dilatih untuk mengimplementasikan konsep variable dan tipe-datanya beserta konsep conditionals. Pada setiap pertanyaan akan terdapat beberapa test cases berupa contoh input dan output yang perlu kalian uji saat membuat kode. Kode yang menjawab pertanyaan adalah kode yang berhasil lolos semua test cases-nya.

Selamat berlatih!

## Q1

Seseorang akan lulus mata kuliah di UHasselt apabila:

- Nilai ujiannya lebih besar atau sama dengan 10
- Nilai ujiannya kurang dari 10 dan lebih besar sama dengan 9, tetapi mata kuliah tersebut dapat ditolerasi

Buatlah kode untuk menentukan apakah seseorang akan lulus ujian mata kuliah di UHasselt berdasarkan nilai yang diperoleh. Print string 'Lulus!' apabila sesuai dengan kriteria lulus, dan print string 'Tidak lulus~' apabila sebaliknya.

Gunakan template ini untuk mengerjakan soal. Nilai ujian (`number`) dan toleransi (`boolean`) diambil dari parameter pada fungsi `main`.

```python
def main(score, tolerable):
    # tulis kode kamu disini


if __name__ == '__main__':
    # test input yang berbeda disini
    main(10, False)
```

**Test Case 1**

```
Input: 
10 False

Output:
'Lulus!'
```

**Test Case 2**

```
Input: 
9 False

Output:
'Tidak lulus~'
```

**Test Case 3**

```
Input: 
9 True

Output:
'Lulus!'
```

## Q2

Neilshan akan mengadakan pesta ulang tahun. Namun, tidak semua orang bisa menghadiri pesta ulang tahun Neilshan. Neilshan akan menerima tamu yang memenuhi semua kriteria di bawah ini:

1. Berpakaian formal (`boolean`)
2. Sudah mengisi RSVP (`boolean`)
3. Tidak mengajak teman lain lebih dari 2 (`number`)
4. Membawa hadiah yang bernilai minimal 200 euro (`number`)

Jika kriteria nomor 1 dan 2 terpenuhi namun ada salah satu dari kriteria 3 dan 4 yang tidak terpenuhi, maka Neilshan akan menanyakan almamater kuliahnya. Apabila tamunya ini beralmamater 'UHasselt' atau 'Unpar' (`string`), maka tamunya akan tetap diterima. Selain itu, tamunya akan ditolak.

Buatlah kode untuk menentukan apakah seseorang dapat menghadiri ulang tahun Neilshan atau tidak. Print string 'Diterima!' apabila Neilshan menerima tamunya, dan print string 'Ditolak~' apabila Neilshan menolak tamunya.

Gunakan template ini untuk mengerjakan soal. Semua nilai kriteria yang dibutuhkan diambil dari parameter pada fungsi `main`.

```python
def main(formal, rsvp, number_of_friends, gift_price, almamater):
    # tulis kode kamu disini


if __name__ == '__main__':
    # test input yang berbeda disini
    main(True, True, 2, 200, 'UHasselt')
```

**Test Case 1**

```
Input: 
True True 2 200 'UHasselt'

Output:
'Diterima!'
```

**Test Case 2**

```
Input: 
True True 2 200 'BSI'

Output:
'Diterima!'
```

**Test Case 3**

```
Input: 
True True 2 100 'Unpar'

Output:
'Diterima!'
```

**Test Case 4**

```
Input: 
True False 2 200 'Unpar'

Output:
'Ditolak~'
```

**Test Case 5**

```
Input: 
True True 5 200 'Unpar'

Output:
'Ditolak~'
```