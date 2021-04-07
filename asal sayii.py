Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>


>>> sayi = int(input("Sayi Girin:"))
          sayac=0
          toplam=0
          sayac1=0
 
for i in range(2,(sayi+1)):
    sayac=0
    for j in range(2,i):
        if(i%j==0):
            sayac=sayac+1
            break
    if(sayac==0):
        print(i)
        sayac1=sayac1+1
        
print("Toplam ",sayac1," asal sayı var.")
