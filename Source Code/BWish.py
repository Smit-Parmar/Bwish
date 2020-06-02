import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
import re
from bs4 import BeautifulSoup
import requests
import os
import sys
from tkinter import messagebox
import getpass

number=[]
name = []
flag=0
condn = True
condn2 = True
birthday_check=False
condition = True
current_date=datetime.today()
today = current_date.strftime("%d/%m/%y")
reqcond = True
win = ""
string = ""
todate = ""
##search_xpath = ""
##user_xpath = ""
##msg_box_xpath = ""
##send_xpath = ""
counter = 0
driver = ""


while reqcond:
    try:
        print("Trying")
        cont = requests.get("https://www.google.com")
        reqcond = False
        break
    except:
        pass
    

def notify():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("BWish","Thank you for using BWish\nPlease scan the QR code to continue\nIf you already did, ignore.")
def extract_paths():
    file = open("paths.txt","w")
    data = requests.get("https://github.com/Ankit404butfound/BirthdayWisher/blob/master/Element_paths")
    source = data.content
    soup = BeautifulSoup(source, 'html.parser')
    for i in range(3):
        content = soup.find("td",attrs={'id':'LC%s'%str(i+1)})
        content = content.text
        file.write(content+"\n")
    file.close()

def extract_n_check():
    global birthday_check
    with open("Data.txt") as file:
        for details in file:
            current_date=datetime.today()
            date=current_date.strftime("%d/%m")
            if "Today" not in details:
                bd=re.search("Birthdate:(.*) MO",details).group(1)
                #print(bd)
                if bd==date:
                    print(details)
                    name.append(re.search("Name:(.*) Birthdate",details).group(1))
                    #print(i)
                    number.append(re.search("MO:(.*)",details).group(1))
                    birthday_check=True
    if birthday_check:
        notification()
            

def send(message,number,condn):
    #input('Press Enter after scanning QR code/Loading page')
    global condn2, driver, counter, condition, driver, win
    if condn and condition:
        win.destroy()
        pth = os.getcwd()
        options=webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36")
        options.add_argument(r'user-data-dir=C:\Python\Memory\WebWhatsAppBot')
        try:
            driver=webdriver.Chrome(pth+"/chromedriver.exe",options=options)
        except Exception as e:
            print(e)
            file = open("errors.txt","a")
            file.write(str(e)+"\n")
            file.close()
            sys.exit(0)
        driver.get('https://web.whatsapp.com/')
        condition = False
    with open("paths.txt") as file:
        for line in file:
            if "search_xpath" in line:
                line = line.replace("search_xpath = ","")
                search_xpath = line

            elif "user_xpath" in line:
                line = line.replace("user_xpath = ","")
                user_xpath = line
               

            elif "msg_box_xpath" in line:
                line = line.replace("msg_box_xpath = ","")
                msg_box_xpath = line

    while condn2:
      
        try:
            search=driver.find_element_by_xpath(search_xpath)
            search.send_keys(number)
            condn2 = False
            condn = False
        except Exception as e:
            counter += 1
            time.sleep(2)
            print(f"[Retrying] {e}: Count = {counter}")
            driver.get_screenshot_as_file("QRcode.png")
            if counter == 8:
                os.startfile("QRcode.png")
            if counter >= 23:
                extract_paths()
                temp(False)
            if counter >= 35: 
##                root = tk.Tk()
##                root.withdraw()
##                messagebox.showinfo("BWish","Failed to execute, with code 0")
                file = open("errors.txt","a")
                file.write(str(e)+"\n")
                file.close()
                sys.exit(0)
    
    time.sleep(2)
    try:
        user=driver.find_element_by_xpath(user_xpath)
        user.click()
        time.sleep(2)
        msg=message
        msg_box=driver.find_element_by_xpath(msg_box_xpath)
        msg_box.send_keys(msg+"\n")#for sending message in message box
        #driver.find_element_by_xpath(send_xpath).click()
        condn2 = True
        condition = False
    except Exception as e:
        print(f"Phone number not valid or {e}")
        file = open("errors.txt","a")
        file.write(str(e)+"\n")
        file.close()
        pass
    
def notification():
    global win
    flag=1
    win = tk.Tk()
    win.geometry("155x70")
    lnt = len(name)
    if lnt > 1:
        lnt = str(lnt)+" persons'"
    else:
        lnt = str(lnt)+" person's"
    tk.Label(win,text=f"Today is {lnt} birthday\nWould you like to wish?").grid(row=0,column=0)
    but1 = tk.Button(win,text="WISH",command=wish)
    but1.place(x=10,y=40)
    but2 = tk.Button(win,text="Cancel",command=win.quit)
    but2.place(x=90,y=40)
    win.pack_propagate()
    win.mainloop()    
    #Wish birthday
def temp(con = True):
    for i in range(len(name)):
        send("Happy birthday%s"%name[i],number[i],con)
        print("Happy birthday%s"%name[i],number[i],con)
    time.sleep(2)
##    current_date = datetime.today()
##    date = current_date.strftime("%d/%m")
##    file = open("date.txt","w")
##    file.write(date)
##    file.close()
    root = tk.Tk()
    root.withdraw()
    x = messagebox.showinfo("BWish","The message has been sent\nPlease close the console/black window.")
    sys.exit(0)
def wish():
    temp()

try:
    file = open("errors.txt")
    
except:
    file = open("errors.txt","w")
    file.close()
    USER_NAME = getpass.getuser()

    file_path=os.getcwd()
    Drive_name=file_path[:2]
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME  #Add path to startup folder
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write('@echo off\n%s\ncd "%s\nstart BWish.exe' % (Drive_name,file_path))

try:
    with open("paths.txt") as file:
        print(file.read())
        

except Exception as e:
    extract_paths()

try:
    with open("Data.txt","r") as file:
        for line in file:
            if "Today" not in line:
                string = string + line
            else:
                todate = line
                todate = todate.replace("Today:","").strip()
                pass
except:
    
    messagebox.showinfo("BWish","You haven't scheduled any Birthday wish\nOpen BWish.bdays app and add some")
    os.startfile("Bwish_Add_Date.exe")
    sys.exit(0)
#todate = todate.replace(",","")
if today==todate:
    sys.exit(0)
else:
    with open("Data.txt","w") as file:
        file.write("Today:"+today+"\n"+string)
        file.close()
        print(today,todate)


file.close()
extract_n_check()
        










    
