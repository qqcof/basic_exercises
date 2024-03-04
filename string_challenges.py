# Вывести последнюю букву в слове
word = 'Архангельск'
last_letter = word[-1]
print(last_letter)

# Вывести количество букв "а" в слове
word = 'Архангельск'
count_a = word.lower().count('а')
print(count_a)

# Вывести количество гласных букв в слове
word = 'Архангельск'
word_lower = word.lower()

letters = list(word_lower)

count_vowels = 0
for letter in letters:
    if letter in 'аеёиоуыэюя':
        count_vowels +=1

print(count_vowels)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
word_count = len(words)
print(word_count)

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()

for word in words:
    print(word[0])
    
# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()

total_chrs = sum(len(word) for word in words)
num_words = len(words)
average_length = total_chrs / num_words

print('Средняя длина слова в предложении:', average_length)


