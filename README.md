
# 🔐 Gerador de Senhas com Interface Gráfica

## Visão Geral

Este projeto é um **Gerador de Senhas** desenvolvido em **Python**, com interface gráfica moderna utilizando **CustomTkinter**. Ele permite criar senhas seguras de forma simples, visual e imediata.

O usuário escolhe o tamanho da senha, define se quer **números** e **letras maiúsculas**, gera a senha e copia com um clique.

---

## 🎯 Funcionalidades

* Seleção do **tamanho da senha** (0 a 60 caracteres)
* Opção de incluir:

  * 🔢 Números
  * 🔠 Letras maiúsculas
* Geração instantânea da senha
* Botão para **copiar automaticamente** para a área de transferência
* Interface limpa e consistente

---

## 🖥️ Interface

A interface foi construída com **CustomTkinter**, trazendo:

* Tema escuro elegante
* Componentes modernos (slider, botões, checkboxes)
* Layout fixo para evitar distorções

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **CustomTkinter** – Interface gráfica moderna
* **string** – Conjunto de caracteres
* **random.choice** – Seleção aleatória
* **pyperclip** – Copiar senha para a área de transferência

---

## 📦 Dependências

Instale as dependências antes de executar o projeto:

```bash
pip install customtkinter pyperclip
```

---

## ▶️ Como Executar

1. Clone ou baixe o projeto
2. Certifique-se de que o Python está instalado
3. Instale as dependências
4. Execute o arquivo:

```bash
python app.py
```
ou se preferir, baixe o executável [aqui](baixar)

---

## ⚙️ Como Funciona?

1. O **slider** define quantos caracteres a senha terá
2. Os **checkboxes** dizem quais tipos de caracteres podem entrar
3. Ao clicar em **Gerar**:

   * O programa sorteia letras e números
   * Respeita as opções escolhidas
   * Monta a senha caractere por caractere
4. A senha aparece na tela
5. O botão **Copiar** salva a senha na área de transferência

---

## 🧠 Observações Técnicas

* Senhas são geradas apenas com **letras e números** (sem símbolos)
* Se nenhuma opção for marcada, a senha será composta apenas por letras minúsculas
* O botão de copiar é **desabilitado automaticamente** após o uso por 1 segundo


---

## 🚀 Possíveis Melhorias Futuras

* Incluir símbolos especiais (!@#$%)
* Botão para regenerar rapidamente
* Indicador de força da senha
* Salvamento de histórico

---

## 📄 Licença

Projeto livre para estudo, aprendizado e evolução.

Use. Modifique. Melhore.

---

## 👨‍💻 Autor

Desenvolvido para estudo prático de Python, GUI e lógica.

