# Variable dan Tipe Data

Variable adalah sebuah simbol/referensi/nama yang kita berikan untuk sebuah nilai atau data yang ingin kita pakai. Cara kita mendefinisikan sebuah variable pada skrip Python adalah seperti contoh ini:

```python
total_purchase = 1000
```

Contoh di atas menunjukkan bahwa `total_purchase` adalah nama variable, dan `1000` merupakan value dari variable `total_purchase`. Dengan mendefinisikan variable, kita dapat menggunakan kembali nilai tersebut dengan melakukan referensi ke nama variablenya.

```python
total_purchase = 1000

print(total_purchase) # output: 1000
```

Apabila kita ingin mengubah nilai dari suatu variable, kita dapat mengeset ulang nilai variable tersebut seperti pada contoh berikut:

```python
total_purchase = 1000
print(total_purchase) # output: 1000

total_purchase = 999
print(total_purchase) # output: 999
```

## Tipe Data

Setiap value (atau data) yang kita set ke sebuah variable memiliki tipe data. Ada beberapa macam tipe data utama yang selalu ada pada bahasa pemrograman, yaitu:

- `number`
- `boolean`
- `string`

Mari kita bahas satu persatu tipe data ini.

### Number

Tipe data `number` ini sudah kita temui pada contoh pembuatan variable `total_purchase`. Karena nilainya berupa angka, kita bisa melakukan operasi matematika pada variable dengan tipe data ini. Perhatikan contoh berikut yang memperlihatkan penggunaan operasi matematika untuk menghitung nilai setelah diskon:

```python
base_price = 50000
payment_fee = 2000
delivery_fee = 5000
fixed_discount = 1000
extra_discount_rate = 0.25
fee_rate = 0.05

total_purchase = base_price + payment_fee + delivery_fee
print(total_purchase) # output: 57000

total_after_discount = total_purchase - fixed_discount
print(total_after_discount) # output: 56000

total_after_extra_discount = total_after_discount - total_after_discount * extra_discount_rate
print(total_after_extra_discount) # output: 42000

billed_price = total_after_extra_discount + total_after_extra_discount * fee_rate
print(billed_price) # output: 44100
```

Lengkapnya, operasi matematika yang bisa dilakukan adalah penambahan (`+`), pengurangan (`-`), perkalian (`*`), pembagian (`/`), dan modulus/sisa hasil bagi (`%`).

```python
my_favorite_number = 100

print(my_favorite_number + 10) # output: 110

print(my_favorite_number - 1) # output: 99

print(my_favorite_number * 10) # output: 1000

print(my_favorite_number / 4) # output: 25

print(my_favorite_number % 8)  # output: 4
```

Selain operasi matematika dasar, kita juga bisa menggunakan library tambahan dari Python untuk melakukan perhitungan yang lebih kompleks. Berikut ini adalah contoh penggunaan library `math`:

```python
import math # baris ini diperlukan untuk memakai fungsi-fungsi math

print(math.ceil(0.25)) # output: 1
print(math.floor(2.5)) # output: 2
print(math.log(2)) # output: 0.6931471805599453
```

### Boolean

Tipe data `boolean` hanya memiliki nilai `True` atau `False`. Biasanya, tipe data `boolean` dipakai untuk melakukan logika perbandingan. Logika perbandingan ini memiliki operator seperti sama dengan (`==`), tidak sama dengan (`!=`), lebih besar (`>`), lebih besar atau sama dengan (`>=`), lebih kecil (`<`), dan lebih kecil atau sama dengan (`<=`). Berikut ini adalah contoh penggunaan tipe data `boolean`.

```python
total_purchase = 1000

print(total_purchase == 1000) # output: True
print(total_purchase == 999) # output: False
print(total_purchase != 999) # output: True

print(total_purchase < 1001) # output: True
print(total_purchase < 999) # output: False
print(total_purchase > 999) # output: True

print(total_purchase <= 1001) # output: True
print(total_purchase <= 1000) # output: True
print(total_purchase >= 999) # output: False
print(total_purchase >= 1000) # output: True
```

Selain yang telah disebutkan, logika perbandingan juga memiliki operator lain seperti `and` dan `or`. Penggunaan operator tersebut bisa dilihat pada contoh berikut ini:

