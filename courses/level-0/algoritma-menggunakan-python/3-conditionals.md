# Conditionals

Conditionals adalah konsep dari programming yang memberikan perintah kepada komputer untuk melakukan keputusan atau menjalankan suatu proses berdasarkan hasil dari logika perbandingan/boolean. Konsep ini dapat divisualisasikan ke dalam bentuk diagram flowchart. Diagram berikut mengilustrasikan contoh kasus conditional untuk memutuskan apakah seseorang akan makan atau tidak.

```mermaidjs
flowchart TD
    A[Start] --> B{Am I hungry?}
    B -- Yes --> C{Is food exist?}
    C -- Yes --> D[Eat]
    B -- No --> E[Skip eating]
    C -- No --> F[Go shopping]
    F --> G{Have enough money?}
    G -- Yes --> H[Buy food]
    H --> D
    G -- No --> I[Can't buy food]
    I --> E
```

Ilustrasi conditional pada contoh dapat diimplementasikan kedalam kode dengan memanfaatkan sintaks Python. Yuk kita ikuti pembahasan lebih detailnya!

## If dan else if 

## Switch

## Ternary