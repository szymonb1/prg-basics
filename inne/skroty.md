

### **1. Ternary if (jednolinijkowy `if/else`)**

```python
x = 5
wynik = "parzysta" if x % 2 == 0 else "nieparzysta"
```

* Wybiera wartość w jednej linijce w zależności od warunku.

---

### **2. List comprehension**

```python
kwadraty = [i**2 for i in range(10) if i % 2 == 0]
```

* Tworzy listę w jednej linijce.
* Możesz dodawać `if` na końcu do filtrowania elementów.

---

### **3. `all()` i `any()`**

```python
digits = "11001"
print(all(d in "01" for d in digits))  # True jeśli wszystkie są 0 lub 1
print(any(d == "1" for d in digits))   # True jeśli przynajmniej jeden znak to 1
```

* `all()` → wszystkie warunki muszą być prawdziwe.
* `any()` → przynajmniej jeden warunek prawdziwy.

---

### **4. Lambda (funkcje anonimowe)**

```python
dodaj = lambda a, b: a + b
print(dodaj(2, 3))
```

* Szybka funkcja bez nazwy, często w jednej linijce.

---

### **5. Funkcja w jednej linijce z `return`**

```python
def is_even(n): return n % 2 == 0
```

* Możesz w jednej linijce zwrócić wynik warunku.

---

### **6. Generator expressions**

```python
suma = sum(i for i in range(10) if i % 2 == 0)
```

* Tworzy „generator” bez listy, do użycia w funkcjach jak `sum()`, `all()`, `any()`.

---

### **7. Sprawdzanie znaku w stringu/zbiorze**

```python
if n in "01":  # lub if n in {"0", "1"}
    print("0 albo 1")
```

* Prosty sposób na sprawdzenie, czy element należy do zbioru znaków.

---

### **8. Walidacja wszystkich elementów w stringu (połączenie z `all()`)**

```python
print("bin" if all(n in "01" for n in number) else "nie bin")
```

* Skraca klasyczną pętlę `for` i zmienną `isbinary` do jednej linijki.


