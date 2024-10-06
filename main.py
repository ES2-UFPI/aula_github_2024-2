from menu import Menu

if __name__ == "__main__":
    main_menu = Menu(["Conta", "Cliente", "Operações"], "Menu Principal")
    print(f"{main_menu.get_selection()} foi selecionada")
    print("Fim")