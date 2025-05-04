#this script contains if a user input is palindrome or not

def checkPalindrome(input: str, start: int, end: int):
    if start >= end:
        return True
    if(input[start] != input[end]):
        return False
    return checkPalindrome(input, start=start +1, end= end -1)
    


while True:
    user_input = input("> ")
    if(user_input != ""):
        palindromeFlag = checkPalindrome(user_input, 0, len(user_input)-1)
        if palindromeFlag:
            print(f"{user_input} is palindrome")
        else:
            print(f"{user_input} not palindrome")
    else:
        print("User input is blank")
    if(user_input == "exit"):
        break




