# as_bgp.py

as_number = input("Ingresa el número de AS de BGP: ")

try:
    asn = int(as_number)
    if 64512 <= asn <= 65534:
        print(f"El AS {asn} es un AS Privado.")
    else:
        print(f"El AS {asn} es un AS Público.")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
