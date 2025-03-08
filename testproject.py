# # 1.Problem: Parking Fee Calculation
# # A parking lot charges a fee based on the number of hours a vehicle is parked. The rules are:
# # First 2 hours → ₹50 fixed fee.
# # Next hours (3rd hour onward) → ₹20 per hour.
# # More than 10 hours → ₹300 fixed fee (instead of per-hour calculation).
# # Write a Python function that takes the number of hours parked as input and calculates the total parking fee using an if-else condition.
def calculates_hours(hours):
    if(hours<=2):
        fee=50
        print("The fee amount is Rs.",fee)
    elif(3<=hours<=10):
        fee=50+(hours-2)*20
        print("The fee amount is Rs.",fee)
    else:
        fee=300
        print("The fee amount is Rs.",fee)
hours=int(input("Please Enter a  total number of hours: "))
calculates_hours(hours)
def cal_fees(hours):
    if(hours<=2):
        fees=50
        print(fees)
    elif(3<=hours<=10):
        fees=50+(hours-2)*20
        print(fees)
    else:
        fees=300
        print(fees)
hours=int(input("enter a total hours: "))
cal_fees(hours)
# #########-----------------################
# # exercise 
# # 7.Problem Statement
# # An e-commerce website offers discounts based on the total purchase amount:
# # If the total bill is less than ₹500, no discount is applied.
# # If the total bill is between ₹500 and ₹2000, a 10% discount is applied.
# # If the total bill is above ₹2000, a 20% discount is applied.
# # Write a Python function that takes the total purchase amount as input and calculates the final amount after the discount.
# ########-------------------###############
def cal_amount(total_bill):
    if(total_bill<=500):
        print("No Discount is applied")
    elif(500<=total_bill<=2000):
        discount=total_bill*0.10
        total_amount=total_bill-discount
        print("A 10% discount is applied & you have to pay",total_amount)
    else:
        discount=total_bill*0.20
        total_amount=total_bill-discount
        print("A 20% discount is applied & you have to pay",total_amount)
total_bill=int(input("Enter a amount: "))
cal_amount(total_bill)
# 1)1.Given a list numbers = [-10, 5, -3, 8, -2], write a function to return a new list containing the absolute values of all elements.
def value(list_num):
    return[abs(num)for num in list_num]
list_num=[-10,5,-3,8,-2]
new_list_num=value(list_num)
print(new_list_num)
# 2)2.Given numbers = [2, 4, 6, 8], write a function that checks whether all numbers are even using all().
def even_num(number):
    return all(num%2==0 for num in number)
number=[2,4,6,8]
output=even_num(number)
print(output)
# 3)3.Write a function that checks whether a list contains at least one negative number using any().
def negative_num(number):
    return any(num < 0 for num in number)
number = [-9,1,2]
output = negative_num(number)
print(output) 
# 4)4.Write a function that takes a list of integers and returns a new list with their binary equivalents.
def new_list(list_num):
    return [bin(num)for num in list_num]
list_num=[1,2,3,4]
output=new_list(list_num)
print(output)
# 5)5.Write a function that takes a string and returns a bytearray with all letters converted to uppercase.
def uc_bytearray(name):
    return bytearray([ord(char.upper()) for char in name])
name="ramesh"
result = uc_bytearray(name)
print(result)
# 6)6.Write a function that prints all uppercase letters (A-Z) using chr() and a loop.
def upper_letter():
    for letter in range(65, 91):
        print(chr(letter),end=' ')
    print()
upper_letter()
class Employee:
 def __init__(self):
    self.name = "Ramesh"
    self.age = 24
    self.salary = 7500
emp = Employee()
print("Age:", emp.age)
print("Salary:", emp.salary)
print("Name:", emp.name)
delattr(emp, 'age')
print("Name:", emp.name)
if hasattr(emp, 'age'):     
    print("Age:", emp.age)
else:   
    print("Age attribute has been deleted.It's null")
