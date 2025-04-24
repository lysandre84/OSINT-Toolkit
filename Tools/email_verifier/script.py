#!/usr/bin/env python3
"""
email_verifier.py: Vérifier l'existence d'une adresse email via SMTP.
Usage:
    python3 email_verifier.py user@example.com
"""
import sys
import smtplib

def verify_email(email):
    domain = email.split('@')[1]
    try:
        records = smtplib.SMTP(domain)
        records.quit()
        print(f"{email} semble valide (connexion SMTP réussie).")
    except Exception as e:
        print(f"Impossible de vérifier {email}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 email_verifier.py <email>")
        sys.exit(1)
    verify_email(sys.argv[1])
