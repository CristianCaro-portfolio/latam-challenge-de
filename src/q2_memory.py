from typing import List, Tuple
from collections import Counter
import json
import re

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Optimizado para uso de memoria.
    Procesa línea por línea y mantiene solo contador de emojis.
    
    Returns:
        Lista de tuplas (emoji, conteo) con los top 10 emojis más usados.
    """
    emoji_counter = Counter()
    
    # Patrón regex para detectar emojis Unicode
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
        "\U0001F680-\U0001F6FF"  # Transport & Map Symbols
        "\U0001F1E0-\U0001F1FF"  # Flags
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"  # Enclosed characters
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002600-\U000026FF"  # Miscellaneous Symbols
        "\U00002700-\U000027BF"  # Dingbats
        "]+",
        flags=re.UNICODE
    )
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            try:
                tweet = json.loads(line)
                # Buscar emojis en el contenido del tweet
                content = tweet.get('content', '')
                if content:
                    emojis = emoji_pattern.findall(content)
                    for emoji in emojis:
                        emoji_counter[emoji] += 1
            except (json.JSONDecodeError, KeyError):
                continue
    
    # Retornar top 10 emojis
    return emoji_counter.most_common(10)


if __name__ == "__main__":
    import sys
    import time
    
    file_path = "../farmers-protest-tweets-2021-2-4.json"
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    
    print("💾 Ejecutando q2_memory...")
    start_time = time.time()
    result = q2_memory(file_path)
    elapsed_time = time.time() - start_time
    
    print(f"⏱️  Tiempo: {elapsed_time:.2f} segundos")
    print(f"📊 Top 10 emojis más usados:")
    for i, (emoji, count) in enumerate(result, 1):
        print(f"  {i}. {emoji} - {count:,} veces")
    print(f"\n✅ Total resultados: {len(result)}")