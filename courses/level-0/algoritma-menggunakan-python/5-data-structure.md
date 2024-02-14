# Data Structure

Selain menggunakan tipe data `number`, `string` dan `boolean`, nilai dari suatu variable dapat direpresentasikan oleh data structure. Pada bab ini, kita akan membahas dua data structure di Python yang lazim kita temui juga di bahasa pemrograman lain, yaitu `list` dan `dictionary`.

## List

List atau array adalah data structure yang dapat menyimpan kumpulan dari beberapa nilai/value. Berikut adalah contoh cara penulisan `list` dalam kode Python:

```python
my_list = [1, 2, 3, 4]

print(my_list) # output: [1, 2, 3, 4]
```

Nilai di dalam `list` seringkali juga disebut sebagai *item*.

Pada bahasa Python, kita juga dapat menggabungkan beberapa tipe data yang berbeda dalam satu `list` seperti pada contoh di bawah ini:

```python
my_list = [1, '2', 3.14, False]
```

Untuk mengakses item di dalam `list`, kita dapat menggunakan index. Item pertama akan memiliki index 0, item kedua memiliki index 1, item ketiga memiliki index 2 dst. Sehingga secara logis, item terakhir pada `list` akan memiliki index `n - 1`, dimana `n` adalah jumlah item pada list.

```python
my_list = [1, 2, 3, 4]

print(my_list[0]) # output: 1
print(my_list[2]) # output: 3
print(my_list[0] + my_list[1] + my_list[2]) # output: 6
```

Apabila kita mencoba untuk mengakses elemen dengan index > `n - 1`, Python akan memunculkan output error.

```python
my_list = [1, 2, 3, 4]

print(my_list[5])
# output: IndexError: list index out of range
```

Selain untuk mengakses item dalam `list` satu persatu, kita juga dapat menggunakan index range untuk mengakses beberapa elemen yang berurutan secara sekaligus (sublist).

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_list[0:5]) # output: [1, 2, 3, 4, 5]
print(my_list[5:7]) # output: [6, 7]
print(my_list[4:]) # output: [5, 6, 7, 8, 9, 10]
print(my_list[:5]) # output: [1, 2, 3, 4, 5]

my_list[0:5] = [5, 4, 3, 2, 1]
print(my_list) # output: [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
```

Untuk mendapatkan informasi jumlah item pada `list`, kita dapat menggunakan fungsi `len`.

```python
my_list = [1, 2, 3, 4]
list_length = len(my_list)

print(list_length) # output: 4
print(my_list[list_length - 1]) # output: 4
```

### Manipulasi list

Struktur dan isi item dari suatu `list` dapat kita manipulasi sesuai dengan keinginan. Salah satu contohnya, kita dapat mengganti nilai item pada suatu `list` dengan memanfaatkan index seperti pada contoh berikut:

```python
my_list = [1, 2, 3, 4]

my_list[2] = 100
print(my_list) # output: [1, 2, 100, 4]
```

Selain mengganti nilai, kita juga dapat menambahkan item pada list dan menggabungkan dua list menjadi satu.

```python
my_list = [1, 2, 3, 4]
my_list.append(5)
print(my_list) # output: [1, 2, 3, 4, 5]

other_list = [6, 7, 8, 9]
merged_list = my_list + other_list
print(merged_list) # output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

List juga dapat digabungkan menjadi satu nilai `string` menggunakan fungsi `join`. Operasi ini hanya dapat dilakukan untuk list yang semua nilai item-nya bertipe data `string`.

```python
my_list = ['Taylor', 'Swift', 'won', 'grammy', 'award']
print(' '.join(my_list)) # output: 'Taylor Swift won grammy award'
```

Untuk mengurangi item pada list, kita dapat menggunakan fungsi `pop` dan `remove`.

```python
my_list = [1, 2, 3, 4]
removed_item = my_list.pop() # fungsi ini akan menghapus item terakhir pada list

print(my_list) # output: [1, 2, 3]
print(removed_item) # output: 4

my_list = [1, 2, 2, 3, 2]
my_list.remove(2) # fungsi ini hanya akan menghapus item bernilai 2 yang muncul pertama kali pada list

print(my_list) # output: [1, 2, 3, 2]
```

Terakhir, untuk mengurutkan item kita dapat menggunakan fungsi `sort`.

```python
my_list = [4, 2, 1, 3]
my_list.sort()

print(my_list) # output: [1, 2, 3, 4]

my_list.sort(reverse = True)
print() # output: [4, 3, 2, 1]

fruits = ['cherry', 'apple', 'strawberry', 'grapes', 'apricot']
fruits.sort()

print(fruits) # output: ['apple', 'apricot', 'cherry', 'grapes', 'strawberry']
```

### Hubungan antara string dan list

Tipe data `string` dan data structure `list` memiliki hubungan yang dekat. Hal ini disebabkan kedua konsep tersebut memiliki sifat yang mirip. Berdasarkan penjelasan `list` di bab ini, bisa kita rangkum bahwa `list` merupakan kumpulan dari beberapa item. Sedangkan tipe data `string` pada hakikatnya juga merupakan *kumpulan dari beberapa karakter*. Sehingga, ada beberapa operasi dari `list` yang bisa kita lakukan juga pada tipe data `string`. Sebagai contoh, kita juga bisa menggunakan index untuk mengakses dan memanipulasi karakter pada `string`.

```python
headline_title = 'Taylor Swift will release her new album \"Midnight\" next year'
print(headline_title[0]) # output: 'T'
print(headline_title[0:6]) # output: 'Taylor'
```

## Dictionary