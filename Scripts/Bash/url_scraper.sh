#!/usr/bin/env bash
#
# =============================================================================================================================================
#  
#   /$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$   /$$$$$$$$                  /$$ /$$       /$$   /$$    
#  /$$__  $$ /$$__  $$|_  $$_/| $$$ | $$|__  $$__/  |__  $$__/                 | $$| $$      |__/  | $$    
# | $$  \ $$| $$  \__/  | $$  | $$$$| $$   | $$        | $$  /$$$$$$   /$$$$$$ | $$| $$   /$$ /$$ /$$$$$$  
# | $$  | $$|  $$$$$$   | $$  | $$ $$ $$   | $$ /$$$$$$| $$ /$$__  $$ /$$__  $$| $$| $$  /$$/| $$|_  $$_/  
# | $$  | $$ \____  $$  | $$  | $$  $$$$   | $$|______/| $$| $$  \ $$| $$  \ $$| $$| $$$$$$/ | $$  | $$    
# | $$  | $$ /$$  \ $$  | $$  | $$\  $$$   | $$        | $$| $$  | $$| $$  | $$| $$| $$_  $$ | $$  | $$ /$$
# |  $$$$$$/|  $$$$$$/ /$$$$$$| $$ \  $$   | $$        | $$|  $$$$$$/|  $$$$$$/| $$| $$ \  $$| $$  |  $$$$/ 
#  \______/  \______/ |______/|__/  \__/   |__/        |__/ \______/  \______/ |__/|__/  \__/|__/   \___/  
#                                                                                                                                 
# =============================================================================================================================================
#  Script     : url_scraper.sh
#  Auteur     : Lysius
#  Date       : 10/08/2023
#  Description: Scraping basique d’URLs avec curl, amélioré par user-agent et sortie JSON.
#               • Récupère tous les liens absolus sur la page
#               • Vérifie code HTTP et en-têtes
#               • Exporte JSON ou TXT selon option
# =============================================================================================================================================
set -euo pipefail
IFS=$'\n\t'

usage() {
  cat <<EOF
Usage: $0 --url <url> --out <dir> [--json]
  --url    URL cible
  --out    Répertoire de sortie
  --json   Génère un fichier links.json au lieu de links.txt
EOF
  exit 1
}

URL="" OUTDIR="" JSON=false
while [[ $# -gt 0 ]]; do
  case $1 in
    --url) URL="$2"; shift;;
    --out) OUTDIR="$2"; shift;;
    --json) JSON=true;;
    *) usage;;
  esac
  shift
done

if [[ -z "$URL" || -z "$OUTDIR" ]]; then
  usage
fi

mkdir -p "$OUTDIR"
echo "[*] Scraping $URL"
HTTP_CODE=$(curl -s -o /dev/null -w '%{http_code}' -A 'Mozilla/5.0' "$URL")
if [[ "$HTTP_CODE" -ne 200 ]]; then
  echo "[!] Erreur HTTP $HTTP_CODE"
  exit 1
fi

LINKS=$(curl -s -A 'Mozilla/5.0' "$URL" | grep -Eo '(http|https)://[^" ]+')
if $JSON; then
  echo "$LINKS" | jq -R -s -c 'split("\n")[:-1]' > "$OUTDIR/links.json"
  echo "[*] Liens JSON enregistrés dans $OUTDIR/links.json"
else
  echo "$LINKS" > "$OUTDIR/links.txt"
  echo "[*] Liens enregistrés dans $OUTDIR/links.txt"
fi
