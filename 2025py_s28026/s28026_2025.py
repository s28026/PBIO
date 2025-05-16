import random

"""
Program generujący losową sekwencję DNA na podstawie podanych danych wejściowych:
- ID sekwencji
- Opis sekwencji
- Długość sekwencji
- Imię użytkownika
Następnie wstawia imię użytkownika w losowe miejsce w sekwencji,
i zapisuje ją do pliku FASTA oraz wyświetla statystyki dla wygenerowanej sekwencji (bez imienia).
"""

# lista znakow do jednej zmiennej
CHARS = 'ACGT'


# Funkcja generująca losową sekwencję DNA na podstawie podanej długości
def generate_dna_sequence(length):
    rand_arr = random.choices(CHARS, k=length)  # losowanie znakow z listy CHARS k razy
    return ''.join(rand_arr)  # łączenie ich w jeden string


# Funkcja obliczająca statystyki sekwencji DNA
def calculate_statistics(dna_sequence):
    total = len(dna_sequence)  # pobranie długość sekwencji
    # ORIGINAL
    # stats = {nuc: dna_sequence.count(nuc) / total * 100 for nuc in 'ACGT'}
    # cg = stats['C'] + stats['G']
    # at = stats['A'] + stats['T']
    # cg_at_ratio = cg / at if at != 0 else float('inf')
    # return stats, cg_at_ratio
    # MODIFIED stworzenie zmiennej CHARS oraz sprowadzenie statystyk do jednego slownika
    stats = {
        # zliczenie wystąpień każdego nukleotydu w sekwencji na podstawie znaków z CHARS
        # i obliczenie ich procentowego udziału
        nuc: dna_sequence.count(nuc) / total * 100 for nuc in CHARS
    }
    # dodanie dodatkowych statystyk dla C i G
    stats['CG'] = stats['C'] + stats['G']
    return stats


def insert_name_into_sequence(dna_sequence, name):
    pos = random.randint(0, len(dna_sequence))
    return dna_sequence[:pos] + name + dna_sequence[pos:]


def main():
    # Pobranie danych od użytkownika
    seq_id = input("Podaj ID sekwencji: ").strip()
    description = input("Podaj opis sekwencji: ").strip()
    while True:  # pętla do walidacji podanej liczby długości sekwencji
        try:
            length = int(input("Podaj długość sekwencji DNA: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Wprowadź poprawną dodatnią liczbę całkowitą.")

    dna_sequence = generate_dna_sequence(length)

    # ORIGINAL
    # name = "Mateusz"
    # MODIFIED imie pobierane od uzytkownika
    name = input("Podaj imię: ").strip()
    sequence_with_name = insert_name_into_sequence(dna_sequence, name)

    stats = calculate_statistics(dna_sequence)

    # Tworzenie zawartości pliku FASTA
    filename = f"{seq_id}.fasta"
    # ORIGINAL
    # fasta_header = f">{seq_id} {description}"
    # fasta_content = f"{fasta_header}\n{sequence_with_name}"
    # MODIFIED uproszczenie do jednej zmiennej
    fasta_content = f">{seq_id} {description}\n{sequence_with_name}"
    # Zapis do pliku
    with open(filename, 'w') as f:
        f.write(fasta_content)

    print(f"\nSekwencja została zapisana do pliku: {filename}")

    # Wyświetlenie statystyk
    print("\nStatystyki sekwencji:")
    # ORIGINAL
    # for nuc in 'ACGT':
    #     print(f"{nuc}: {stats[nuc]:.2f}%")
    # print(f"Stosunek (C+G)/(A+T): {cg_at_ratio:.2f}")
    # MODIFIED uproszczenie do jednej zmiennej `stats`
    for n, c in stats.items():
        print(f"{n}: {c:.2f}%")


if __name__ == "__main__":
    main()
