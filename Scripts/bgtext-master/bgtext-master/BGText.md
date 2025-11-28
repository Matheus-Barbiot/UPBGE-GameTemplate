#README 
## BGText: texto dinâmico na BGE

BGText é um utilitário do [Blender Game Engine](https://en.wikipedia.org/wiki/Blender_Game_Engine) e do [UPBGE](https://upbge.org/) que visa aprimorar a experiência com objetos de texto.

# Motivações:

Antigamente, o BGE tinha um recurso conhecido como texto bitmap. Ele permitia configurar a textura de uma fonte para um plano, mapear seu UV para um único caractere, habilitar a opção Texto no material, adicionar uma propriedade Texto ao objeto e exibir um texto baseado nessa propriedade, o que era bem complicado. Depois, ele foi substituído pelo texto dinâmico, agora baseado em fontes True Type, onde você adiciona um texto, uma propriedade chamada Texto e exibe um texto baseado nessa propriedade.

Embora os textos dinâmicos sejam muito mais fáceis de usar do que os textos bitmap, ambos têm seus prós e contras. As principais desvantagens são:

- **Textos bitmap**
	- Sem suporte para caracteres latinos.
	- Bastante difícil e trabalhoso de configurar, até mesmo para criar uma textura de fonte funcional.

- **Textos dinâmicos**
	- A resolução do texto é frequentemente um problema.
	- Quando dimensionado em tempo de execução, o texto precisa ser redesenhado, deixando o mecanismo bastante lento.
	- O texto deve ser plano, sem estilos personalizados além da cor.
- **Ambos**
	- Sem suporte para alinhamento e justificação de texto.
	- Distância horizontal e vertical entre caracteres são fixas.
	- Sem ajuste automático de texto.

Obs.: O UPBGE corrigiu os problemas de resolução em textos dinâmicos, permitindo que você alterasse a resolução em tempo de execução.

Eu uso textos dinâmicos há muito tempo devido à sua facilidade e conheço algumas pessoas que ainda usam texto bitmap devido à capacidade de estilizar o texto com contornos e outras coisas. Com base nisso, pensei em trabalhar de alguma forma para superar esses problemas.
# Características do BGText

O BGText tenta combinar os prós e corrigir a maioria dos contras em textos bitmap e textos dinâmicos, além de fornecer uma interface fácil de usar para configurar cada recurso (usando as propriedades do jogo). Os principais recursos são:

- Fácil de usar, mas também complexo, se necessário.
- Estilos de texto baseados em texturas, tornando-o altamente personalizável.
- Tamanho dos caracteres baseado na origem de cada caractere.
- Deslocamento horizontal e vertical dos caracteres (distância entre os caracteres).
- Quebra automática de texto com base no número de caracteres por linha.
- Alinhamento de texto à esquerda, centralizado e à direita (justificado).
- Texto literal ou expressões Python (uma grande economia de tempo!).
- Cor baseada em nomes de cores predefinidos ou vetores RGBA.
- Texto estático ou atualizado em um intervalo especificado.
- Atualiza textos sem a necessidade de processamento constante com a mensagem `UpdateText`.
- Mensagens `UpdateText` podem atualizar `Todos` os textos ou aqueles com propriedades `Id` específicas.

O BGText é compatível com BGE vanilla e UPBGE. O BGText usa ações de teclas de forma para alternar entre valores de caracteres.

# Como usar:

É simples: no seu arquivo Blend, vincule o grupo BGText do arquivo Blend BGText (`Arquivo` > `Vincular`) e você estará pronto para usá-lo. Para configurar o texto, basta adicionar propriedades à instância do grupo BGText e, ao jogar, as propriedades fornecidas serão aplicadas.

Todos os caracteres na instância BGText serão automaticamente vinculados ao objeto do grupo, permitindo que você execute qualquer lógica que desejar sobre a instância, até mesmo alterando o texto em tempo de execução (veja o uso das mensagens `UpdateText` abaixo).
# Messages

O BGText pode desencadear ações específicas usando mensagens. Para usar essa funcionalidade, basta enviar uma mensagem com um assunto específico e pronto.

- **Assunto:** `UpdateText`
- **Descrição:** Atualiza o texto no comando sem a necessidade de processar o texto a cada quadro com a propriedade `Update`.
- **Corpo:** `All` para atualizar todos os textos ou um valor `Id` para atualizar apenas os textos com este valor.

# Referência

Esta referência mostra quais atributos você pode usar na instância do grupo BGText para alterar seu comportamento. Você não precisa adicionar todos os atributos, apenas aqueles que deseja configurar.

- `Text`
	- **Descrição:** Literal de string ou expressão Python (ao iniciar com o caractere `>`).
	- **Tipo:** `String`

- `Size`
	- **Descrição:** Multiplicador de tamanho individual de caractere.
	- **Tipo:** `Float`

- `Offset`
	- **Descrição:** Multiplicador de distância entre cada caractere.
	- **Tipo:** `Float`

- `OffsetH`
	- **Descrição:** Multiplicador de distância horizontal entre cada caractere. Substitui `Offset`.
	- **Tipo:** `Float`

- `OffsetV`
	- **Descrição:** Multiplicador de distância vertical entre cada caractere. Substitui `Offset`.
	- **Tipo:** `Float`

- `Wrap`
	- **Descrição:** Número de caracteres antes da quebra de linha.
	- **Tipo:** `Integer`

- `Justify`
	- **Descrição:** Alinhamento de texto. Pode ser `left` (padrão), `right` ou `center` (sem distinção entre maiúsculas e minúsculas).
	- **Tipo:** `String`

- `Update`
	- **Descrição:** Atualiza valores constantemente (por exemplo, tempo). O valor é o número de quadros pulados. Se o valor for menor que 0, `Update` será desativado.
	- **Tipo:** `Integer`

- `Style`
	- **Descrição:** Qual estilo de fonte (textura) usar no texto atual. Atualmente, suporta de 1 a 5. O padrão é 1 se o estilo não existir.
	- **Tipo:** `Integer`

- `Color`
	- **Descrição:** Nome da cor ou vetor. Atualmente, suporta `red`, `green`, `blue`, `white`, `black`, `yellow`, `purple`, `cyan` (sem distinção de maiúsculas e minúsculas) ou uma tupla ou lista como `(1, 0.5, 0.1, 1)` representando valores RGBA.
	- **Tipo:** `String`

- `Id`
	- **Descrição:** Identificador do texto atual. Pode ser usado para atualizar textos com identificadores específicos com mensagens `UpdateText`.
	- **Tipo:** `String`

# Problemas Conhecidos

Observei alguns problemas ao usar o BGText, então eles estão na lista para serem corrigidos ou melhorados no futuro.

## O desempenho do script não é ideal

Por motivos de portabilidade, optei por usar o modo Script no controlador Python em vez do modo Módulo. Isso corrige alguns problemas de importação de script e dá liberdade ao desenvolvedor para colocar o arquivo Blender do BGText onde quiser, mas tem um preço. Como o modo Script faz com que o script seja analisado em tempo de execução, ele é muito mais lento que o modo Módulo, e isso pode ser um problema sério ao usar muitas instâncias do BGText com a propriedade `Update`. Não pretendo alterar o modo do controlador pelos motivos já mencionados, mas o script `bgtext.py` já está em formato de módulo; portanto, se o desempenho se tornar um problema sério para você, você só poderá alterar os pontos de entrada nos controladores Python do arquivo Blender do BGText para atender às suas necessidades. Os comentários nas últimas linhas do `bgtext.py` explicarão o que fazer.

# Extras

Além das texturas de estilo de fonte padrão, o BGText vem com algumas sobreposições de imagem para você criar suas próprias texturas de estilo de fonte. Elas estão no diretório `source` e vêm com uma única sobreposição (`TextStyleOverlay.png`) ou múltiplas sobreposições (diretório `TextStyleOverlay`). Elas são úteis quando você está trabalhando com um editor de imagens que suporta camadas.

A ordem dos caracteres é a seguinte:


```text
! " # $ % & ' ( ) * + , - . / 0
1 2 3 4 5 6 7 8 9 : ; < = > ? @
A B C D E F G H I J K L M N O P
Q R S T U V W X Y Z [ \ ] ^ _ `
a b c d e f g h i j k l m n o p
q r s t u v w x y z { | } ~ ¡ ¢
£ ¥ © ® À Á Â Ã Ç É Ê Í Ñ Ó Ô Õ
Ú Ü à á â ã ç é ê í ñ ó ô õ ú ü
```
