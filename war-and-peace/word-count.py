#!/usr/bin/python3
import time


def blocks(files, size=65536):
    while True:
        b = files.read(size)
        if not b:
            break
        yield len(b.split())


def word_count_by_blocks():
    start_time = time.time()
    with open('book-war-and-peace.txt', 'r', encoding="utf-8", errors='ignore') as wap_file:
        word_count = sum(bl for bl in blocks(wap_file))
    print(f'\n\tBLOCKS\n1. Total Time: {time.time() - start_time:.3f}\n2. Word Count: {word_count}')
    # 1. Total Time: 20.831
    # 2. Word Count: 190290198


def word_count_by_loop():
    start_time = time.time()
    with open('book-war-and-peace.txt', 'r', encoding="utf-8", errors='ignore') as wap_file:
        word_count = 0
        for line in wap_file:
            word_count += len(line.split())
    print(f'\n\tLOOP\n1. Total Time: {time.time() - start_time:.3f}\n2. Word Count: {word_count}')
    # 1. Total Time: 28.728
    # 2. Word Count: 190279488


if __name__ == "__main__":
    word_count_by_blocks()
    # word_count_by_loop()
