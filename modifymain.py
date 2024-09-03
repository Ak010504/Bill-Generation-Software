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
from tkinter import filedialog

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
    
def back():
    window1.destroy()
    main()
def back9():
    window16.destroy()
    attendance()
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
    df = pd.read_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv")

    # Get today's date
    today = date.today()
    
    # Convert bank_chosen to string
    bank_chosen = str(bank_chosen)
    
    # Check if today's date column exists, if not, create it
    if str(today) not in df.columns:
        df[str(today)] = ""

    # Convert the entire first column to string
    df.iloc[:, 0] = df.iloc[:, 0].astype(str)

    # Check if the bank_chosen row exists in the first column, if not, create it
    if not df.iloc[:, 0].str.contains(bank_chosen).any():
        df.loc[len(df)] = [bank_chosen] + [""] * (len(df.columns) - 1)

    # Set the advance_val for the bank_chosen and today's date
    df.loc[df.iloc[:, 0].str.contains(bank_chosen), str(today)] = advance_val

    # Write the DataFrame back to the CSV file
    df.to_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv", index=False)

    
def bill(bank_cho):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count11 = 0
    count12 = 0
    count13 = 0
    count14 = 0
    price1 = 0
    price2 = 0
    price3 = 0
    price4 = 0
    price5 = 0
    price6 = 0
    price7 = 0
    price8 = 0
    price9 = 0
    price10 = 0
    price11 = 0
    price12 = 0
    price13 = 0
    price14=0
    count15=0

# Read the CSV file into a DataFrame
    df = pd.read_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\bank.csv")

# Drop rows where all values are NaN (blank rows)
    df.dropna(how='all', inplace=True)

# Write the DataFrame back to a CSV file
    df.to_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\bank.csv", index=False)

    df2 = pd.read_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv")
# Replace 0 with NaN (or another null representation)
    df2.replace(0, np.nan, inplace=True)
    df2.to_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv", index=False)
    with open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\bank.csv", mode='r') as f20:
        wr5 = csv.reader(f20, delimiter=',')
        for a54 in wr5:
            if int(float(a54[4])) == int(float(bank_cho)):
                if a54[3] == "FREG":
                    print("Hello")
                    count1+=float(a54[5])
                    price1+=float(a54[10])
                if a54[3] == "DA FR":
                    print("Hello")
                    price1+=float(a54[10])
                if a54[3] == "DA FRP":
                    print("Hello")
                    price3+=float(a54[10])
                if a54[3] == "RP" :
                    count2+=float(a54[5])
                    price2+=float(a54[10])
                if a54[3] == "DA RP":
                    print("Hello")
                    price2+=float(a54[10])
                if a54[3] == "FRP":
                    count3+=float(a54[5])
                    price3+=float(a54[10])
                if a54[3] == "BMS":
                    count4+=float(a54[5])
                    price4+=float(a54[10])
                if a54[3] == "NBMS":
                    count5+=float(a54[5])
                    price5+=float(a54[10])
                if a54[3] == "DP":
                    count6+=float(a54[5])
                    price6+=float(a54[10])
                if a54[3] == "PC":
                    count7+=float(a54[5])
                    price7+=float(a54[10])
                if a54[3] == "BP":
                    count8+=float(a54[5])
                    price8+=float(a54[10])
                if a54[3] == "FORD":
                    count9+=float(a54[5])
                    price9+=float(a54[10])
                if a54[3] == "ILC":
                    count10+=float(a54[5])
                    price10+=float(a54[10])
                if a54[3] == "SPP":
                    count11+=float(a54[5])
                    price11+=float(a54[10])
                if a54[3] == "DA SP":
                    price11+=float(a54[10])
                if a54[3] == "FSPEED":
                    count12+=float(a54[5])
                    price12+=float(a54[10])
                if a54[3] == "DA FS":
                    print("Hello")
                    price12+=float(a54[10])
                if a54[3] == "RILC":
                    count13+=float(a54[5])
                    price13+=float(a54[10])
                if a54[3] == "RPP":
                    count14+=float(a54[5])
                    price14+=float(a54[10])
    sumbms = price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8 + price9 + price10 + price11 + price12 + price13 + price14
