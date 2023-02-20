a = str(input ("Masukkan kata: "))

kata = dict()

for key in a.split():
    if key in kata:
        kata.update({
            key: kata[key] + 1
        })
    else:
        kata[key] = 1

print("Output:")


kataUnik = 0
for x in kata:
    kataUnik = kataUnik + kata[x]
    print(f"{x} = {kata[x]}")

print(f"total kata  = {kataUnik}")
print(f"total kata unik = {len(kata)}")
