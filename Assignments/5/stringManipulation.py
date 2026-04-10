init = "UNIVERSITAS NUSA PUTRA SUKABUMI"
words = init.split()

# putra nusa
a = f"{words[2].lower()} {words[1].lower()}"
print(a)

# NIVERSITAS NSA PTRA SKABUMI
deleteU = init.replace("U", "")
print(deleteU)

# SUKABUMI PUTRA NUSA UNIVERSITAS 
reversing = " ".join(words[::-1])
print(reversing)

# UNPS
for w in words:
    print(w[0], end=" ")

print()

# TAS SAPU BUMI
tas = words[0][-3:]
sa = words[1][-2:]
pu = words[2][:2]
bumi = words[3][-4:]
print(f"{tas} {sa}{pu} {bumi}")


