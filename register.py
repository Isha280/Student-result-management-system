from tkinter import *
from tkinter import ttk, messagebox

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # ================= LEFT FRAME =================
        left_frame = Frame(self.root, bg="#08224A")
        left_frame.place(x=80, y=100, width=450, height=500)

        Label(left_frame, text="SOCIAL IMPACT",
              font=("times new roman", 28, "bold"),
              fg="white", bg="#08224A").place(x=50, y=120)

        Label(left_frame,
              text="Our reach, scale &\ncommitment has given millions\n"
                   "a merit based access to life\nchanging opportunities.",
              font=("times new roman", 13),
              fg="white", bg="#08224A",
              justify=LEFT).place(x=50, y=190)

        # ================= RIGHT FRAME =================
        right_frame = Frame(self.root, bg="white")
        right_frame.place(x=530, y=100, width=700, height=500)

        Label(right_frame, text="REGISTER HERE",
              font=("times new roman", 22, "bold"),
              fg="green", bg="white").place(x=20, y=20)

        # First Name
        Label(right_frame, text="First Name",
              font=("times new roman", 14),
              bg="white").place(x=20, y=80)
        self.txt_fname = Entry(right_frame, font=("times new roman", 14), bg="lightgray")
        self.txt_fname.place(x=20, y=110, width=250)

        # Last Name
        Label(right_frame, text="Last Name",
              font=("times new roman", 14),
              bg="white").place(x=350, y=80)
        self.txt_lname = Entry(right_frame, font=("times new roman", 14), bg="lightgray")
        self.txt_lname.place(x=350, y=110, width=250)

        # Contact
        Label(right_frame, text="Contact No.",
              font=("times new roman", 14),
              bg="white").place(x=20, y=160)
        self.txt_contact = Entry(right_frame, font=("times new roman", 14), bg="lightgray")
        self.txt_contact.place(x=20, y=190, width=250)

        # Email
        Label(right_frame, text="Email",
              font=("times new roman", 14),
              bg="white").place(x=350, y=160)
        self.txt_email = Entry(right_frame, font=("times new roman", 14), bg="lightgray")
        self.txt_email.place(x=350, y=190, width=250)

        # Security Question
        Label(right_frame, text="Security Question",
              font=("times new roman", 14),
              bg="white").place(x=20, y=240)
        self.cmb_quest = ttk.Combobox(right_frame, state="readonly",
                                      font=("times new roman", 13))
        self.cmb_quest["values"] = ("Select",
                                    "Your First Pet Name",
                                    "Your Birth Place",
                                    "Your Best Friend Name")
        self.cmb_quest.current(0)
        self.cmb_quest.place(x=20, y=270, width=250)

        # Answer
        Label(right_frame, text="Answer",
              font=("times new roman", 14),
              bg="white").place(x=350, y=240)
        self.txt_answer = Entry(right_frame, font=("times new roman", 14), bg="lightgray")
        self.txt_answer.place(x=350, y=270, width=250)

        # Password
        Label(right_frame, text="Password",
              font=("times new roman", 14),
              bg="white").place(x=20, y=320)
        self.txt_pass = Entry(right_frame, font=("times new roman", 14),
                              bg="lightgray", show="*")
        self.txt_pass.place(x=20, y=350, width=250)

        # Confirm Password
        Label(right_frame, text="Confirm Password",
              font=("times new roman", 14),
              bg="white").place(x=350, y=320)
        self.txt_cpass = Entry(right_frame, font=("times new roman", 14),
                               bg="lightgray", show="*")
        self.txt_cpass.place(x=350, y=350, width=250)

        self.var_chk = IntVar()
        Checkbutton(right_frame,
                    text="I Agree The Terms & Conditions",
                    variable=self.var_chk,
                    bg="white",
                    font=("times new roman", 12)).place(x=20, y=390)

        Button(right_frame, text="REGISTER NOW →",
               font=("times new roman", 15, "bold"),
               bg="green", fg="white",
               width=20, cursor="hand2",
               command=self.register_data).place(x=200, y=430)

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_email.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txt_pass.get() != self.txt_cpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same")
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please agree to terms & conditions")
        else:
            messagebox.showinfo("Success", "Registered Successfully")
