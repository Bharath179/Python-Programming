email=input("What's your email? ").strip()
'''if "@" in email:
    print("Valid")
else:
    print("Invalid")'''

'''username,domain=email.split("@")
if username and "." in domain:
    print("Vaild")
else:
    print("Invalid")'''

username,domain=email.split("@")
if username and domain.endswith(".edu"):
    print("Vaild")
else:
    print("Invalid")