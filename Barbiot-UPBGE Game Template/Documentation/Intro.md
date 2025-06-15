 #cena

# Objetivo

 Uma cena de carregamento, feita para carregar o `GlobalDict`, útil caso você queira apresentar sua logomarca no início da jogatina.
 
---
# Component Intro

**Arquivo:** [[logic_intro.py]] 
**Componente:** Intro
**Ordered Dict:**
- *"Loading Timer"* - Tempo que o componente demorará para carregar o menu.
	`você pode aproveitar para colocar alguma animação de logomarca nessa parte.`


---
## Precisa de

- [[UserConfig]] [[config_user.py]] Para carregar as configurações salvas

---
## Lógica
### OrderedDict

- `Timer` - Tempo de tela que a cena Intro ficará na tela.
### Start

- Carrega o `globalDict`
- Define a resolução do dispositivo como o padrão no `defaultSize`
- Aplica as configurações de vídeo com  `applyVideoOptions`
- Termina definindo um timer e um valor mínimo para ele

### Update

- Verifica se o timer atingiu o valor mínimo
- Se não ele continua atualizando o timer
- Se sim, ele manda para o [[Menu & Pause]]