#!/usr/bin/env python3
"""
Script para ejecutar todas las funciones del challenge y mostrar resultados.
"""

import sys
import time
from pathlib import Path

# Agregar el directorio actual al path para imports
sys.path.insert(0, str(Path(__file__).parent))

from q1_time import q1_time
from q1_memory import q1_memory
from q2_time import q2_time
from q2_memory import q2_memory
from q3_time import q3_time
from q3_memory import q3_memory


def main():
    file_path = "../farmers-protest-tweets-2021-2-4.json"
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    
    print("=" * 70)
    print("🚀 EJECUTANDO TODAS LAS FUNCIONES DEL CHALLENGE")
    print("=" * 70)
    print()
    
    results = {}
    
    # Q1
    print("📅 Q1: Top 10 fechas con más tweets + usuario más activo")
    print("-" * 70)
    
    print("🕐 Ejecutando q1_time...")
    start = time.time()
    q1_time_result = q1_time(file_path)
    q1_time_elapsed = time.time() - start
    print(f"⏱️  Tiempo: {q1_time_elapsed:.2f} segundos")
    results['q1_time'] = q1_time_elapsed
    
    print("\n💾 Ejecutando q1_memory...")
    start = time.time()
    q1_memory_result = q1_memory(file_path)
    q1_memory_elapsed = time.time() - start
    print(f"⏱️  Tiempo: {q1_memory_elapsed:.2f} segundos")
    results['q1_memory'] = q1_memory_elapsed
    
    print("\n📊 Resultados Q1 (primeros 3):")
    for i, (date, username) in enumerate(q1_time_result[:3], 1):
        print(f"  {i}. {date} - {username}")
    
    if q1_time_result == q1_memory_result:
        print("✅ Los resultados coinciden entre ambas versiones")
    else:
        print("⚠️  Los resultados difieren")
    
    print("\n" + "=" * 70)
    print("😀 Q2: Top 10 emojis más usados")
    print("-" * 70)
    
    print("🕐 Ejecutando q2_time...")
    start = time.time()
    q2_time_result = q2_time(file_path)
    q2_time_elapsed = time.time() - start
    print(f"⏱️  Tiempo: {q2_time_elapsed:.2f} segundos")
    results['q2_time'] = q2_time_elapsed
    
    print("\n💾 Ejecutando q2_memory...")
    start = time.time()
    q2_memory_result = q2_memory(file_path)
    q2_memory_elapsed = time.time() - start
    print(f"⏱️  Tiempo: {q2_memory_elapsed:.2f} segundos")
    results['q2_memory'] = q2_memory_elapsed
    
    print("\n📊 Top 10 emojis:")
    for i, (emoji, count) in enumerate(q2_time_result, 1):
        print(f"  {i}. {emoji} - {count:,} veces")
    
    if q2_time_result == q2_memory_result:
        print("✅ Los resultados coinciden entre ambas versiones")
    else:
        print("⚠️  Los resultados difieren")
    
    print("\n" + "=" * 70)
    print("👥 Q3: Top 10 usuarios más influyentes (por menciones)")
    print("-" * 70)
    
    print("🕐 Ejecutando q3_time...")
    start = time.time()
    q3_time_result = q3_time(file_path)
    q3_time_elapsed = time.time() - start
    print(f"⏱️  Tiempo: {q3_time_elapsed:.2f} segundos")
    results['q3_time'] = q3_time_elapsed
    
    print("\n💾 Ejecutando q3_memory...")
    start = time.time()
    q3_memory_result = q3_memory(file_path)
    q3_memory_elapsed = time.time() - start
    print(f"⏱️  Tiempo: {q3_memory_elapsed:.2f} segundos")
    results['q3_memory'] = q3_memory_elapsed
    
    print("\n📊 Top 10 usuarios más mencionados:")
    for i, (username, count) in enumerate(q3_time_result, 1):
        print(f"  {i}. @{username} - {count:,} menciones")
    
    if q3_time_result == q3_memory_result:
        print("✅ Los resultados coinciden entre ambas versiones")
    else:
        print("⚠️  Los resultados difieren")
    
    # Resumen
    print("\n" + "=" * 70)
    print("📊 RESUMEN DE TIEMPOS")
    print("=" * 70)
    print(f"{'Función':<20} {'Tiempo (s)':<15} {'Diferencia (%)':<15}")
    print("-" * 70)
    
    for func in ['q1', 'q2', 'q3']:
        time_val = results[f'{func}_time']
        memory_val = results[f'{func}_memory']
        diff = ((memory_val - time_val) / time_val * 100) if time_val > 0 else 0
        print(f"{func}_time:         {time_val:<15.2f}")
        print(f"{func}_memory:       {memory_val:<15.2f} {diff:+.2f}%")
    
    total_time = sum(results.values())
    print("-" * 70)
    print(f"{'TOTAL':<20} {total_time:<15.2f}")
    print("=" * 70)
    print("\n✅ Todas las funciones ejecutadas correctamente")


if __name__ == "__main__":
    main()
