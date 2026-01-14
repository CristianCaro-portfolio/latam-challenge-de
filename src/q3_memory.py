from typing import List, Tuple
from collections import Counter
import json
import re

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Optimizado para uso de memoria.
    Procesa línea por línea y mantiene solo contador de menciones.
    
    Returns:
        Lista de tuplas (username, conteo_menciones) con los top 10 usuarios
        más influyentes según menciones recibidas.
    """
    mention_counter = Counter()
    
    # Patrón regex para detectar menciones @username
    mention_pattern = re.compile(r'@(\w+)')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            try:
                tweet = json.loads(line)
                # Buscar menciones en el contenido del tweet
                content = tweet.get('content', '')
                if content:
                    mentions = mention_pattern.findall(content)
                    for username in mentions:
                        mention_counter[username] += 1
            except (json.JSONDecodeError, KeyError):
                continue
    
    # Retornar top 10 usuarios más mencionados
    return mention_counter.most_common(10)