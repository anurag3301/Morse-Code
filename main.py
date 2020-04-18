import function as f
import tkinter as tk

# if you want to use the console version use the below code and comment out the rest
'''
while True:
    choice = int(input('1. AlphaNumeric to Morse\n2. Morse to AlphaNumeric'))
    if choice == 1:
        message = str(input('Enter the messsage: '))
        morse = f.alpha_to_morse(message)
        print('Morse Code: ', morse)
        choice = input("Play the morse (y/n)")
        if choice == 'y' or choice == 'Y':
            f.morse_play(morse)

    if choice == 2:
        morse = input("Enter the morse code: ")
        message = f.morse_to_alphanumeric(morse)
        print(message)
        
'''

# below code is for GUI

def morse(morse):
    output_text.delete('1.0', tk.END)
    alpha = f.morse_to_alphanumeric(morse)
    output_text.insert(1.0, alpha)


def alpha(alpha):
    output_text.delete('1.0', tk.END)
    morse = f.alpha_to_morse(alpha)
    output_text.insert(1.0, morse)


def play(alpha):
    output_text.delete('1.0', tk.END)
    morse = f.alpha_to_morse(alpha)
    output_text.insert(1.0, morse)
    f.morse_play(morse)


root = tk.Tk()

canvas = tk.Canvas(root, height=650, width=750)
head_label = tk.Label(canvas, text='Morse Converter', font=('verdana', 25))
notice_frame = tk.Frame(canvas, height=200, width=550, bd=10, bg='#a0a0a0')
input_notice1 = tk.Label(notice_frame, text='The input is accepted in Morse or Alpha-Numeric.', bg='#a0a0a0', font=('verdana', 10))
input_notice2 = tk.Label(notice_frame,
                         text='If input is in morse then leave one space between each character and two space between each word.',
                         bg='#a0a0a0', font=('verdana', 10))
input_label = tk.Label(canvas, text='Input: ', font=('verdana', 20))
input_entry = tk.Entry(canvas, font=('verdana', 13), width=58)
output_label = tk.Label(canvas, text='Output ↓', font=('verdana', 20))
output_text = tk.Text(canvas, height=9, width=56, borderwidth=1, font=('verdana', 15))
morse_alpha_button = tk.Button(canvas, text='Morse → AlphaNumeric', font=('verdana', 15),
                               command=lambda: morse(input_entry.get()))
alpha_morse_button = tk.Button(canvas, text='AlphaNumeric → Morse', font=('verdana', 15),
                               command=lambda: alpha(input_entry.get()))
play_button = tk.Button(canvas, text='Play\nMorse', font=('verdana', 15), height=3,
                        command=lambda: play(input_entry.get()))

canvas.pack()
head_label.place(y=2, relx=0.35)
notice_frame.place(y=55, x=25)
input_notice1.pack()
input_notice2.pack()
input_label.place(y=150, x=5)
input_entry.place(y=160, x=95)
output_label.place(y=225, x=5)
output_text.place(y=275, x=10)
alpha_morse_button.place(y=520, x=375)
morse_alpha_button.place(y=565, x=375)
play_button.place(y=520, x=645)

root.mainloop()
