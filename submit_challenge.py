#!/usr/bin/env python3
"""
Script para enviar el desafío a la API de evaluación.
"""

import requests
import json

def submit_challenge():
    """
    Envía el desafío a la API de evaluación.
    """
    url = "https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer"
    
    payload = {
        "name": "Cristian Caro",
        "mail": "cristian.caro93@hotmail.com",
        "github_url": "https://github.com/CristianCaro-portfolio/latam-challenge-de.git"
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        print("Enviando desafío a la API...")
        print(f"URL: {url}")
        print(f"Payload: {json.dumps(payload, indent=2)}")
        print("-" * 50)
        
        response = requests.post(url, json=payload, headers=headers)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            print("\n✅ ¡Desafío enviado exitosamente!")
        else:
            print(f"\n⚠️  El servidor respondió con código {response.status_code}")
            print("Por favor, revisa la respuesta del servidor.")
            
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error al enviar el request: {e}")
        return False
    
    return True

if __name__ == "__main__":
    submit_challenge()