```python
print(True and True) # output: True
print(True and False) # output: False
print(False and True) # output: False
print(False and False) # output: False

print(True or True) # output: True
print(True or False) # output: True
print(False or True) # output: True
print(False or False) # output: False

print((True and True) or False) # output: True
print((True and True) and False) # output: False
```

Tentu saja, nilai `True` dan `False` bisa diset menjadi value dari suatu variable seperti pada contoh di bawah ini:

```python
are_you_hungry = True
can_buy_food = False

will_eat = are_you_hungry and can_buy_food
print(will_eat) # output: False 

will_eat = are_you_hungry or can_buy_food 
print(will_eat) # output: True
```

### String

Tipe data `string` menyimpan data kumpulan karakter (alfanumerik dan simbol). Berbeda dengan tipe data `number` dan `boolean`, penulisan data `string` perlu diapit menggunakan tanda petik (single quote `'` dan double quote `"`).

```python
my_name = 'John Doe'
my_name = "John Doe"

print(my_name) # output: 'John Doe'
```

> [!TIP]
> Q: Bagaimana cara menentukan apakah pakai double quote atau pakai single quote untuk variable string?  
> A: Sebenarnya tidak ada aturan khusus. Yang penting, pakai salah satu style dan gunakan style tersebut secara konsisten untuk semua kode kalian.

Operator boolean seperti `==` dan `!=` juga bisa dilakukan dengan tipe data `string` seperti pada contoh di bawah ini.

```python
my_name = 'John Doe'

print(my_name == 'John Doe') # output: True
print(my_name == 'John Lennon') # output: False
print(my_name != 'John Lennon') # output: True
```

Dua atau lebih variable `string` dapat digabung dengan menggunakan operator `+`.

```python
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name

print(full_name) # output: 'John Doe'
```

Berbeda dengan tipe data `number` and `boolean`, tipe data `string` dapat menggunakan fungsi `len` untuk mendapatkan panjang karakter.

```python
first_name = 'John'
last_name = 'Doe'

print(len(first_name)) # output: 4
print(len(last_name)) # output: 3

print(len(first_name + ' ' + last_name)) # output: 8
```

Selain itu, kita juga bisa mengkonstruksi nilai `string` dengan lebih dinamis menggunakan fungsi `format` dan `f-strings` seperti contoh berikut ini. 

```python
my_name = 'John Doe'
my_age = 21

# Contoh penggunaan fungsi format

print(
  'Hi, my name is {} and I am {} years old'.format(my_name, my_age)
) # output: 'Hi, my name is John Doe and I am 21 years old'

print(
  'Hi, my name is {name} and I am {age} years old'.format(name=my_name, age=my_age)
) # output: 'Hi, my name is John Doe and I am 21 years old'


# Contoh penggunaan fungsi f-strings (interpolation)

print(
  f'Hi, my name is {my_name} and I am {my_age} years old'
) # output: 'Hi, my name is John Doe and I am 21 years old'
```

Semua contoh variable `string` yang diberikan sampai tahap ini belum ada yang mengandung single quote (`'`) atau double quote (`"`) dalam value-nya. Hal ini disebabkan ada beberapa trik yang perlu digunakan untuk menghindari sintaks error.

```python
# Contoh di bawah ini akan memunculkan error 'SyntaxError: invalid syntax'
caption_text = 'Indonesian's rain forest in Kalimantan are rapidly decreasing due to illegal clearing'
```

Ada beberapa trik yang bisa dilakukan untuk menghindari error tersebut. Salah satunya adalah dengan mengapit `string` yang mengandung single quote dengan double quote.

```python
caption_text = "Indonesian's rain forest in Kalimantan are rapidly decreasing due to illegal clearing"
```

Untuk `string` yang mengandung double quote, value-nya perlu diapit dengan single quote.

```python
headline_title = 'Taylor swift will release her new album "Midnight" next year'
```

Selain mengkombinasikan antara single quote dan double quote, cara lain yang dapat dilakukan adalah dengan meng-escaped karakter tersebut di dalam string dengan menggunakan tanda `backslash`.

```python
caption_text = 'Indonesian\'s rain forest in Kalimantan are rapidly decreasing due to illegal clearing'
headline_title =  "Taylor swift will release her new album \"Midnight\" next year"
```

> [!NOTE]
> Terminologi dalam bab ini (untuk memudahkan pencarian Google):
> - String concatenation: penggabungan string  
> - String formatting/interpolation: pembentukan/konstruksi string