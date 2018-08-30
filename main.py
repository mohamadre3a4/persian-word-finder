def createDictionary(file_name):
    words = []
    word_list_file = open(file_name)
    for word in word_list_file:
        words.append(word)
    word_list_file.close()
    return words


def main():
    words = createDictionary('words.txt')
    n = int(input('how many letters do you have? '))
    print('write each of them and enter')

    all_letters = []
    for i in range(n):
        all_letters.append(input())
    print(all_letters)
    letter_number = input('how many letters does your word have?(you can seperate them with "," ')
    letter_number = letter_number.split(',')
    m = []
    for number in letter_number:
        m.append(int(number))
    candidate_words = []

    for word in words:
        word = word.strip()
        if len(word) in m:
            status = True
            for letter in word:
                if word.count(letter) > 1:
                    status = False
                if letter not in all_letters:
                    status = False
            if status == True:
                candidate_words.append(word)


    for word in candidate_words:
        print(word)

main()