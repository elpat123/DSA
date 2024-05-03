# Student no: 21721463

import Graphs as gr

def displayMenu():
    print("\n----------------------------------")
    print('DSA Prac 6: Graphs- Interactive Menu')
    print("------------------------------------")
    print('(a) Add node')
    print('(b) Delete node')
    print('(c) Add edge')
    print('(d) Delete edge')
    print('(e) displayAsList')
    print('(f) displayAsMatrix')
    print('(g) Breadth First Search')
    print('(h) Depth First Search')
    print('(x) Exit')


def add_node():
    nd_flag = True
    while nd_flag:
        try:
            add_nd = int(input('\nKey you want to add: '))
            nd_desc = input('Key description/value: ')
            #bst.insert(add_nd, nd_desc)

            # Add another?
            inp_nd = input('\nDo you want to add another node? (y/n): ')
            while inp_nd != 'y' and inp_nd != 'n':
                print('Wrong input. Please enter (y) or (n) as response.')
                inp_nd = input('\nDo you want to add another node? (y/n): ')
            if inp_nd == 'n':
                print('Returning to Main Menu.')
                nd_flag = False

        except ValueError:
            print('Wrong input. Please enter a numeric response')

        except Exception as e:
            print(e)


def del_node():
    nd_flag = True
    while nd_flag:
        try:
            del_nd = int(input('\nKey you want to delete: '))
            #bst.delete(del_nd)

            # Delete another?
            if bst.height() == -1:
                print('Tree is empty. Returning to Main Menu.')
                nd_flag = False
            else:
                inp_nd = input('\nDo you want to delete another key? (y/n): ')
                while inp_nd != 'y' and inp_nd != 'n':
                    print('Wrong input. Please enter (y) or (n) as response.')
                    inp_nd = input('\nDo you want to delete another key? (y/n): ')
                if inp_nd == 'n':
                    print('Returning to Main Menu.')
                    nd_flag = False

        except ValueError:
            print('Wrong input. Please enter a numeric response!')

        except Exception as e:
            print(e)


if __name__ == '__main__':


    valid = True
    displayMenu()
    choice = input('\nEnter your choice: ')

    while valid:
        if choice == 'a':
            add_node()
        elif choice == 'b':
            del_node()
        elif choice == 'c':
            #add_edge()
            pass
        elif choice == 'd':
            #del_edge()
            pass
        elif choice == 'e':
            #disp_list()
            pass
        elif choice == 'f':
            #disp_matrix()
            pass
        elif choice == 'g':
            #bfs()
            pass
        elif choice == 'h':
            #dfs()
            pass

        elif choice == 'x':
            print('Exiting the program')
            valid = False
        else:
            print('Invalid choice! Please try again.')

        if valid:
            displayMenu()
            choice = input('\nEnter your choice: ')