print("Salary:", emp.salary)
code = "x = 10\ny = 20\n"
compiled_code = compile(code, "<string>", "exec")
exec(compiled_code)
print(x*y)
a=complex(input("Enter a 1st number is: "))
b=complex(input("Enter a 2nd number is: "))
print("Add",a+b)
print("sub",a-b)
print("Mul",a*b)
print("Div",a/b)
class Employee:
    def __init__(self):
         self.name = "Ramesh"
         self.age = 24
         self.salary = 7500
emp = Employee()
print("Age:", emp.age)
print("Salary:", emp.salary)
print("Name:", emp.name)
delattr(emp, 'age')
print("Name:", emp.name)
if hasattr(emp, 'age'):     
    print("Age:", emp.age)
else:   
    print("Age attribute has been deleted.It's null")
print("Salary:", emp.salary)
tuples_list = [("name", "Ramesh"), ("age", 24), ("salary", 7500)]
result_dict = dict(tuples_list)
print(result_dict)
tuples_list = [("name", "Ramesh"), ("age", 24), ("salary", 7500)]
result_dir = dir(tuples_list)
print(result_dir)
class ToDoList:
    def __init__(self):
        self.tasks = {}
    def add_task(self, task_name):
        self.tasks[task_name] = False  # False means not done
    def mark_done(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name] = True  # Mark as done
        else:
            print(f"Task '{task_name}' not found.")
    def remove_task(self, task_name):
        if hasattr(self, 'tasks') and task_name in self.tasks:
            del self.tasks[task_name]  # Remove the task using del
        else:
            print(f"Task '{task_name}' not found.")
    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for task, status in self.tasks.items():
                status_text = "Done" if status else "Not Done"
                print(f"- {task}: {status_text}")
# Main program
todo = ToDoList()
# Adding tasks
todo.add_task("Buy groceries")
todo.add_task("Walk the dog")
todo.add_task("Read a book")
# Display tasks
todo.show_tasks()
# Marking a task as done
todo.mark_done("Walk the dog")
print("\nAfter marking 'Walk the dog' as done:")
todo.show_tasks()
# Removing a task
todo.remove_task("Walk the dog")
print("\nAfter removing 'Walk the dog':")
todo.show_tasks()
a="hello"
b="Ramesh"
print(f" the{a}result is ")
def demo(amount):
    deno=[2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    for i in deno:
      count = amount // i
      if count > 0:  
             print(str(i) + " x " + str(count))
             amount = amount % i  
amount = int(input("Enter a number: "))
demo(amount)
employees = [
    {"name": "Alice", "salary": 60000},
    {"name": "Bob", "salary": 45000},
    {"name": "Charlie", "salary": 70000}
]
def __init__(employee):
    return employee["salary"] > 50000
output= list(filter(__init__,employees))
print(output)
datetime_module = __import__("datetime")
print(datetime_module.datetime.now())
output = float(input("Enter the area of the circle: "))
area = 3.14 * (output ** 2)
print(f"This is area of circle {area}")
price = float(input("Enter a Number: "))
format_price = format(price,".2f")
print("The price is:", format_price)
fs1 = frozenset(["Name"])
fs2 = frozenset(["Age"])
my_dict = {
	fs1: "Ramesh",
	fs2: 24
	}
for key, value in my_dict.items():
    print(f"{set(key)}: {value}")
class Person:
	def __init__(self, name, age, city):
		self.name = name
		self.age = age
		self.city = city
person = Person("Alice", 30, "New York")
attributes = ['name', 'age', 'city']
for output in attributes:
	value = getattr(person, output)
	print(f"{output}: {value}")
def doc_help():
	help(input)
doc_help()
num = 42
print("Hash of integer:", hash(num))
flat = 3.14
print("Hash of float:", hash(flat))
string = "Hello"
print("Hash of string:", hash(string))
tpl = (1, 2, 3)
print("Hash of tuple:", hash(tpl))
numbers = [10, 15, 25, 100, 1000]
hex_values = [hex (i) for i in numbers]
print("Hexadecimal values:", hex_values)
decimal_values = [int(i, 16) for i in hex_values]
print("Converted back to Decimal:", decimal_values)
class Person:
	pass
class Employee(Person):
	pass
class Manager(Person):
	pass
emp = Employee()
mgr = Manager()
print("emp is instance of Person:", isinstance(emp, Person))
print("mgr is instance of Person:", isinstance(mgr, Person))
print("Employee is subclass of Person:", issubclass(Employee, Person))
print("Manager is subclass of Person:", issubclass(Manager, Person))
my_list=["Ramesh","Ram","mani","jhafrin"] 
ite=iter(my_list)
print(my_list)
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite,"No data found"))
def count_words(sentence):
	count = len(sentence)            
	words = len(sentence.split())
	print("Number of characters:", count)
	print("Number of words:", words)
