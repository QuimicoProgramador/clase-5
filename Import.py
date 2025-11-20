import csv

filename = "transactions.csv"

try:
    # Usamos 'with' para manejo seguro de recursos
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file) # Convierte cada fila en un diccionario
        print(f"--- Leyendo {filename} ---")
        for row in reader:
            print(f"Transacción {row['id']}: {row['type']} de {row['amount']} {row['currency']}")

except FileNotFoundError:
    print(f"❌ Error: El archivo '{filename}' no se encuentra. Verifica la ruta.")
except Exception as e:
    print(f"⚠️ Ocurrió un error inesperado: {e}")
finally:
    print("--- Fin del proceso de lectura ---")
