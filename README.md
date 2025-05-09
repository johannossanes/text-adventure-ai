## Text Adventure IA

Um jogo de aventura interativo via terminal ou interface gráfica (`tkinter`), onde você conversa com uma IA adaptativa que conduz sua jornada por mundos fantásticos. Escolha ações, enfrente criaturas e explore lugares misteriosos — tudo com geração de texto dinâmica usando o modelo Gemini Flash 1.5 da Google.

---

## Requisitos

- Python 3.10 ou superior (recomendado 3.11+)
- Conta e chave de API da Google AI (Gemini)
- Bibliotecas Python:
  - `google-generativeai`
  - `tkinter` (já vem com o Python em muitos casos)

---

## Como rodar

1. **Clone o repositório:**

git clone https://github.com/johannossanes/text-adventure-ia.git
cd text-adventure-ia

2. Instale as dependências:

  pip install -r requirements.txt

3. Configure a chave de API da Google:

  Crie um arquivo .env ou defina diretamente em seu script:

  import google.generativeai as genai
  genai.configure(api_key="SUA_API_KEY")

  Ou use uma variável de ambiente:

  set GOOGLE_API_KEY=sua_api_key

4. Execute o jogo via terminal:

  python textadventure.py

## Recursos implementados

  - Interface interativa com tkinter

  - Comunicação com modelo Gemini da Google

  - Sistema de entrada e resposta via chat

  - Pronto para integração com:

    - Aventuras base (desenvolendo)

    - Sistema de inventário, combate e escolhas(desenvolvendo)

## Em desenvolvimento

  - Escolha de classe

  - Pontos de vida

  - Inventário

  - Combate com IA ou sistema próprio

  - Bestiário e coleta de criaturas

  - Geração de imagens para locais

## Autor

  Desenvolvido por Johann Ossanes
  Feito com Python, criatividade e um pouco de magia negra IA.
