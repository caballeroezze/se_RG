import gradio as gr
from engine import inferir_recomendaciones

# Palabras clave para perfilar al usuario
keywords_perfil = {
    "historia": "historiador",
    "museo": "curioso",
    "naturaleza": "naturalista",
    "pescar": "pescador",
    "pesca": "pescador",
    "malvinas": "patriota",
    "aventura": "aventurero",
    "arte": "artista",
    "cultura": "artista"
}

keywords_accesibilidad = {
    "fácil": 4,
    "accesible": 4,
    "difícil": 2,
    "lejos": 2,
    "alejado": 2
}

# Función que interpreta el texto del usuario
def interpretar_texto(texto_usuario):
    texto = texto_usuario.lower()
    perfil = None
    accesibilidad = None

    for palabra, p in keywords_perfil.items():
        if palabra in texto:
            perfil = p
            break

    for palabra, valor in keywords_accesibilidad.items():
        if palabra in texto:
            accesibilidad = valor
            break

    return perfil, accesibilidad

# Función que responde en el chatbot
def responder(mensaje_usuario):
    perfil, accesibilidad = interpretar_texto(mensaje_usuario)

    if perfil is None:
        return "No entendí bien tu perfil. Podés decir cosas como 'me interesa la naturaleza' o 'quiero ir a un museo'."

    resultado = inferir_recomendaciones(perfil)

    mensaje = f"Según tu perfil ({perfil}) te recomiendo:\n"
    for lugar in resultado.get("lugares_recomendados", []):
        mensaje += f"- {lugar}\n"

    return mensaje

# Interfaz Gradio con entrada de texto y salida de texto
iface = gr.Interface(
    fn=responder,
    inputs="text",
    outputs="text",
    title="Asistente Turístico de Río Grande",
    description="Escribí lo que te interesa y te recomiendo lugares. Ejemplo: 'Quiero un lugar cultural con fácil acceso'"
)

iface.launch()
