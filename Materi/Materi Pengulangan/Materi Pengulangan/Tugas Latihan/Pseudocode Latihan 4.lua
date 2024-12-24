--16923151 / Muhamad Hanif Hafizhan

--Pseudocode Latihan 4

--{Inisialisasi}
input(N)     --{input jumlah anak ayam}

--{Proses pengulangan while}

while N != 1 and N > 0 do
    if N > 0 then
        N << N - 1
        output("Mati satu tinggalah", N)
    else {N = 1}   {di samadengankan 1 karena jika 0 "Mati satu tinggalah 0"}
        output("Mati satu tinggal induknya")

i traversal [N...0]
        output("Mati satu tinggalah", i)
        if i == 1 then
            print("Mati satu tinggal induknya")

while true do
    if N > 0 then
        N << N - 1
        print("Mati satu tinggal", N)
    if N == 1 then
        print("Mati satu tinggalah induknya")
        break 
