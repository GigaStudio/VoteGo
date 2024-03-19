import tkinter as tk
from tkinter import messagebox

class VotingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Voting Software")

        self.candidates = ["Candidate A", "Candidate B"]
        self.votes = [0, 0]
        self.session_active = True

        self.create_widgets()

    def create_widgets(self):
        self.label_registration = tk.Label(self.master, text="Enter your registration number:")
        self.label_registration.pack()

        self.entry_registration = tk.Entry(self.master)
        self.entry_registration.pack()

        self.button_check_registration = tk.Button(self.master, text="Check Registration", command=self.check_registration)
        self.button_check_registration.pack()

        self.label_vote = tk.Label(self.master, text="Select your candidate:")
        self.label_vote.pack()

        self.buttons_candidates = []
        for idx, candidate in enumerate(self.candidates):
            button_candidate = tk.Button(self.master, text=candidate, command=lambda idx=idx: self.vote(idx), state=tk.DISABLED)
            button_candidate.pack()
            self.buttons_candidates.append(button_candidate)

        self.button_access_results = tk.Button(self.master, text="Access Results", command=self.show_results, state=tk.DISABLED)
        self.button_access_results.pack()

        self.button_new_session = tk.Button(self.master, text="Start New Session", command=self.start_new_session, state=tk.DISABLED)
        self.button_new_session.pack()

    def check_registration(self):
        # Assume registration is valid
        self.button_check_registration.config(state=tk.DISABLED)
        self.entry_registration.config(state=tk.DISABLED)
        for button in self.buttons_candidates:
            button.config(state=tk.NORMAL)

    def vote(self, idx):
        if self.session_active:
            self.votes[idx] += 1
            for button in self.buttons_candidates:
                button.config(state=tk.DISABLED)
            self.button_access_results.config(state=tk.NORMAL)
            self.button_new_session.config(state=tk.NORMAL)
            self.session_active = False
            messagebox.showinfo("Vote Recorded", "Your vote has been recorded.")
        else:
            messagebox.showerror("Voting Error", "Voting session has ended.")

    def show_results(self):
        results = "\n".join([f"{candidate}: {votes}" for candidate, votes in zip(self.candidates, self.votes)])
        messagebox.showinfo("Results", results)

    def start_new_session(self):
        self.session_active = True
        for button in self.buttons_candidates:
            button.config(state=tk.NORMAL)
        self.button_access_results.config(state=tk.DISABLED)
        self.button_new_session.config(state=tk.DISABLED)
        messagebox.showinfo("New Session Started", "A new voting session has started.")

root = tk.Tk()
app = VotingApp(root)
root.mainloop()
