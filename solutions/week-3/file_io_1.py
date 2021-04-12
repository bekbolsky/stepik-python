with open("solutions/week-3/dataset_3363_2.txt") as f:
    info = f.readline().strip()
print(info)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
output = []
umno = []
dec = info * 2

for i in range(len(info) - 1):
    if dec[i] in alphabet:
        output.append(dec[i])
    if dec[i] in alphabet and dec[i + 1] in digits and dec[i + 2] not in digits:
        umno.append(dec[i + 1])
    elif dec[i] in digits and dec[i + 1] in digits:
        umno.append(dec[i] + dec[i + 1])

for i in range(len(output)):
    print(output[i] * int(umno[i]), end="")
