contacts = []

def list_contacts(contacts):
    print("\n📃 Seus contatos:")
    for index, contact in enumerate(contacts, start=1):
        status = "❤️" if contact["favorite"] else " "
        print(f"{index}. {contact["name"]} | {contact["email"]} | {contact["phone"]} | {status}")
        print("--------------------------------------------------------------------------------")

    return

def add_contact(name, email, phone):
    new_contact = {
        "name": name,
        "email": email,
        "phone": phone,
        "favorite": False
    }

    contacts.append(new_contact)
    return

def update_contact(contacts, contact_index, new_name, new_email, new_phone):
    adjusted_index = int(contact_index) - 1
    if adjusted_index >= 0 and adjusted_index < len(contacts):
        contacts[adjusted_index]["name"] = new_name
        contacts[adjusted_index]["email"] = new_email
        contacts[adjusted_index]["phone"] = new_phone
    else:
        print("Índice de contato inválido")
    return

def delete_contact(contacts, contact_index):
    adjusted_index = int(contact_index) - 1
    contacts.remove(contacts[adjusted_index])
    return

def add_to_favorite(contacts, contact_index):
    adjusted_index = int(contact_index) - 1
    contacts[adjusted_index]["favorite"] = True
    return

def remove_contact_from_favorite(contacts, contact_index):
    adjusted_index = int(contact_index) - 1
    contacts[adjusted_index]["favorite"] = False

def list_favorite_contacts(contacts):
    favorite_contacts = []
    for contact in contacts:
        if contact["favorite"] == True:
            favorite_contacts.append(contact)
            print(f"{contact["name"]} | {contact["email"]} | {contact["phone"]} | ❤️")
            print("--------------------------------------------------------------------------------")

    return

while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Visualizar contatos")
    print("2. Adicionar contato")
    print("3. Editar contato")
    print("4. Deletar contato")
    print("5. Adicionar contato como favorito")
    print("6. Remover contato dos favoritos")
    print("7. Visualizar favoritos")
    print("8. Sair")
    choice = input("Digite a sua escolha: ")

    if choice == "1":
        list_contacts(contacts)

    elif choice == "2":
        print("Preencha as opções abaixo para cadastrar um novo contato:")
        contact_name = input("Qual o nome do seu contato? ")
        contact_email = input("Qual o email do seu contato? ")
        contact_phone = input("Qual o celular/telefone do seu contato? ")
        add_contact(name=contact_name, email=contact_email, phone=contact_phone)
        print("✅ Contato adicionado com sucesso!")

    elif choice == "3":
        print("Escolha um desses contatos para atualizar.")
        list_contacts(contacts)
        chosen_contact = input("Digite o número do contato que deseja atualizar: ")
        new_name = input("Digite o novo nome do contato: ")
        new_email = input("Digite o novo email do contato: ")
        new_phone = input("Digite o novo celular/telefone do contato: ")
        update_contact(
            contacts=contacts,
            contact_index=chosen_contact,
            new_name=new_name,
            new_email=new_email,
            new_phone=new_phone
        )
        print("✅ Contato atualizao com suzesso!")

    elif choice == "4":
        list_contacts(contacts)
        chosen_contact_to_delete = input("Insira o número do contato que deseja deletar: ")
        delete_contact(contacts=contacts, contact_index=chosen_contact_to_delete)
        print("✅ Contato deletado com sucesso!")


    elif choice == "5":
        list_contacts(contacts)
        chosen_favorite_contact = input("Digite o número do contato que deseja adicionar aos favoritos: ")
        add_to_favorite(contacts=contacts, contact_index=chosen_favorite_contact)
        print("✅ Contato adicionado aos favoritos")

    elif choice == "6":
        list_contacts(contacts)
        chosen_favorite_contact_to_remove = input("Digite o número do contato que deseja remover dos favoritos: ")
        remove_contact_from_favorite(contacts=contacts, contact_index=chosen_favorite_contact_to_remove)
        print("✅ Contato removido dos favoritos")

    elif choice == "7":
        print("❤️ Contatos favoritos")
        list_favorite_contacts(contacts=contacts)

    elif choice == "8":
        break