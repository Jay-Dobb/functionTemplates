import gspread
from oauth2client.service_account import ServiceAccountCredentials

def integrate(idno,name,email,phone,created_on,updated_on):

    scope=   ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    credentials=ServiceAccountCredentials.from_json_keyfile_name('mycredentials.json',scope)
    gc=gspread.authorize(credentials)
    wks=gc.open('Sele').sheet1
    try:
        wks.append_row([idno,name,email,phone,created_on,updated_on])
        #[idno,name,email,phone,created_on,updated_on] google sheet field    #names.
        print("Inserted Successfully !")
    except:
        print("Error Occurred")
    return

#Getting Input from user
idno=int(input("Date"))
name=input("Location")
email=input("Title")
phone=int(input("Description (comment)"))
created_on=str(input("Location"))
updated_on=str(input("Updated on:"))

#Function Call
integrate(idno,name,email,phone,created_on,updated_on)

