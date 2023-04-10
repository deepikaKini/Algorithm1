"""
file: decodings.py
CSCI-665: Hw 3 Problem 5 Solution
Authors: Deepika Kini, Adith Shetty
language: python3
"""


def get_input():
    codeword = input()
    return codeword


def main():
    code = get_input()

    count = [0 for _ in range(len(code))]

    count[0] = 1

    for index in range(1, len(code)):
        if code[index] == '0':
            if code[index - 1] == "0":
                count[index] = count[index - 1]
            else:
                if index == 1:
                    count[index] = 2
                else:
                    count[index] = count[index - 1] + count[index - 2]
        else:
            if index > 2 and (code[index - 2:index] == "01" or code[index - 2:index] == "11"):
                count[index] = count[index - 1] + count[index - 3]
            else:
                if index == 1:
                    count[index] = count[index - 1] + (0 if code[index - 1] == '1' else 1)
                else:
                    count[index] = count[index - 1] + count[index - 2]

    print(count[-1])


if __name__ == '__main__':
    main()
