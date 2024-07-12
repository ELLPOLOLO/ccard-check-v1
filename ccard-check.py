def check_credit_card(card_number):
    card_info = {
        "American Express": {"prefixes": ["34", "37"], "bank": "American Express"},
        "Visa": {"prefixes": ["4"], "bank": "Visa"},
        "MasterCard": {"prefixes": ["51", "52", "53", "54", "55"], "bank": "MasterCard"},
        "Discover": {"prefixes": ["6011"], "bank": "Discover"}
    }
    
    bin_country = {
        "United States": ["4"],
        "Canada": ["4"],
        "Mexico": ["4"],
        "United Kingdom": ["51", "52", "53", "54", "55"],
        "Australia": ["51", "52", "53", "54", "55"]
    }
    
    bank_names = {
        "011": "Bancomer",
        "012": "Banamex",
        "013": "Santander",
        "014": "HSBC",
        "017": "BBVA"
    }

    card_number = card_number.replace(" ", "").replace("-", "")
    
    if len(card_number) != 16 or not card_number.isdigit():
        return False, None, None, None, None
    
    card_type = "Desconocido"
    bank = "Desconocido"
    country = "Desconocido"
    bank_brand = "Desconocido"

    for key, value in card_info.items():
        for prefix in value["prefixes"]:
            if card_number.startswith(prefix):
                card_type = key
                bank = value["bank"]
                break

    for country_name, country_bins in bin_country.items():
        for bin in country_bins:
            if card_number.startswith(bin):
                country = country_name
                break
    
    if card_number[:3] in bank_names:
        bank_brand = bank_names[card_number[:3]]
    
    return True, card_type, bank, country, bank_brand

card_number = input("Ingresa el número de la tarjeta de crédito: ")

valid, card_type, bank, country, bank_brand = check_credit_card(card_number)

if valid:
    print("La tarjeta de crédito es válida.")
    print("Tipo de Tarjeta:", card_type)
    print("Banco:", bank)
    print("País:", country)
    print("Marca de Banco:", bank_brand)
else:
    print("La tarjeta de crédito es inválida.")