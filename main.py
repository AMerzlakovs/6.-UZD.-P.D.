#6. uzd
print("Programma paradīs lielāko skaitli un tā indeksu")
print("Ievadit bez komata, ar atstarpi")

skaiti = [int(skaitli) for skaitli in input("Ievadiet skaitļus: ").split()]

lielindex = 0

for i in range(1, len(skaiti)):
  if skaiti[i] > skaiti[lielindex]:
    lielindex = i

print(f"Lielakais skaitli:{skaiti[lielindex]} ar indeksu {lielindex}")
