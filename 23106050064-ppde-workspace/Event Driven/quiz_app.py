import tkinter as tk
from tkinter import messagebox, ttk
import random

class QuizApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz Interaktif - Tugas Akhir")
        self.window.geometry("700x500")
        self.window.configure(bg="white")

        # Data quiz (10 soal)
        self.questions = [
            {
                "question": "Apa itu event-driven programming?",
                "options": ["Program berurutan", "Program merespons event", "Program tanpa GUI", "Program berbasis web"],
                "correct": 1
            },
            {
                "question": "Fungsi dari tkinter dalam Python adalah?",
                "options": ["Web server", "GUI toolkit", "Database", "Networking"],
                "correct": 1
            },
            {
                "question": "Metode untuk menjalankan mainloop tkinter adalah?",
                "options": ["run()", "execute()", "start()", "mainloop()"],
                "correct": 3
            },
            {
                "question": "Widget untuk input teks pada tkinter adalah?",
                "options": ["Label", "Entry", "Button", "Canvas"],
                "correct": 1
            },
            {
                "question": "Fungsi messagebox.showinfo() adalah?",
                "options": ["Tampilkan pesan info", "Input data", "Tutup aplikasi", "Buat jendela baru"],
                "correct": 0
            },
            {
                "question": "Metode untuk menambahkan widget ke window?",
                "options": ["pack(), grid(), place()", "insert()", "append()", "add()"],
                "correct": 0
            },
            {
                "question": "Tipe variabel tkinter untuk angka adalah?",
                "options": ["StringVar", "IntVar", "DoubleVar", "BooleanVar"],
                "correct": 1
            },
            {
                "question": "Shortcut untuk submit jawaban di aplikasi ini?",
                "options": ["Esc", "Enter", "Ctrl", "Alt"],
                "correct": 1
            },
            {
                "question": "Progress bar tkinter ada di modul?",
                "options": ["ttk", "messagebox", "os", "sys"],
                "correct": 0
            },
            {
                "question": "Event handler tkinter bekerja dengan?",
                "options": ["Polling", "Event loop", "Compiler", "Thread"],
                "correct": 1
            },
        ]
        random.shuffle(self.questions)

        # State management
        self.current_question = 0
        self.score = 0
        self.time_left = 30
        self.selected_answer = tk.IntVar(value=-1)

        self.buat_interface()
        self.load_question()
        self.start_timer()

        # Keyboard shortcut
        self.window.bind("<Return>", lambda e: self.submit_answer())
        self.window.bind("<Escape>", lambda e: self.skip_question())

        self.window.mainloop()

    def buat_interface(self):
        # Label pertanyaan
        self.question_label = tk.Label(self.window, text="", font=("Arial", 14), wraplength=650, bg="white")
        self.question_label.pack(pady=20)

        # Frame opsi jawaban
        self.options_frame = tk.Frame(self.window, bg="white")
        self.options_frame.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.options_frame, text="", variable=self.selected_answer, value=i,
                                font=("Arial", 12), bg="white", anchor="w")
            rb.pack(fill="x", pady=5, padx=20)
            self.option_buttons.append(rb)

        # Timer
        self.timer_label = tk.Label(self.window, text="Waktu: 30", font=("Arial", 12, "bold"), bg="white", fg="red")
        self.timer_label.pack(pady=10)

        # Progress bar score
        self.progress = ttk.Progressbar(self.window, orient="horizontal", mode="determinate", length=400)
        self.progress.pack(pady=10)
        self.progress["maximum"] = len(self.questions)

        # Tombol submit
        self.submit_btn = tk.Button(self.window, text="Submit", font=("Arial", 12), command=self.submit_answer)
        self.submit_btn.pack(pady=20)

    def load_question(self):
        if self.current_question >= len(self.questions):
            self.show_result()
            return

        q = self.questions[self.current_question]
        self.question_label.config(text=f"Soal {self.current_question+1}: {q['question']}")
        self.selected_answer.set(-1)

        for i, option in enumerate(q["options"]):
            self.option_buttons[i].config(text=option)

        # Reset timer
        self.time_left = 30
        self.timer_label.config(text=f"Waktu: {self.time_left}")

    def start_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Waktu: {self.time_left}")
            self.window.after(1000, self.start_timer)
        else:
            self.skip_question()

    def submit_answer(self):
        q = self.questions[self.current_question]
        selected = self.selected_answer.get()

        if selected == -1:
            messagebox.showwarning("Peringatan", "Silakan pilih jawaban terlebih dahulu!")
            return

        if selected == q["correct"]:
            self.score += 1
            self.feedback_animation("green")
        else:
            self.feedback_animation("red")

        self.progress["value"] = self.current_question + 1
        self.current_question += 1
        self.window.after(1000, self.load_question)

    def skip_question(self):
        self.progress["value"] = self.current_question + 1
        self.current_question += 1
        self.load_question()

    def feedback_animation(self, color):
        self.question_label.config(bg=color)
        self.window.after(500, lambda: self.question_label.config(bg="white"))

    def show_result(self):
        messagebox.showinfo("Hasil Quiz", f"Skor Anda: {self.score}/{len(self.questions)}")
        self.window.destroy()

if __name__ == "__main__":
    QuizApp()
