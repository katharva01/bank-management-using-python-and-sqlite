import sqlite3

conn= sqlite3.connect('bank.db')
cur=conn.cursor()

cur.executescript(
    """ CREATE TABLE IF NOT EXISTS ACCOUNT(
        name text,
        accNo int,
        birthDate text,
        phone text,
        balance real
    );

    CREATE TABLE IF NOT EXISTS AMOUNT(
        accNo text,
        name text,
        balance real
    );
    """
)
conn.commit()


def start():
    print("""
    1. open new account 
    2. view balance amount
    3. deposite cash 
    4. withdraw cash
    5. display customer details
    6. close account 
    """)
    inp=int(input("enter your choice : "))
    if (inp==1):
        openAcc()
    elif(inp==2):
        balance()
    elif(inp==3):
        deposite()
    elif(inp==4):
        withdraw()
    elif(inp==5):
        display()
    elif(inp==6):
        closeAcc()
    else:
        print("enter a valid option")
    start()

def openAcc():
    conn= sqlite3.connect('bankd.db')
    cur=conn.cursor()
    
    name=input("enter customer name : ")
    accNo=int(input("enter account Nunber :"))
    dob=input("enter customer birthdate(dd/mm/yyyy) : ")
    phon=input("enter customer phone no. : ")
    amount=float(input("enter amount to be deposite : "))

    data1=(name.upper,accNo,dob,phon,amount)
    data2=(name.upper,accNo,amount)

    query1="INSERT INTO ACCOUNT VALUES (?,?,?,?,?)"
    query2="INSERT INTO AMOUNT VALUES (?,?,?)"

    cur.execute(query1,data1)
    cur.execute(query2,data2)

    conn.commit()
    conn.close()
    start()
    
def openAcc():
    conn= sqlite3.connect('bank.db')
    cur=conn.cursor()
    
    name=input("enter customer name : ")
    accNo=int(input("enter account Nunber : "))
    dob=input("enter customer birthdate(dd/mm/yyyy) : ")
    phon=input("enter customer phone no. : "  )
    amount=float(input("enter amount to be deposite : "))

    data1=(name,accNo,dob,phon,amount)
    data2=(accNo,name,amount)

    query1="INSERT INTO ACCOUNT VALUES (?,?,?,?,?)"
    query2="INSERT INTO AMOUNT VALUES (?,?,?)"

    cur.execute(query1,data1)
    cur.execute(query2,data2)

    conn.commit()
    start()


def balance():
    conn= sqlite3.connect('bank.db')
    cur=conn.cursor()
    
    accNum=int(input("enter account Nunber : "))
    a=(accNum,)

    query="SELECT balance FROM AMOUNT WHERE accNo==(?)"

    cur.execute(query,a)
    temp=cur.fetchone()
    print("balance money in account (rupees) : ",temp)
    conn.commit()
    conn.close()
    start()

def display():
    conn= sqlite3.connect('bank.db')
    cur=conn.cursor()
    
    accNum=int(input("enter account Nunber : "))
    a=(accNum,)

    query="SELECT * FROM ACCOUNT WHERE accNo==(?)"

    cur.execute(query,a)
    temp=cur.fetchone()
    print("Name of account holder: ",temp[0])
    print("account Number : ",temp[1])
    print("birthdate(ddmmyyyy) : ",temp[2])
    print("contact Number : ",temp[3])
    print("balance money in account (rupees) : ",temp[4])

    conn.commit()
    conn.close()
    start() 


def closeAcc():
    conn= sqlite3.connect('bank.db')
    cur=conn.cursor()
    
    accNum=int(input("enter account Nunber : "))
    a=(accNum,)

    query1="DELETE FROM ACCOUNT WHERE accNo==(?)"
    query2="DELETE FROM AMOUNT WHERE accNo==(?)"


    cur.execute(query1,a)
    cur.execute(query2,a)
    
    print("Account deleted successfully ")
   

    conn.commit()
    conn.close()
    start()        

start()

# cur.execute("INSERT INTO ACCOUNT VALUES('Aditya',12345288,'20-11-2001',9122109190,3000)")

# below  command to check all data from table Account

# cur.execute("SELECT * FROM ACCOUNT")
# print(cur.fetchall())
# conn.commit()
# conn.close()