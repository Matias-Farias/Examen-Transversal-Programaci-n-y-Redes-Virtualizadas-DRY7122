def verificar_vlan(vlan):
    try:
        vlan = int(vlan)
        if 1 <= vlan <= 1005:
            return "VLAN Normal"
        elif 1006 <= vlan <= 4094:
            return "VLAN Extendida"
        else:
            return "VLAN fuera de rango válido"
    except ValueError:
        return "Entrada inválida. Debes ingresar un número entero."

if __name__ == "__main__":
    while True:
        entrada = input("Ingrese el número de VLAN (o 's' para salir): ")
        if entrada.lower() == 's':
            break
        resultado = verificar_vlan(entrada)
        print(resultado)