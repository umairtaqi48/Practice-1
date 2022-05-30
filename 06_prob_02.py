Letter = '''Dear <|Name|>,
Greeting from ABS Coding Company. I am happy to tell you about your selection
You are selected!
Have a grear day ahead 
Thanks and regards,
Umair
Date: <|Date|>
'''
Name=input("Enter your Name\n")
Date=input("Enter Date\n")
Letter = Letter.replace("<|Name|>", Name)
Letter = Letter.replace("<|Date|>", Date)
print(Letter)

