sentence = "Це приклад речення для аналізу"
# Розбиваємо речення на слова
words = sentence.split()
# Знаходимо найкоротше слово
min_word_length = min(len(word) for word in words)
print("Довжина найкоротшого слова:", min_word_length)