#cena 
# Cena

A cena inicial do game, serve para o jogador acessar as cenas de [[Options]], **Game**  e sair do jogo.

![[Pasted image 20250613211808.png]]

---
## 🧊 Objetos:

**Hierarquia dos objetos do Menu**
![[Pasted image 20250613211930.png]]

---
## 🎨Personalização

A UI é bem modular e aberta para manipulação:

- *As cores dos **botões** podem ser mudados pela aba de **Materiais***

- *A posição pode ser mudada com facilidade também, cada botão faz parte de um grupo bem definido

---
# Componente Menu

## 🧠 Objetivo
Permitir o jogador acessar as cenas de **Options** e **Game**.

---
## 🧩 Depende de
- [[mouse]] → sistema de clique e hover nos botões.
- [[InputMapping.py]] → usado para detectar a tecla de saída.

### ⚠ Importante

Sempre inicie e exporte o jogo a partir da cena **Intro**. Ela será responsável por carregar as configurações do player.

Importante que os Botões tenham em seus nomes "Play", "Options" e "Quit" para que a lógica funcione.

---
## ✈ Botões

- `Btn_Play` -> Manda o jogador para **Game**
- `Btn_Options` -> Manda o jogador para [[Options]]
- `Btn_Quit` -> Sai do jogo

---

## 🔁 Fluxo de lógica:

- **start():**
	- Carrega a cena atual
	
	- Inicializa mouse e input
	
	- Define a cena atual último menu acessado `"lastMenu"`

- **update():**
	- **Se pressionar o teclado** > verifica se é *Enter* > entra em **Game**
	
	- **Se clicar com o mouse** > verifica se o objeto clicado é algum botão > aplica as ações configuradas

---