user_name = input("Enter a sentence: ")
count_words(user_name)
my_tuple = ("ramesh", "mani")
my_list = list(my_tuple)
my_list.append("Ram")
my_list.sort()
print(my_list)
def local_var():
	name = "Ramesh"
	age = 24
	city = "Erode"
	print("Local Variables:", locals())
local_var() 
price=[100,200,300,400,500]
dic_price=list(map(lambda x:x-(x*0.10),price))
print(dic_price)
dict={"Name":"Ramesh","Age":24,"City":"Erode"}
my_dict=iter(dict.items())
print(next(my_dict))
print(next(my_dict))
print(next(my_dict))
salary=[10000,1500,1000,5000,2000]
salary.sort(key=lambda x:x)
print(salary)
person={"Ramesh":24,"Mani":26,"Satya":35,"Naresh":25}
old_person=max(person.items())
print(old_person)
from datetime import datetime
dates=["17-02-2025","01-02-2025","26-01-2025","26-02-2025"]
dates.sort(key=lambda x: datetime.strptime(x, '%d-%m-%Y'))
print(dates)
binary_data=bytearray(b'\x01\x02\x03\x04')
print("Orginal Binary Data : ",binary_data)
binary_data[0]=0x10
print("Modified Binary Data : ",binary_data)
# ####File Path(Read)
file_path="C:\\Test.txt"
with open(file_path,"r") as file:
    content = file.read()
    print(content)
#Write
file_path="E:\\Test.txt"
with open(file_path,"w",encoding="UTF-8") as file:
    file.write("Its easy to learn python")
def replace_text_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
          content = file.read()
        updated_content = content.replace('Python', 'Java')       
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)   
file_path = "E:\\Test.txt"
replace_text_file(file_path)
print(ord('🙂'))
text = "Hello\nWorld"
print(text)    
print(repr(text))
person = object()
attributes = {}
attributes["Name"] = "Ramesh"
attributes["Age"] = 24
attributes["City"] = "Erode"
print(f"Name: {attributes["Name"]}, Age: {attributes["Age"]}, City: {attributes["City"]}")
def octal_pyramid(num):
	for i in range(1, num+1):
		print(" " * (num-i), end="")
		for j in range(1, i+1):
			print(oct(j)[2:], end=" ")
		print()
num = int(input("Enter the number of pyramid: "))
octal_pyramid(num)
def name_to_ascii():
	name= input("Enter the full name: ").split()
	asc_dict = {index[0].upper():ord(index[0].upper())for index in name}
	return asc_dict
asc_values = name_to_ascii()
print("ASCII values of initials:", asc_values)
def sum_of_cubes(numbers):
	return sum([pow(x, 3, 1000) for x in numbers])
numbers = map(int,input("Enter numbers : ").split())
print("Sum of cubes mod 1000:", sum_of_cubes(numbers))
def multi_table():
	for i in range(1, 11):
		for j in range(1, 11):
			print(f"{i * j:3}", end=" ")
		print()
