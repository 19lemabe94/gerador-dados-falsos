import customtkinter as ctk
import pandas as pd
from faker import Faker

# Configuração inicial do Faker
fake = Faker("pt_BR")

# Função para gerar os dados falsos
def generate_data():
    num_rows = int(entry_num_rows.get())
    selected_fields = [field for field, var in fields.items() if var.get()]
    
    data = []
    for _ in range(num_rows):
        row = {}
        if "Nome" in selected_fields:
            row["Nome"] = fake.name()
        if "Endereço" in selected_fields:
            row["Endereço"] = fake.address()
        if "Data de Nascimento" in selected_fields:
            row["Data de Nascimento"] = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%d/%m/%Y")
        if "Telefone" in selected_fields:
            row["Telefone"] = fake.phone_number()
        if "Email" in selected_fields:
            row["Email"] = fake.email()
        if "CPF" in selected_fields:
            row["CPF"] = fake.cpf()
        
        data.append(row)
    
    df = pd.DataFrame(data)
    text_output.delete("1.0", ctk.END)
    text_output.insert(ctk.END, df.to_string(index=False))
    return df

# Função para salvar em CSV
def save_to_csv():
    df = generate_data()
    df.to_csv("dados_falsos.csv", index=False, sep=';')

# Configuração da interface gráfica
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Gerador de Dados Falsos")
root.geometry("600x500")

# Entrada para quantidade de linhas
ctk.CTkLabel(root, text="Quantidade de Linhas:").pack(pady=5)
entry_num_rows = ctk.CTkEntry(root)
entry_num_rows.pack(pady=5)

# Checkbuttons para seleção de campos
fields = {"Nome": ctk.BooleanVar(), "Endereço": ctk.BooleanVar(), "Data de Nascimento": ctk.BooleanVar(),
          "Telefone": ctk.BooleanVar(), "Email": ctk.BooleanVar(), "CPF": ctk.BooleanVar()}

ctk.CTkLabel(root, text="Selecione os Campos:").pack(pady=5)
for field, var in fields.items():
    ctk.CTkCheckBox(root, text=field, variable=var).pack(anchor='w', padx=20)

# Botão para gerar os dados
btn_generate = ctk.CTkButton(root, text="Gerar Dados", command=generate_data)
btn_generate.pack(pady=10)

# Botão para salvar em CSV
btn_save = ctk.CTkButton(root, text="Salvar em CSV", command=save_to_csv)
btn_save.pack(pady=10)

# Área de saída de texto
text_output = ctk.CTkTextbox(root, height=10)
text_output.pack(pady=10, fill='both', expand=True)

root.mainloop()
