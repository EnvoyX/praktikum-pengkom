pertama = int(input("Masukkan angka pertama: "))
kedua = int(input("Masukkan angka kedua: "))
operator = str(input("Masukkan operator: "))

if operator == "+":
    execute = pertama + kedua
    print(f"{pertama} {operator} {kedua} = {execute} ")

elif operator == "-":
    execute = pertama - kedua
    print(f"{pertama} {operator} {kedua} = {execute} ")

    
elif operator == "*":
    execute = pertama * kedua
    print(f"{pertama} {operator} {kedua} = {execute} ")


elif operator == "/":
    execute = pertama / kedua
    print(f"{pertama} {operator} {kedua} = {execute} ")


elif operator == "%":
    execute = pertama % kedua
    print(f"{pertama} {operator} {kedua} = {execute} ")

else:
    print("Input operator salah!")
