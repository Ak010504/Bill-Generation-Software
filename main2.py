import tkinter
from tkinter import Button, Label, ttk, Entry
import time
import datetime
from time import strftime 
import csv
from PIL import Image,ImageTk
import pandas as pd
from datetime import date
import numpy as np
import itertools

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text="Time: " + string)
    lbl.after(1000, time)

def closed():
    label = Label(window, text="Thank you", font='Verdana 12')
    label.place(x=735, y=800)
    window.after(2000, window.destroy)
      
def closed1():
    label = Label(window1, text="Thank you", font='Verdana 12')
    label.place(x=735, y=800)
    window1.after(2000, window1.destroy) 
    
def closed2():
    label = Label(window2, text="Thank you", font='Verdana 12')
    label.place(x=735, y=800)
    window2.after(2000, window2.destroy) 
    
def closed4():
    label = Label(window3, text="Thank you", font='Verdana 12')
    label.place(x=735, y=800)
    window3.after(2000, window3.destroy)    
    
def closed5():
    label = Label(window4, text="Thank you", font='Verdana 12')
    label.place(x=735, y=800)
    window4.after(2000, window4.destroy)
    
def closed6():
    label = Label(window5, text="Thank you", font='Verdana 12')
    label.place(x=735, y=800)
    window5.after(2000, window5.destroy)
    
def closed7():
    label = Label(window7, text="Thank you", font='Verdana 12')
    label.place(x=735, y=800)
    window7.after(2000, window7.destroy)
    
def closed8():
    label = Label(window5, text="Thank you", font='Verdana 12')
    label.place(x=735, y=800)
    window5.after(2000, window5.destroy)
def closed9():
    label = Label(window15, text="Thank you", font='Verdana 12')
    label.place(x=735, y=800)
    window15.after(2000, window15.destroy)
def closed10():
    label = Label(window16, text="Thank you", font='Verdana 12')
    label.place(x=735, y=800)
    window16.after(2000, window16.destroy)
    
def closed11():
    label = Label(window15, text="Thank you", font='Verdana 12')
    label.place(x=735, y=800)
    window15.after(2000, window15.destroy)
    
def closed12():
    label = Label(window16, text="Thank you", font='Verdana 12')
    label.place(x=735, y=800)
    window16.after(2000, window16.destroy)
    
    
def back():
    window1.destroy()
    main()
def back9():
    window16.destroy()
    main()
def back8():
    window15.destroy()
    main()

def back7():
    window5.destroy()
    article()
    
def back1():
    window2.destroy()
    comp_det()
    
def back2():
    window3.destroy()
    comp_det()

def back3():
    window5.destroy()
    article()
    
def back4():
    window7.destroy()
    comp_det()
    
def back5():
    window4.destroy()
    advance()

def back10():
    window15.destroy()
    advance()    

def back11():
    window16.destroy()
    attendance()  
    
def main_next():
    window.destroy()
    comp_det()
    
def comp_next():
    window1.destroy()
    advance()
    
def comp_next1():
    window1.destroy()
    article()
    
def entry():
    advance_val = txt.get()
    bank_chosen = combo.get()

# Read the CSV file
    df = pd.read_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv", index_col=0)

# Get today's date
    today = date.today()
    

# Check if today's date column exists, if not, create it
    if str(today) not in df.columns:
        df[str(today)] = ""

# Check if the bank_chosen row exists, if not, create it
    if bank_chosen not in df.index:
        df.loc[bank_chosen] = ""

# Set the advance_val for the bank_chosen and today's date
    df.at[bank_chosen, str(today)] = advance_val

# Write the DataFrame back to the CSV file
    df.to_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv")
    
def bill(bank_cho):
    
    df2 = pd.read_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv")
# Replace 0 with NaN (or another null representation)
    df2.replace(0, np.nan, inplace=True)

