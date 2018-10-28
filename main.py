import urllib.request
import urllib.parse
import os
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def clear_screen():
    os.system(['clear','cls'][os.name == 'nt'])

clear_screen()
os.system("echo OS: " + ['Linux','Windows'][os.name == 'nt'])
os.system("echo -------------------------------------------------")
os.system("echo Facebook Flood Comment by ARYouMe")
os.system("echo https://github.com/aryoume/Project1")
os.system("echo Thai and Space Fix" + ['',' + Windows Patch'][os.name == 'nt'] + " by Demza")
os.system("echo -------------------------------------------------")

msg = input("Message: ")
token = input("Token: ")
id = input("ID Post: ")

def reload():
    main()

def main():
    clear_screen()
    os.system("echo How much you want to flood?")
    print("[1] 10 Comment\n" + "[2] 100 Comment\n" + "[3] 500 Comment")
    main = input("Enter Number: ")
    n = 10 if main == "1" else 100 if main == "2" else 500 if main == "3" else 0
    if n == 0:
        clear_screen()
        reload()
    flood(n)

def flood(n):
    clear_screen()
    os.system("echo Start")
    for i in range(n):
        rq = urllib.request.urlopen("https://graph.facebook.com/" + urllib.parse.quote_plus(id) + "/comments?message=" + urllib.parse.quote_plus(msg) +"&method=post&access_token=" + urllib.parse.quote_plus(token))
        if rq.getcode() == 200:
            print(str(i+1) + " SUCCESS");
        else:
            print(str(i+1) + " ERROR [" + rq.getcode() + "]");
    print("Job Done.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass