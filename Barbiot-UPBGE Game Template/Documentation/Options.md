# Cena

Uma cena feita para que o jogador possa configurar o display e o áudio do game.

![[Pasted image 20250613205802.png]]

## 🧊 Objetos

**Print da hierarquia de objetos**
![[Pasted image 20250613205553.png]]

## 🎨Personalização

A UI é bem modular e aberta para manipulação:

- *As cores dos **botões** podem ser mudados pela aba de **Materiais***

- *A posição pode ser mudada com facilidade também, cada botão faz parte de um grupo bem definido*

---
# Componente Options

## 🧠 Objetivo
Breve descrição da função principal desse script.
> Ex: Controla o menu de opções, alterando resolução, fullscreen, vsync e volumes. Aplica e salva configs no globalDict.

---

## 🧩 Depende de
- [[UserConfig]] → responsável por aplicar as opções de vídeo.
- [[Mouse]] → sistema de clique e hover nos botões.
- [[InputMapping.py]] → usado para detectar a tecla de saída.

---

## 📦 Propriedades manipuladas
- `screenSize` → índice da resolução na lista
- `fullscreen` → bool: tela cheia ou não
- `vsync` → 0 ou 1
- `music` → volume da música (0.0–2.0)
- `sounds` → volume dos efeitos (0.0–2.0)

---

## 🔄 Fluxo da lógica

- **start():**
    - Carrega a cena atual
    - Inicializa mouse, input e vídeo
    - Define textos e carrega configurações do globalDict

- **update():**
    - Se clicar → detecta botão → altera valor → atualiza texto
    - Se pressionar tecla → aplica ou retorna ao menu

- **updateVisualValues():**
    - Atualiza os textos com os valores atuais da config

- **saveOptions():**
    - Salva os valores do objeto no globalDict e aplica no sistema

- **loadOptions():**
    - Carrega valores do globalDict e aplica ao objeto

---