# Kod źródłowy z użyciem wyrażeń listowych (list comprehensions)
import csv
import calculators as calc


# Przykładowa funkcja do analizy danych
def analyze_data_with_comprehensions(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        sales_values = [
            float(row["value"])
            for row in reader
            if row["variable"] == "Sales, government funding, grants and subsidies"
            and row["unit"] == "DOLLARS(millions)"
            and row["value"].replace('.', '', 1).isdigit()
        ]
        print(f"Average Sales: {calc.average(sales_values):.2f}")
        print(f"Median: {calc.calculate_median(sales_values):.2f}")
        print(f"Number of items: {len(sales_values)}")
        print(f"Max: {max(sales_values):.2f}")
        print(f"Min: {min(sales_values):.2f}")

def main():
    # Wywołanie funkcji
    analyze_data_with_comprehensions("file.csv")


if __name__ == "__main__":
    main()
