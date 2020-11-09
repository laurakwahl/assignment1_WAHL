def smallest_common_denominator(val1, val2):       # 2 Zahlen werden miteinander verglichen
    if (val1 == val2):                             # und es wird der kleinste gemeinsame Nenner gesucht
        return val1                                # man erhält dann einen gemeinsamen Nenner
    else:
        new1 = val1
        new2 = val2
        while (new1 != new2):
            if (new1 < new2):
                new1 += val1
            else:
                new2 += val2
        return new1

def biggest_common_counter(val1, val2):            # nach dem ersten Schritt (Aufsuchen eines gemeinsamen Nenners)
    if (val1 < val2):                              # wird der gemeinsame Zähler gesucht, ausgegeben wird der Faktor
        small = val1
        big = val2
    else:
        small = val2
        big = val1
    
    factor = small
    while (factor > 0 and (big % factor != 0 or small % factor != 0)):
        factor -= 1

    return factor

def add_frac(counter1, denominator1, counter2, denominator2): #finale Berechnung der Zahl
    denominator = smallest_common_denominator(denominator1, denominator2)
    counter = ((denominator / denominator1) * counter1) + ((denominator / denominator2) * counter2)

    # Kürzen
    teiler = biggest_common_counter(counter, denominator)
    counter /= teiler
    denominator /= teiler

    counter = int(counter)
    denominator = int(denominator)

    return [counter, denominator]

print(add_frac(1, 2, 3, 4))
print(add_frac(667, 3, 700, 7))
print(add_frac(333, 4035, 677, 12))
