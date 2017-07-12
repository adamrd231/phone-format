
def main():
    # This is the spot where the input from slack should come
    result = input("please enter a telephone number: ")

    #This line is to format the output of numbers correctly
    print(result[:3] + "." + result[3:6] + "." + result[6:])

if __name__ == '__main__':
    main()
