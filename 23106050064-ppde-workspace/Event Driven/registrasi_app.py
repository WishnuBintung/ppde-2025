import tkinter as tk
from tkinter import ttk, messagebox

class RegistrasiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Form Registrasi")
        self.root.geometry("400x600")
        self.root.configure(bg="lightgray")

        # Variabel
        self.nama_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.umur_var = tk.IntVar(value=18)
        self.gender_var = tk.StringVar(value="Pria")
        self.agree_var = tk.BooleanVar(value=False)

        # Panggil interface
        self.buat_interface()

    def buat_interface(self):
        # Frame utama
        self.main_frame = tk.Frame(self.root, bg="lightgray", padx=20, pady=20)
        self.main_frame.pack(fill="both", expand=True)

        # Judul
        title_label = tk.Label(
            self.main_frame,
            text="Form Registrasi",
            font=("Arial", 18, "bold"),
            bg="lightgray"
        )
        title_label.pack(pady=10)

        # Input fields
        self.buat_input_field("Nama Lengkap", self.nama_var)
        self.buat_input_field("Email", self.email_var)
        self.buat_input_field("Password", self.password_var, show="*")

        # Umur
        umur_label = tk.Label(self.main_frame, text="Umur", bg="lightgray", anchor="w")
        umur_label.pack(fill="x")
        umur_spinbox = tk.Spinbox(self.main_frame, from_=0, to=100, textvariable=self.umur_var)
        umur_spinbox.pack(fill="x", pady=(0, 10))

        # Gender
        gender_label = tk.Label(self.main_frame, text="Gender", bg="lightgray", anchor="w")
        gender_label.pack(fill="x")
        gender_frame = tk.Frame(self.main_frame, bg="lightgray")
        gender_frame.pack(fill="x", pady=(0, 10))
        tk.Radiobutton(gender_frame, text="Pria", variable=self.gender_var, value="Pria", bg="lightgray").pack(side="left", padx=10)
        tk.Radiobutton(gender_frame, text="Wanita", variable=self.gender_var, value="Wanita", bg="lightgray").pack(side="left", padx=10)

        # Agreement
        agree_check = tk.Checkbutton(
            self.main_frame,
            text="Saya menyetujui syarat dan ketentuan",
            variable=self.agree_var,
            bg="lightgray",
            command=self.update_submit_button
        )
        agree_check.pack(pady=10)

        # Progress bar
        self.progress_frame = tk.Frame(self.main_frame, bg="lightgray")
        self.progress_frame.pack(fill="x", pady=10)
        self.progress = ttk.Progressbar(self.progress_frame, orient="horizontal", mode="determinate", maximum=100)
        self.progress.pack(fill="x")
        self.progress_label = tk.Label(self.progress_frame, text="0%", bg="lightgray")
        self.progress_label.pack()

        # Submit button
        self.submit_btn = tk.Button(
            self.main_frame,
            text="Submit",
            state="disabled",
            command=self.submit_form
        )
        self.submit_btn.pack(pady=20)

        # Trace variabel untuk update progress
        self.nama_var.trace_add("write", lambda *args: self.update_submit_button())
        self.email_var.trace_add("write", lambda *args: self.update_submit_button())
        self.password_var.trace_add("write", lambda *args: self.update_submit_button())
        self.umur_var.trace_add("write", lambda *args: self.update_submit_button())
        self.gender_var.trace_add("write", lambda *args: self.update_submit_button())
        self.agree_var.trace_add("write", lambda *args: self.update_submit_button())

    def buat_input_field(self, label_text, variable, show=None):
        label = tk.Label(self.main_frame, text=label_text, bg="lightgray", anchor="w")
        label.pack(fill="x")
        entry = tk.Entry(self.main_frame, textvariable=variable, show=show)
        entry.pack(fill="x", pady=(0, 10))

    def update_submit_button(self):
        # Hitung progress
        progress_value = 0
        if self.nama_var.get(): progress_value += 20
        if self.email_var.get(): progress_value += 20
        if self.password_var.get(): progress_value += 20
        if self.umur_var.get() > 0: progress_value += 20
        if self.agree_var.get(): progress_value += 20

        self.progress["value"] = progress_value
        self.progress_label.config(text=f"{progress_value}%")

        # Enable/disable tombol
        if progress_value == 100:
            self.submit_btn.config(state="normal")
        else:
            self.submit_btn.config(state="disabled")

    def submit_form(self):
        data = (
            f"Nama: {self.nama_var.get()}\n"
            f"Email: {self.email_var.get()}\n"
            f"Password: {self.password_var.get()}\n"
            f"Umur: {self.umur_var.get()}\n"
            f"Gender: {self.gender_var.get()}\n"
            f"Agreement: {self.agree_var.get()}"
        )
        messagebox.showinfo("Data Registrasi", data)


if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrasiApp(root)
    root.mainloop()
