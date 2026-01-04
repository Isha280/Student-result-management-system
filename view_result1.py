from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class ViewResult:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1000x550+150+80")
        self.root.config(bg="white")

        # ================= VARIABLES =================
        self.var_roll = StringVar()

        # ================= DATABASE =================
        self.con = sqlite3.connect("srms.db")
        self.cur = self.con.cursor()

        # ================= TITLE =================
        title = Label(
            self.root,
            text="View Student Results",
            font=("times new roman", 26, "bold"),
            bg="#f4a300",
            fg="black"
        )
        title.pack(fill=X)

        # ================= SEARCH FRAME =================
        search_frame = Frame(self.root, bg="white")
        search_frame.place(x=150, y=90, width=700, height=60)

        lbl_search = Label(
            search_frame,
            text="Search By | Roll No.",
            font=("times new roman", 14),
            bg="white"
        )
        lbl_search.grid(row=0, column=0, padx=10)

        txt_search = Entry(
            search_frame,
            textvariable=self.var_roll,
            font=("times new roman", 14),
            bg="#ffffe0"
        )
        txt_search.grid(row=0, column=1, padx=10)

        btn_search = Button(
            search_frame,
            text="Search",
            font=("times new roman", 12, "bold"),
            bg="#3498db",
            fg="white",
            cursor="hand2",
            command=self.search
        )
        btn_search.grid(row=0, column=2, padx=10, ipadx=10)

        btn_clear = Button(
            search_frame,
            text="Clear",
            font=("times new roman", 12, "bold"),
            bg="lightgray",
            cursor="hand2",
            command=self.clear
        )
        btn_clear.grid(row=0, column=3, padx=10, ipadx=10)

        # ================= TABLE FRAME =================
        table_frame = Frame(self.root, bd=2, relief=RIDGE)
        table_frame.place(x=50, y=170, width=900, height=250)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.result_table = ttk.Treeview(
            table_frame,
            columns=(
                "roll",
                "name",
                "course",
                "marks",
                "total",
                "percentage"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
            show="headings"
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.result_table.xview)
        scroll_y.config(command=self.result_table.yview)

        self.result_table.heading("roll", text="Roll No")
        self.result_table.heading("name", text="Name")
        self.result_table.heading("course", text="Course")
        self.result_table.heading("marks", text="Marks Obtained")
        self.result_table.heading("total", text="Total Marks")
        self.result_table.heading("percentage", text="Percentage")

        self.result_table.column("roll", width=100, anchor=CENTER)
        self.result_table.column("name", width=180)
        self.result_table.column("course", width=150)
        self.result_table.column("marks", width=130, anchor=CENTER)
        self.result_table.column("total", width=120, anchor=CENTER)
        self.result_table.column("percentage", width=120, anchor=CENTER)

        self.result_table.pack(fill=BOTH, expand=1)

        self.result_table.bind("<ButtonRelease-1>", self.get_data)

        # ================= DELETE BUTTON =================
        btn_delete = Button(
            self.root,
            text="Delete",
            font=("times new roman", 14, "bold"),
            bg="red",
            fg="white",
            cursor="hand2",
            command=self.delete
        )
        btn_delete.place(x=430, y=450, width=140, height=40)

        self.show()

    # ================= FUNCTIONS =================
    def show(self):
        self.result_table.delete(*self.result_table.get_children())
        self.cur.execute(
            "SELECT roll, name, course, marks, total, percentage FROM result"
        )
        rows = self.cur.fetchall()
        for row in rows:
            self.result_table.insert("", END, values=row)

    def search(self):
        if self.var_roll.get() == "":
            messagebox.showerror("Error", "Roll No is required")
            return

        self.result_table.delete(*self.result_table.get_children())
        self.cur.execute(
            "SELECT roll, name, course, marks, total, percentage FROM result WHERE roll=?",
            (self.var_roll.get(),)
        )
        rows = self.cur.fetchall()

        if rows:
            for row in rows:
                self.result_table.insert("", END, values=row)
        else:
            messagebox.showinfo("Info", "No record found")

    def clear(self):
        self.var_roll.set("")
        self.show()

    def get_data(self, ev):
        f = self.result_table.focus()
        content = self.result_table.item(f)
        row = content["values"]
        if row:
            self.var_roll.set(row[0])

    def delete(self):
        if self.var_roll.get() == "":
            messagebox.showerror("Error", "Select a record first")
            return

        op = messagebox.askyesno("Confirm", "Do you really want to delete?")
        if op:
            self.cur.execute(
                "DELETE FROM result WHERE roll=?",
                (self.var_roll.get(),)
            )
            self.con.commit()
            messagebox.showinfo("Deleted", "Result deleted successfully")
            self.clear()


# ================= RUN FILE =================
if __name__ == "__main__":
    root = Tk()
    ViewResult(root)
    root.mainloop()
