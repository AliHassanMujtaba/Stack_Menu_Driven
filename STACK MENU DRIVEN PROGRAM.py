top_of_stack = -1
max = 10

def options():
    print("1 to Push")
    print("2 to Pop")
    print("3 to Transverse")
    print("4 to Search")
    print("5 Quit")
    x = int(input("Enter your Choice : "))
    return x

def initialize(stack):
    global top_of_stack
    global max
    i = 0
    while i < max:
        stack[i] = " "
        i = i+1
    top_of_stack = -1

def push(new_item,stack):
    global top_of_stack
    global max
    if top_of_stack == max-1:
        print("STACK IS FULL ! ")
    else:
        top_of_stack = top_of_stack+1
        stack[top_of_stack] = new_item
        print("ITEM PUSHED SUCCESSFULLY")

def pop(stack):
    global top_of_stack
    if top_of_stack == -1:
        print("STACK IS ALREADY EMPTY")
    else:
        stack[top_of_stack] = " "
        top_of_stack = top_of_stack-1
        print("ITEM SUCCESSFULLY POPPED")

def transverse(stack):
    global top_of_stack
    i = top_of_stack
    while i >= 0:
        print(stack[i])
        i = i - 1

def search(search_item,stack):
    global top_of_stack
    i = 0
    while i <= top_of_stack:
        if stack[i] == search_item:
            return i
        i = i + 1
    return -1

def main():
    global top_of_stack
    global max
    stack = [" "] * max
    initialize(stack)
    choice = 0
    while choice != 5:
        choice = options()
        if choice == 1:
            new_item = input("Enter Character : ")
            push(new_item,stack)

        elif choice == 2:
            pop(stack)

        elif choice == 3:
            transverse(stack)

        elif choice == 4:
            search_item = input("Enter character you want to search : ")
            index = search(search_item,stack)
            if index == -1:
                print("CHARACTER NOT FOUND IN STACK ")
            else:
                print("ITEM FOUND AT INDEX ",index)

        elif choice == 5:
            print("GOOD BYE ! ")

        else:
            print("Invalid Input Try Again ! ")

main()