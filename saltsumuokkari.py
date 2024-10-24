import random
import csv


#Leet speekit
Leetspeech = {
    'a' : '4',
    'e' : '3',
    'g' : '6',
    'i' : '1',
    'q' : '9',
    's' : '5',
    't' : '7',
    'z' : '2'
}

Spessuchars = list("!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~")

numbers = list("0123456789")


#Muuttaa sanasta alle puolet leet puheeksi
def leetspeek(word):
    word_list = list(word)
    usable_letters = []
    usable_indexes = []
    x = 0

    for x, _ in enumerate(word_list):
        if _ in Leetspeech:
            usable_letters.append(_)
            usable_indexes.append(x)
        else:
            continue
    
    if usable_letters == []:
        return word

    leetspeek_count = random.randint(1, len(usable_letters))

    used_indices = set()

    for _ in range(leetspeek_count):
        temp = random.choice(usable_indexes)
        char = word_list[temp].lower()
        if char in Leetspeech:
            word_list[temp] = Leetspeech[word_list[temp]]
        used_indices.add(temp)
    return ''.join(word_list)

#etsii sanan
def sanakirjaprobe(filu):
    with open(filu, 'r', newline='', encoding='utf-8', errors='replace') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        selected_word = None
        for i, row in enumerate(reader):
            if random.randint(0, i) == 0:
                selected_word = row['Hakusana']
        return selected_word.encode('ascii', 'replace').decode()

#Lisää erikoismerkkejä 1
def erikoismerkkistä(word):
    word_list = list(word)
    
    random_choice = random.choice(Spessuchars)
    word_list.append(random_choice)

    return ''.join(word_list)

#tekee .txt josta löytyy 100 salasanaa
def listanteko():
    sanalistattu = open("100salasanaa.txt", "w")
    for _ in range(100):
        salsu = sanakirjaprobe()
        temp = leetspeek(salsu)
        temp2 = erikoismerkkistä(temp)
        sanalistattu.write(temp2)
        sanalistattu.write("\n")
        print(f"Valmis: {_}")
    print("teksti valmis")

listanteko()

