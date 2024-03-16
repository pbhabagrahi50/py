def add (num1,num2):
    a=num1+num2
    return a
def sub(num1,num2):
    b=num1-num2
    return b
def mul(num1,num2):
    c=num1*num2
    return c


x=add(5,45)
y=sub(45,5)
z=mul(544,333)
print("addition :",x)
print(y)
print(z)

from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Access the variable
db_password = os.getenv('DB_PASSWORD')
print(db_password)

