a=int(input('masukkan awal deret:'))
b=int(input('masukkan akhir deret:'))
for i in range(a,b):
    if i%2==1 and i%6!=0 and i%3!=0:
        print(i)
