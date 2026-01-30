import tkinter as tk
import logic

# Logic sınıfını başlatıyoruz
Settings_Logic = logic.SettingsLogic()
Students_Logic = logic.StudentsLogic()

root = tk.Tk()
root.minsize(300,300)
root.title("To Do List")
root.iconbitmap("tick_icon.ico")
root.config(bg=Settings_Logic.bg_color)

font_label = ("Segoe UI", 11, "bold")
font_entry = ("Segoe UI", 10)

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()
    create_menubar()

def set_dark_mode():
    Settings_Logic.set_dark_mode()

    root.config(bg=Settings_Logic.bg_color)
    for widget in root.winfo_children():
        try:
            if isinstance(widget, (tk.Label, tk.Button)):
                widget.config(bg=Settings_Logic.bg_color, fg=Settings_Logic.fg_color)
            elif isinstance(widget, tk.Entry):
                widget.config(bg="#333333", fg="white", insertbackground="white")
        except:
            pass

def create_menubar():
    menubar = tk.Menu(root)
    
    # Adding File Menu
    file = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='File', menu = file)
    file.add_command(label ='Files', command= None, state="normal")
    file.add_command(label ='New File', command = None, state="normal")
    file.add_command(label ='Open...', command = None, state="normal")
    file.add_command(label ='Save', command = None, state="normal")
    file.add_separator()
    file.add_command(label ='Exit', command = root.destroy)

    # Adding Edit Menu
    edit = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Edit', menu = edit)
    edit.add_command(label ='Cut', command = None, state="normal")
    edit.add_command(label ='Copy', command = None, state="normal")
    edit.add_command(label ='Paste', command = None, state="normal")
    #edit.add_command(label ='Select All', command = None)
    edit.add_separator()
    edit.add_command(label ='Find...', command = None, state="normal")

    # Adding Student Management Menu
    file = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Students', menu = file)
    file.add_command(label ='Student', command = S_UI.show_students, state="normal")
    file.add_command(label ='New Student', command = S_UI.add_student, state="normal")

    # Adding Help Menu
    help_ = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Help', menu = help_)
    help_.add_command(label ='Help', command = None, state="normal")
    help_.add_separator()
    help_.add_command(label ='Settings', command = set_dark_mode, state="normal")

    root.config(menu = menubar)

