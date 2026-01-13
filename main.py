from groq import Groq
import sys
import os

def main():

    # ---------- TRY 0: API KEY ----------
    try:
        API_KEY = os.getenv("GROQ_API_KEY")
        if not API_KEY:
            raise ValueError("GROQ_API_KEY no encontrada en variables de entorno")
    except Exception as e:
        print("❌ Error con la API KEY")
        print(e)
        sys.exit(1)

    # ---------- TRY 1: Cliente ----------
    try:
        client = Groq(api_key=API_KEY)
        print("✅ Cliente Groq inicializado")
    except Exception as e:
        print("❌ Error al inicializar el cliente Groq")
        print(e)
        sys.exit(1)

    # ---------- TRY 2: Llamada al modelo ----------
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": "¿Por qué la inferencia rápida es crítica en modelos de razonamiento?"
                }
            ],
            temperature=0.3
        )
        print("✅ Petición enviada correctamente")
    except Exception as e:
        print("❌ Error al hacer la petición a Groq")
        print(e)
        sys.exit(1)

    # ---------- TRY 3: Lectura de respuesta ----------
    try:
        response_text = completion.choices[0].message.content
        if not response_text:
            raise ValueError("La respuesta vino vacía")
        print("\n🤖 Respuesta del modelo:\n")
        print(response_text)
    except IndexError:
        print("❌ Error: No se encontró contenido en choices")
    except ValueError as ve:
        print("❌ Error de validación:")
        print(ve)
    except Exception as e:
        print("❌ Error inesperado al procesar la respuesta")
        print(e)

if __name__ == "__main__":
    main()
