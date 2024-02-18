# Exercises - Part 3

Selamat datang di chapter 'Exercises - Part 3'! Pada exercises ini, kamu akan dilatih untuk mengimplementasikan konsep fungsi dan class. Pada setiap pertanyaan akan terdapat beberapa test cases berupa contoh input dan output yang perlu kalian uji saat membuat kode.

Selamat berlatih!

## Q1

Stanley ada seorang manajer di sebuah toko retail. Dia ingin melakukan analisis terhadap produk yang dijual di tokonya. Kebetulan, tokonya sudah punya sistem dan Stanley bisa mengambil data dari sistemnya dengan bentuk `list`. Struk `item` pada `list`-nya adalah berbentuk `dictionary` dengan key `id`, `product_name`, `category`, `price`, `stock` dan `sold` seperti di bawah ini:

```python
data = [
    {
        'id': 1,
        'product_name': 'Soft overcoat coat',
        'category': 'coat',
        'price': 65.95,
        'stock': 120,
        'sold': 30
    },
    {
        'id': 2,
        'product_name': 'High neck knit sweater',
        'category': 'sweater',
        'price': 39.95,
        'stock': 49,
        'sold': 0
    },
    {
        'id': 3,
        'product_name': 'Wide-leg jumpsuit with golden buttons',
        'category': 'pants',
        'price': 55.95,
        'stock': 100,
        'sold': 50
    },
    {
        'id': 4,
        'product_name': 'Wide-leg trousers with drawstring waistband',
        'category': 'pants',
        'price': 39.95,
        'stock': 83,
        'sold': 125      
    },
    {
        'id': 5,
        'product_name': 'Mom Jeans',
        'category': 'pants',
        'price': 29.95,
        'stock': 5,
        'sold': 234
    },
    {
        'id': 6,
        'product_name': 'Soft oversize coat',
        'category': 'coat',
        'price': 69.95,
        'stock': 124,
        'sold': 12
    },
    {
        'id': 7,
        'product_name': 'ZW collection trench coat with belt',
        'category': 'coat',
        'price': 89.95,
        'stock': 95,
        'sold': 97
    },
    {
        'id': 8,
        'product_name': 'Contrast knit sweater',
        'category': 'sweater',
        'price': 39.95,
        'stock': 2,
        'sold': 55
    },
    {
        'id': 9,
        'product_name': 'Sweatshirt with rhinestone slogan',
        'category': 'sweater',
        'price': 39.95,
        'stock': 24,
        'sold': 135
    },
    {
        'id': 10,
        'product_name': 'High waist boot-cut jeans',
        'category':  'pants',
        'price': 39.95,
        'stock': 2,
        'sold' 143
    }
]


```

### Q1.1

Buatlah fungsi `get_product_by_category` untuk memfilter data berdasarkan nilai `category`. Fungsi ini menerima dua parameter: `data_source` (list dictionary) dan `category_name` (`string`), dan mengembalikan data dengan format yang sama dengan data-nya:

Gunakan template ini untuk mengerjakan soal.

```python
def get_product_by_category(data, category_name):
    # tulis kode kamu disini
    return


if __name__ == '__main__':
    # copy data dari deskripsi di Q1
    print(get_product_by_category(data, 'sweater'))
```

### Q1.2

Buatlah fungsi `sort_product` untuk melakukan sorting data. Fungsi ini menerima tiga parameter: `data_source` (list dictionary), `key` (`string`, kemungkinan nilainya adalah 'id', 'product_name', 'category', 'price', 'stock', dan 'sold'), dan `direction` (`string`, 'asc' untuk mengurutkan nilai dari kecil ke besar, 'desc' untuk sebaliknya), dan mengembalikan data dengan format yang sama dengan data-nya. Contoh penggunaannya adalah sebagai berikut:

```python
output = sort_product(data, 'id', 'asc')
output = sort_product(data, 'category', 'desc')
output = sort_product(data, 'sold', 'desc')
```

Gunakan template ini untuk mengerjakan soal.

```python
def sort_product(data, key, direction):
    # tulis kode kamu disini
    return


if __name__ == '__main__':
    # copy data dari deskripsi di Q1
    print(sort_product(data, 'price', 'asc'))
```

> [!TIP]
> Kamu tidak perlu membuat pengecekan terhadap tipe data `number` dan `string` saat sorting.
> Untuk melakukan perbandingan dengan `string`, kamu bisa menggunakan cara yang sama dengan perbandingan dengan `number`.
> ```python
> # Penggunaan operator >, >=, <, dan <= pada dua buah string akan menghasilkan nilai boolean.
> # Python akan otomatis membandingkan string berdasarkan urutan alphabet.
> print('coat' < 'sweater') # Output: True
> print('pants' > 'coat') # Output: True
> ```

### Q1.3

Buatlah fungsi `get_sum` untuk menghitung aggregate penjumlahan dari data. Fungsi ini menerima dua parameter: `data_source` (list dictionary) dan `key` (`string`, kemungkinan nilainya adalah key dengan tipe data number), dan mengembalikan tipe data `number` hasil penjumlahan. Contoh penggunaannya adalah sebagai berikut:

```python
some_data = [
    {
        'id': 7,
        'product_name': 'ZW collection trench coat with belt',
        'category': 'coat',
        'price': 89.95,
        'stock': 95,
        'sold': 97       
    },
    {
        'id': 8,
        'product_name': 'Contrast knit sweater',
        'category': 'sweater',
        'price': 39.95,
        'stock': 2,
        'sold': 55
    }
]
print(get_sum(some_data, 'price')) # Output: 129.9
print(get_sum(some_data, 'sold')) # OUtput: 152
```