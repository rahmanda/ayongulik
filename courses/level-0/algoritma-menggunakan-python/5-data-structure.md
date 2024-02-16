# Data Structure

Selain menggunakan tipe data `number`, `string` dan `boolean`, nilai dari suatu variable dapat direpresentasikan oleh data structure. Pada chapter ini, kita akan membahas dua data structure di Python yang lazim kita temui juga di bahasa pemrograman lain, yaitu `list` dan `dictionary`.

## List

List atau array adalah data structure yang dapat menyimpan kumpulan dari beberapa nilai/value. Berikut adalah contoh cara penulisan `list` dalam kode Python:

```python
my_list = [1, 2, 3, 4]

print(my_list) # output: [1, 2, 3, 4]
```

Nilai di dalam `list` seringkali disebut sebagai *item*.

Pada bahasa Python, kita dapat menggabungkan beberapa tipe data yang berbeda seperti `number`, `string`, `boolean` ke dalam satu `list`. Kita juga bisa memasukkan `list` menjadi item pada suatu `list`.

```python
my_list = [1, '2', 3.14, False, [1, 2, 3]]
```

Untuk mengakses item di dalam `list`, kita dapat menggunakan index. Item pertama akan memiliki index 0, item kedua memiliki index 1, item ketiga memiliki index 2 dst. Sehingga secara logis, item terakhir pada `list` akan memiliki index `n - 1`, dimana `n` adalah jumlah item pada `list`.

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

> [!TIP]
> Apabila kamu perlu membuat `list` dengan item `number` yang berurutan dalam rentang tertentu secara cepat, kamu bisa memakai fungsi `range`.
> ```python
> my_list = list(range(0, 5))
> print(my_list) # [0, 1, 2, 3, 4]
> ```

### Manipulasi list

Struktur dan isi item dari suatu `list` dapat kita manipulasi sesuai dengan keinginan. Salah satu contohnya, kita dapat mengganti nilai item pada suatu `list` dengan memanfaatkan index seperti pada contoh berikut:

```python
my_list = [1, 2, 3, 4]

my_list[2] = 100
print(my_list) # output: [1, 2, 100, 4]
```

Selain mengganti nilai, kita juga dapat menambahkan item pada list dan menggabungkan dua list menjadi satu.

