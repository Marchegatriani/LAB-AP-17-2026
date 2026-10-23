level_pedas = int(input("Masukkan persentase cabai: "))

if level_pedas >= 0 and level_pedas <= 10:
    print("Level aman")
elif level_pedas >= 11 and level_pedas <= 40:
    print("Level sedang")
elif level_pedas >= 41 and level_pedas <= 70:
    print("Level pedas")
elif level_pedas >= 71 and level_pedas <= 100:
    print("level ekstrim")
else:
    print("Invalid")