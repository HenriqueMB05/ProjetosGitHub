from random import choice, randint
# Banco de palavras
dic = {
    "Linguagens": ["Python", "Java", "JavaScript", "PHP", "lua", "ecmaScript", "TypeScript","C","C++", "C#", "Assembly"],
    "Comida": ["Tacaca", "Vatapa", "Acai", "Feijoada", "moqueca","Ensopado", "buchada","Strogonoff","Bolo", "Cocada"],
    "Trabalhos": ["chapeiro","Policial","Acougueiro", "Empresario", "Mecanico","Padeiro", "Confeiteiro"]
}
# Sorteando a chave do dicionario de forma separada, para conseguir usar no len de sua lista e também como a dica
key = choice(list(dic.keys()))
palavra = dic[key][randint(0,len(dic[key])-1)]
print(palavra)
letras_usuario = []

chances = 4


while True:

    print(f"Dica: {key}")

    # Verificando as letras da palavra
    # Se a letra dentro da lista onde ficam armazendas as tentativas do user existir na palavra els será digitada caso o contrario será escrito uma "_" 
    for letra in palavra:

        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"Você tem {chances} chances")

    tentativa = input("Escolha uma letra para adivinhar: ")
    letras_usuario.append(tentativa.lower())

    

    # Esse bloco funciona para a finalização do jogo, caso as chances se zerem ou caso a variavel ganhou mantenha o seu status de True será finalizado.
    if tentativa.lower() not in palavra.lower():
        chances -= 1
    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False
    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns, você ganhou. A palavra era: {palavra}")
else:
    print(f"Você perdeu! A palavra era: {palavra}")