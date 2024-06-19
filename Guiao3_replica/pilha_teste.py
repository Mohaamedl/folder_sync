from Stack import Stack

my_instance = Stack()

while True:
    print('Push <value>')
    print('Pop')
    print('Clear')
    print('Size')
    print('Quit')

    my_input = input('What operation would you like to perform ? ').split()

    my_op = my_input[0].strip().lower()
    if my_op == 'push':
        print('>> PUSH')
        my_instance.push(int(my_input[1]))

    elif my_op == 'pop':
        print('>> POP')
        if my_instance.isEmpty():
            print('The stack is empty')
        else:
            print('Value at top of Stack is : ', my_instance.top())
            print('The deleted value is : ', my_instance.pop())
    
    elif my_op == 'size':
        print(f"Stack size = {my_instance.size()}")
    
    
    elif my_op == 'clear':
        print('>> CLEAR ')
        my_instance.clear()
        print("Stack reseted")

    print(my_instance)