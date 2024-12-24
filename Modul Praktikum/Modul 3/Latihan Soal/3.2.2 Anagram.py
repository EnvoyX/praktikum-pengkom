A = int(input("Masukkan banyak elemen A: "))
B = int(input("Masukkan banyak elemen B: "))


Arr_A = [0 for i in range(A)]
Arr_B = [0 for j in range(B)]

for x in range(A):
    Arr_A[x] = int(input("Masukkan elemen A ke" + str("-") + str(x+1) + str(": ")))

for y in range(B):
    Arr_B[y] = int(input("Masukkan elemen B ke" + str("-") + str(y+1) + str(": ")))

print(Arr_A)
print(Arr_B)

change = [0 for i in range(A)]

for i in range(A):
    for j in range(B):
        if Arr_B[i] == Arr_A[j]:
            change[i] = Arr_A[j]
        
if change == Arr_B:
    print("B adalah anagram dari A")
else:
    print("B bukan anagram dari A")

print(change)