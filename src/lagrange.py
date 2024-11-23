import os

def lagrange_interpolation(X, Y, valor_x):
    resultado_lagrange = 0
    n = len(X)
    for i in range(n):
        producto_parcial = 1
        for j in range(n):
            if j != i:
                producto_parcial *= (valor_x - X[j]) / (X[i] - X[j])
        resultado_lagrange += producto_parcial * Y[i]
    return resultado_lagrange

def main():
    print("\t\t\tM E T O D O   N U M E R I C O   L A G R A N G E")
    print("\tM E D I N A   G O N Z A L E Z   J O S E   R U B E N")
    print("\tG A R A Y   M E N D O Z A   M A T I A S")
    print("\t23310341\t\t23310331\n")

    n = int(input("Ingrese número de puntos (X, Y): "))
    print()

    X = [0] * n
    Y = [0] * n

    print("Iteración".ljust(15) + "Xi".ljust(15) + "Yi")
    print("-" * 35)
    for i in range(n):
        print(str(i).ljust(15) + f"X{i}".ljust(15) + f"Y{i}")

    print("\nIngrese valores en Xi:")
    for i in range(n):
        X[i] = float(input(f"x[{i}]: "))

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\t\t\tM E T O D O   N U M E R I C O   L A G R A N G E")
    print("\tM E D I N A   G O N Z A L E Z   J O S E   R U B E N")
    print("\tG A R A Y   M E N D O Z A   M A T I A S")
    print("\t23310341\t\t23310331\n")

    print("Iteración".ljust(15) + "Xi".ljust(15) + "Yi")
    print("-" * 35)
    for i in range(n):
        print(str(i).ljust(15) + str(X[i]).ljust(15) + f"Y{i}")

    print("\nIngrese valores en Yi:")
    for i in range(n):
        Y[i] = float(input(f"f(x)[{i}]: "))

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t\t\tM E T O D O   N U M E R I C O   L A G R A N G E")
        print("\tM E D I N A   G O N Z A L E Z   J O S E   R U B E N")
        print("\tG A R A Y   M E N D O Z A   M A T I A S")
        print("\t23310341\t\t23310331\n")

        print("Iteración".ljust(15) + "Xi".ljust(15) + "Yi")
        print("-" * 35)
        for i in range(n):
            print(str(i).ljust(15) + str(X[i]).ljust(15) + str(Y[i]))

        while True:
            valor_x = float(input("\nIngrese valor de X para calcular su F(X): "))
            if valor_x < X[0] or valor_x > X[-1]:
                print("\nEl valor solicitado de X se encuentra fuera del rango de interpolación")
                print("Ingrese un nuevo valor para X")
            else:
                break

        resultado = lagrange_interpolation(X, Y, valor_x)

        fix = int(input("Fix 0~9? "))
        print(f"\nValor interpolar F({valor_x}) = {round(resultado, fix)}")

        opc = int(input("\n¿Desea encontrar otro valor para F(X)? 1)Sí 2)No: "))
        if opc == 2:
            break

if __name__ == "__main__":
    main()