multi_table()
class Temperature:
	def __init__(self, celsius):
		self.celsius = celsius
	@property
	def fahrenheit(self):
		return (self.celsius * 9/5) + 32
temp = Temperature(25) 
print(temp.fahrenheit)
def missing_num(num):
	return [i for i in range(min(num),max(num)+1)if i not in num]
num=[1,2,4,6,7]
out=missing_num(num)
print(out)
class bankacct:
	def __init__(self,name,balance):
		self.name=name
		self.balance=balance
	def __repr__(self):
		return(f"Name : {self.name} Balance : {self.balance}")
acc=bankacct("Ramesh",1000)
print(repr(acc))
product_codes = ["Lap123", "Mob456", "Wat789", "Acc101"]
print(list(reversed(product_codes)))
jan_cust = ["Ramesh", "Mani", "Raghul", "Sathya"]
feb_cust = ["Surjith", "Vignesh", "Pirai", "Ramesh"]
all_cust = jan_cust + feb_cust
uni_cust = set(all_cust) 
print("Unique customers across both months :", uni_cust)
def convert_to_inr(usd_amount, exchange_rate=86.84):
	inr_amount = round(usd_amount * exchange_rate,2)
	return inr_amount
print(convert_to_inr(100))
class user:
	def __init__(self, name, email_veri=False):
		self.name = name
		self.email_veri = email_veri
name = user("Ramesh")
setattr(name, "email_veri", True)
print(name.email_veri)
from datetime import datetime
employees = [
    ("Ramesh", "01-01-2020"),  
    ("Suresh", "03-02-2019"),
    ("Naresh", "02-03-2021"), 
    ("Dinesh", "08-01-2025") 
	]
employees.sort(key=lambda x: datetime.strptime(x[1], "%d-%m-%Y"))
for i in employees:
	print(i[::-1])
orders= [199.911, 299.997, 149.789, 249.967, 399.766, 299.997, 149.789]
uniq_ord={round(amount, 2) for amount in orders}
sort_ord=sorted(uniq_ord,reverse=True)
print(sort_ord)
product_id = 12345
message = "Product ID: " + str(product_id)
print(message)
class Car:
	@staticmethod
	def info():
		print("car is to transport people from one place to another on roads")
Car.info()

class base:
	def info(self):
		print("This is a vehicle.")
class sub(base):
	def info(self):
		super().info()
		print("This is a car.")
car = sub()
car.info()


def calc(num, start):
	return sum(num, start)
num=[10, 20, 30, 40, 50]
start=60
print(calc(num, start))

x=input("Enter a Sentence: ")
y=x.split()
print(y)
z=tuple(x)
print(type(z))

Elect= type("Elect", (object,), {"category": "Electronics"})
obj=Elect()
print(obj.category)

print(list(range(10,15,2)))
x=slice([1,5,2])
print(x)

x="ramesh"
y=x(slice[::-1])
print(y)
class training:
    def __init__(self,lang,taken_by,year):
            self.lan=lang
            self.taken_by=taken_by
            self.year=year
name=training("python training","jhafrin",2025)
result=vars(name)
print(result)
name=["Ramesh","Mani","Satya"]
sub=["python","apex","oaf"]
mark=[95,99,60]
print(list(zip(name,sub,mark)))

Oops---Automatic File writing 
import os
os.makedirs("test_directory", exist_ok=True)
file_path = os.path.join("test_directory", "testing.txt")
with open(file_path, "w") as file:
    file.write("Hello Ramesh, this is Jhafrin! Are you enjoying learning python?")
print("Files in directory:", os.listdir("test_directory"))
os.system(f"notepad {file_path}")
 
class phone:
    charger_type="Type-c"
    price="25000"
    def __init__(self,brand):
        self.brand=brand
    def display(self):
        print("brand:",self.brand)
        print("price :",self.price)
        print("charger_type :",self.charger_type)
