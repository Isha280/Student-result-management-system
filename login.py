from tkinter import *
from tkinter import messagebox
from register import Register
from forgot_password import ForgotPassword

class Login(Frame):
    def __init__(self, root, switch_frame):
        super().__init__(root)
        self.root = root
        self.switch_frame = switch_frame
        self.place(relwidth=1, relheight=1)

        self.root.title("Login Window")
        self.root.geometry("1100x600+100+50")
        self.root.config(bg="#0A3D62")

        # ================= MAIN FRAME =================
        main_frame = Frame(self, bg="white")
        main_frame.place(x=80, y=80, width=950, height=450)

        # ================= LEFT FRAME =================
        left_frame = Frame(main_frame, bg="#061A2D")
        left_frame.place(x=0, y=0, width=350, height=450)

        Label(left_frame, text="WebCode Clock",
              font=("times new roman", 22, "bold"),
              fg="white", bg="#061A2D").place(x=60, y=30)

        Label(left_frame,
              text="Login System\nPython Tkinter Project",
              font=("times new roman", 14),
              fg="white", bg="#061A2D",
              justify=LEFT).place(x=50, y=120)

        # ================= RIGHT FRAME =================
        right_frame = Frame(main_frame, bg="white")
        right_frame.place(x=350, y=0, width=600, height=450)

        Label(right_frame, text="LOGIN HERE",
              font=("times new roman", 22, "bold"),
              fg="#0097E6", bg="white").place(x=200, y=40)

        # Email
        Label(right_frame, text="EMAIL ADDRESS",
              font=("times new roman", 13, "bold"),
              fg="gray", bg="white").place(x=150, y=120)

        self.txt_email = Entry(right_frame, font=("times new roman", 14), bg="lightgray")
        self.txt_email.place(x=150, y=150, width=300, height=30)

        # Password
        Label(right_frame, text="PASSWORD",
              font=("times new roman", 13, "bold"),
              fg="gray", bg="white").place(x=150, y=200)

        self.txt_pass = Entry(right_frame, font=("times new roman", 14),
                              bg="lightgray", show="*")
        self.txt_pass.place(x=150, y=230, width=300, height=30)

        # Links
        lbl_reg = Label(right_frame, text="Register new Account?",
                        font=("times new roman", 11),
                        fg="#6F1E51", bg="white", cursor="hand2")
        lbl_reg.place(x=150, y=280)
        lbl_reg.bind("<Button-1>", self.open_register)

        lbl_forget = Label(right_frame, text="Forget Password?",
                           font=("times new roman", 11),
                           fg="#6F1E51", bg="white", cursor="hand2")
        lbl_forget.place(x=330, y=280)
        lbl_forget.bind("<Button-1>", self.open_forgot)

        # Login Button
        Button(right_frame, text="Login",
               font=("times new roman", 14, "bold"),
               bg="#B71540", fg="white",
               width=15, cursor="hand2",
               command=self.login).place(x=220, y=320)

    def login(self):
        if self.txt_email.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            messagebox.showinfo("Success", "Login Successfully")
            self.switch_frame("dashboard")  # Switch to dashboard

    def open_register(self, event):
        self.new_win = Toplevel(self.root)
        Register(self.new_win)

    def open_forgot(self, event):
        self.new_win = Toplevel(self.root)
        ForgotPassword(self.new_win)


# ===== START APP =====
if __name__ == "__main__":
    root = Tk()
    Login(root)
    root.mainloop()
