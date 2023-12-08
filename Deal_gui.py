import tkinter as tk
import Deal_logic

class Gui:
        
    def __init__(self, window):
        self.window = window
        self.round = 0
        #player_case = 0
        self.player_case_copy = 0
        self.player_case_value = 0
        self.cases_to_pick = 0
        self.player_name = ""
        self.label_heading = tk.Label(self.window, text="Deal or No Deal", font=('Arial', 30))
        self.label_heading.grid(row=0, column=0)
        self.frame_first = tk.Frame(self.window)
        self.textbox = tk.Entry(self.frame_first, font=(('Arial'), 16))
        self.textbox.grid()
        self.button = tk.Button(self.frame_first, text='START', font=(('Arial'),18),command=self.start)
        self.button.grid()
        self.frame_first.grid(row=500)
        self.howie_label = tk.Label(self.window,text="",font=('Arial',18))
        start_text = Deal_logic.begin()
        self.howie_label.config(text=f'{start_text}')
        self.howie_label.grid()
        
    def start(self):
        self.player_name = self.textbox.get()
        self.howie_label.config(text=f"Hello, {self.player_name}! " + Deal_logic.start_game())
        self.cases_label = tk.Label(self.window,text=f'Cases Left: {Deal_logic.print_cases()}')
        self.cases_label.grid()
        self.money_label = tk.Label(self.window,text=f'Money Amounts Left: {Deal_logic.print_money()}')
        self.money_label.grid()
        self.textbox.delete(0,len(self.player_name))
        self.button.destroy()
        self.enter_button = tk.Button(self.frame_first, text='ENTER', font=(('Arial'),18),command=self.enter)
        self.enter_button.grid()
        
    def enter(self):
        player_case = self.textbox.get()
        if(Deal_logic.check_case(player_case)):
            self.player_case_copy = int(player_case)
            self.player_case_value = Deal_logic.player_case(player_case)
            Deal_logic.delete_cases(player_case)
            self.howie_label.config(text=f"Howie: You picked case number {player_case}. This is your case to keep until the end of the game unless you choose to sell it.\n We'll get more into that later. To find out what's in your case, we have to open all the other cases. Pick a case to open.")
            self.textbox.delete(0,len(player_case))
            self.cases_label.config(text=Deal_logic.print_cases())
            self.enter_button.destroy()
            self.round += 1
            self.cases_to_pick = Deal_logic.get_num_of_cases_to_pick(self.round)
            self.continue_button = tk.Button(self.window, text='PICK CASE', font=(('Arial'),18),command=self.pick)
            self.continue_button.grid()
            self.cases_to_pick_label = tk.Label(self.window,text=f"Cases left to pick: {self.cases_to_pick}")
            self.cases_to_pick_label.grid()
        else:
            self.howie_label.config(text="Howie: I need you to pick one of the available cases.")
        
    def pick(self):
        
        if(self.cases_to_pick > 0):
            case_picked = self.textbox.get()
            if(Deal_logic.check_case(case_picked)):
                self.cases_to_pick -= 1
                self.cases_to_pick_label.config(text=f"Cases left to pick: {self.cases_to_pick}")
                self.howie_label.config(text=Deal_logic.open_case(case_picked, self.round))
                self.cases_label.config(text=f'Cases Left: {Deal_logic.print_cases()}')
                self.money_label.config(text=f'Money Values Left: {Deal_logic.print_money()}')
                if(self.cases_to_pick == 0):
                    #self.howie_label.config(text=f"The round is over! Now it's time to hear what the banker has to say!")
                    self.textbox.grid_forget()
                    self.continue_button.configure(text="HEAR OFFER",command=self.offer)
                else:
                    self.textbox.delete(0,len(case_picked))
            else:
                self.howie_label.config(text="Howie: I need you to pick one of the available cases.")
                
    def offer(self):
        self.continue_button.grid_forget()
        self.label_heading.config(text=f"OFFER: ${Deal_logic.offers():,d}")
        self.howie_label.config(text=f"Howie: Now, {self.player_name}, I have to ask you: Deal, or No Deal?")
        self.deal_button = tk.Button(self.frame_first, text='DEAL', font=(('Arial'),18),command=self.deal)
        self.deal_button.grid()
        self.no_deal_button = tk.Button(self.frame_first, text='NO DEAL', font=(('Arial'),18),command=self.no_deal)
        self.no_deal_button.grid()
        
    def deal(self):
        self.deal_button.destroy()
        self.no_deal_button.destroy()
        self.continue_button.destroy()
        if((Deal_logic.offers()) > (self.player_case_value)):
            self.howie_label.config(text=f"Howie: Congratulations, {self.player_name}! You just won ${Deal_logic.offers():,d}!\nBut was it a good deal? The case you picked, {self.player_case_copy}, has ${self.player_case_value:,d}.\nYou made a great deal!")
        else:
            self.howie_label.config(text=f"Howie: Congratulations, {self.player_name}! You just won ${Deal_logic.offers()}!\nBut was it a good deal? The case you picked, {self.player_case_copy}, has ${self.player_case_value}.\nYou made not such a great deal.")
    
    def no_deal(self):
        self.continue_button.grid()
        self.deal_button.destroy()
        self.no_deal_button.destroy()
        self.label_heading.config(text="Deal or No Deal")
        self.round += 1
        if(self.round < 10):
            self.howie_label.config(text=f"Howie: Now we are on round {self.round}! Pick some more cases!")
            self.textbox = tk.Entry(self.frame_first, font=(('Arial'), 16))
            self.textbox.grid()
            self.cases_to_pick = Deal_logic.get_num_of_cases_to_pick(self.round)
            self.continue_button.configure(text="PICK CASE",command=self.pick)
            self.cases_to_pick_label.config(text=f"Cases left to pick: {self.cases_to_pick}")
        else:
            self.textbox.grid()
            self.textbox.delete(0,10)
            self.cases_label.grid_forget()
            self.cases_to_pick_label.grid_forget()
            self.howie_label.config(text=f"Howie: So, {self.player_name}, we have two cases left, {self.player_case_copy}, and {Deal_logic.print_cases()}.\nNow, you can either keep the case you picked at the start of the game or swap it with the other.\nOne case has ${Deal_logic.get_last_money_amounts(0)}, and the other has ${Deal_logic.get_last_money_amounts(1)}.\nWhatever is in the case you pick, is what you are taking home.")
            self.continue_button.configure(text="PICK CASE",command=self.final_choice)
            
    def final_choice(self):
        last_case_picked = self.textbox.get()
        if(Deal_logic.check_case(last_case_picked) or (int(last_case_picked) == self.player_case_copy)):
            self.textbox.grid_forget()
            self.continue_button.grid_forget()
            Deal_logic.delete_money(self.player_case_value)
            if(int(last_case_picked) == self.player_case_copy): 
                self.howie_label.config(text=f"Howie: You picked case {last_case_picked}.\nNow, did you make a good deal?\n This case has ${self.player_case_value}, and the other has ${Deal_logic.print_money()}.")
            else:
                self.howie_label.config(text=f"Howie: You picked case {last_case_picked}.\nNow, did you make a good deal?\n This case has ${Deal_logic.print_money()}, and the other has ${self.player_case_value}.")
        else:
            self.howie_label.config(text="Howie: I need you to pick one of the last two cases.")
            