from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Results | SRMS")
        self.root.geometry("1050x550+100+50")
        self.root.config(bg="#ecf0f1")

        # ================= VARIABLES =================
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()

        # ================= TITLE =================
        title = Label(self.root, text="Manage Student Results", font=("times new roman", 22, "bold"),
                      bg="#34495e", fg="white", pady=10)
        title.pack(fill=X)

        # ================= INPUT FRAME =================
        input_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        input_frame.place(x=20, y=60, width=400, height=470)

        Label(input_frame, text="Roll No:", font=("times new roman", 14), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        Entry(input_frame, textvariable=self.var_roll, font=("times new roman", 14)).grid(row=0, column=1, padx=10, pady=10)

        Label(input_frame, text="Name:", font=("times new roman", 14), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        Entry(input_frame, textvariable=self.var_name, font=("times new roman", 14)).grid(row=1, column=1, padx=10, pady=10)

        Label(input_frame, text="Course:", font=("times new roman", 14), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        Entry(input_frame, textvariable=self.var_course, font=("times new roman", 14)).grid(row=2, column=1, padx=10, pady=10)

        Label(input_frame, text="Marks Obtained:", font=("times new roman", 14), bg="white").grid(row=3, column=0, padx=10, pady=10, sticky=W)
        Entry(input_frame, textvariable=self.var_marks, font=("times new roman", 14)).grid(row=3, column=1, padx=10, pady=10)

        Label(input_frame, text="Full Marks:", font=("times new roman", 14), bg="white").grid(row=4, column=0, padx=10, pady=10, sticky=W)
        Entry(input_frame, textvariable=self.var_full_marks, font=("times new roman", 14)).grid(row=4, column=1, padx=10, pady=10)

        # ================= BUTTONS =================
        btn_frame = Frame(input_frame, bg="white")
        btn_frame.place(x=10, y=250, width=370)

        Button(btn_frame, text="Add", width=8, command=self.add_result, bg="#27ae60", fg="white").grid(row=0, column=0, padx=5, pady=10)
        Button(btn_frame, text="Update", width=8, command=self.update_result, bg="#2980b9", fg="white").grid(row=0, column=1, padx=5, pady=10)
        Button(btn_frame, text="Delete", width=8, command=self.delete_result, bg="#c0392b", fg="white").grid(row=0, column=2, padx=5, pady=10)
        Button(btn_frame, text="Clear", width=8, command=self.clear_fields, bg="#7f8c8d", fg="white").grid(row=0, column=3, padx=5, pady=10)

        # ================= RESULT TABLE =================
        table_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=440, y=60, width=590, height=470)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.result_table = ttk.Treeview(table_frame,
                                         columns=("rid", "roll", "name", "course", "marks", "full_marks"),
                                         xscrollcommand=scroll_x.set,
                                         yscrollcommand=scroll_y.set,
                                         show="headings")
        scroll_x.config(command=self.result_table.xview)
        scroll_y.config(command=self.result_table.yview)

        # Table headings
        for col, width in zip(
            ["rid", "roll", "name", "course", "marks", "full_marks"],
            [50, 80, 150, 120, 100, 100]
        ):
            self.result_table.heading(col, text=col.replace("_", " ").title())
            self.result_table.column(col, width=width, anchor=CENTER)

        self.result_table.pack(fill=BOTH, expand=1)
        self.result_table.bind("<ButtonRelease-1>", self.get_cursor)

        # Load data
        self.show_results()

    # ================= FUNCTIONS =================
    def add_result(self):
        if self.var_roll.get() == "" or self.var_marks.get() == "" or self.var_full_marks.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return
        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO result (roll, name, course, marks, full_marks) VALUES (?, ?, ?, ?, ?)",
                        (self.var_roll.get(), self.var_name.get(), self.var_course.get(), self.var_marks.get(), self.var_full_marks.get()))
            con.commit()
            messagebox.showinfo("Success", "Result added successfully")
            self.show_results()
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")
        finally:
            con.close()

    def show_results(self):
        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        try:
            self.result_table.delete(*self.result_table.get_children())
            cur.execute("SELECT rid, roll, name, course, marks, full_marks FROM result")
            rows = cur.fetchall()
            for row in rows:
                self.result_table.insert("", END, values=row)
        finally:
            con.close()

    def get_cursor(self, event=""):
        cursor_row = self.result_table.focus()
        contents = self.result_table.item(cursor_row)
        row = contents["values"]
        if row:
            self.var_roll.set(row[1])
            self.var_name.set(row[2])
            self.var_course.set(row[3])
            self.var_marks.set(row[4])
            self.var_full_marks.set(row[5])

    def update_result(self):
        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        try:
            cur.execute("UPDATE result SET roll=?, name=?, course=?, marks=?, full_marks=? WHERE rid=?",
                        (self.var_roll.get(), self.var_name.get(), self.var_course.get(),
                         self.var_marks.get(), self.var_full_marks.get(), self.result_table.focus()))
            con.commit()
            messagebox.showinfo("Success", "Result updated successfully")
            self.show_results()
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")
        finally:
            con.close()

    def delete_result(self):
        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        try:
            selected = self.result_table.focus()
            if not selected:
                messagebox.showerror("Error", "Please select a record to delete")
                return
            values = self.result_table.item(selected, "values")
            rid = values[0]
            cur.execute("DELETE FROM result WHERE rid=?", (rid,))
            con.commit()
            messagebox.showinfo("Deleted", "Result deleted successfully")
            self.show_results()
            self.clear_fields()
        finally:
            con.close()

    def clear_fields(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")


# ================= RUN DIRECTLY =================
if __name__ == "__main__":
    root = Tk()
    ResultClass(root)
    root.mainloop()
