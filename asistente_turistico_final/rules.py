from knowledge import lugares, perfiles

def aplicar_reglas(perfil_usuario):
    tipo_preferido = perfiles.get(perfil_usuario)
    if not tipo_preferido:
        return []

    recomendaciones = []

    for lugar in lugares:
        if lugar["tipo"] == tipo_preferido:
            # Reglas adicionales por perfil
            if perfil_usuario == "aventurero":
                if lugar["accesibilidad"] <= 3 and lugar["estetica"] >= 4:
                    recomendaciones.append(lugar["nombre"])
            elif perfil_usuario == "naturalista":
                if lugar["accesibilidad"] >= 3 and lugar["estetica"] >= 4:
                    recomendaciones.append(lugar["nombre"])
            elif perfil_usuario == "pescador":
                if lugar["accesibilidad"] >= 2 and lugar["estetica"] >= 4:
                    recomendaciones.append(lugar["nombre"])
            elif perfil_usuario == "curioso":
                if lugar["accesibilidad"] >= 3:
                    recomendaciones.append(lugar["nombre"])
            else:
                # Default para otros perfiles
                recomendaciones.append(lugar["nombre"])

    return recomendaciones
