# 1. import library
from spellchecker import SpellChecker


class SpellCheckerApp:
    def __init__(self):  # Fixed typo here
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []  # Un-commented this list to store corrected words

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f"Correcting '{word}' to '{corrected_word}' ")
            else:
                print(f"'{word}' is spelled correctly.")
            corrected_words.append(corrected_word)

        return ' '.join(corrected_words)

    def run(self):
        print("\n---Spell Checker---")

        while True:
            text = input('Enter text to check or type "exit" to quit: ')

            if text.lower() == 'exit':
                print('Closing the program.')
                break

            corrected_text = self.correct_text(text)
            print(f'Corrected Text: {corrected_text}')


if __name__ == "__main__":
    SpellCheckerApp().run()
