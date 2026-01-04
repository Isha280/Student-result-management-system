from tkinter import *
from login import Login
from dashboard import RMS

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Result Management System")
        self.geometry("1100x600+100+50")
        self.resizable(False, False)

        self.frames = {}

        # Initialize frames
        self.frames["login"] = Login(self, self.show_frame)
        self.frames["dashboard"] = RMS(self, self.show_frame)

        # Show login first
        self.show_frame("login")

    def show_frame(self, name):
        # Hide all frames
        for frame in self.frames.values():
            frame.place_forget()

        # Show selected frame
        frame = self.frames[name]
        frame.place(relwidth=1, relheight=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()
