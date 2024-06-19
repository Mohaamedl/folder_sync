from Queue import Queue


def test():
    my_instance = Queue()


    while True:
        print("--- OPTIONS ---")
        print('Add <value>')
        print('Remove')
        print('Size')
        print('Clear')
        print('Quit')
        print("---------------")

        my_input = input('What operation would you like to perform ? ').split()

        my_op = my_input[0].strip().lower()
        if my_op == 'add':
            #print('>> ADD')
            my_instance.add(int(my_input[1]))

        elif my_op == 'remove':
            #print('>> REMOVE')
            if my_instance.isEmpty():
                print('NOT POSSIBLE ! The Queue is empty.')
            else:
                print('1st element in queue  : ', my_instance.first())
                print('Removed from the queue: ', my_instance.remove())
        
        elif my_op == 'clear':
            #print('>> CLEAR ')
            my_instance.clear()
            print("Queue reseted")

        elif my_op == 'size':
            print(f"Queue size = {my_instance.size()}")

        print(my_instance)

if __name__ == "__main__":
    test()