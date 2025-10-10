
def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    
    parenthesis = False
    for ch in my_string:
        if ch in "()[]":
            parenthesis = True
            break
    if parenthesis == False:
        return True

    n0 = 0
    n1 = -1
    while my_string[n0] not in "()[]":
        n0 += 1
    while my_string[n1] not in "()[]":
        n1 -= 1

    if not (my_string[n0] == '(' and my_string[n1] == ')'):
        if not (my_string[n0] == '[' and my_string[n1] == ']'):
            return False

    # remove first and last character
    return balanced_brackets(my_string[n0+1:n1])


def main():
    ok = balanced_brackets("(((())))")
    print(ok)

    # there is one closing bracket too many, so this produces False
    ok = balanced_brackets("()())")
    print(ok)

    # this one starts with a closing bracket, False again
    ok = balanced_brackets(")()")
    print(ok)

    # this produces False because the function only handles entirely nested brackets
    ok = balanced_brackets("()(())")
    print(ok)


    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)

    ok = balanced_brackets("()")
    #rint(ok)
    
    ok = balanced_brackets("((x)")
    print(ok)
    
    ok = balanced_brackets("x[[]")
    print(ok)

if __name__ == "__main__":
    main()

