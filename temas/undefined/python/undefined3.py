from typing import Optional

def obtener_casa(nombre: str) -> Optional[str]:
    casas = {"Harry": "Gryffindor", "Hermione": "Gryffindor", "Ron": "Gryffindor"}
    if nombre in casas:
        return casas[nombre]
    else:
        return None

nombre = "Harry"
casa = obtener_casa(nombre)
if casa is not None:
    print(f"La casa de {nombre} es {casa}.")
else:
    print(f"No se encontró la casa de {nombre}.")

