
City = ['new york','DC','maroc']
Value = input("Enter your city")
Inage = int(input("your age"))
if Value in City and Inage >= 18:
    print('you are allowd here')
elif Inage < 18 and Value not in City:
    print("NOT WORKING")
else:
    print("sorry you are not allowd")