Iqoo=phone("iqoo")
Samsung=phone("Samsung")
Iqoo.display()
Samsung.display()

class phone:
    charger_type="Type-c"
    def __init__(self,price="100000",brand=):
        self.brand=""
        print("price: ",price)
    # def set_price(self,price):
    #     self.price=price
    def get_price(self):
        print("Brand:",self.brand)
        print("charger_type",self.charger_type)
    @classmethod
    def info(cls,charger_type="Type-B"):
        print("Charger Type:",charger_type)
  
Iqoo=phone()
Iqoo.set_price("15000")
Iqoo.get_price()
Iqoo.info()
*********************************
Single
class Dad():
    def phone(self):
        print("dad's phone")
class son(Dad):
    def laptop(self):
        print("Son's laptop")
S1=son()
S1.laptop()
S1.phone()
************************************
Multiple
class Dad():
    def phone(self):
        print("dad's phone")
class Mom():
    def Snack(self):
        print("Mom's snack")
class son(Dad,Mom):
    def laptop(self):
        print("Son's laptop")
S1=son()
S1.laptop()
S1.phone()
S1.Snack()

*************************************
Multilevel
class grandpa():
    def money(self):
        print("grandpa 's Money")
class Dad(grandpa):
    def phone(self):
        print("dad's phone")
class son(Dad):
    def laptop(self):
        print("Son's laptop")
S1=son()
S1.laptop()
S1.phone()
S1.money()
*************************************
 Hirarchy
class dad():
    def money(self):
        print("dad's Money")
class land():
    def property(self):
        print("Single property")
class son1(dad,land):
    def phone(self):
        print("s1 Phone")
class son2(dad):
    def phone(self):
        print("s2 phone")
S1=son1()
S2=son2()
S1.phone()
S1.money()
S1.property()
S2.phone()
S2.money()
S2.property()
class BankAccount:
	def __init__(self):
		print("BA")
class SavingsAccount(BankAccount):
	def saac(self):
		print("SA")
class CurrentAccount(SavingsAccount):
	def cuac(self):
		print("CA")
out = CurrentAccount()
out.cuac()
Constructor Memory Space allocating default when objcet is created
class pythonlearning:
    def __init__(self):
        print("I enjoy learning ")
    def Learn(self):
        print("This is more Interesting")
out=pythonlearning()
out.Learn()
import mymodule
print(mymodule.greet("Ramesh"))
print(mymodule.add(15,9))
import mymodule
import importlib
print(mymodule.greet("Ramesh"))
# print(mymodule.add(15,9))
importlib.reload(mymodule)#Reload Function
print(mymodule.greet("Ramesh"))
code="""
def add(n):
    return n+n
print(add(10))
"""
exec(code)

Dirctroy location
import os
print(os.listdir("."))

import sys  #(kwargv & argv)
print("Arguments Passed:",sys.argv)#we print only terminal

class employee:
	def __init__(self,name,emp_id,department):
		self.name=name
		self.emp_id=emp_id
		self.department=department
class developer(employee):
	def __init__(self,name,emp_id,department,salary,program_lang):
		super().__init__(name,emp_id,department)
		self.salary=salary
		self.program_lang=program_lang
output=developer("Ramesh","D-040","IT","7500","Python")
print(f"Name:{output.name}")
print(f"emp_id:{output.emp_id}")
print(f"department:{output.department}")
print(f"salary:{output.salary}")
print(f"program_lang:{output.program_lang}")

class employee:
	def __init__(self,name,department):
		self.name=name
		self.department=department
class freelancer:
	def __init__(self,hourly_rate):
		self.hourly_rate=hourly_rate
class freelanceDeveloper(employee,freelancer):
	def __init__(self,name,department,hourly_rate):
		employee.__init__(self,name,department)
		freelancer.__init__(self,hourly_rate)
output=freelanceDeveloper("Ramesh","Python","500")
print(f"Name:{output.name}")
print(f"Department:{output.department}")
print(f"Hourly_rate:{output.hourly_rate}")

