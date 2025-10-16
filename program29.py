def modifyStr(str1):
    if str1.endswtich("ing"):
        return str1 + "ly"
    else:
        return str1 + "ing"
str1 = input("Enter a string: ")
result = modifyStr(str1)
print(result)