class StudentsUI():
    def add_student(self):
        clear_window()

        # --- ÖĞRENCİ BİLGİLERİ ---
        tk.Label(root, text="Student Name:", font=font_label).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.student_name = tk.Entry(root, font=font_entry)
        self.student_name.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(root, text="Student Surname:", font=font_label).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.student_surname = tk.Entry(root, font=font_entry)
        self.student_surname.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Phone Number:", font=font_label).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.student_phone = tk.Entry(root, font=font_entry)
        self.student_phone.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(root, text="ID Number:", font=font_label).grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.student_id = tk.Entry(root, font=font_entry)
        self.student_id.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(root, text="Grade Level:", font=font_label).grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.student_grade = tk.Entry(root, font=font_entry)
        self.student_grade.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(root, text="Student Address:", font=font_label).grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.student_address = tk.Entry(root, font=font_entry)
        self.student_address.grid(row=5, column=1, padx=5, pady=5)

        # --- VELİ BİLGİLERİ ---
        tk.Label(root, text="Parent Name:", font=font_label).grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.parent_name = tk.Entry(root, font=font_entry)
        self.parent_name.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(root, text="Parent Surname:", font=font_label).grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.parent_surname = tk.Entry(root, font=font_entry)
        self.parent_surname.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(root, text="Occupation:", font=font_label).grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.parent_job = tk.Entry(root, font=font_entry)
        self.parent_job.grid(row=2, column=3, padx=5, pady=5)

        tk.Label(root, text="Relationship:", font=font_label).grid(row=3, column=2, padx=5, pady=5, sticky="w")
        self.parent_rel = tk.Entry(root, font=font_entry)
        self.parent_rel.grid(row=3, column=3, padx=5, pady=5)

        tk.Label(root, text="Parent Income:", font=font_label).grid(row=4, column=2, padx=5, pady=5, sticky="w")
        self.parent_income = tk.Entry(root, font=font_entry)
        self.parent_income.grid(row=4, column=3, padx=5, pady=5)

        tk.Label(root, text="Agreed Fee:", font=font_label).grid(row=5, column=2, padx=5, pady=5, sticky="w")
        self.agreed_fee = tk.Entry(root, font=font_entry)
        self.agreed_fee.grid(row=5, column=3, padx=5, pady=5)

        tk.Label(root, text="Parent Phone:", font=font_label).grid(row=6, column=2, padx=5, pady=5, sticky="w")
        self.parent_phone = tk.Entry(root, font=font_entry)
        self.parent_phone.grid(row=6, column=3, padx=5, pady=5)

        tk.Label(root, text="Parent ID:", font=font_label).grid(row=7, column=2, padx=5, pady=5, sticky="w")
        self.parent_id = tk.Entry(root, font=font_entry)
        self.parent_id.grid(row=7, column=3, padx=5, pady=5)

        tk.Label(root, text="Parent Address:", font=font_label).grid(row=8, column=2, padx=5, pady=5, sticky="w")
        self.parent_address = tk.Entry(root, font=font_entry)
        self.parent_address.grid(row=8, column=3, padx=5, pady=5)

        save_btn = tk.Button(root, text="Save Student", command=self.collect_and_save)
        save_btn.grid(row=10, column=0, columnspan=4, pady=20)

    def collect_and_save(self):
        # UI'daki verileri topla
        info = {
            "Student Name": self.student_name.get(), "Student Surname": self.student_surname.get(),
            "Student_Phone": self.student_phone.get(), "Student ID": self.student_id.get(),
            "Student Grade": self.student_grade.get(), "Student Adress": self.student_address.get(),
            "Parent Name": self.parent_name.get(), "Parent Surname": self.parent_surname.get(),
            "Parent Occupation": self.parent_job.get(), "Parent Relationship": self.parent_rel.get(),
            "Parent Income": self.parent_income.get(), "Agreed Fee": self.agreed_fee.get(),
            "Parent Phone": self.parent_phone.get(), "Parent ID": self.parent_id.get(),
            "Parent Adress": self.parent_address.get()
        }
        
        # Logic tarafına gönder
        count = Students_Logic.save_to_json(self.student_id.get(), info)
        print(count)

        # Temizlik
        for widget in root.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)

    def show_students(self):
        clear_window()
        #edit.entryconfigure("")
        data = Students_Logic.load_json()
        person = 0
        for id in data:
            tk.Button(root, text=f"{data[id]['Student Name']} {data[id]['Student Surname']}",
                      command=lambda current_id=id: self.show_students_info(current_id),
                      width=20).grid(row=person//3, column=person%3, padx=10, pady=10)
            person += 1

    def show_students_info(self, id):
        clear_window()
        # --- Öğrenci Bilgileri ---
        data = Students_Logic.load_json()
        tk.Label(root, text=f"Student Name:{data[id]["Student Name"]}", font=font_label).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Label(root, text=f"Student Surname:{data[id]["Student Surname"]}", font=font_label).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        tk.Label(root, text=f"Student Phone:{data[id]["Student_Phone"]}", font=font_label).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        tk.Label(root, text=f"Student ID:{data[id]["Student ID"]}", font=font_label).grid(row=3, column=0, padx=5, pady=5, sticky="w")
        tk.Label(root, text=f"Student Grade:{data[id]["Student Grade"]}", font=font_label).grid(row=4, column=0, padx=5, pady=5, sticky="w")
        tk.Label(root, text=f"Student Adress:{data[id]["Student Adress"]}", font=font_label).grid(row=5, column=0, padx=5, pady=5, sticky="w")
        # --- VELİ BİLGİLERİ ---
        tk.Label(root, text=f"Parent Name: {data[id]['Parent Name']}", font=font_label).grid(row=0, column=1, padx=5, pady=5, sticky="w")
        tk.Label(root, text=f"Parent Surname: {data[id]['Parent Surname']}", font=font_label).grid(row=1, column=1, padx=5, pady=5, sticky="w")
        tk.Label(root, text=f"Occupation: {data[id]['Parent Occupation']}", font=font_label).grid(row=2, column=1, padx=5, pady=5, sticky="w")
        tk.Label(root, text=f"Relationship: {data[id]['Parent Relationship']}", font=font_label).grid(row=3, column=1, padx=5, pady=5, sticky="w")
        tk.Label(root, text=f"Parent Income: {data[id]['Parent Income']}", font=font_label).grid(row=4, column=1, padx=5, pady=5, sticky="w")
        tk.Label(root, text=f"Agreed Fee: {data[id]['Agreed Fee']}", font=font_label).grid(row=5, column=1, padx=5, pady=5, sticky="w")
        tk.Label(root, text=f"Parent Phone: {data[id]['Parent Phone']}", font=font_label).grid(row=6, column=1, padx=5, pady=5, sticky="w")
        tk.Label(root, text=f"Parent ID: {data[id]['Parent ID']}", font=font_label).grid(row=7, column=1, padx=5, pady=5, sticky="w")
        tk.Label(root, text=f"Parent Address: {data[id]['Parent Adress']}", font=font_label).grid(row=8, column=1, padx=5, pady=5, sticky="w")

S_UI = StudentsUI()
create_menubar()
root.mainloop()