class person:
	def __init__(self,name):
		self.name=name
class employee(person):
	def __init__(self,name,emp_id):
		super().__init__(name)
		self.emp_id=emp_id
class manager(employee):
	def __init__(self,name,emp_id):
		super().__init__(name,emp_id)
out=manager("Ramesh","ITS-0040")
print(f"Name : {out.name}")
print(f"Employee ID : {out.emp_id}")

class person:
	def per_det(self):
		print("Person class")
class researcher(person):
	def res_per(self):
		print("Researcher Person")
class teacher(researcher):
	def tea_per(self):
		print("Researcher Person teacher")
out=teacher()
out.tea_per()
out.res_per()
out.per_det()

class BankAccount:
	def __init__(self):
		print("BA")
class SavingsAccount(BankAccount):
	def saac(self):
		print("SA")
class CurrentAccount(SavingsAccount):
	def cuac(self): 
		print("CA")
out = CurrentAccount()
out.cuac()

with open("Test1.txt","r") as file:
    code=file.read()
    exec(code)

file_path="E:\\Test1.txt"
with open(file_path,"r") as file:
    code=file.read()
    exec(code)

file_path="E:\\Test1.txt"
with open(file_path,"r")as file:
    code=file.read()
    exec(code)

file_path = "E:\\Test2.txt"
with open(file_path, "w") as file:
    file.write("print('Hello from Ramesh! This is Mulitification')\n")
    file.write("a = 10\n")
    file.write("b = 20\n")
    file.write("print('Mul:', a * b)\n")
print(f"File '{file_path}' has been created and written successfully!")
file_path="E:\\Test1.txt"
with open(file_path,"r")as file:
    code=file.read()
    exec(code)

file_path="E:\\Test2.txt"
with open(file_path,"w")as file:
    file.write("print('Nan panna test 2 project')\n")
    file.write("a=10\n")
    file.write("b=20\n")
    file.write("print('Mul:',a*b)\n")
with open(file_path,"r")as file:
    code=file.read()
    exec(code)

code = """
a = 10
b = 20
print("Sum:", a + b)
"""
exec(code)
file_path="E:\\Test2.txt"
with open(file_path, "r") as file:
    code = file.read()
    print(code)
def reverse(sentence):
	words=sentence.split()
	words.reverse()
	return " ".join(words)
sentence=input("Enter a word:")
print("Reversed Sentense is :",reverse(sentence))
def sec_larg(lists):
	numbers=set(lists)
	return sorted(numbers)[-2]
lists=[99,45,89,100,35,90]
print(sec_larg(lists))
def palindrome(word):
    if word==word[::-1]:
        print("Given Words is Palindrome")
    else:
        print("Given Word is non palindrome")
word=input("Enter a Palindrome name: ")
palindrome(word)
	5. Given a sentence, reverse the order of words.
def reverse(word):
    output=word.split()
    output.reverse()
    return " ".join(output)
word=input("Enter a Words")
print("Reverse word is ",reverse(word))
def reverse(sentence):
	words=sentence.split()
	words.reverse()
	return " ".join(words)
sentence=input("Enter a word:")
print("Reversed Sentense is :",reverse(sentence))
def sec_large(lists):
    output=set(lists)
    return sorted(output)[-2]
lists=[23,26,25,42,44]
result=sec_large(lists)
print("Second Largest Number is : ",result)
def palindrome(word):
    if word==word[::-1]:
        print("Given words is palindrome")
    else:
        print("Given words is not palindrome")
word=input("Enter a Sentense: ")
palindrome(word)
def rev_wrd(words):
	output=words.split()
	output.reverse()
	return " ".join(output)
words=input("Enter a sentance: ")
print("The Given word reversed : ",rev_wrd(words))
def most_freq(lists):
	return max(lists,key=lists.count)
lists=[1,2,3,2,4,5,3,1,2,3,2]
print(most_freq(lists))
