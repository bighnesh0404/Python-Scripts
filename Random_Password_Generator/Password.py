import random

LOWERCASE_CHARS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z')
UPPERCASE_CHARS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z')
DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
SPECIALS = ('@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<')

SEQUENCE = (LOWERCASE_CHARS,
            UPPERCASE_CHARS,
            DIGITS,
            SPECIALS,
            )

def generate_random_password(total, sequences):
    r = _generate_random_number_for_each_sequence(total, len(sequences))

    password = []
    for (population, k) in zip(sequences, r):
        n = 0
        while n < k:
            position = random.randint(0, len(population)-1)
            password += population[position]
            n += 1
    random.shuffle(password)
    
    while _is_repeating(password):
        random.shuffle(password)
        
    return ''.join(password)

def _generate_random_number_for_each_sequence(total, sequence_number):
    current_total = 0
    r = []
    for n in range(sequence_number-1, 0, -1):
        current = random.randint(1, total - current_total - n)
        current_total += current
        r.append(current)
    r.append(total - sum(r))
    random.shuffle(r)

    return r

def _is_repeating(password):
    n = 1
    while n < len(password):
        if password[n] == password[n-1]:
            return True
        n += 1
    return False

# if __name__ == '__main__':
a = int(input("Minimum length: "))
b = int(input("Maximum length: "))
print (generate_random_password(random.randint(a, b), SEQUENCE))
