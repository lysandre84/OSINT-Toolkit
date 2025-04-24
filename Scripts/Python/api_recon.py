#!/usr/bin/env python3
"""
============================================================================================================================================
   
  /$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$   /$$$$$$$$                  /$$ /$$       /$$   /$$    
 /$$__  $$ /$$__  $$|_  $$_/| $$$ | $$|__  $$__/  |__  $$__/                 | $$| $$      |__/  | $$    
| $$  \ $$| $$  \__/  | $$  | $$$$| $$   | $$        | $$  /$$$$$$   /$$$$$$ | $$| $$   /$$ /$$ /$$$$$$  
| $$  | $$|  $$$$$$   | $$  | $$ $$ $$   | $$ /$$$$$$| $$ /$$__  $$ /$$__  $$| $$| $$  /$$/| $$|_  $$_/  
| $$  | $$ \____  $$  | $$  | $$  $$$$   | $$|______/| $$| $$  \ $$| $$  \ $$| $$| $$$$$$/ | $$  | $$    
| $$  | $$ /$$  \ $$  | $$  | $$\\  $$$   | $$        | $$| $$  | $$| $$  | $$| $$| $$_  $$ | $$  | $$ /$$
|  $$$$$$/|  $$$$$$/ /$$$$$$| $$ \\  $$   | $$        | $$|  $$$$$$/|  $$$$$$/| $$| $$ \\  $$| $$  |  $$$$/ 
 \______/  \______/ |______/|__/  \__/   |__/        |__/ \\______/  \______/ |__/|__/  \__/|__/   \___/  
   
============================================================================================================================================
Script     : api_recon.py
Auteur     : Lysius
Date       : 30/11/2024
Description: Interroge une API REST, gère pagination et erreurs.
             • Authentification via header Bearer
             • Pagination automatique jusqu’à épuisement
             • Formate et exporte en JSON ou XML selon option
============================================================================================================================================
"""
import argparse
import requests
import json
import sys

def fetch_data(endpoint, apikey, output_format):
    headers = {'Authorization': f'Bearer {apikey}'}
    params = {'page': 1}
    results = []
    while True:
        resp = requests.get(endpoint, headers=headers, params=params)
        if resp.status_code != 200:
            print(f"[!] Erreur HTTP {resp.status_code}")
            sys.exit(1)
        data = resp.json()
        results.extend(data.get('items', data))
        if not data.get('next_page'):
            break
        params['page'] += 1

    if output_format == 'json':
        print(json.dumps(results, indent=2))
    else:
        # simple XML conversion
        from dicttoxml import dicttoxml
        print(dicttoxml(results).decode())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--endpoint', required=True, help='URL de l'API')
    parser.add_argument('--apikey', required=True, help='Clé API')
    parser.add_argument('--format', choices=['json','xml'], default='json', help='Format de sortie')
    args = parser.parse_args()
    fetch_data(args.endpoint, args.apikey, args.format)
