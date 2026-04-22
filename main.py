# main.py
import csv

def load_shows(filename):
    shows = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            shows.append(row)
    return shows


def main():
    data = load_shows("shows.csv")
    print(f"Loaded {len(data)} shows from your list!")
    
    print("--- Welcome to the Show watch priority engine ---")
    
    if data:
        print(data[0])
    

if __name__ == "__main__":
    main()