# Save the modified DataFrame back to a CSV file
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
    if count1>0:
        print("Hi")
        count15+=1
        data.insert(16, ["Foreign Regsitered Articles Posted", count1, price1])
    if count2>0:
        print("Hi")
        count15+=1
        data.insert(16, ["Registered Parcel Posted", count2, price2])
    if count3>0:
            print("Hi")
            count15+=1
            data.insert(16, ["Foreign Registered Parcel Posted", count3, price3])
    if count4>0:
            print("Hi")
            count15+=1
            data.insert(16, ["BMS Posted", count4, price4])
    if count5>0:
            print("Hi")
            count15+=1
            data.insert(16, ["NBMS Posted", count5, price5])
    if count6>0:
            print("Hi")
            count15+=1
            data.insert(16, ["DP Posted", count6, price6])
    if count7>0:
            print("Hi")
            count15+=1
            data.insert(16, ["PC Posted", count7, price7])
    if count8>0:
            print("Hi")
            count15+=1
            data.insert(16, ["BP Posted", count8, price8])
    if count9>0:
            print("Hi")
            count15+=1
            data.insert(16, ["FORD Posted", count9, price9])
    if count10>0:
            print("Hi")
            count15+=1
            data.insert(16, ["ILC Posted", count10, price10])
    if count11>0:
            print("Hi")
            count15+=1
            data.insert(16, ["SPP Posted", count11, price11])
    if count12>0:
            print("Hi")
            count15+=1
            data.insert(16, ["Foreign Speed Article Posted", count12, price12])
    if count13>0:
            print("Hi")
            count15+=1
            data.insert(16, ["RILC Posted", count13, price13])
    if count14>0:
            print("Hi")
            count15+=1
            data.insert(16, ["RBP Posted", count14, price14])
                    
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
            data[5][0] = row[1]
            break
    
    f1 = open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\bank.csv", mode='r')
    f2 = open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv", mode = 'r+')
    wr2 = csv.reader(f2)
    wr1 = csv.reader(f1)
    adv2=0.0
    k=0
    csv_data = list(wr2)[1:]
    for a1 in csv_data:
        print(a1[0])
        print(a1[1])
        if int(float(a1[0])) == int(float(bank_cho)):
            print("Hey")
            # Found the matching row
            data[17+count15][2] = a1[1]
            k = len(a1) - 2     
            # Iterate through the relevant columns
            for j in range(2, len(a1)):
                if a1[j] and a1[j]!=0:
                    advance_string = f"Advance received vide CHQ/NEFT DT:{csv_data[0][j]}"
                    data.insert(18+count15, [advance_string, "", a1[j]])
                    adv2 += float(a1[j])

    k=len(data)-(39+count15)+count15
    print(k)
    data[18+k][2] = adv2 + float(data[17+count15][2])
    service = 0.0
    st=0.0
    for row in wr1:
        if len(row) >17:
            if int(float(row[4])) == int(float(bank_cho)):
                if row[17] == 'yes':
                    print(row[3])
                    if row[3] == 'ORD':
                        data[10][1] = float(data[10][1]) + float(row[5])
                        data[10][2] = float(data[10][2]) + float(row[10])
                    if (row[3] == "DP DA"):
                        data[10][2] = float(data[10][2]) + float(row[10])
                    if row[3] == 'REG':
                        data[12][1] = float(data[12][1]) + float(row[5])
                        data[12][2] = float(data[12][2]) + float(row[10])
                    if (row[3] == "DA R"):
                        data[12][2] = float(data[12][2]) + float(row[10])
                    if row[3] == 'SPEED':
                        data[14][1]=  float(data[14][1]) + float(row[5])
                        data[14][2] = float(data[14][2]) + float(row[10])
                    if (row[3] == "DA S"):
                        data[14][2] = float(data[14][2]) + float(row[10])
                if row[17] == 'no':
                    if row[3] == 'ORD':
                        data[11][1] = float(data[11][1]) + float(row[5])
                        data[11][2] = float(data[11][2]) + float(row[10])
                    if (row[3] == "DP DA"):
                        data[11][2] = float(data[11][2]) + float(row[10])
                    if row[3] == 'REG':
                        data[13][1] = float(data[13][1]) + float(row[5])
                        data[13][2] = float(data[13][2]) + float(row[10])
                    if (row[3] == "DA R"):
                        data[12][2] = float(data[12][2]) + float(row[10])
                    if row[3] == 'SPEED':
                        data[15][1]=  float(data[15][1]) + float(row[5])
                        data[15][2] = float(data[15][2]) + float(row[10])
                    if (row[3] == "DA S"):
                        data[14][2] = float(data[14][2]) + float(row[10])
                if (row[17] == 'no'):
                    service = float(service) + float(row[15])
                st = float(st)+float(row[11])
                data[22+k][2] = float(data[22+k][2]) + float(row[15])

    totalart=0
    totalsum = 0
    for i in range(10, 16+count15):
        totalart = totalart + float(data[i][1])
        totalsum = totalsum + float(data[i][2])
    data[16+count15][1] = totalart
    data[16+count15][2] = totalsum
    data[23+k][2] = service*0.09
    data[24+k][2] = service*0.09
    data[19+k][2] = data[16+count15][2]
    
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
    
    
    csv_file_path = r"D:\\Amrit\\College\\SSN\\CS\\Post\\adv.csv"