# Save the modified DataFrame back to a CSV file
    df2.to_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv", index=False)
    data = [
    ["DEPARTMENT OF POSTS, INDIA"],
    ["Business Post Centre, Anna Road, Chennai-600 002."],
    ["GST:33AAAGH0873D1ZV", "PAN:AAAGH0873D"],
    ["TO", "Claim Bill No: A/640/01-24"],
    ["The Manager", "Dated:08.01.2024"],
    ["CAMS (HSBC) Mutual Fund", "Chennai 600 002"],
    ["GST NO: 33AAACC3035G1ZA", ""],
    ["PAN:", "AAACC3035G"],
    ["BILL FOR THE MONTH OF : DEC-23", ""],
    ["DETAILS", "Count", "Amount"],
    ["Ordinary Articles Posted <10gm:", "0", "0"],
    ["Ordinary Articles Posted >10gm:", "0", "0"],
    ["Registered Articles Posted <10gm:", "0", "0"],
    ["Registered Articles Posted >10gm:", "0", "0"],
    ["Speed Articles Posted <10gm:", "0", "0"],
    ["Speed Articles Posted <10gm:", "0", "0"],
    ["TOTAL NO: OF ARTICLES", "0", "0"],
    ["Opening Balance vide Bill/Invoice No:A/606/12-23", "",  "0"],
    ["Total amount @ credit", "", "0"],
    ["Postage (Ord+Reg+Speed)", "", "0"],
    ["CGST @ 9%(As per Annexure)", "", "0"],
    ["SGST @ 9%(As per Annexure)", "", "0"],
    ["Service Charge (Fkg, Spl Handling, Processing - As per Annexure)", "", "0"],
    ["CGST @ 9% for Service charge", "", "0"],
    ["SGST @ 9% for Service charge", "", "0"],
    ["TOTAL", "", "0"],
    ["R/O TOTAL", "", "0"],
    ["CLOSING BALANCE ( A-B)", "", "0"],
    ["Terms & Conditions:", ""],
    ["1. Sufficient advance amount should be paid to pick up/process your mails without break.", ""],
    ["2. Kindly issue Cheques/DD for the above amount in favour of 'The Chief Postmaster Anna Road HPO,", ""],
    ["   Chennai-2' and forward the same  to Business Post Centre, Anna Road, Chennai-600 002.", ""],
    ["3. Advance payment may be made by ECS/NEFT with relevant details to the", ""],
    ["   e-mail id: cs.aspbpc@gmail.com & bpcannaroad@indiapost.gov.in", ""],
    ["4. No mails will be accepted without sufficient balance.", ""],
    ["* E&OE", ""],
    ["ACCOUNTANT", "HSA"],
    ["BPC Anna Road", "BPC Anna Road"],
    ["Chennai-600002", "Chennai-600002"]
    ]
    with open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\comp.csv", mode='r') as f:
        wr = csv.reader(f, delimiter=',')
        n = sum(1 for _ in wr)  # Count the number of rows
    f= open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\comp.csv", mode='r')
    wr = csv.reader(f, delimiter=',')
    for i, row in enumerate(wr, 1):
        if i != 1 and row[0] == bank_cho:  # Skip header row
            data[6][0] = "GST:" + row[4]
            data[7][1] = row[5]
            data[4][1] = "Date:" + datetime.datetime.today().strftime('%d/%m/%Y')
            data[8][0] = "BILL FOR THE MONTH OF : " + datetime.datetime.now().strftime('%b-%Y')

            break
    data[5][0] = bank_cho
    f1 = open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\bank.csv", mode='r')
    f2 = open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv", mode = 'r+')
    wr2 = csv.reader(f2)
    wr1 = csv.reader(f1)
    adv2=0.0
    k=0
    csv_data = list(wr2)
    for a1 in csv_data:
        if a1[0] == bank_cho:
            # Found the matching row
            data[17][2] = a1[1]  # Update the label as per your requirement
            k = len(a1) - 2  # Based on your code, but ensure this logic matches your need
            
            
            # Iterate through the relevant columns
            for j in range(2, len(a1)):
                if a1[j] and a1[j]!=0:  # This checks if the cell is not empty
                    # Your specific label might need updating or handling dynamically
                    advance_string = f"Advance received vide CHQ/NEFT DT:{csv_data[0][j]}"
                    data.insert(18, [advance_string, "", a1[j]])
                    adv2 += float(a1[j])  # Sum up the values, assuming they're convertible to float

    k=len(data)-39
    data[18+k][2] = adv2 + float(data[17][2])
    service = 0.0
    st=0.0
    for row in wr1:
        if len(row) >17:
            if row[4] == bank_cho:
                if row[17] == 'yes':
                    if row[3] == 'ord':
                        data[10][1] = float(data[10][1]) + float(row[5])
                        data[10][2] = float(data[10][2]) + float(row[10])
                    if row[3] == 'reg':
                        data[12][1] = float(data[12][1]) + float(row[5])
                        data[12][2] = float(data[12][2]) + float(row[10])
                    if row[3] == 'speed':
                        data[14][1]=  float(data[14][1]) + float(row[5])
                        data[14][2] = float(data[14][2]) + float(row[10])
                if row[17] == 'no':
                    if row[3] == 'ord':
                        data[11][1] = float(data[11][1]) + float(row[5])
                        data[11][2] = float(data[11][2]) + float(row[10])
                    if row[3] == 'reg':
                        data[13][1] = float(data[13][1]) + float(row[5])
                        data[13][2] = float(data[13][2]) + float(row[10])
                    if row[3] == 'speed':
                        data[15][1]=  float(data[15][1]) + float(row[5])
                        data[15][2] = float(data[15][2]) + float(row[10])
                if (row[17] == 'no'):
                    service = float(service) + float(row[15])
                
                st = float(st)+float(row[11])
                data[22+k][2] = float(data[22+k][2]) + float(row[15])
    data[16][1] = float(data[10][1]) + float(data[11][1]) + float(data[12][1]) + float(data[13][1]) + float(data[14][1]) + float(data[15][1])
    data[16][2] = float(data[10][2]) + float(data[11][2]) + float(data[12][2]) + float(data[13][2]) + float(data[14][2]) + float(data[15][2])
    data[23+k][2] = service*0.09
    data[24+k][2] = service*0.09
    data[19+k][2] = data[16][2]
    
    if (float(data[19+k][2]) *0.18 > st):
        data[20+k][2] = float(data[19+k][2]) * 0.18*0.5
        data[21+k][2] = float(data[19+k][2]) * 0.18*0.5
    else:
        data[20+k][2] = st*0.5
        data[21+k][2] = st*0.5
    data[25+k][2] = float(data[19+k][2]) + float(data[20+k][2]) +float(data[21+k][2]) +float(data[22+k][2]) +float(data[23+k][2]) +float(data[24+k][2])
    data[26+k][2] = round(data[25+k][2])
    data[27+k][2] = float(data[18+k][2]) - float(data[26+k][2])  
    closing=data[27+k][2]
    f3 = open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv", mode = 'r+')
    wr3 = csv.reader(f3)
    ww3=csv.writer(f3)
    l17=[]

    for a in wr3:
        if(a[0]==bank_cho):
            reader1= itertools.tee(csv.reader(f3))
            columns = len(next(reader1))
            l17.append(a[0])
            l17.append(closing)
            for i in range(2,columns):
                l17.append(0)
    rows = []
    with open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv", 'r', newline='') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if row[0] != bank_cho:
                rows.append(row)
        rows.append(l17)

    with open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)



            




    # Writing data to a CSV file
    with open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\post_details_ %s .csv"%(bank_cho), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("CSV file created successfully.")

