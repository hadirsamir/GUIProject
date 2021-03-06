from tkinter import *
from tkinter import messagebox

# Import DBManager
from DBManager import *

# Import Utils
from Utils import *

class Grades:
    # Constructor
    def __init__(self, parentTopLevel):
        # Create Current Window.
        self.currentTopLevel = Toplevel(parentTopLevel) # Current Window from the parent TopLevel Window.
        self.currentTopLevel.wm_title("Grades")

        # Add to the current window Frames
        self.currentFrame = Frame(self.currentTopLevel)
        self.currentFrame.pack()

        # Add to the current frame labels, textArea and buttons.
        lab1 = Label(self.currentFrame, text = "Student name").pack(fill=X)

        # The Add Student text area.
        self.searchNameBox= addEntryTextToFrame(self.currentFrame,True)

        # Add Buttons.
        addButtonToFrame(self.currentFrame, "Search", X, self.search_query)
        addButtonToFrame(self.currentFrame, "Insert", X, self.insert_query)
        addButtonToFrame(self.currentFrame, "Delete", X, self.delete_query)

        # Bool Flag
        self.studentIsDisplayed = False

    def search_query(self,event):
        check=self.searchNameBox.get()
        rows.execute("SELECT _id, name, age FROM students WHERE name LIKE %s",(check.lower(),))
        student =rows.fetchone()
        if student is None:
           messagebox.showinfo("Warning","Your search query doesn't match any student!");
        else:
            if(not(self.studentIsDisplayed)):
                # messagebox.showinfo("Message","%s is found"%student[2])
                Label(self.currentFrame, text="Name =").pack(fill=X)
                self.nameEntry = addEntryTextToFrame(self.currentFrame, placeHolderText=student[1])
                self.idLabel = Label(self.currentFrame, text="ID = " + str(student[0]))
                self.idLabel.pack(fill=X)
                self.idEntry = student[0];
                Label(self.currentFrame, text="Age = ").pack(fill=X)
                self.ageEntry = addEntryTextToFrame(self.currentFrame, placeHolderText=student[2])
                addButtonToFrame(self.currentFrame, "Update", X, self.update_query)
                self.studentIsDisplayed = True
            else:
                self.nameEntry.delete(0, len(self.nameEntry.get()))
                self.nameEntry.insert(0, student[1])
                self.idLabel.configure(text="ID = " + str(student[0]))
                self.idEntry = student[0];
                self.ageEntry.delete(0, len(self.ageEntry.get()))
                self.ageEntry.insert(0, student[2])


        #print(results,check)

    def insert_query(self,event):
     self.newWindow = Toplevel(self.currentTopLevel)
     self.newWindow.wm_title("Insert")
     self.currentFrame = Frame(self.newWindow)
     self.currentFrame.pack()
     label1= Label(self.currentFrame, text = "Student's name").pack(fill=X)
     self.firstentry=addEntryTextToFrame(currentFrame=self.currentFrame,addFocus=True)
     self.addname=self.firstentry.get()
     #label2= Label(self.currentFrame, text = "Student's id").pack(fill=X)
     #self.idEntry=addEntryTextToFrame(self.currentFrame,addFocus=True)
    # self.addid=self.idEntry.get()
     label3= Label(self.currentFrame, text="Student's age").pack(fill=X)
     self.ageEntry=addEntryTextToFrame(self.currentFrame,addFocus=True)
     #self.addage=self.ageEntry.get()
     self.insertbutton=addButtonToFrame(self.currentFrame,"insert",X,self.confirm)

    def confirm(self,event):

     rows.execute("INSERT INTO students (name, age)  VALUES (%s, %s)",(self.firstentry.get(),str(self.ageEntry.get()),))
     mariadb_connection.commit()
 # check2=self.input1.get()
        # StrSql2=rows.execute("INSERT INTO students (name)VALUES (%s)",(check2,))
        # mariadb_connection .commit()

    def delete_query(self,event):
        check3=self.searchNameBox.get()
        StrSql3=rows.execute("DELETE FROM students WHERE name=%s",(check3,))
        mariadb_connection.commit()

    def update_query(self, event):
        # Check Name is valid TODO
        # Check Valid age ToDo
        rows.execute("UPDATE students SET name = %s , age = %s WHERE _id = %s", ( self.nameEntry.get(), str(self.ageEntry.get()), str(self.idEntry)))
        mariadb_connection.commit();
        return 1
