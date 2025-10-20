import random
import string

# Combina letras maiúsculas, minúsculas, dígitos e pontuação.
all_characters = string.ascii_letters + string.digits + string.punctuation


def gen_password(length):
    # Gera uma senha aleatória com o comprimento especificado.
    if length < 8:
        print("O comprimento da senha deve ser de pelo menos 8 caracteres!")
        return None

    # Gera a senha usando a variável all_characters
    password = "".join(random.choice(all_characters) for i in range(length))
    return password


def validate_password(password):
    # Valida se uma senha atende aos critérios de segurança.
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in string.punctuation for char in password):
        return False
    return True


def main():
    #
    while True:
        print("\n" + "-" * 20)
        print("1. Gerar senha")
        print("2. Validar senha")
        print("3. Sair")
        print("-" * 20)

        choice = input("Entre com a sua escolha: ")

        if choice == "1":
            try:
                length = int(input("Digite o comprimento da senha: "))
                password = gen_password(length)

                # Se a senha foi gerada com sucesso, mostre-a
                if password:
                    print(f"Senha gerada: {password}")
            except ValueError:
                print("Por favor, digite um número válido para o comprimento.")

        elif choice == "2":
            user_password = input("Digite a senha para validar: ")

            if validate_password(user_password):
                print("Senha forte e válida!")
            else:
                print(
                    "Senha fraca ou inválida. Requisitos: mínimo 8 caracteres, com maiúscula, minúscula, número e símbolo."
                )

        elif choice == "3":
            print("Saindo do programa...")
            break
            # Quebra o loop while True e encerra o programa

        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
