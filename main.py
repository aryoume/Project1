import urllib.request
import os
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

os.system("clear && figlet ARYouMe")
os.system("figlet Comment")

msg = input("Message: ")
token = input("Token: ")
id = input("Id Post: ")
n = 0

def main():
    os.system("clear && figlet Comment")
    print("[1] 10 Comment\n" + "[2] 100 Comment\n" + "[3] 500 Comment")
    main = input("Enter Number: ")
    os.system("clear && figlet Start")
    if main == "1":
        n = 10
    elif main == "2":
        n = 100
    elif main == "3":
        n = 500
    else:
        os.system("clear && figlet Wrong!")
        time.sleep(0.5)
        os.system("python3 main.py")
    flood(n)

def flood(n):
    for i in range(n):
        urllib.request.urlopen(" https://graph.facebook.com/" + id + "/comments?message=" + msg +"&method=post&access_token=" + token)
    print("Done")

if __name__ == "__main__":
    main()
