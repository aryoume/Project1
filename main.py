import urllib.request
import os
import time

os.system("clear && figlet ARYouMe")
os.system("figlet Comment")

msg = input("Message: ")
token = input("Token: ")
id = input("Id Post: ")
def main():
   os.system("clear && figlet Comment")
   print("[1] 10 Comment")
   print("[2] 100 Comment")
   print("[3] 500 Comment")
   print(" ")
   main = input("Enter Number: ")
   if main == "1":
      os.system("clear && figlet Start")
      one()
   elif main == "2":
      os.system("clear && figlet Start")
      two()
   elif main == "3":
      os.system("clear && figlet Start")
      three()
   else:
      os.system("clear && figlet Wrong!")
      time.sleep(0.5)
      os.system("python3 main.py")
def one():
   i = 1
   while i <= 10:
    urllib.request.urlopen(" https://graph.facebook.com/" + id + "/comments?message=" + msg +"&method=post&access_token=" + token)
    print("Done")
    i = i + 1
def two():
   i = 1
   while i <= 100:
    urllib.request.urlopen(" https://graph.facebook.com/" + id + "/comments?message=" + msg +"&method=post&access_token=" + token)
    print("Done")
    i = i + 1
def three():
   i = 1
   while i <= 500:
    urllib.request.urlopen(" https://graph.facebook.com/" + id + "/comments?message=" + msg +"&method=post&access_token=" + token)
    print("Done")
    i = i + 1
main()
