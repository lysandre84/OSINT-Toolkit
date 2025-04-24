#!/usr/bin/env python3
"""
dns_enumeration.py: DNS enumeration for a domain.
Usage:
    python3 dns_enumeration.py example.com
"""
import sys
import dns.resolver

def enum_dns(domain):
    try:
        records = ['A', 'MX', 'NS', 'TXT', 'CNAME']
        for rtype in records:
            answers = dns.resolver.resolve(domain, rtype, raise_on_no_answer=False)
            print(f"--- {rtype} records ---")
            for rdata in answers:
                print(rdata.to_text())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 dns_enumeration.py <domain>")
        sys.exit(1)
    enum_dns(sys.argv[1])
