# Requests a set of integers separated by a space and then prints a stack with the numbers. 
# Then, it prints the elements one by one multiplied by two. Implement the stack using the deque library.

from collections import deque

def main():
    user_input = input()
    numbers = map(int, user_input.split())
    
    stack = deque(numbers)

    print(stack)
    
    while stack:
        num = stack.pop()
        print(num * 2)

if __name__ == "__main__":
    main()
