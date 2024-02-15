# Kod źródłowy z użyciem pętli
import csv
import calculators as calc


# Przykładowa funkcja do analizy danych
def analyze_data_with_loops(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        values = []

        for row in reader:
            if (
                row["variable"] == "Sales, government funding, grants and subsidies"
                and row["unit"] == "DOLLARS(millions)"
            ):
                if row["value"].replace('.', '', 1).isdigit():
                    # total_sales += float(row["value"])
                    values.append(float(row["value"]))

        print(f"Average Sales: {calc.average(values):.2f}")
        print(f"Median: {calc.calculate_median(values):.2f}")
        print(f"Number of items: {len(values)}")
        print(f"Max: {max(values):.2f}")
        print(f"Min: {min(values):.2f}")


def main():
    # Wywołanie funkcji
    analyze_data_with_loops("file.csv")


if __name__ == "__main__":
    main()
