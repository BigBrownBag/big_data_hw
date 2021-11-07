import os
import time


class WordCounter:
    def __init__(self):
        self.filename = 'multiplicator-result-10240.txt '
        self.words_dict = dict()

    def get_words(self):
        with open(self.filename) as file:
            for line in file:
                line = line.replace("\n", " ")
                line = line.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace(")", "")
                line = line.replace("(", "").replace("\"", "").replace("[", "").replace("]", "").replace("-", "")
                line = line.replace(">", "").replace("*", "").replace(";", "").replace(":", "").replace("<", "")
                line = line.lower()
                words = line.split()
                words.sort()
                self.get_words_dict(words)

    def get_words_dict(self, words):
        for word in words:
            if word in self.words_dict:
                self.words_dict[word] = self.words_dict[word] + 1
            else:
                self.words_dict[word] = 1

    def main(self):
        if not os.path.exists(self.filename):
            print("Указанный файл не существует")
        else:
            self.get_words()
            with open('words_counter.txt', 'w+') as file:
                for word in self.words_dict:
                    file.write('{} {} \n'.format(word.ljust(50), self.words_dict[word]))


if __name__ == "__main__":
    start_time = time.time()
    newCounter = WordCounter()
    newCounter.main()
    print("--- %s seconds ---" % (time.time() - start_time))
