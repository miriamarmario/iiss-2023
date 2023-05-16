from typing import Optional

def procesar_stream_magia(stream_magia) -> None:
    for lectura in stream_magia:
        hechizo: Optional[str] = obtener_hechizo(lectura)
        if hechizo is None:
            # No hay hechizo válido en este momento
            print("No hay hechizo disponible.")
        else:
            # Procesar el hechizo válido
            lanzar_hechizo(hechizo)

def obtener_hechizo(lectura) -> Optional[str]:
    
    if lectura == "Lumos":
        return "Lumos"
    elif lectura == "Accio":
        return "Accio"
    elif lectura == "Expelliarmus":
        return "Expelliarmus"
    else:
        return None

def lanzar_hechizo(hechizo: str) -> None:
    print(f"Lanzando hechizo: {hechizo}")


stream_magia = ["Lumos", "Accio", "Wingardium Leviosa", "Expelliarmus"]
procesar_stream_magia(stream_magia)
