# Requests a set of words separated by spaces and then prints a queue containing those words.
# Then, it prints each word individually, but only if it contains the letter ‘a’. Implement the queue using the deque library.

from collections import deque

def main():
    user_input = input()
    words = user_input.split()

    words.reverse()

    queue = deque(words)

    print(queue)

    while queue:
        word = queue.pop()

        if 'a' in word.lower():
            print(word)

if __name__ == "__main__":
    main()