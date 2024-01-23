import openai
import json
import informacoes

chave_api = informacoes.API_KEY


openai.api_key = chave_api
assistant_gpt = informacoes.informacoes


def enviar_mensagem(mensagem, lista_mensagens=[{"role": "assistant", "content": assistant_gpt[0]},
                                               {"role": "assistant",
                                                   "content": assistant_gpt[1]},
                                               {"role": "assistant",
                                                   "content": assistant_gpt[2]},
                                               {"role": "assistant",
                                                   "content": assistant_gpt[3]}
                                               ]):

    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )

    resposta = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens
    )

    return resposta.choices[0].message


lista_mensagens = []
while True:
    texto = input("-> --")


    resposta = enviar_mensagem(texto, lista_mensagens)
    lista_mensagens.append(resposta)
    print("chatbot:", resposta.content)
