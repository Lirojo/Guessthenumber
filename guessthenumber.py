def guess_the_number():
    print("Pomyśl liczbę od 1 do 100, a komputer spróbuje zgadnąć ją w maksymalnie 5 próbach.")
    input("Naciśnij Enter, gdy będziesz gotowy...")

    lower_number = 1
    higher_number = 100
    tries = 0
    guess = False
    even_number = None

    # Komputer pyta o parzystość liczby
    while even_number is None:
        even_answer = input("Czy twoja liczba jest parzysta? (tak/nie): ").lower()
        if even_answer == "tak":
            even_number = True
        elif even_answer == "nie":
            even_number = False
        else:
            print("Niepoprawna odpowiedź. Odpowiedz 'tak' lub 'nie'.")

    # Główna pętla gry (maksymalnie 5 prób)
    while tries < 5 and not guess:
        tries += 1

        # Komputer zgaduje liczbę
        try_guess = (lower_number + higher_number) // 2

        # Jeśli komputer wie, że liczba jest parzysta/nieparzysta, zgaduje odpowiednie liczby
        if even_number:
            if try_guess % 2 != 0:
                try_guess += 1  # Jeśli liczba jest nieparzysta, przesuń ją na najbliższą parzystą
        else:
            if try_guess % 2 == 0:
                try_guess -= 1  # Jeśli liczba jest parzysta, przesuń ją na najbliższą nieparzystą

        print(f"Próba {tries}: Czy to twoja liczba {try_guess}?")

        # Pobranie odpowiedzi i dalsza walidacja
        answer = input("Odpowiedz 'za duża', 'za mała', lub 'tak': ").lower()

        if answer == "tak":
            print(f"Komputer zgadł twoją liczbę {try_guess} w {tries} próbach!")
            guess = True
        elif answer == "za duża":
            higher_number = try_guess - 1
        elif answer == "za mała":
            lower_number = try_guess + 1
        else:
            print("Niepoprawna odpowiedź. Użyj 'za duża', 'za mała' lub 'tak'.")

    # Jeżeli komputer nie zgadł po 5 próbach
    if not guess:
        print("Komputer nie zgadł twojej liczby w 5 próbach.")


def play_game():
    play_again = True
    total_games = 0

    while play_again:
        total_games += 1
        print(f"\nGra {total_games} z kolei:")

        # Wywołanie funkcji zgadywania liczby
        guess_the_number()

        # Zapytanie, czy użytkownik chce zagrać ponownie
        play_more = input("\nCzy chcesz zagrać ponownie? (tak/nie): ").lower()
        if play_more != 'tak':
            play_again = False

    # Podsumowanie
    print(f"\nDziękuję za grę! Zagrałeś w sumie {total_games} razy.")
    print("Do zobaczenia!")


# Uruchomienie gry
if __name__ == "__main__":
    play_game()
