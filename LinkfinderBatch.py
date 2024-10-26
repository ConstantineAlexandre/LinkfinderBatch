#!/usr/bin/env python3
import subprocess
import os
from colorama import Fore, Style, init
import time  

init(autoreset=True)

def run_linkfinder(url):
    try:
        start_time = time.time()  # Start processing time
        result = subprocess.run(['python3', 'linkfinder.py', '-i', url, '-o', 'cli'], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        processing_time = time.time() - start_time  # Calculate processing time

        if result.returncode == 0:
            if result.stdout.strip():  # Check if output is not empty
                print(f"{Fore.CYAN}[ Processing ]: {url} took {processing_time:.2f} seconds.")
                print(f"{Fore.GREEN}[ Results ]: for {url}:\n{Fore.YELLOW}{result.stdout}\n")
            
        else:
            print(f"{Fore.RED}Error processing {url}: {result.stderr}")
    
    except Exception as e:
        print(f"{Fore.RED}Exception occurred while processing {url}: {str(e)}")

def process_urls(file_path):
    if not os.path.exists(file_path):
        print(f"{Fore.RED}File {file_path} does not exist.")
        return
    
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file.readlines()]
        
        for url in urls:
            run_linkfinder(url)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Process interrupted by user.")

try:
    url_file = input(f"{Fore.CYAN}Enter the path to the file containing URLs: ").strip()
    if url_file:  # Proceed only if a file path was entered
        process_urls(url_file)
    else:
        print(f"{Fore.RED}No file path provided.")
except KeyboardInterrupt:
    print(f"\n{Fore.RED}Input interrupted by user.")
