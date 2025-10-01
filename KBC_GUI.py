import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Full list of 50 questions (you can extend it)
questions = [
    {"question": "Bharat ki Rashtriya Pashu kaun sa hai?", "options": ["a) Bengal Tiger", "b) Peacock", "c) Elephant", "d) Lion"], "answer": "a"},
    {"question": "Taj Mahal kis shah ne banwaya tha?", "options": ["a) Shah Jahan", "b) Akbar", "c) Aurangzeb", "d) Jahangir"], "answer": "a"},
    {"question": "Hawa Mahal kis shahar mein sthit hai?", "options": ["a) Udaipur", "b) Jodhpur", "c) Jaipur", "d) Delhi"], "answer": "c"},
    {"question": "Somnath Mandir kis rajya mein hai?", "options": ["a) Gujarat", "b) Andhra Pradesh", "c) Rajasthan", "d) Madhya Pradesh"], "answer": "a"},
    {"question": "UN ka headquarters kahaan hai?", "options": ["a) Geneva", "b) New York", "c) London", "d) Paris"], "answer": "b"},
    {"question": "Sabse unobstructed mountain kaunsa hai?", "options": ["a) Everest", "b) K2", "c) Kangchenjunga", "d) Lhotse"], "answer": "a"},
    {"question": "Solar system mein sabse chhota planet kaunsa hai?", "options": ["a) Mercury", "b) Mars", "c) Venus", "d) Pluto"], "answer": "a"},
    {"question": "DNA ka full form kya hai?", "options": ["a) Deoxyribonucleic Acid", "b) Deoxynucleic Acid", "c) Dinucleic Acid", "d) Dioxynucleic Acid"], "answer": "a"},
    {"question": "Light ki speed approx kya hai vacuum mein?", "options": ["a) 3 × 10^8 m/s", "b) 3 × 10^6 m/s", "c) 3 × 10^5 km/s", "d) 3 × 10^7 m/s"], "answer": "a"},
    {"question": "World War II kab khatam hua?", "options": ["a) 1945", "b) 1948", "c) 1942", "d) 1940"], "answer": "a"},
    {"question": "Computer mein binary system ka numeral kya hota hai?", "options": ["a) 0-1", "b) 0-9", "c) 1-2", "d) 0-2"], "answer": "a"},
    {"question": "Internet ka acronym kya hai?", "options": ["a) International Network", "b) Interconnected Networks", "c) Internet Work", "d) Interface Network"], "answer": "b"},
    {"question": "Olympics 2024 kis desh mein hoga?", "options": ["a) Japan", "b) France", "c) USA", "d) UK"], "answer": "b"},
    {"question": "Bharat ki rashtriya bhasha kya hai?", "options": ["a) Hindi", "b) English", "c) Sanskrit", "d) Urdu"], "answer": "a"},
    {"question": "Microsoft ka sthapna kisne kiya tha?", "options": ["a) Steve Jobs", "b) Bill Gates", "c) Mark Zuckerberg", "d) Larry Page"], "answer": "b"},
    {"question": "Google search engine kab launch hua?", "options": ["a) 1998", "b) 1995", "c) 2000", "d) 1992"], "answer": "a"},
    {"question": "Tropical region ka central fruit kya hai?", "options": ["a) Mango", "b) Apple", "c) Orange", "d) Banana"], "answer": "a"},
    {"question": "Mahabharata ke mukhya patra kaun hai?", "options": ["a) Arjun", "b) Krishna", "c) Yudhishthir", "d) Bhim"], "answer": "b", "prize": 18000},
    {"question": "Zero ka invention kisne kiya?", "options": ["a) Babylonians", "b) Mayans", "c) Indians", "d) Egyptians"], "answer": "c", "prize": 19000},
    {"question": "Mount Everest kis range mein hai?", "options": ["a) Himalayas", "b) Andes", "c) Alps", "d) Rockies"], "answer": "a", "prize": 20000},
    {"question": "Bharat ki rashtriya naadi kaun si hai?", "options": ["a) Ganga", "b) Yamuna", "c) Godavari", "d) Kaveri"], "answer": "a", "prize": 21000},
    {"question": "Plane mein lift kya generate karta hai?", "options": ["a) Drag", "b) Thrust", "c) Lift", "d) Weight"], "answer": "c", "prize": 22000},
    {"question": "Ozone layer kis se protect karti hai?", "options": ["a) Infrared", "b) UV rays", "c) X-rays", "d) Gamma rays"], "answer": "b", "prize": 23000},
    {"question": "Atmosphere mein sabse adhik gas kaunsi hoti hai?", "options": ["a) Oxygen", "b) Nitrogen", "c) CO2", "d) Argon"], "answer": "b", "prize": 24000},
    {"question": "Brazil ki official language kya hai?", "options": ["a) Spanish", "b) Portuguese", "c) English", "d) French"], "answer": "b", "prize": 25000},
    {"question": "Apple iPhone kab launch hua tha?", "options": ["a) 2005", "b) 2007", "c) 2009", "d) 2010"], "answer": "b", "prize": 26000},
    {"question": "WWW ka full form kya hai?", "options": ["a) World Wide Web", "b) Web Wide World", "c) World Web Wide", "d) Web World Wide"], "answer": "a", "prize": 27000},
    {"question": "Android OS kisne banaya?", "options": ["a) Apple", "b) Google", "c) Microsoft", "d) Nokia"], "answer": "b", "prize": 28000},
    {"question": "Sabse bada land animal kya hai?", "options": ["a) Elephant", "b) Horse", "c) Hippo", "d) Giraffe"], "answer": "a", "prize": 29000},
    {"question": "Penicillin kisne discover kiya tha?", "options": ["a) Fleming", "b) Pasteur", "c) Curie", "d) Einstein"], "answer": "a", "prize": 30000},
    {"question": "Tsunami majorly kis wajah se hota hai?", "options": ["a) Volcano", "b) Earthquake", "c) Cyclone", "d) Rainfall"], "answer": "b", "prize": 31000},
    {"question": "Dinosaur kab extinct hua tha?", "options": ["a) 65M years ago", "b) 55M", "c) 45M", "d) 35M"], "answer": "a", "prize": 32000},
    {"question": "Solar eclipse ka matlab kya hai?", "options": ["a) Moon shadows Earth", "b) Earth shadows Moon", "c) Sun shadows Earth", "d) Moon shadows Sun"], "answer": "d", "prize": 33000},
    {"question": "India ka biggest airport kaun sa hai?", "options": ["a) IGI Airport", "b) CS Airport", "c) Bangalore Airport", "d) Kolkata Airport"], "answer": "a", "prize": 34000},
    {"question": "Blue whale kya hai?", "options": ["a) Fish", "b) Mammal", "c) Reptile", "d) Amphibian"], "answer": "b", "prize": 35000},
    {"question": "Mount Kilimanjaro kis continent mein hai?", "options": ["a) Asia", "b) Africa", "c) S. America", "d) Europe"], "answer": "b", "prize": 36000},
    {"question": "FIFA trophy ka asli naam kya hai?", "options": ["a) FIFA Cup", "b) World Cup", "c) Jules Rimet Trophy", "d) Champions Trophy"], "answer": "c", "prize": 37000},
    {"question": "India ka sabse bada desert kaunsa hai?", "options": ["a) Thar", "b) Sahara", "c) Gobi", "d) Kalahari"], "answer": "a", "prize": 38000},
    {"question": "World Environment Day kab manaya jaata hai?", "options": ["a) 5 June", "b) 22 April", "c) 1 May", "d) 15 August"], "answer": "a", "prize": 39000},
    {"question": "CPU ka full form kya hai?", "options": ["a) Central Processing Unit", "b) Computer Processing Unit", "c) Central Program Unit", "d) Control Processing Unit"], "answer": "a", "prize": 40000},
    {"question": "Bharat ka pehla PM kaun tha?", "options": ["a) Rajendra Prasad", "b) Sardar Patel", "c) Jawaharlal Nehru", "d) Subhash Chandra Bose"], "answer": "c", "prize": 41000},
    {"question": "HTML ka full form kya hai?", "options": ["a) HyperText Markup Language", "b) HighText Markup Language", "c) HyperText Markdown Language", "d) None"], "answer": "a", "prize": 42000},
    {"question": "Gandhi Jayanti kis din hoti hai?", "options": ["a) 15 August", "b) 26 January", "c) 2 October", "d) 5 September"], "answer": "c", "prize": 43000},
    {"question": "Green Revolution kis field mein hua?", "options": ["a) Medicine", "b) Agriculture", "c) Space", "d) Education"], "answer": "b", "prize": 44000},
    {"question": "PM Narendra Modi ka janm kab hua tha?", "options": ["a) 1950", "b) 1949", "c) 1951", "d) 1952"], "answer": "a", "prize": 45000},
    {"question": "Bluetooth kis ke liye use hota hai?", "options": ["a) Charging", "b) Communication", "c) Display", "d) Cooling"], "answer": "b", "prize": 46000}
]