# Define the bank_cho and the new balance value

    # Read the existing data from the CSV file
    rows = []
    with open(csv_file_path, mode='r') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Find the indices of the "balance" and "id" columns
    header_row = rows[0]
    balance_column_index = None
    id_column_index = None
    for i, header in enumerate(header_row):
        if header.strip().lower() == "balance":
            balance_column_index = i
        elif header.strip().lower() == "id":
            id_column_index = i

    # Update the balance column for the specific bank_cho
    if balance_column_index is not None:
        for row in rows:
            if row and row[0] == bank_cho:  # Check if the row exists and matches bank_cho
                row[balance_column_index] = closing  # Update the balance column with the new value

    # Filter out columns that do not have the column header as "balance" or "id"
    filtered_rows = []
    for row in rows:
        filtered_row = [row[i] for i in [id_column_index, balance_column_index] if i is not None]
        filtered_rows.append(filtered_row)

    # Write the modified data back to the CSV file
    with open(csv_file_path, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)
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
    l99.place(x=0,y=670)
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


            
def art_submit(bank_choice,today,frank,prod,art,rate_art,tax,sc, weight):

    list1=[0,today, frank, prod, bank_choice, art, 0, rate_art,0, tax, float(art)*float(rate_art), 0, float(art)*float(tax), float(art)*float(tax)*0.18, float(sc)*float(art)*0.18 , float(sc)*float(art), float(sc), weight]
    f1=open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\bank.csv", mode='a')
    ww=csv.writer(f1)
    ww.writerow(list1)
    f1.close()

def art_next():
    window3.destroy()
    newfrankie()
    
def article():
    global window3, label, lbl, l1, txt1, combo4   
    window3 = tkinter.Tk()
    window3.attributes('-fullscreen', True)
    window3.title("Article details")
    window3['background'] = '#add8e6'
   
    
    My_label = tkinter.Label(window3, text="Article Details!", font="verdana 20", bg='#add8e6', fg="#123499", padx=70, pady=30)
    My_label.place(x=550, y=40)


    def open_file_dialog():
        file_path = filedialog.askopenfilename()
        if file_path:
            print(f"Selected file: {file_path}")
            df = pd.read_excel(file_path)  # Assuming the file is Excel based on your previous example
            df.to_csv('article.csv', encoding='utf-8')
            with open('article.csv', "r") as f:
                next(f)  # Skip header line
                for line in f:
                    l = line.strip().split(',')  # Assuming CSV is comma-separated
                    if (l[10] == ''):
                        bank_choice = l[1]
                        today = l[2]
                        frank = l[3]
                        prod = l[4]
                        art = l[6]
                        rate_art = l[8]
                        rate = l[7]
                        tax = int(rate_art) - int(rate)
                    else:
                        bank_choice = l[1]
                        today = l[2]
                        frank = l[3]
                        prod = l[4]
                        art = l[6]
                        rate_art = l[7]
                    
                        tax = l[10]
                    sc = l[17]
                    weight = l[18]                    
                    print(f"Processing: bank_choice={bank_choice}, today={today}, frank={frank}, prod={prod}, art={art}, rate_art={rate_art}, tax={tax}, sc={sc}")
                    
                    # Call your submit function here with the extracted data
                    art_submit(bank_choice, today, frank, prod, art, rate_art, tax, sc, weight)       
        # You can do further processing with the selected file path here


