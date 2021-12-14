input_dice_count = input("Ievadi metamo kauliņu skaitu (2-5): ")

try:
  dice_count = int(input_dice_count)
except ValueError:
  print("Ievadi skaitli")
  exit()

if 2 > dice_count or dice_count > 5:
    print("Ievadi skaitli no 2 līdz 5")
    exit()

# Uzmestie kauliņi ir pāra skaitļi
print("Varbūtība, ka uzmestie kauliņi ir pāra skaitļi: " + str(1 ** dice_count) + "/" + str(2 ** dice_count))

# Uzmestie kauliņi ir vienādi skaitļi
print("Varbūtība, ka uzmestie kauliņi ir vienādi skaitļi: " + str(1 ** dice_count) + "/" + str(6 ** dice_count))

# Uzmestie kauliņi ir nepāra skaitļi
print("Varbūtība, ka uzmestie kauliņi ir nepāra skaitļi: " + str(1 ** dice_count) + "/" + str(2 ** dice_count))

# No uzmestajiem kauliņiem neviens skaitlis neatkārtojas
print("Varbūtība, ka no uzmestajiem kauliņiem neviens skaitlis neatkārtojas: " + str(5 ** dice_count) + "/" + str(6 ** dice_count))

# No uzmestajiem kauliņiem divi ir vienādi skaitļi
x = 1 ** 2

if dice_count - 2 > 0:
  x += 6 ** (dice_count - 2)

print("Varbūtība, ka no uzmestajiem kauliņiem divi ir vienādi skaitļi: " + str(x) + "/" + str(6 ** dice_count))