class KBCGame:
    def __init__(self, root):
        self.root = root
        self.root.title("KBC Quiz Game")
        self.root.geometry("700x500")

        self.player_name = simpledialog.askstring("Player Name", "Enter your name:")
        if not self.player_name:
            messagebox.showinfo("Exit", "Name is required to start the game.")
            self.root.destroy()
            return

        self.q_index = 0
        self.used_lifelines = {"50:50": False, "Audience Poll": False, "Flip": False, "Expert": False}

        self.prize_money = [f"₹{i*1000:,}" for i in range(1, 16)]

        if len(questions) < 15:
            messagebox.showerror("Error", "Not enough questions to start the game.")
            self.root.destroy()
            return

        self.selected_questions = random.sample(questions, 15)

        self.question_label = tk.Label(self.root, text="", wraplength=600, font=("Arial", 16))
        self.question_label.pack(pady=30)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", width=30, font=("Arial", 14), command=lambda i=i: self.check_answer(self.buttons[i]['text']))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.feedback_label.pack(pady=20)

        lifeline_frame = tk.Frame(self.root)
        lifeline_frame.pack(pady=10)

        self.lifeline_buttons = {}
        for name in self.used_lifelines:
            b = tk.Button(lifeline_frame, text=name, command=lambda n=name: self.use_lifeline(n))
            b.pack(side=tk.LEFT, padx=5)
            self.lifeline_buttons[name] = b

        self.quit_btn = tk.Button(self.root, text="Quit", command=self.quit_game, fg="red")
        self.quit_btn.pack(side=tk.LEFT, padx=20, pady=10)

        self.replay_btn = tk.Button(self.root, text="Replay", command=self.replay_game)
        self.replay_btn.pack(side=tk.RIGHT, padx=20, pady=10)

        self.load_question()

    def load_question(self):
        if self.q_index < len(self.selected_questions):
            self.feedback_label.config(text="")
            current_q = self.selected_questions[self.q_index]
            self.question_label.config(text=f"Q{self.q_index+1}: {current_q['question']}")
            options = current_q['options'][:]
            random.shuffle(options)
            for i in range(4):
                self.buttons[i].config(text=options[i], state=tk.NORMAL)
        else:
            messagebox.showinfo("Congratulations!", f"{self.player_name}, you've won {self.prize_money[self.q_index - 1]}!")
            self.root.destroy()

    def check_answer(self, selected):
        correct = self.selected_questions[self.q_index]['answer']
        selected_clean = selected.split(') ')[0].lower()
        if selected_clean == correct:
            self.feedback_label.config(text=f"Correct! You won {self.prize_money[self.q_index]}!", fg="green")
            self.q_index += 1
            self.root.after(2000, self.load_question)
        else:
            self.feedback_label.config(text=f"Wrong! Correct answer was: {correct.upper()}", fg="red")
            self.root.after(3000, self.root.destroy)

    def use_lifeline(self, name):
        if self.used_lifelines[name]:
            messagebox.showinfo("Lifeline Used", f"{name} has already been used.")
            return

        self.used_lifelines[name] = True
        if name == "50:50":
            self.lifeline_5050()
        elif name == "Audience Poll":
            self.audience_poll()
        elif name == "Flip":
            self.q_index += 1
            self.load_question()
        elif name == "Expert":
            correct = self.selected_questions[self.q_index]['answer']
            messagebox.showinfo("Expert Advice", f"Expert thinks the correct answer is: {correct.upper()}")

        self.lifeline_buttons[name].config(state=tk.DISABLED)

    def lifeline_5050(self):
        correct = self.selected_questions[self.q_index]['answer']
        options = [btn['text'] for btn in self.buttons]
        wrong = [opt for opt in options if not opt.startswith(correct + ")")]
        to_disable = random.sample(wrong, 2)
        for btn in self.buttons:
            if btn['text'] in to_disable:
                btn.config(state=tk.DISABLED)

    def audience_poll(self):
        correct = self.selected_questions[self.q_index]['answer']
        options = [btn['text'] for btn in self.buttons]

        poll_result = {}
        remaining_percent = 100
        correct_percent = random.randint(60, 80)
        poll_result[correct] = correct_percent
        remaining_percent -= correct_percent

        wrong_options = [opt[0].lower() for opt in options if not opt.startswith(correct + ")")]
        for i, opt in enumerate(wrong_options):
            if i == len(wrong_options) - 1:
                poll_result[opt] = remaining_percent
            else:
                percent = random.randint(0, remaining_percent)
                poll_result[opt] = percent
                remaining_percent -= percent

        result_text = "Audience Poll Results:\n\n"
        for opt in ['a', 'b', 'c', 'd']:
            label = next((o for o in options if o.startswith(opt + ")")), None)
            if label:
                result_text += f"{label}: {poll_result.get(opt, 0)}%\n"

        messagebox.showinfo("Audience Poll", result_text)

    def quit_game(self):
        messagebox.showinfo("Quit", f"You won {self.prize_money[self.q_index - 1] if self.q_index > 0 else '₹0'}. Thanks for playing, {self.player_name}!")
        self.root.destroy()

    def replay_game(self):
        self.root.destroy()
        root = tk.Tk()
        KBCGame(root)
        root.mainloop()

root = tk.Tk()
game = KBCGame(root)
root.mainloop()
