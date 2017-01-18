import fileinput
# import os
import random


def chain(Iterrable_one, iterable_two):

    for i in Iterrable_one:
        yield i
    for y in iterable_two:
        yield y


def compress(iterable, mask):
    for el in range(len(mask)):
        if mask[el] is True:
            yield iterable[el]


def cycle(iterable):
    while True:
        for el in iterable:
            yield el


def book_reader():
    with fileinput.input(files=("001.txt", "002.txt")) as f:
        for line in f:
            if '#' in line:
                input("Press space and enter to continue")
            yield line


def book_generator(chapter_count, word_count):
    word_file = "/usr/share/dict/words"
    WORDS = open(word_file).read().splitlines()

    words_per_chapter = word_count // chapter_count
    chapter_list = []
    chapter_text = ""

    for y in range(chapter_count):
        for i in range(words_per_chapter):
            chapter_text += random.choice(WORDS) + " "
        chapter_list.append(chapter_text)

    with open("book_generator.txt", "w") as output_file:
        for i in range(chapter_count):
            # yield ("Chapter{}\n".format(i + 1))
            yield output_file.write("Chapter{}\n".format(i + 1) + chapter_list[i] + "\n")


def main():
    # print(list(chain(range(0, 4), range(4, 8))))
    # print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
    # endless = cycle(range(0, 10))
    # for item in endless:
    #     print(item)
    for i in book_generator(200, 50000):
        print("Creating chapter")


if __name__ == "__main__":
    main()