```python
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list) # output: [1, 2, 3]

other_list = [4, 5, 6, 7]
merged_list = my_list + other_list
print(merged_list) # output: [1, 2, 3, 4, 5, 6, 7]
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

Tipe data `string` dan data structure `list` memiliki hubungan yang dekat. Hal ini disebabkan kedua konsep tersebut memiliki sifat yang mirip. Berdasarkan penjelasan `list` di chapter ini, bisa kita rangkum bahwa `list` merupakan kumpulan dari beberapa item. Sedangkan tipe data `string` pada hakikatnya juga merupakan *kumpulan dari beberapa karakter*. Sehingga, ada beberapa operasi dari `list` yang bisa kita lakukan juga pada tipe data `string`. Sebagai contoh, kita juga bisa menggunakan index untuk mengakses dan memanipulasi karakter pada `string`.

```python
headline_title = 'Taylor Swift will release her new album \"Midnight\" next year'
print(headline_title[0]) # output: 'T'
print(headline_title[0:6]) # output: 'Taylor'
```

Namun berbeda dengan `list`, apabila kita mencoba mengganti nilai item dengan menggunakan index, program Python akan mengeluarkan pesan error.

```python
my_name = 'John Doe'
my_name[0] = 'B' # TypeError: 'str' object does not support item assignment
```

## Dictionary

Dictionary atau hash map adalah data structure yang menyimpan data dengan format key-value. Berbeda dengan `list` yang akses nilai-nya melalui index yang dihasilkan secara otomatis (`0...(n-1)`), nilai pada `dictionary` diakses menggunakan key yang kita definisikan sendiri.

```python
my_dict = {
    'base_price': 50000,
    'delivery_fee': 5000,
    'discount_rate': 0.25
}
print(my_dict) # output: {'base_price': 50000, 'delivery_fee': 5000, 'discount_rate': 0.25}
print(my_dict['base_price']) # output: 50000
print(my_dict['base_price'] * my_dict['discount_rate']) # output: 12500
```

Kita dapat mengeset value pada `dictionary` dengan tipe data `number`, `string`, `boolean`, `list`, dan `dictionary` juga (nested) seperti pada contoh berikut:

```python
my_dict = {
    'base_price': 50000,
    'can_use_discount': True,
    'discount_rate': 0.25,
    'payment_methods': ['atm', 'credit_card', 'digital_wallet'],
    'payment_method_fees': {
        'atm': {
            'type': 'fixed',
            'amount': 1500
        },
        'credit_card': {
            'type': 'rate',
            'amount': 0.01
        }
    }
}
```

Pada umumnya, key pada `dictionary` bertipe data `string`. Namun, kita juga bisa membuat key dengan tipe data `number`. Tipe data `boolean` juga bisa digunakan sebagai key, namun penggunaannya sangat jarang.

```python
my_dict = {
    1: 'satu',
    2.5: 'dua koma lima',
    3: 3,
    False: True
}
print(my_dict) # output: {1: 'satu', 2: 'dua koma lima', 3: 3, False: True}
print(my_dict[1]) # output: 'satu'
print(my_dict[False]) # output: True
```

Key-key pada `dictionary` dipastikan unik. Apabila kita mencoba mendefinisikan dua key yang sama persis pada satu `dictionary`, Python akan hanya mengambil pasangan key-value yang terakhir.

```python
my_dict = {
    'base_price': 50000,
    'base_price': 5000,
    'discount_rate': 0.25
}
print(my_dict) # output: {'base_price': 5000, 'discount_rate': 0.25}
```

Untuk mendapatkan semua key pada sebuah variable `dictionary`, kita dapat menggunakan fungsi `keys`.

```python
my_dict = {
    'base_price': 50000,
    'delivery_fee': 5000,
    'discount_rate': 0.25
}
my_dict_keys = my_dict.keys()
print(my_dict_keys) # output: dict_keys(['base_price', 'delivery_fee', 'discount_rate'])
print(len(my_dict_keys)) # output: 3
```

### Manipulasi dictionary

Seperti halnya `list`, kita juga dapat memanipulasi struktur dari `dictionary` yang kita definisikan. Pertama, kita bisa mengganti nilai atau value pada key tertentu dalam `dictionary`.

```python
my_dict = {
    'base_price': 50000,
    'delivery_fee': 5000,
    'discount_rate': 0.25
}

my_dict['discount_rate'] = 0.05

print(my_dict) # output: {'base_price': 50000, 'delivery_fee': 5000, 'discount_rate': 0.05} 
```

Selain itu, kita juga bisa menambahkan key-value baru ke dalam `dictionary` yang telah kita definisikan seperti contoh berikut:

```python
my_dict = {
    'base_price': 50000,
    'delivery_fee': 5000,
    'discount_rate': 0.25
}

my_dict['payment_methods'] = ['atm', 'credit_card', 'digital_wallet']

print(my_dict) # output: {'base_price': 50000, 'delivery_fee': 5000, 'discount_rate': 0.25, 'payment_methods': ['atm', 'credit_card', 'digital_wallet']}
```

Untuk menghapus key pada `dictionary`, kita dapat menggunakan fungsi `del` dan `pop`.

```python
my_dict = {
    'base_price': 50000,
    'delivery_fee': 5000,
    'discount_rate': 0.25
}

del my_dict['discount_rate']
print(my_dict) # output: {'base_price': 50000, 'delivery_fee': 5000}

my_dict.pop('delivery_fee', None)
print(my_dict) # output: {'base_price': 50000}
```

Untuk menggabungkan dua `dictionary`, Python menyediakan fungsi `update` yang dapat digunakan seperti pada contoh:

```python
my_dict = {
    'base_price': 50000,
    'delivery_fee': 5000,
    'discount_rate': 0.25
}

other_dict = {
    'discount_rate': 0.05,
    'payment_methods': ['atm', 'credit_card', 'digital_wallet'],
}

my_dict.update(other_dict)

print(my_dict) # output: {'base_price': 50000, 'delivery_fee': 5000, 'discount_rate': 0.05, 'payment_methods': ['atm', 'credit_card', 'digital_wallet']}
```