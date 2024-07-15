import mariadb
import sys
import os
from dotenv import load_dotenv

load_dotenv()

try:
   conn = mariadb.connect(
      host=os.getenv("HOST"),
      user=os.getenv("MYSQL_USER"),
      password=os.getenv("MYSQL_PASSWORD"))
except mariadb.Error as e:
   print(f"Error connecting to the database: {e}")
   sys.exit(1)

#Connecting cursor to variable cur
cur=conn.cursor()
#Opening database 'new'
cur.execute("use new;")
#Deleting the table projects
cur.execute("drop table projects;")
conn.commit()
#Creating a table projects
cur.execute("create table projects(project_id int,project_name varchar(255) not null,begin_date date,end_date date,cost decimal(15,2) not null);")
cur.execute("describe projects;")
row= cur.fetchall()
print(*row, sep='\n')
print("\n")
#Inserting rows of values to the table
cur.execute("insert into projects values(2,'second','1/2/12','2/2/12',75);")
cur.execute("insert into projects values(1,'first','2/2/12','3/2/12',50);")
cur.execute("insert into projects values(3,'third','3/2/12','4/2/12',100);")
cur.execute("select * from projects;")
row= cur.fetchall()
print(*row, sep='\n')
print("\n")
#Adding a new column called Incharge
cur.execute("alter table projects add incharge varchar(255);")
cur.execute("select * from projects;")
row= cur.fetchall()
print(*row, sep='\n')
print("\n")
#Updating project_id as primary key
cur.execute("alter table projects add primary key(project_id);")
cur.execute("describe projects;")
row= cur.fetchall()
print(*row, sep='\n')
print("\n")
#Adding the values to the new column incharge
cur.execute("update projects set incharge='Prateek' where project_id=1;")
cur.execute("update projects set incharge='Nishtha' where project_id=2;")
cur.execute("update projects set incharge='Karan' where project_id=3;")
cur.execute("select * from projects;")
row= cur.fetchall()
print(*row, sep='\n')
print("\n")
#Printing the table content in descending order
cur.execute("select * from projects order by project_id desc;")
row= cur.fetchall()
print(*row, sep='\n')
print("\n")
#Displaying the minimum amount in the cost column
cur.execute("select min(cost) from projects;")
row= cur.fetchall()
print(*row, sep='\n')
print("\n")
#Displaying the columns incharge and project_id only
cur.execute("select incharge as Contactperson, project_id as ID from projects;")
row= cur.fetchall()
print(*row, sep='\n')
print("\n")
#Deleting a column
cur.execute("alter table projects drop column begin_date;")
cur.execute("select * from projects;")
row= cur.fetchall()
print(*row, sep='\n')
print("\n")

#Closing Connection
conn.close()