def comp_next2():
    window1.destroy()
    company()
    
def daily():
    balance=0
    bank_cho = combo101.get()
    window7.destroy()
    f = open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv", mode="r")
    wr = csv.reader(f, delimiter=',')
    for a in wr:
        if a[0]==bank_cho:
            balance = a[1]
# Read the CSV file
    df = pd.read_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\dailybalance.csv", index_col=0)

# Get today's date
    today = date.today()
    
# Check if today's date column exists, if not, create it
    if str(today) not in df.columns:
        df[str(today)] = ""

# Check if the bank_chosen row exists, if not, create it
    if bank_cho not in df.index:
        df.loc[bank_cho] = ""

# Set the advance_val for the bank_chosen and today's date
    df.at[bank_cho, str(today)] = balance

# Write the DataFrame back to the CSV file
    df.to_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\dailybalance %s.csv"%{bank_cho})
def company_daily():
    global window7, label, lbl, l1, combo1, combo2, combo3, txt2, txt3, txt4, txt1, combo100 , combo101   
    window7 = tkinter.Tk()
    window7.attributes('-fullscreen', True)
    window7.title("Article details")
    window7['background'] = '#add8e6'
    l96= Label(window7, text="select the company for the bill", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l96.place(x=20, y=320)
    My_label = tkinter.Label(window7, text="Bill Generation!", font="verdana 20", bg='#add8e6', fg="#123499", padx=70, pady=30)
    My_label.place(x=450, y=40)
    combo101=ttk.Combobox(window7, width=25, height=4)
    f = open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\comp.csv", mode="r")
    wr = csv.reader(f, delimiter=',')

    count = 0
    bank_name = []

    for a in wr:  # Check if the count is even (alternate lines)
        if len(a) > 1:  # Ensure 'a' has at least two elements
            for i in bank_name:
                if a[1] == i:
                    count += 1
                    break
            else:
                bank_name.append(a[0])
    count += 1

    bank_tuple = tuple(bank_name)
    combo101['values']=bank_tuple
    combo101.place(x=500,y=350)
    bb = Button(window7, text="Exit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=closed7)
    bb.place(x=800, y=700)
    bw= Button(window7, text="back", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=back4)
    bw.place(x=800, y=800)
    bv = Button(window7, text="submit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=daily)
    bv.place(x=1000, y=700)
    
def comp_det():
    global window1, label, lbl
    window1 = tkinter.Tk()
    window1.attributes('-fullscreen', True)
    window1.title("Indian Postal Service Bill Calculation")
    window1['background'] = '#add8e6'

    bt = Button(window1, text="Advance Details", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=comp_next)
    bt.place(x=400, y=400)
    
    br = Button(window1, text="Article Details", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=comp_next1)
    br.place(x=900, y=400)
    
    bh = Button(window1, text="Bill Generation", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=comp_next2)
    bh.place(x=400, y=250)
    
    bl = Button(window1, text="Daily Balance Generation", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=company_daily)
    bl.place(x=900, y=250)

    bq = Button(window1, text="Exit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=closed1)
    bq.place(x=700, y=700)

    bq = Button(window1, text="Back", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=back)
    bq.place(x=700, y=550)
    
    image = Image.open("D:\Amrit\College\SSN\CS\Post\logo.png")
    resize_image = image.resize((300, 300))
    img = ImageTk.PhotoImage(resize_image)
    label1 = Label(window1, image=img, bg="#add8e6")
    label1.image = img
    
    label1.place(x=20, y=20)

    image2 = Image.open("D:\Amrit\College\SSN\CS\Post\india-post.png")
    resize_image = image2.resize((300, 200))
    img2 = ImageTk.PhotoImage(resize_image)
    label2 = Label(window1, image=img2, bg="#add8e6")
    label2.image = img2
    label2.place(x=1200, y=600)
    
    My_label = tkinter.Label(window1, text="Company Details!", font="verdana 20", bg='#add8e6', fg="#123499", padx=70, pady=30)
    My_label.place(x=450, y=40)
    
    lbl = Label(window1, font=('calibri', 20, 'bold'),
            background='#add8e6',
            foreground='#123499')
    
    date=datetime.datetime.now()
    label = Label(window1, text=f"{date:%A, %B %d, %Y}", font=('calibri', 20, 'bold'), bg="#add8e6", fg="#123499")
    label.place(x=1225,y=50)
    
    lbl.pack(anchor='ne', text=time())
    window1.mainloop()

def adv_next():
    window2.destroy()
    add_comp()

def company_next():
    bank_cho = combo100.get()
    window7.destroy()
    bill(bank_cho)
def company():
    global window7, label, lbl, l1, combo1, combo2, combo3, txt2, txt3, txt4, txt1, combo100    
    window7 = tkinter.Tk()
    window7.attributes('-fullscreen', True)
    window7.title("Article details")
    window7['background'] = '#add8e6'
    l96= Label(window7, text="select the company for the bill", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l96.place(x=20, y=320)
    My_label = tkinter.Label(window7, text="Bill Generation!", font="verdana 20", bg='#add8e6', fg="#123499", padx=70, pady=30)
    My_label.place(x=450, y=40)
    combo100=ttk.Combobox(window7, width=25, height=4)
    f = open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\comp.csv", mode="r")
    wr = csv.reader(f, delimiter=',')

    count = 0
    bank_name = []

    for a in wr:  # Check if the count is even (alternate lines)
        if len(a) > 1:  # Ensure 'a' has at least two elements
            for i in bank_name:
                if a[1] == i:
                    count += 1
                    break
            else:
                bank_name.append(a[0])
    count += 1

    bank_tuple = tuple(bank_name)
    combo100['values']=bank_tuple
    combo100.place(x=500,y=350)
    bb = Button(window7, text="Exit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=closed7)
    bb.place(x=800, y=700)
    bw= Button(window7, text="back", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=back4)
    bw.place(x=800, y=800)
    bv = Button(window7, text="submit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=company_next)
    bv.place(x=1000, y=700)
    
    
def advance():
    global window2, label, lbl, txt, l1, combo
    window2 = tkinter.Tk()
    window2.attributes('-fullscreen', True)
    window2.title("Indian Postal Service Bill Calculation")
    window2['background'] = '#add8e6'

    bt = Button(window2, text="Add new Company", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=adv_next)
    bt.place(x=500, y=700)
    
    br = Button(window2, text="Submit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=entry)
    br.place(x=500, y=550)

    bq = Button(window2, text="Exit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=closed2)
    bq.place(x=900, y=700)

    bq = Button(window2, text="Back", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=back1)
    bq.place(x=900, y=550)
    
    My_label = tkinter.Label(window2, text="Advance Details!", font="verdana 20", bg='#add8e6', fg="#123499", padx=70, pady=30)
    My_label.place(x=550, y=40)
    
    lbl = Label(window2, font=('calibri', 20, 'bold'),
            background='#add8e6',
            foreground='#123499')
    
    image = Image.open("D:\Amrit\College\SSN\CS\Post\logo.png")
    resize_image = image.resize((300, 300))
    img = ImageTk.PhotoImage(resize_image)
    label1 = Label(window2, image=img, bg="#add8e6")
    label1.image = img
    
    label1.place(x=20, y=20)

    
    image2 = Image.open("D:\Amrit\College\SSN\CS\Post\india-post.png")
    resize_image = image2.resize((300, 200))
    img2 = ImageTk.PhotoImage(resize_image)
    label2 = Label(window2, image=img2, bg="#add8e6")
    label2.image = img2
    label2.place(x=1200, y=600)
    
    l53 = Label(window2, text="Enter the company details", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l53.place(x=440, y=400)
    date=datetime.datetime.now()
    label = Label(window2, text=f"{date:%A, %B %d, %Y}", font=('calibri', 20, 'bold'), bg="#add8e6", fg="#123499")
    label.place(x=1225,y=40)
    l1 = Label(window2, text="Enter the advance amount", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l1.place(x=840, y=325)
    lbl.pack(anchor='ne', text=time())
    combo=ttk.Combobox(window2, width=25, height=4)

# Open the CSV file for reading

# Open the CSV file for reading
    f = open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\comp.csv", mode="r")
    wr = csv.reader(f, delimiter=',')

    count = 0
    bank_name = []

    for a in wr:  # Check if the count is even (alternate lines)
        if len(a) > 1:  # Ensure 'a' has at least two elements
            for i in bank_name:
                if a[1] == i:
                    count += 1
                    break
            else:
                bank_name.append(a[0])
    count += 1

    bank_tuple = tuple(bank_name)
    combo['values']=bank_tuple
    combo.place(x=500,y=400)
    txt=Entry(window2,width=20)
    txt.place(x=900,y=400)
    f.close()
    window2.mainloop()

def add_save():
    dc = txt19.get()
    comp = txt20.get()
    phone = txt21.get()
    add = txt22.get()
    gst = txt23.get()
    pan = txt24.get()
    bal = txt25.get()
    f=open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\comp.csv", mode='a')
    l2=[dc, comp, add, phone, gst, pan]
    ww = csv.writer(f)
    ww.writerow(l2)
    f.close()
    df = pd.read_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv")
    l = [dc, bal]
    col = df.shape[1]
    row = df.shape[0]
    for i in range(2, col):
        l.append(0)
    df.loc[row] = l
    df.to_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv", index = False)
    

# Open the CSV file for reading
    with open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\comp.csv", mode="r", newline='') as file:
        # Create a CSV reader
        reader = csv.reader(file)

        # Read all rows and filter out the empty ones
        non_empty_rows = [row for row in reader if any(cell.strip() for cell in row)]

    # Open the same CSV file again, but this time in write mode
    with open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\comp.csv", mode="w", newline='') as file:
        # Create a CSV writer
        writer = csv.writer(file)

        # Write the non-empty rows back to the file
        writer.writerows(non_empty_rows)

    print("Empty rows deleted successfully.")
    
def add_comp():
    
    global window4, label, lbl, txt20, txt21, txt22, txt23, txt24, txt19, l99, txt25
    window4 = tkinter.Tk()
    window4.attributes('-fullscreen', True)
    window4.title("Indian Postal Service Bill Calculation")
    window4['background'] = '#add8e6'

    bt = Button(window4, text="Submit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=add_save)
    bt.place(x=750, y=700)

    bq = Button(window4, text="Exit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=closed5)
    bq.place(x=1250, y=700)

    bq = Button(window4, text="Back", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=back5)
    bq.place(x=1000, y=700)
    
    My_label = tkinter.Label(window4, text="Add Company!", font="verdana 20", bg='#add8e6', fg="#123499", padx=70, pady=30)
    My_label.place(x=450, y=40)
    
    lbl = Label(window4, font=('calibri', 20, 'bold'),
            background='#add8e6',
            foreground='#123499')
    
    date=datetime.datetime.now()
    label = Label(window4, text=f"{date:%A, %B %d, %Y}", font=('calibri', 20, 'bold'), bg="#add8e6", fg="#123499")
    label.place(x=1225,y=50)
    
    l49 = Label(window4, text="Enter DC Number", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l49.place(x=20,y=170)
    txt19=Entry(window4,width=20)
    txt19.place(x=500,y=200)
    
    l99 = Label(window4, text="Enter the previous month balance", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l99.place(x=20,y=700)
    txt25=Entry(window4,width=20)
    txt25.place(x=500,y=730)
    
    l50 = Label(window4, text="Enter Company Name", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l50.place(x=700,y=170)
    txt20=Entry(window4,width=20)
    txt20.place(x=1200,y=200)
    
    l51 = Label(window4, text="Enter Phone number", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l51.place(x=20,y=370)
    txt21=Entry(window4,width=20)
    txt21.place(x=500,y=400)
    
    l52 = Label(window4, text="Enter Address", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l52.place(x=700,y=370)
    txt22=Entry(window4,width=20)
    txt22.place(x=1200,y=400)
    
    l53 = Label(window4, text="Enter GST Number", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l53.place(x=20,y=570)
    txt23=Entry(window4,width=20)
    txt23.place(x=500,y=600)
    
    l54 = Label(window4, text="Enter Pan Number", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l54.place(x=700,y=570)
    txt24=Entry(window4,width=20)
    txt24.place(x=1200,y=600)
    
    lbl.pack(anchor='ne', text=time())
    window4.mainloop()

def newfrankie():
    global window5, txt1
    
    window5 = tkinter.Tk()
    window5.attributes('-fullscreen', True)
    window5.title("new frankie")
    window5['background'] = '#add8e6'
    
    My_label = tkinter.Label(window5, text="New Frankie machine no", font="verdana 20", bg='#add8e6', fg="#123499", padx=70, pady=30)
    My_label.place(x=450, y=40)
    
    l25 = Label(window5, text="Enter the new frankie machine no", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l25.place(x=300, y=320)
    
    
    txt1 = Entry(window5, width=20)
    txt1.place(x=900, y=350)

    # Button to save new frankie machine number to CSV
    ba = Button(window5, text="save", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=save_to_csv)
    ba.place(x=1000, y=700)
    bd = Button(window5, text="back", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=back7)
    bd.place(x=800, y=800)
    bp = Button(window5, text="Exit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=closed8)
    bp.place(x=800, y=700)



def save_to_csv():
    # Read existing CSV file into DataFrame
    try:
        df = pd.read_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\Book1.csv")
    except FileNotFoundError:
        # If the file doesn't exist, create an empty DataFrame
        df = pd.DataFrame(columns=["frankie no", "company name"])
    
    # Add new frankie machine number to DataFrame
    new_frankie_no = txt1.get()
    new_row = {"frankie no": new_frankie_no, "company name": ""}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    
    # Write DataFrame back to CSV
    df.to_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\Book1.csv", index=False)


def art_submit():
    prod = combo1.get()
    bank_choice = combo2.get()
    art = int(txt1.get())
    rate_art = int(txt2.get())
    tax = int(txt3.get())
    sc = float(txt4.get())
    weight = combo4.get()
    frank = combo3.get()
    today = date.today()
    list1=[0,today, frank, prod, bank_choice, art, 0, rate_art, 0, tax, art*rate_art, 0, art*tax, art*tax*0.18, sc*art*0.18 , sc*art, sc, weight]
    f1=open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\bank.csv", mode='a')
    ww=csv.writer(f1)
    ww.writerow(list1)
    f1.close()

def art_next():
    window3.destroy()
    newfrankie()
def article():
    global window3, label, lbl, l1, combo1, combo2, combo3, txt2, txt3, txt4, txt1, combo4   
    window3 = tkinter.Tk()
    window3.attributes('-fullscreen', True)
    window3.title("Article details")
    window3['background'] = '#add8e6'
    l20 = Label(window3, text="Enter the product type", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l20.place(x=20, y=320)
    combo1=ttk.Combobox(window3, width=25, height=4)
    combo1['values']=("ord","reg","speed")
    combo1.place(x=500,y=350)
    
    l2 = Label(window3, text="Enter the Customer name", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l2.place(x=700, y=170)
    combo2=ttk.Combobox(window3, width=25, height=4)
    
    My_label = tkinter.Label(window3, text="Article Details!", font="verdana 20", bg='#add8e6', fg="#123499", padx=70, pady=30)
    My_label.place(x=550, y=40)

    
    l27= Label(window3, text="Enter whether greater than or less than 10g", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l27.place(x=20, y=730)
    combo4=ttk.Combobox(window3, width=25, height=4)
    combo4['values']=("yes","no")
    combo4.place(x=500,y=780)

    
    l3 = Label(window3, text="Enter the no of articles", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l3.place(x=700,y=320)
    txt1=Entry(window3,width=20)
    txt1.place(x=1200,y=350)
    
    bs = Button(window3, text="Exit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=closed4)
    bs.place(x=800, y=700)
    bu = Button(window3, text="back", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=back2)
    bu.place(x=800, y=800)
    by = Button(window3, text="submit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=art_submit)
    by.place(x=1000, y=700)
    bp= Button(window3, text="new frankie machine", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=art_next)
    bp.place(x=1000, y=800)

    l4 = Label(window3, text="Enter the rate per article", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l4.place(x=20, y=470)
    txt2=Entry(window3,width=20)
    txt2.place(x=500,y=500)
    
    
    l5 = Label(window3, text="Enter the tax rate", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l5.place(x=700, y=470)
    txt3=Entry(window3,width=20)
    txt3.place(x=1200,y=500)
    
    l6 = Label(window3, text="Enter the service charge", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l6.place(x=20, y=630)
    txt4=Entry(window3,width=20)
    txt4.place(x=500,y=670)

    l7 = Label(window3, text="Enter the frakie machine no", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l7.place(x=20, y=170)
    combo3=ttk.Combobox(window3, width=25, height=4)
    f1 = open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\Book1.csv", mode="r")
    wr1 = csv.reader(f1, delimiter=',')

    count1 = 0
    bank_name1 = []

    for a in wr1: # Check if the count is even (alternate lines)
        if len(a) > 1:  # Ensure 'a' has at least two elements
            for i in bank_name1:
                if a[0] == i:
                    count1 += 1
                    break
            else:
                bank_name1.append(a[0])
    count1 += 1

    bank_tuple1 = tuple(bank_name1)
    combo3['values']=bank_tuple1
    combo3.place(x=500,y=200)
    
    
    
    f = open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\comp.csv", mode="r")
    wr = csv.reader(f, delimiter=',')

    count = 0
    bank_name = []

    for a in wr: # Check if the count is even (alternate lines)
        if len(a) > 1:  # Ensure 'a' has at least two elements
            for i in bank_name:
                if a[1] == i:
                    count += 1
                    break
            else:
                bank_name.append(a[0])
    count += 1

    bank_tuple = tuple(bank_name)
    combo2['values']=bank_tuple
    combo2.place(x=1200,y=200)
    f.close()
def entry1():
    empname = combo49.get()
    mudiyadhu = txt111.get()
    mudiyadhu1=txt99.get()
    
    

# Read the CSV file
    df = pd.read_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\attendance.csv", index_col=0)

# Get today's date
    today = date.today()
    

# Check if today's date column exists, if not, create it
    if str(today) not in df.columns:
        df[str(today)] = ""

# Check if the bank_chosen row exists, if not, create it
    if empname not in df.index:
        df.loc[empname] = ""

# Set the advance_val for the bank_chosen and today's date
    if(int(mudiyadhu)-int(mudiyadhu1)==0):
        
        df.at[empname, str(today)] = "b"
    else:
        df.at[empname, str(today)] ="p entry: %s exit: %s"%(mudiyadhu1, mudiyadhu)


# Write the DataFrame back to the CSV file
    df.to_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\attendance.csv")

def attlee():
    window15.destroy()
    addemployee()
    
def attendance():
    global window15, label, lbl, l1, combo1, combo2, combo3, txt2, txt3, txt4, txt1, combo49,txt99,txt111
    window15 = tkinter.Tk()
    window15.attributes('-fullscreen', True)
    window15.title("Article details")
    window15['background'] = '#add8e6'
    bg = Button(window15, text="Exit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=closed11)
    bg.place(x=800, y=700)
    bi = Button(window15, text="back", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=back10)
    bi.place(x=800, y=800)
    be = Button(window15, text="submit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=entry1)
    be.place(x=1000, y=700)
    by = Button(window15, text="add employee", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=attlee)
    by.place(x=800, y=600)
    l97= Label(window15, text="choose your employee", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l97.place(x=100, y=265)
    combo49=ttk.Combobox(window15, width=25, height=4)
    f = open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\attendance.csv", mode="r")
    wr = csv.reader(f, delimiter=',')

    count = 0
    bank_name = []

    for a in wr: # Check if the count is even (alternate lines)
        if len(a) > 1:  # Ensure 'a' has at least two elements
            for i in bank_name:
                if a[1] == i:
                    count += 1
                    break
            else:
                bank_name.append(a[0])
    count += 1

    bank_tuple = tuple(bank_name)
    combo49['values']=bank_tuple
    combo49.place(x=500,y=300)
    l9 = Label(window15, text="Enter the entry time ", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l9.place(x=120, y=470)
    txt99=Entry(window15,width=20)
    txt99.insert(0,'0')

    txt99.place(x=500,y=500)
    My_label = tkinter.Label(window15, text="Indian Postal Service Bill Generation!", font="verdana 20", bg='#add8e6', fg="#123499", padx=70, pady=30)
    My_label.place(x=450, y=40)
    l111 = Label(window15, text="Enter the exit time", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l111.place(x=150, y=680)
    txt111=Entry(window15,width=20)
    txt111.insert(0,'0')

    txt111.place(x=500,y=700)
def hiamrit():
    window16.destroy()
    attendancecsv()

def addemployee():
    global window16, label, lbl, l1, combo1, combo2, combo3, txt2, txt3, txt4, txt1, combo4,combo78,txt9  
    window16 = tkinter.Tk()
    window16.attributes('-fullscreen', True)
    window16.title("Article details")
    window16['background'] = '#add8e6'
    bg = Button(window16, text="Exit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=closed12)
    bg.place(x=800, y=700)
    bi = Button(window16, text="back", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=back11)
    bi.place(x=800, y=800)
    be = Button(window16, text="submit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=attendancecsv)
    be.place(x=1000, y=700)
    l9 = Label(window16, text="Enter the employee name ", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l9.place(x=20, y=170)
    txt9=Entry(window16,width=20)
    

    txt9.place(x=500,y=200)
    My_label = tkinter.Label(window16, text="Indian Postal Service Bill Generation!", font="verdana 20", bg='#add8e6', fg="#123499", padx=70, pady=30)
    My_label.place(x=450, y=40)
    l11 = Label(window16, text="Enter the emplyoee grade", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l11.place(x=20, y=470)
    combo78=ttk.Combobox(window16, width=25, height=4)
    combo78['values']=("a","b","c","d","e")
    combo78.place(x=500,y=500)

def attendancecsv():
    grade1=combo78.get()
    name1=txt9.get()
    df=pd.read_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\attendance.csv")
    new_row = {'names':name1 , 'grade': grade1}
    new_row_df = pd.DataFrame([new_row])
    df = pd.concat([df, new_row_df], ignore_index=True)
    print("Updated DataFrame:")
    print(df)


    df.to_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\attendance.csv", index=False)

    
def mainnext():
    window.destroy()
    attendance()
    
   

def main():
    global window, label, lbl
    window = tkinter.Tk()
    window.attributes('-fullscreen', True)
    window.title("Indian Postal Service Bill Calculation")
    window['background'] = '#add8e6'

    bt = Button(window, text="Client Side", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=main_next)
    bt.place(x=400, y=400)
    
    br = Button(window, text="Attendance Manager", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12",command=mainnext)
    br.place(x=900, y=400)
    bq = Button(window, text="Exit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=closed)
    bq.place(x=700, y=700)
    #vishal

    My_label = tkinter.Label(window, text="Indian Postal Service Bill Generation!", font="verdana 20", bg='#add8e6', fg="#123499", padx=70, pady=30)
    My_label.place(x=450, y=40)
    
       
   
    
    lbl = Label(window, font=('calibri', 20, 'bold'),
            background='#add8e6',
            foreground='#123499')
    
    date=datetime.datetime.now()
    label = Label(window, text=f"{date:%A, %B %d, %Y}", font=('calibri', 20, 'bold'), bg="#add8e6", fg="#123499")
    label.place(x=1225,y=50)

    lbl.pack(anchor='ne', text=time())
    window.mainloop()


main()