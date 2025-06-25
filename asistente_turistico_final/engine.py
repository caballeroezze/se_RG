from rules import aplicar_reglas

def inferir_recomendaciones(perfil_usuario):
    recomendaciones = aplicar_reglas(perfil_usuario)
    if not recomendaciones:
        return {
            "perfil": perfil_usuario,
            "mensaje": "No se encontraron recomendaciones para este perfil.",
            "lugares_recomendados": []
        }
    return {
        "perfil": perfil_usuario,
        "mensaje": "Recomendaciones generadas con éxito.",
        "lugares_recomendados": recomendaciones
    }
