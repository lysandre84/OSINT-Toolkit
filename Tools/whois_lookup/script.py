#!/usr/bin/env python3
"""
whois_lookup.py: Perform a WHOIS lookup for a domain.
Usage:
    python3 whois_lookup.py example.com
"""
import sys
import whois

def lookup(domain):
    try:
        w = whois.whois(domain)
        for key, value in w.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 whois_lookup.py <domain>")
        sys.exit(1)
    lookup(sys.argv[1])
