#print("|||||||")
#print("Your turn!")
import random

# Pide cuántos lápices se usarán
print("How many pencils would you like to use:")
inp = input()
while (not inp.isnumeric()) or (int(inp) < 1):
    if not inp.isnumeric():
        print("The number of pencils should be numeric")
    else:
        print("The number of pencils should be positive")
    inp = input()
pencils = int(inp)

# Pide quién va primero
print("Who will be the first (John, Jack):")
while True:
    turn = input()
    if turn != "John" and turn != "Jack":
        print("Choose between 'John' and 'Jack'")
    else:
        break

# Bucle principal del juego
while pencils > 0:
    # Imprime los lápices restantes y el turno actual
    print('|' * pencils)
    print(f"{turn}'s turn!")

    # Turno de John
    if turn == "John":
        while True:
            k = input()
            if k.isnumeric() and 1 <= int(k) <= 3:
                if int(k) <= pencils:
                    break
                else:
                    print("Too many pencils were taken")
            else:
                print("Possible values: '1', '2', or '3'")
        pencils -= int(k)
        # Si los lápices se acaban, Jack gana porque fue turno de John
        if pencils == 0:
            print("Jack won!")
            break
        turn = "Jack"  # Cambia el turno a Jack

    # Turno de Jack (bot)
    else:
        # Estrategia simple para el bot: intentar dejar un múltiplo de 4
        bottake = (pencils - 1) % 4
        if bottake == 0:  # Si no hay una jugada óptima, toma un número aleatorio
            bottake = 1 if pencils == 1 else random.randint(1, 3)
        print(bottake)
        pencils -= bottake
        # Si los lápices se acaban, John gana porque fue turno de Jack
        if pencils == 0:
            print("John won!")
            break
        turn = "John"  # Cambia el turno a John