# Create a button to trigger file selection
    bsa = Button(window3, text="Open File", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=open_file_dialog)
    bsa.place(x=500, y=500)
    bs = Button(window3, text="Exit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=closed4)
    bs.place(x=800, y=700)
    bu = Button(window3, text="back", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=back2)
    bu.place(x=800, y=800)
    by = Button(window3, text="submit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=art_submit)
    by.place(x=1000, y=700)

    
def add_attendance_entry_exit():
    entry_time = txt9.get()
    exit_time = txt11.get()
    employee_name = combo4.get()

    if entry_time == '0' and exit_time == '0':
        df = pd.read_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\attendance.csv")

    # Get today's date
        today_date = date.today().strftime("%Y-%m-%d")

    # Filter the DataFrame for the selected employee
        employee_df = df[df['names'] == employee_name]

    # Update the entry and exit time for the selected employee
        employee_df[today_date] = "b"

    # Update the original DataFrame with the modified entry for the selected employee
        df.update(employee_df)

    # Write the updated DataFrame back to the CSV file
        df.to_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\attendance.csv", index=False)
    # Read the CSV file into a DataFrame
    else:
        
        df = pd.read_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\attendance.csv")

        # Get today's date
        today_date = date.today().strftime("%Y-%m-%d")

        # Filter the DataFrame for the selected employee
        employee_df = df[df['names'] == employee_name].copy()  # Make a copy to avoid SettingWithCopyWarning

        # Update the entry and exit time for the selected employee
        employee_df.loc[:, today_date] = entry_time + " - " + exit_time

        # Update the original DataFrame with the modified entry for the selected employee
        df.loc[employee_df.index, today_date] = employee_df.loc[:, today_date]

        # Write the updated DataFrame back to the CSV file
        df.to_csv(r"D:\\Amrit\\College\\SSN\\CS\\Post\\attendance.csv", index=False)

def attendance():
    global window15, label, lbl, l1, combo1, combo2, combo3, txt2, txt3, txt4, txt1, combo4, txt9, txt11  
    window15 = tkinter.Tk()
    window15.attributes('-fullscreen', True)
    window15.title("Article details")
    window15['background'] = '#add8e6'
    bg = Button(window15, text="Exit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=closed9)
    bg.place(x=800, y=700)
    bi = Button(window15, text="back", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=back8)
    bi.place(x=800, y=800)
    be = Button(window15, text="submit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=add_attendance_entry_exit)
    be.place(x=1000, y=700)
    by = Button(window15, text="add employee", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=hisidd)
    by.place(x=800, y=600)
    l97= Label(window15, text="choose your employee", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l97.place(x=240, y=200)
    combo4=ttk.Combobox(window15, width=25, height=4)
    f1 = open(r"D:\\Amrit\\College\\SSN\\CS\\Post\\attendance.csv", mode="r")
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
    combo4['values']=bank_tuple1
    combo4.place(x=300,y=300)
    l9 = Label(window15, text="Enter the entry time ", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l9.place(x=240, y=400)
    txt9=Entry(window15,width=20)
    txt9.insert(0,'0')

    txt9.place(x=300,y=450)
    My_label = tkinter.Label(window15, text="Indian Postal Service Bill Generation!", font="verdana 20", bg='#add8e6', fg="#123499", padx=70, pady=30)
    My_label.place(x=450, y=40)
    l11 = Label(window15, text="Enter the exit time", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l11.place(x=240, y=550)
    txt11=Entry(window15,width=20)
    txt11.insert(0,'0')

    txt11.place(x=300,y=600)
def hiamrit():
    window16.destroy()
    attendancecsv()
    
def hisidd():
    window15.destroy()
    addemployee()

def addemployee():
    global window16, label, lbl, l1, combo1, combo2, combo3, txt2, txt3, txt4, txt1, combo4,combo78,txt9  
    window16 = tkinter.Tk()
    window16.attributes('-fullscreen', True)
    window16.title("Article details")
    window16['background'] = '#add8e6'
    bg = Button(window16, text="Exit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=closed10)
    bg.place(x=800, y=700)
    bi = Button(window16, text="back", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=back9)
    bi.place(x=800, y=800)
    be = Button(window16, text="submit", padx=50, pady=20, bg="#123499", fg="white", font="verdana 12", command=attendancecsv)
    be.place(x=1000, y=700)
    l9 = Label(window16, text="Enter the employee name ", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l9.place(x=20, y=470)
    txt9=Entry(window16,width=20)
    

    txt9.place(x=500,y=500)
    My_label = tkinter.Label(window16, text="Indian Postal Service Bill Generation!", font="verdana 20", bg='#add8e6', fg="#123499", padx=70, pady=30)
    My_label.place(x=450, y=40)
    l11 = Label(window16, text="Enter the emplyoee grade", font="verdana 20", bg='#add8e6', fg="#123499", padx=60, pady=20)
    l11.place(x=60, y=180)
    combo78=ttk.Combobox(window16, width=25, height=4)
    combo78['values']=("a","b","c","d","e")
    combo78.place(x=500,y=200)

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
    back9()

    
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
    

    My_label = tkinter.Label(window, text="Indian Postal Service Bill Generation!", font="verdana 20", bg='#add8e6', fg="#123499", padx=70, pady=30)
    My_label.place(x=450, y=40)
    
    image = Image.open("D:\Amrit\College\SSN\CS\Post\logo.png")
    resize_image = image.resize((300, 300))
    img = ImageTk.PhotoImage(resize_image)
    label1 = Label(window, image=img, bg="#add8e6")
    label1.image = img
    
    label1.place(x=20, y=20)

    image2 = Image.open("D:\Amrit\College\SSN\CS\Post\india-post.png")
    resize_image = image2.resize((300, 200))
    img2 = ImageTk.PhotoImage(resize_image)
    label2 = Label(window, image=img2, bg="#add8e6")
    label2.image = img2
    label2.place(x=1200, y=600)
   
    
    lbl = Label(window, font=('calibri', 20, 'bold'),
            background='#add8e6',
            foreground='#123499')
    
    date=datetime.datetime.now()
    label = Label(window, text=f"{date:%A, %B %d, %Y}", font=('calibri', 20, 'bold'), bg="#add8e6", fg="#123499")
    label.place(x=1225,y=50)

    lbl.pack(anchor='ne', text=time())
    window.mainloop()
    
main()