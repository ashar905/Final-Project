from tkinter import *
from tkinter.messagebox import askokcancel,showinfo
import sys

class diseasefinder:
    def __init__(self,main):
        # def enter(event):
        #     self.disfind.config(bg='white',fg='black')
        # def leave(event):    
        #     self.disfind.config(bg='black',fg='white')
        self.main = main
        self.main.config(background='blue4')
        self.main.protocol('WM_DELETE_WINDOW',self.exit)
        self.main.geometry('500x450')
        self.main.resizable(0,0)
        self.main.title('DISEASE FINDER')
        self.title = Label(main,text='Welcome To Disease Finder',bg='blue4',fg='gold1',font='cursive 20 bold italic').pack()
        self.btn = Button(main,text='Find Disease',bg='gold1',fg='blue4',font='cursive 12',height=2,width=15,command=self.find_disease).place(x=25,y=380)
        self.label = Label(main,text='Your Disease May Be :',font='cursive 10 bold',fg='gold1',bg='blue4').place(x=200,y=50)
        self.textarea = Text(main,font='cursive 10',height=22,width=35)
        self.textarea.place(x=200,y=80)
        self.menubar = Menu(main)
        self.help = Menu(self.menubar,tearoff=0)
        self.help.add_command(label='Credits',command=self.showcredits)
        self.menubar.add_cascade(label='Help',menu=self.help)
        self.main.config(menu=self.menubar)   

        symptoms = ['Fever','Cough','Headache','Fatigue','Nausea','Joint Pain','Shortness of Breath','Rash','Abdominal Pain','Dizziness'] 
        self.chosen_symptoms = []

        for index,symptom in enumerate(symptoms):
            checkbox = Checkbutton(main,text=symptom,bg='blue4',fg='gold1',command=lambda s=symptom:self.other_symptoms(s))
            checkbox.place(x=20,y=30 + index * 30)

    def other_symptoms(self,symptom):
        if symptom in self.chosen_symptoms:
            self.chosen_symptoms.remove(symptom)
        else:
            self.chosen_symptoms.append(symptom)         

    def find_disease(self):
        symptom_dict = {
        'Fever': ['Flu', 'Common Cold'],
        'Cough': ['Flu', 'Common Cold', 'Bronchitis'],
        'Headache': ['Migraine', 'Tension Headache'],
        'Fatigue': ['Flu', 'Chronic Fatigue Syndrome'],
        'Nausea': ['Food Poisoning', 'Stomach Flu'],
        'Joint Pain': ['Rheumatoid Arthritis', 'Lupus'],
        'Shortness of Breath': ['Asthma', 'Pneumonia'],
        'Rash': ['Allergic Reaction', 'Eczema'],
        'Abdominal Pain': ['Appendicitis', 'Gastritis'],
        'Dizziness': ['Vertigo', 'Anemia']
        }  
        your_disease=[]

        for symptom in self.chosen_symptoms:
            your_disease.extend(symptom_dict.get(symptom,[]))

        self.textarea.delete('1.0',END)
        if your_disease:
            self.textarea.insert('1.0','\n'.join(set(your_disease))) 
        else:
            self.textarea.insert('1.0','No disease found according to your symptoms!')       

    def exit(self):
        question = askokcancel('disease finder','Do you really want to exit?')
        if question:
            sys.exit()
        else:
            pass
    
    def showcredits(self):
        showinfo('Disease finder','This disease finder is creater by M.Ashar Riaz')

window = Tk()
diseasefinder(window)
window.mainloop()   