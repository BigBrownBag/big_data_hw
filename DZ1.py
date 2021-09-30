import os
import random


class DataGenerator:
    def __init__(self):
        self.file = 'shagren.txt_Ascii.txt'
        self.result = 'result.txt'
        self.multiplicator_result = 'multiplicator-result.txt'

    def generate(self):
        m = 0
        with open(self.file, 'r') as f:
            lines = f.readlines()
        count = len(lines)
        with open(self.result, 'w+') as file:
            while os.path.getsize(self.result) / (1024 * 1024) < 1:
                try:
                    m += 1
                    random_index = random.randrange(0, count)
                    file.write(lines[random_index])
                except IndexError:
                    print('-')

    def __read_result(self):
        with open(self.result, 'r') as file:
            lines = file.readlines()
        return lines

    def multiplicator(self, w):
        result_lines = self.__read_result()
        with open('multiplicator-result-{}.txt'.format(w), 'w+') as file:
            while os.path.getsize('multiplicator-result-{}.txt'.format(w)) / (1024 * 1024) < w:
                file.writelines(result_lines)


if __name__ == "__main__":
    newFile = DataGenerator()
    newFile.generate()
    w_list = [10, 100, 1 * 1024, 5 * 1024, 10 * 1024]
    for item in w_list:
        newFile.multiplicator(item)

