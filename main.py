import customtkinter as ctk
import string
from random import choice
import pyperclip

colors = {
    'background': '#3a4e48',
    'button_color': '#274136',
    'disable_button': '#525C58',
    'hover_button': '#14271F',
    'slider_color': '#4b7865',
    'text_color': '#D9C9E0',
    'panel_color': '#4B7865'
}

def button_callback():
    generated_password = ''
    chars = list(string.ascii_letters + string.digits)

    for i in range(0, int(qtd_caracteres.get())):
        caractere = choice(chars)
        while caractere.isupper() and not checkbox_uppercase.get() or caractere.isnumeric() and not checkbox_numbers.get():
            caractere = choice(chars)

        generated_password += caractere

    lbl_password.configure(text=generated_password)
    btn_copy.configure(state='normal')

def copy_event():
    pyperclip.copy(lbl_password._text)
    btn_copy.configure(text='copiado!!', state='disabled', fg_color=colors['disable_button'])
    app.after(1000, lambda: btn_copy.configure(text='copiar', state='normal', fg_color=colors['button_color']))

def slider_event(value):
    lbl_qtd_caracteres.configure(text=f'{int(value)} caracteres')

app = ctk.CTk(fg_color=colors['background'])
app.title('Gerador de Senha')
app.geometry('500x350')
app.minsize(500, 350)
app.maxsize(500, 350)
app.grid_columnconfigure(0, weight=1)

qtd_caracteres = ctk.CTkSlider(app, from_=0, to=60, number_of_steps=60, command=slider_event, fg_color=colors['slider_color'])
qtd_caracteres.grid(row=0, column=0, padx=10, pady=10)

lbl_qtd_caracteres = ctk.CTkLabel(app, text=f'{int(qtd_caracteres.get())} caracteres', text_color=colors['text_color'])
lbl_qtd_caracteres.grid(row=0, column=1, padx=10, pady=10)

panel_checkbox = ctk.CTkFrame(app, fg_color=colors['panel_color'])
panel_checkbox.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='ew', columnspan=2)

checkbox_numbers = ctk.CTkCheckBox(panel_checkbox, text='Incluir números',  fg_color=colors['button_color'], text_color=colors['text_color'])
checkbox_numbers.grid(row=0, column=0, padx=20, pady=(20, 20), sticky='w')

checkbox_uppercase = ctk.CTkCheckBox(panel_checkbox, text='Incluir maiúsculos', fg_color=colors['button_color'], text_color=colors['text_color'])
checkbox_uppercase.grid(row=0, column=1, padx=20, pady=(20, 20), sticky='w')

btn = ctk.CTkButton(app, text='Gerar', command=button_callback, fg_color=colors['button_color'], hover_color=colors['hover_button'] ,text_color=colors['text_color'])
btn.grid(row=2, column=0, padx=20, pady=20, sticky='ew', columnspan=2)

panel_output = ctk.CTkFrame(app, fg_color=colors['panel_color'])
panel_output.grid(row=3, column=0, padx=20, pady=(20, 0), sticky='ew', columnspan=2)

lbl_password = ctk.CTkLabel(panel_output, text='', text_color=colors['text_color'])
lbl_password.pack()

btn_copy = ctk.CTkButton(app, text='copiar', state='disabled', command=copy_event, fg_color=colors['button_color'], hover_color=colors['hover_button'] ,text_color=colors['text_color'])
btn_copy.grid(row=4, column=0, sticky='nsw', columnspan=2)

app.mainloop()