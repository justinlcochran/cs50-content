

def main():
    bottom_text = input("Enter your meme text: ")
    print(memify(bottom_text))

def memify(input_str):
    modified_str = ''
    for i in range(len(input_str)):
        if input_str[i] != ' ':
            if i % 2 == 0:
                modified_str += input_str[i].lower()
            else:
                modified_str += input_str[i].upper()
        else:
            modified_str += ' '
    return modified_str


if __name__ == "__main__":
    main()