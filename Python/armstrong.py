def is_armstrong_number(number):
    # Convertir le nombre en chaîne pour faciliter l'itération
    str_number = str(number)
    num_digits = len(str_number)

    # Initialiser la somme
    sum = 0

    # Itérer sur chaque chiffre
    for digit in str_number:
        # Convertir le chiffre en nombre et l'élever à la puissance du nombre total de chiffres
        sum += int(digit) ** num_digits

    # Si la somme est égale au nombre original, alors c'est un nombre d'Armstrong
    return sum == number
