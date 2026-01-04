from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Management")
        self.root.geometry("1200x500+80+80")
        self.root.config(bg="white")
        self.root.focus_force()

        # ===== TITLE =====
        Label(
            self.root,
            text="Manage Course Details",
            font=("goudy old style", 22, "bold"),
            bg="#033054",
            fg="white",
            pady=10
        ).pack(fill=X)

        # ===== VARIABLES =====
        self.var_cid = StringVar()
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.var_search = StringVar()

        # ===== FORM LABELS =====
        Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=80)
        Label(self.root, text="Duration", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=120)
        Label(self.root, text="Charges", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=160)
        Label(self.root, text="Description", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=200)

        # ===== FORM ENTRIES =====
        Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=80, width=300)
        Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=120, width=300)
        Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=160, width=300)

        self.txt_description = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_description.place(x=150, y=200, width=500, height=120)

        # ===== BUTTONS =====
        Button(self.root, text="Save", font=("goudy old style", 15, "bold"),
               bg="#2196f3", fg="white", command=self.add).place(x=150, y=340, width=110, height=40)

        Button(self.root, text="Update", font=("goudy old style", 15, "bold"),
               bg="#4caf50", fg="white", command=self.update).place(x=270, y=340, width=110, height=40)

        Button(self.root, text="Delete", font=("goudy old style", 15, "bold"),
               bg="#f44336", fg="white", command=self.delete).place(x=390, y=340, width=110, height=40)

        Button(self.root, text="Clear", font=("goudy old style", 15, "bold"),
               bg="#607d8b", fg="white", command=self.clear).place(x=510, y=340, width=110, height=40)

        # ===== SEARCH FRAME =====
        search_frame = LabelFrame(
            self.root, text="Search Course",
            font=("goudy old style", 14, "bold"),
            bg="white", bd=2, relief=RIDGE
        )
        search_frame.place(x=720, y=60, width=470, height=80)

        Label(search_frame, text="Course Name",
              font=("goudy old style", 13), bg="white").place(x=15, y=25)

        Entry(search_frame, textvariable=self.var_search,
              font=("goudy old style", 13),
              bg="lightyellow").place(x=120, y=23, width=180, height=28)

        Button(search_frame, text="Search",
               font=("goudy old style", 13, "bold"),
               bg="#4caf50", fg="white",
               command=self.search).place(x=315, y=20, width=65, height=32)

        Button(search_frame, text="Show All",
               font=("goudy old style", 13, "bold"),
               bg="#607d8b", fg="white",
               command=self.show).place(x=385, y=20, width=75, height=32)

        # ===== TABLE FRAME =====
        table_frame = Frame(self.root, bd=2, relief=RIDGE)
        table_frame.place(x=720, y=150, width=470, height=300)

        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(
            table_frame,
            columns=("cid", "name", "duration", "charges", "description"),
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.CourseTable.xview)
        scroll_y.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Course Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")

        self.CourseTable["show"] = "headings"

        self.CourseTable.column("cid", width=60)
        self.CourseTable.column("name", width=120)
        self.CourseTable.column("duration", width=80)
        self.CourseTable.column("charges", width=80)
        self.CourseTable.column("description", width=200)

        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    # ===== FUNCTIONS =====
    def get_data(self, ev):
        row = self.CourseTable.focus()
        data = self.CourseTable.item(row)['values']
        if data:
            self.var_cid.set(data[0])
            self.var_course.set(data[1])
            self.var_duration.set(data[2])
            self.var_charges.set(data[3])
            self.txt_description.delete("1.0", END)
            self.txt_description.insert(END, data[4])

    def add(self):
        if self.var_course.get() == "":
            messagebox.showerror("Error", "Course name required", parent=self.root)
            return
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("INSERT INTO course(name,duration,charges,description) VALUES (?,?,?,?)",
                    (self.var_course.get(), self.var_duration.get(),
                     self.var_charges.get(), self.txt_description.get("1.0", END)))
        con.commit()
        con.close()
        self.show()
        self.clear()

    def update(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("UPDATE course SET name=?,duration=?,charges=?,description=? WHERE cid=?",
                    (self.var_course.get(), self.var_duration.get(),
                     self.var_charges.get(), self.txt_description.get("1.0", END),
                     self.var_cid.get()))
        con.commit()
        con.close()
        self.show()

    def delete(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("DELETE FROM course WHERE cid=?", (self.var_cid.get(),))
        con.commit()
        con.close()
        self.show()
        self.clear()

    def clear(self):
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0", END)

    def show(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM course")
        rows = cur.fetchall()
        self.CourseTable.delete(*self.CourseTable.get_children())
        for row in rows:
            self.CourseTable.insert("", END, values=row)
        con.close()

    def search(self):
        if self.var_search.get() == "":
            messagebox.showerror("Error", "Enter course name to search", parent=self.root)
            return
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM course WHERE name LIKE ?", ('%' + self.var_search.get() + '%',))
        rows = cur.fetchall()
        self.CourseTable.delete(*self.CourseTable.get_children())
        for row in rows:
            self.CourseTable.insert("", END, values=row)
        con.close()


# ===== MAIN =====
if __name__ == "__main__":
    root = Tk()
    CourseClass(root)
    root.mainloop()
