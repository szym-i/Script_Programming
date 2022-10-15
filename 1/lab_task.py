def sprzedaz(article, quantity, client, clients_bought_items, items):
    if article not in items.keys():
        print(f"Brak {article} na stanie")
        return items, clients_bought_items
    elif items[article] < quantity:
        print(f"Brak wystarczającej ilości {article} na stanie")
        return items, clients_bought_items
    else:
        print(f"Udało się kupić {article}")
        clients_bought_items[client] = {article: quantity}
        items[article] -= quantity
        return items, clients_bought_items

def zwrot(article, quantity, client, clients_bought_items, items):
    if article not in items.keys():
        print("Nie możesz zwrócić przedmiotu którego nie ma w sklepie")
        return items, clients_bought_items
    else:
        if client not in clients_bought_items.keys():
            print("Nie możesz czegoś zwrócić jeśli nic nie kupiłeś!")
            return items, clients_bought_items
        else:
            if clients_bought_items[client][article] > quantity:
                clients_bought_items[client][article] -= quantity
                items[article] += quantity
                return items, clients_bought_items
            else:
                print("NIe możesz zwrócić więcej niż kupiłeś")
                return items, clients_bought_items

if __name__ == '__main__':
    clients_bought_items = {}
    print("Wprowadzaj dane w postaci: {operation} {article} {quantity} {client}")
    items = {"laptop":10, "RAM":4}
    try:
        while True:
            print(f"Dostępne artykuły:\n{items}")
            x = input().split()
            if len(x) == 4:
                operation = x[0]
                article = x[1]
                quantity = int(x[2])
                client = x[3]
                if operation == 'sprzedaz':
                    items, clients_bought_items = sprzedaz(article, quantity, client, clients_bought_items, items)
                elif operation == 'zwrot':
                    items, clients_bought_items = zwrot(article, quantity, client, clients_bought_items, items)
                else:
                    print("Wprowadź poprawną operację") 
            else:
                print("Wprowadzaj poprawne dane")
    except EOFError:
        print(f"Lista zakupów klientów:\n{clients_bought_items}")
    except:
        print("Wprowadzaj poprawne dane") 
