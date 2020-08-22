# List comprehension adalah cara mudah untuk mendefinisikan dan membuat list di Python.

# List comprehension terdiri dari sebuah ekspresi diikuti oleh pernyataan for yang diletakkan di dalam tanda kurung [ ].Dengan menggunakan list 
# comprehension kita bisa membuat list secara otomatis dalam satu baris perintah saja. Ini sangat berguna jika anggota list yang hendak kita buat cukup banyak.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # list commprehension
    print([[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1) if i + j + k != n]) 
