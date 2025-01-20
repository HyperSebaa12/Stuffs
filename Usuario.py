import sys

def validar_nombre(nombre):
    
    if not nombre[0].isupper():
        print("Error: El nombre debe comenzar con mayúscula.")
        sys.exit()
    return nombre

def obtener_sexo():
    
    sexo = input("Sexo (Masculino/Femenino): ").capitalize()
    if sexo not in ["Masculino", "Femenino"]:
        print("Error: Entrada de sexo inválida.")
        sys.exit()
    return sexo

def obtener_region():
    
    print("\nRegiones disponibles:")
    print("1. Francia")
    print("2. Japón")
    print("3. México")
    
    while True:
        try:
            region_num = int(input("Seleccione el número de su región: "))
            if 1 <= region_num <= 3:
                break
            else:
                print("Por favor, ingrese un número entre 1 y 3.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

    regiones = {1: "Francia", 2: "Japón", 3: "México"}
    return regiones[region_num]

def obtener_favorito(region, sexo):
    
    opciones = {
        "Francia": ["Baguettes", "Vino", "Papas a la francesa"],
        "Japón": ["Sushi", "Anime", "Waifus"],
        "México": ["Tacos", "Chimichanga", "Picante"],
    }

    print(f"\n{ 'Sus' if sexo == 'Femenino' else 'Sus'} opciones favoritas de {region} son:")
    for i, opcion in enumerate(opciones[region]):
        print(f"{i+1}. {opcion}")
    
    while True:
        try:
            favorito_num = int(input(f"Seleccione el número de { 'su' if sexo == 'Femenino' else 'su'} opción favorita: "))
            if 1 <= favorito_num <= len(opciones[region]):
                break
            else:
                print(f"Por favor, ingrese un número entre 1 y {len(opciones[region])}.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
            
    return opciones[region][favorito_num - 1]

def main():
    """Función principal del programa."""
    print("Bienvenido al Creador de Perfiles")

    nombre = input("Nombre: ")
    nombre = validar_nombre(nombre)

    sexo = obtener_sexo()

    region = obtener_region()

    favorito = obtener_favorito(region, sexo)

    print("\n-- Perfil del Usuario --")
    print(f"Nombre: {nombre}")
    print(f"Sexo: {sexo}")
    print(f"Región: {region}")
    print(f"Cosa Favorita de {region}: {favorito}")
    print("¡Perfil creado con éxito!")

if __name__ == "__main__":
    main()



    