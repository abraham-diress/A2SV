

# we initiate a list
# we accept the number of commmands we are gonna accept from the user
# we loop until the number of commands
# we accept the commands and split them and store them in a list
# we store the first element of the list in another variable
# we store the remaining elements in another variable
# we check if the command is not print
# if not we join the remaining elements other than the command by " ," and use eval with the command
# print the list

if __name__ == '__main__':
    N = int(input())
    list1  = []

    for _ in range(N):
        input1 = input().split()    #list1.command(arguements) "("+ ",".join(args) +")"
        command = input1[0]
        arguments = input1[1:]

        if command != "print":
            arguments = "("+ ",".join(arguments) +")"
            stmt = command+arguments
            eval("list1."+stmt)
        else:
            print(list1)
