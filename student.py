from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management | SRMS")
        self.root.geometry("1200x600+80+80")
        self.root.config(bg="white")

        # ================= DATABASE =================
        self.con = sqlite3.connect("srms.db")
        self.cur = self.con.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS student(
                roll TEXT PRIMARY KEY,
                name TEXT,
                email TEXT,
                gender TEXT,
                dob TEXT,
                contact TEXT,
                course TEXT,
                adm_date TEXT,
                state TEXT,
                city TEXT,
                pin TEXT,
                address TEXT
            )
        """)
        self.con.commit()

        # ================= TITLE =================
        Label(self.root, text="Manage Student Details",
              font=("goudy old style", 20, "bold"),
              bg="#0b5377", fg="white").place(x=10, y=10, width=760, height=40)

        # ================= SEARCH =================
        Label(self.root, text="Search | Roll No.",
              font=("goudy old style", 15),
              bg="white").place(x=780, y=15)

        self.var_search = StringVar()
        Entry(self.root, textvariable=self.var_search,
              font=("goudy old style", 15),
              bg="lightyellow").place(x=950, y=15, width=150)

        Button(self.root, text="Search",
               font=("goudy old style", 15, "bold"),
               bg="#03a9f4", fg="white",
               command=self.search).place(x=1110, y=15, width=80)

        # ================= VARIABLES =================
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_adm_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # ================= LEFT FRAME =================
        left = Frame(self.root, bg="white")
        left.place(x=10, y=60, width=760, height=530)

        # ================= FORM =================
        Label(left, text="Roll No.", font=("goudy old style", 15), bg="white").place(x=10, y=10)
        Entry(left, textvariable=self.var_roll, font=("goudy old style", 15),
              bg="lightyellow").place(x=130, y=10, width=200)

        Label(left, text="D.O.B", font=("goudy old style", 15), bg="white").place(x=350, y=10)
        Entry(left, textvariable=self.var_dob, font=("goudy old style", 15),
              bg="lightyellow").place(x=580, y=10, width=160)

        Label(left, text="Name", font=("goudy old style", 15), bg="white").place(x=10, y=50)
        Entry(left, textvariable=self.var_name, font=("goudy old style", 15),
              bg="lightyellow").place(x=130, y=50, width=200)

        Label(left, text="Contact", font=("goudy old style", 15), bg="white").place(x=350, y=50)
        Entry(left, textvariable=self.var_contact, font=("goudy old style", 15),
              bg="lightyellow").place(x=580, y=50, width=160)

        Label(left, text="Email", font=("goudy old style", 15), bg="white").place(x=10, y=90)
        Entry(left, textvariable=self.var_email, font=("goudy old style", 15),
              bg="lightyellow").place(x=130, y=90, width=200)

        Label(left, text="Course", font=("goudy old style", 15), bg="white").place(x=350, y=90)
        ttk.Combobox(left, textvariable=self.var_course,
                     values=("Select", "Python", "Java", "Web", "Data Science"),
                     state="readonly",
                     font=("goudy old style", 14)).place(x=580, y=90, width=160)

        Label(left, text="Gender", font=("goudy old style", 15), bg="white").place(x=10, y=130)
        ttk.Combobox(left, textvariable=self.var_gender,
                     values=("Select", "Male", "Female", "Other"),
                     state="readonly",
                     font=("goudy old style", 14)).place(x=130, y=130, width=200)

        Label(left, text="Admission Date", font=("goudy old style", 15), bg="white").place(x=350, y=130)
        Entry(left, textvariable=self.var_adm_date, font=("goudy old style", 15),
              bg="lightyellow").place(x=580, y=130, width=160)

        Label(left, text="State", font=("goudy old style", 15), bg="white").place(x=10, y=170)
        Entry(left, textvariable=self.var_state, font=("goudy old style", 15),
              bg="lightyellow").place(x=130, y=170, width=200)

        Label(left, text="City", font=("goudy old style", 15), bg="white").place(x=350, y=170)
        Entry(left, textvariable=self.var_city, font=("goudy old style", 15),
              bg="lightyellow").place(x=580, y=170, width=160)

        Label(left, text="Address", font=("goudy old style", 15), bg="white").place(x=10, y=210)
        self.txt_address = Text(left, font=("goudy old style", 14),
                                bg="lightyellow")
        self.txt_address.place(x=130, y=210, width=200, height=80)

        Label(left, text="Pin Code", font=("goudy old style", 15), bg="white").place(x=350, y=210)
        Entry(left, textvariable=self.var_pin, font=("goudy old style", 15),
              bg="lightyellow").place(x=580, y=210, width=160)

        # ================= BUTTONS =================
        btn_frame = Frame(left, bg="white")
        btn_frame.place(x=130, y=320, width=500)

        Button(btn_frame, text="Save", bg="#2196f3", fg="white",
               font=("goudy old style", 14, "bold"),
               command=self.add_student).grid(row=0, column=0, padx=10)

        Button(btn_frame, text="Update", bg="#4caf50", fg="white",
               font=("goudy old style", 14, "bold"),
               command=self.update_student).grid(row=0, column=1, padx=10)

        Button(btn_frame, text="Delete", bg="#f44336", fg="white",
               font=("goudy old style", 14, "bold"),
               command=self.delete_student).grid(row=0, column=2, padx=10)

        Button(btn_frame, text="Clear", bg="#607d8b", fg="white",
               font=("goudy old style", 14, "bold"),
               command=self.clear).grid(row=0, column=3, padx=10)

        # ================= TABLE =================
        table_frame = Frame(self.root, bd=2, relief=RIDGE)
        table_frame.place(x=780, y=60, width=410, height=520)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            columns=("roll", "name", "email", "gender", "dob",
                     "contact", "course", "adm_date",
                     "state", "city", "pin", "address"),
            show="headings",
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        headings = ["Roll", "Name", "Email", "Gender", "DOB",
                    "Contact", "Course", "Adm Date",
                    "State", "City", "Pin", "Address"]

        for col, txt in zip(self.student_table["columns"], headings):
            self.student_table.heading(col, text=txt)
            self.student_table.column(col, width=120)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_data)

        self.fetch_all()

    # ================= FUNCTIONS =================
    def add_student(self):
        self.cur.execute("INSERT OR REPLACE INTO student VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                         (self.var_roll.get(), self.var_name.get(), self.var_email.get(),
                          self.var_gender.get(), self.var_dob.get(), self.var_contact.get(),
                          self.var_course.get(), self.var_adm_date.get(), self.var_state.get(),
                          self.var_city.get(), self.var_pin.get(),
                          self.txt_address.get("1.0", END)))
        self.con.commit()
        self.fetch_all()
        messagebox.showinfo("Success", "Student Saved Successfully")

    def fetch_all(self):
        self.student_table.delete(*self.student_table.get_children())
        self.cur.execute("SELECT * FROM student")
        for row in self.cur.fetchall():
            self.student_table.insert("", END, values=row)

    def get_data(self, ev):
        row = self.student_table.focus()
        data = self.student_table.item(row, "values")
        if data:
            (self.var_roll.set(data[0]), self.var_name.set(data[1]),
             self.var_email.set(data[2]), self.var_gender.set(data[3]),
             self.var_dob.set(data[4]), self.var_contact.set(data[5]),
             self.var_course.set(data[6]), self.var_adm_date.set(data[7]),
             self.var_state.set(data[8]), self.var_city.set(data[9]),
             self.var_pin.set(data[10]))
            self.txt_address.delete("1.0", END)
            self.txt_address.insert(END, data[11])

    def update_student(self):
        self.add_student()

    def delete_student(self):
        self.cur.execute("DELETE FROM student WHERE roll=?", (self.var_roll.get(),))
        self.con.commit()
        self.fetch_all()
        self.clear()

    def clear(self):
        for v in (self.var_roll, self.var_name, self.var_email, self.var_gender,
                  self.var_dob, self.var_contact, self.var_course,
                  self.var_adm_date, self.var_state, self.var_city, self.var_pin):
            v.set("")
        self.txt_address.delete("1.0", END)

    def search(self):
        self.student_table.delete(*self.student_table.get_children())
        self.cur.execute("SELECT * FROM student WHERE roll=?", (self.var_search.get(),))
        for row in self.cur.fetchall():
            self.student_table.insert("", END, values=row)


if __name__ == "__main__":
    root = Tk()
    studentClass(root)
    root.mainloop()
