from groq import Groq
from dotenv import load_dotenv
import sys
import os
import traceback

def main():

    # ---------- PRE TRY: cargar .env ----------
    try:
        load_dotenv()
        print("✅ Archivo .env cargado")
    except Exception as e:
        print("❌ Error cargando .env")
        print(e)
        sys.exit(1)

    # ---------- TRY 0: API KEY ----------
    try:
        API_KEY = os.getenv("GROQ_API_KEY")

        if not API_KEY:
            raise ValueError("GROQ_API_KEY no encontrada en variables de entorno")

        if not API_KEY.startswith("gsk_"):
            raise ValueError("Formato de API KEY inválido")

        print("✅ API KEY validada")

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
        traceback.print_exc()
        sys.exit(1)

    # ---------- TRY 2: Llamada al modelo ----------
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un asistente experto en sistemas y modelos de IA."
                },
                {
                    "role": "user",
                    "content": "¿Por qué la inferencia rápida es crítica en modelos de razonamiento?"
                }
            ],
            temperature=0.3,
            max_tokens=200
        )

        print("✅ Petición enviada correctamente")

    except Exception as e:
        print("❌ Error al hacer la petición a Groq")
        traceback.print_exc()
        sys.exit(1)

    # ---------- TRY 3: Lectura de respuesta ----------
    try:
        if not completion or not completion.choices:
            raise ValueError("La API respondió sin choices")

        message = completion.choices[0].message

        if not message or not message.content:
            raise ValueError("La respuesta vino vacía")

        print("\n🤖 Respuesta del modelo:\n")
        print(message.content)

    except IndexError:
        print("❌ Error: índice fuera de rango en choices")
    except ValueError as ve:
        print("❌ Error de validación:")
        print(ve)
    except Exception as e:
        print("❌ Error inesperado al procesar la respuesta")
        traceback.print_exc()


if __name__ == "__main__":
    main()
