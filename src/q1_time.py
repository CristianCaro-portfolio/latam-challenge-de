from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter
import json

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Optimizado para tiempo de ejecución.
    Carga todos los tweets en memoria y usa estructuras eficientes (defaultdict, Counter).
    
    Returns:
        Lista de tuplas (fecha, username) con las top 10 fechas con más tweets
        y el usuario más activo de cada fecha.
    """
    # Contadores: fecha -> conteo total de tweets
    date_counts = defaultdict(int)
    # Contadores anidados: fecha -> username -> conteo
    date_user_counts = defaultdict(lambda: defaultdict(int))
    
    # Leer y procesar todo el archivo
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            try:
                tweet = json.loads(line)
                # Extraer fecha y username
                date_str = tweet.get('date', '')
                username = tweet.get('user', {}).get('username', '')
                
                if date_str and username:
                    # Parsear fecha (formato esperado: "2021-02-04T...")
                    date = datetime.fromisoformat(date_str.replace('Z', '+00:00')).date()
                    
                    # Actualizar contadores
                    date_counts[date] += 1
                    date_user_counts[date][username] += 1
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                # Ignorar líneas mal formateadas
                continue
    
    # Obtener top 10 fechas por conteo total
    top_dates = sorted(date_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    
    # Para cada fecha, obtener el usuario con más tweets
    result = []
    for date, _ in top_dates:
        if date_user_counts[date]:
            top_user = max(date_user_counts[date].items(), key=lambda x: x[1])[0]
            result.append((date, top_user))
    
    return result


if __name__ == "__main__":
    import sys
    import time
    
    file_path = "../farmers-protest-tweets-2021-2-4.json"
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    
    print("🕐 Ejecutando q1_time...")
    start_time = time.time()
    result = q1_time(file_path)
    elapsed_time = time.time() - start_time
    
    print(f"⏱️  Tiempo: {elapsed_time:.2f} segundos")
    print(f"📊 Top 10 fechas con más tweets:")
    for i, (date, username) in enumerate(result, 1):
        print(f"  {i}. {date} - {username}")
    print(f"\n✅ Total resultados: {len(result)}")