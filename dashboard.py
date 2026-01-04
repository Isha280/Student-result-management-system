from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from course import CourseClass
from student import studentClass
from result import ResultClass
from view_result1 import ViewResult


class RMS(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.place(relwidth=1, relheight=1)

        parent.title("Student Result Management System")
        parent.state("zoomed")
        parent.config(bg="white")

        self.FOOTER_H = 40
        self.DASH_H = 120

        # ================= TITLE =================
        logo = Image.open("images/logo.png").resize((50, 50), Image.Resampling.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(logo)

        Label(
            self,
            text="  Student Result Management System",
            image=self.logo_img,
            compound=LEFT,
            font=("goudy old style", 22, "bold"),
            bg="#033054",
            fg="white"
        ).pack(fill=X)

        # ================= MENU =================
        menu = LabelFrame(self, text="Menus",
                          font=("times new roman", 14, "bold"),
                          bg="white", bd=2)
        menu.pack(fill=X, padx=10, pady=8)

        btn_font = ("goudy old style", 14, "bold")
        items = [
            ("Course", self.add_course),
            ("Student", self.add_student),
            ("Result", self.add_result),
            ("View Student Result", self.view_results),
            ("Logout", lambda: controller("login")),
            ("Exit", parent.destroy)
        ]

        for i, (txt, cmd) in enumerate(items):
            Button(
                menu,
                text=txt,
                font=btn_font,
                bg="#0b5377" if txt != "Exit" else "red",
                fg="white",
                bd=0,
                cursor="hand2",
                command=cmd
            ).grid(row=0, column=i, padx=5, pady=8, sticky="nsew")
            menu.columnconfigure(i, weight=1)

        # ================= BODY =================
        self.body = Frame(self, bg="white")
        self.body.pack(fill=BOTH, expand=True)

        # ================= DASHBOARD =================
        dash = Frame(self.body, bg="white", bd=2, relief=RIDGE)
        dash.pack(side=BOTTOM, fill=X, padx=10, pady=5)

        c, s, r = self.get_counts()

        self.make_box(dash, f"Total Courses\n[{c}]", "#e43b06")
        self.make_box(dash, f"Total Students\n[{s}]", "#0676ad")
        self.make_box(dash, f"Total Results\n[{r}]", "#038074")

        # ================= FOOTER =================
        Label(
            self,
            text="SRMS - Student Result Management System | Contact: 987XXXX01",
            font=("goudy old style", 12),
            bg="#262626",
            fg="white"
        ).pack(side=BOTTOM, fill=X)

        # ================= BACKGROUND =================
        self.after(200, self.load_background)

    # ================= HELPERS =================
    def make_box(self, parent, text, color):
        Label(
            parent,
            text=text,
            font=("goudy old style", 18),
            bg=color,
            fg="white",
            bd=10,
            relief=RIDGE
        ).pack(side=LEFT, expand=True, fill=BOTH, padx=10, pady=10)

    def load_background(self):
        bw = self.body.winfo_width()
        bh = self.body.winfo_height() - self.DASH_H - 10

        if bw <= 0 or bh <= 0:
            self.after(200, self.load_background)
            return

        bg = Image.open("images/bg.jpg").resize((bw, bh), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(bg)

        Label(self.body, image=self.bg_img).place(
            x=0, y=0, width=bw, height=bh
        )

    # ================= FUNCTIONS =================
    def add_course(self):
        CourseClass(Toplevel(self))

    def add_student(self):
        studentClass(Toplevel(self))

    def add_result(self):
        ResultClass(Toplevel(self))

    def view_results(self):
        ViewResult(Toplevel(self))

    def get_counts(self):
        con = sqlite3.connect("srms.db")
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM course")
        c = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM student")
        s = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM result")
        r = cur.fetchone()[0]
        con.close()
        return c, s, r
