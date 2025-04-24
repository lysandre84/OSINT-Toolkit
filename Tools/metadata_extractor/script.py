#!/usr/bin/env python3
"""
metadata_extractor.py: Extract metadata from files (images, documents).
Usage:
    python3 metadata_extractor.py <file_path>
"""
import sys
import subprocess

def extract_metadata(file_path):
    try:
        result = subprocess.run(['exiftool', file_path], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("ExifTool not found. Please install exiftool.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 metadata_extractor.py <file_path>")
        sys.exit(1)
    extract_metadata(sys.argv[1])
