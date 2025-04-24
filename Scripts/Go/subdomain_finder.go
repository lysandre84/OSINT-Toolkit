#!/usr/bin/env go run
/*
=============================================================================================================================================
 
  /$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$   /$$$$$$$$                  /$$ /$$       /$$   /$$    
 /$$__  $$ /$$__  $$|_  $$_/| $$$ | $$|__  $$__/  |__  $$__/                 | $$| $$      |__/  | $$    
| $$  \ $$| $$  \__/  | $$  | $$$$| $$   | $$        | $$  /$$$$$$   /$$$$$$ | $$| $$   /$$ /$$ /$$$$$$  
| $$  | $$|  $$$$$$   | $$  | $$ $$ $$   | $$ /$$$$$$| $$ /$$__  $$ /$$__  $$| $$| $$  /$$/| $$|_  $$_/  
| $$  | $$ \____  $$  | $$  | $$  $$$$   | $$|______/| $$| $$  \ $$| $$  \ $$| $$| $$$$$$/ | $$  | $$    
| $$  | $$ /$$  \ $$  | $$  | $$\\  $$$   | $$        | $$| $$  | $$| $$  | $$| $$| $$_  $$ | $$  | $$ /$$
|  $$$$$$/|  $$$$$$/ /$$$$$$| $$ \\  $$   | $$        | $$|  $$$$$$/|  $$$$$$/| $$| $$ \\  $$| $$  |  $$$$/ 
 \______/  \______/ |______/|__/  \__/   |__/        |__/ \\______/  \______/ |__/|__/  \__/|__/   \___/  
                                                                                                                                 
=============================================================================================================================================
 Script     : subdomain_finder.go
 Auteur     : Lysius
 Date       : 15/01/2023
 Description: Génère des sous-domaines à partir d’une wordlist.
              • Lit “subdomains.txt” avec gestion d’erreur
              • Gère option --file pour liste custom
              • Ignore lignes vides
=============================================================================================================================================
*/
package main

import (
    "flag"
    "fmt"
    "io/ioutil"
    "log"
    "strings"
)

func main() {
    domain := flag.String("domain", "", "Domaine à scanner (ex: example.com)")
    file := flag.String("file", "subdomains.txt", "Fichier de wordlist")
    flag.Parse()

    if *domain == "" {
        flag.Usage()
        return
    }
    data, err := ioutil.ReadFile(*file)
    if err != nil {
        log.Fatalf("Impossible de lire %s: %v", *file, err)
    }

    for _, line := range strings.Split(strings.TrimSpace(string(data)), "
") {
        if line == "" {
            continue
        }
        fmt.Printf("%s.%s\n", line, *domain)
    }
}
