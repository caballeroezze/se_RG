from engine import inferir_recomendaciones

perfil = input("Ingresá tu perfil de usuario (ej. amante_de_naturaleza): ")
resultado = inferir_recomendaciones(perfil)
print(resultado)
