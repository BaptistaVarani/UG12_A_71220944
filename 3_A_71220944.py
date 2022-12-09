c=int(input('masukkan pembatas :'))
d=int(input('masukkan angka yang dilarang'))
for i in range(c):
    if i==d:
        continue
    print(i,end=' ')
