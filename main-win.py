import urllib.request
import urllib.parse
import os
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

os.system("cls && echo ARYouMe")
os.system("echo Comment")

msg = input("Message: ")
token = input("Token: ")
id = input("Id Post: ")

def main():
    os.system("cls && echo Comment")
    print("[1] 10 Comment\n" + "[2] 100 Comment\n" + "[3] 500 Comment")
    main = input("Enter Number: ")
    os.system("cls && echo Start")
    n = 10 if main == "1" else 100 if main == "2" else 500 if main == "3" else 0
    if n == 0:
        os.system("cls && echo Wrong!")
        time.sleep(0.5)
        os.system("python main.py") 
    flood(n)

def flood(n):
    for i in range(n):
        urllib.request.urlopen(" https://graph.facebook.com/" + id + "/comments?message=" + urllib.parse.quote_plus(msg) +"&method=post&access_token=" + token)
    print("Done")

if __name__ == "__main__":
    main()

    
