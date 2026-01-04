from tkinter import *
from tkinter import messagebox

class ForgotPassword:
    def __init__(self, root):
        self.root = root
        self.root.title("Forgot Password")
        self.root.geometry("500x400+400+200")
        self.root.config(bg="white")

        Label(root, text="FORGOT PASSWORD",
              font=("times new roman", 22, "bold"),
              fg="#B71540", bg="white").pack(pady=20)

        Label(root, text="Email Address",
              font=("times new roman", 14),
              bg="white").pack(pady=5)

        self.txt_email = Entry(root, font=("times new roman", 14), bg="lightgray")
        self.txt_email.pack(pady=10, ipadx=80)

        Label(root, text="New Password",
              font=("times new roman", 14),
              bg="white").pack(pady=5)

        self.txt_new = Entry(root, font=("times new roman", 14),
                             bg="lightgray", show="*")
        self.txt_new.pack(pady=10, ipadx=80)

        Label(root, text="Confirm Password",
              font=("times new roman", 14),
              bg="white").pack(pady=5)

        self.txt_cnew = Entry(root, font=("times new roman", 14),
                              bg="lightgray", show="*")
        self.txt_cnew.pack(pady=10, ipadx=80)

        Button(root, text="RESET PASSWORD",
               font=("times new roman", 14, "bold"),
               bg="#0097E6", fg="white",
               width=18, command=self.reset).pack(pady=20)

    def reset(self):
        if self.txt_email.get() == "" or self.txt_new.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txt_new.get() != self.txt_cnew.get():
            messagebox.showerror("Error", "Passwords do not match")
        else:
            messagebox.showinfo("Success", "Password Reset Successfully")
