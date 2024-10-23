print("Bilz Login System")
def login():
    while True:
        name =input("what is your username: ").strip()
        password = input("what is your password: ").strip()
        if name == "bilz" and password == "bilz060196":
            print("Welcome to your profile")
            break
        else:
            print("whoops! I dont recognize thas username or password, please try again")
login()