from Deal_gui import *

def main():
    window = tk.Tk()
    window.title('Deal or No Deal')
    window.geometry('1000x500')
    window.resizable(True, True)
        
    Gui(window)
    window.mainloop()
        
if __name__ == '__main__':
    main()