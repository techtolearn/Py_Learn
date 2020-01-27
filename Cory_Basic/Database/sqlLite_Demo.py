import  sqlite3
from Employee import Employee

# conn = sqlite3.connect('employee.db')   # it create the file name with employee if it doesn't exist else it does simply connects
conn = sqlite3.connect(':memory:')   # memory keyword - will clean the data and run with fresh entry
c = conn.cursor()

c.execute("""CREATE TABLE employee(
            first text,
            last text,
            pay integer
            )""")

def insert_emp(emp):
    with conn:   # using this will auto commit transactions
        c.execute("INSERT INTO employee VALUES (:first, :last, :pay)", {'first':emp.first,'last':emp.last,'pay': emp.pay}) # Dictionary method

def get_emp_by_name(lastname):
    c.execute("SELECT * FROM employee where last=:last", {'last': lastname})
    return  c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employee  SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove(emp):
    with conn:
        c.execute("DELETE FROM employee WHERE first = :first AND last = :last",
                  {'first':emp.first, 'last':emp.last})

# indirect insertion through class
emp1 = Employee('satheeh','kumar',1000000)
emp2 = Employee('Ram','kumar',2000000)

insert_emp(emp1)
insert_emp(emp2)

emps = get_emp_by_name('kumar')
print(emps)

update_pay(emp2, 10000)
remove(emp1)

emp = get_emp_by_name('kumar')
print(emp)

conn.close()


# Direct insertion
# c.execute("INSERT INTO employee VALUES ('Tanvi','Satheesh','60000')")
# conn.commit()
# c.execute("INSERT INTO employee VALUES ('Divya','Satheesh','70000')")
# conn.commit()

# c.execute("DELETE FROM employee WHERE first='Divya'")




# c.execute("INSERT INTO employee VALUES (?,?,?)", (emp1.first,emp1.last,emp1.pay))   # tuple method
# conn.commit()
# #or
# c.execute("INSERT INTO employee VALUES (:first, :last, :pay)", {'first':emp2.first,'last':emp2.last,'pay': emp2.pay}) # Dictionary method
# conn.commit()
#
# c.execute("SELECT * FROM employee where last=?",('Satheesh',))
# # print(c.fetchone())  #it fetch the rows, you can pass number of rows you want fectch
# print(c.fetchall())   # it fetch all rows,
#  #or
# c.execute("SELECT * FROM employee where last=:last", {'last': 'kumar'})
# print(c.fetchall())
# conn.commit()


