# Sistema Experto de Turismo en Río Grande

Este proyecto es un sistema experto desarrollado para recomendar lugares turísticos en la ciudad de Río Grande, Tierra del Fuego, basado en los intereses del visitante.

## Objetivo

Guiar al usuario a través de un flujo de preguntas para identificar qué tipo de viajero es, y sugerirle destinos turísticos específicos con enlaces y descripciones útiles.

---

## Tecnologías utilizadas

- Python
- Pandas
- JSON
- Gradio (interfaz web)
- Scikit-learn (modelo de árbol de decisión)
- Matplotlib (visualización)

---

## ¿Cómo funciona?

1. El sistema muestra un cartel de bienvenida.
2. El usuario responde dos preguntas:
   - ¿Preferís actividades al aire libre o en interior?
   - ¿Qué tipo de viajero sos? (naturalista, patriota, gastronómico, etc.)
3. El sistema recomienda lugares turísticos relevantes.
4. Se puede reiniciar para volver a comenzar el recorrido.

---

## Estructura del proyecto

proyecto_turismo/
│
├── data/
│ └── dataset_turismo_actualizado.csv
│
├── src/
│ ├── main.py ← contiene toda la lógica y la interfaz en Gradio
│ └── arbol_turismo.json
│
├── notebooks/
│ └── sistema_experto_turismo.ipynb
│
├── README.md

## ¿Cómo se ejecuta?

1. Cloná o descargá este repositorio.
2. Instalá las dependencias:
```bash
pip install pandas gradio scikit-learn matplotlib
Ejecutá la aplicación:

bash
Copiar
Editar
python src/main.py
Se abrirá una interfaz web local para interactuar con el sistema.

📊 Incluye modelo con scikit-learn
El proyecto también entrena un árbol de decisión con scikit-learn, usando categoría y perfil como variables de entrada, y lugar como salida. Esto cumple con los requisitos técnicos del proyecto y demuestra una alternativa automática a la lógica manual.

Video de presentación
El proyecto incluye un video explicativo mostrando el flujo paso a paso.

 Autor
Ezequiel Caballero
Politécnico de TMalvinas Argentinas – 2025
