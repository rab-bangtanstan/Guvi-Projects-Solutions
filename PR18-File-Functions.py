file_name2 = input('Enter the file name:')
def mine_pro(choice):

    if (os.path.exists(file_name2)):
        print("the file exist ")
    else:
        print("the file doesn't exist")

    if choice == 1:

        with open(file_name2, 'r') as f:
            content = f.read()
            print(content)
            print("your file is opened in read mode")

    elif choice == 2:

        with open(file_name2, 'w') as f:
            user_data = input('Enter any sentences:')
            f.write(user_data)
            print("your file is opened in write mode")

    elif choice == 3:

        with open(file_name2, 'a') as f:
            user_data = input('Enter any sentences:')
            f.write(user_data)
            print("your file is opened in append mode")

    else:
        print('Invalid choice')



choice = int(input('Enter a choice \n(press 1: read, press 2 : write, press 3 : append)'))

mine_pro(choice)
