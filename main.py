from forex_python.converter import CurrencyRates

cr = CurrencyRates()

def valeurs():
    valeur_de_base = float(input("quel est le montant que vous souhaitez convertir ? "))
    devise_de_base = input("Quelle devise correspond a ce montant ? (euro, livre ou dollar) ")
    devise_cible = input("En quelle devise souhaitez vous convertir ce montant ? (euro, livre ou dollar) ")

    dictionnaire_devise = {
        "euro" : "EUR",
        "dollar" : "USD",
        "livre" : "GBP"
    }

    if devise_de_base not in dictionnaire_devise and devise_cible not in dictionnaire_devise:
        print("Devise non prise en charge, veuillez selectionner une devise valide.")
        return

    taux_de_change = cr.get_rate(dictionnaire_devise[devise_de_base], dictionnaire_devise[devise_cible])

    convertir_montant = valeur_de_base / taux_de_change

    print(f"{valeur_de_base}{devise_de_base} équivaut à {convertir_montant:.2f}{devise_cible}")


while True:
    valeurs()
    cont = input("Voulez-vous effectuer une autre conversion ? (oui/non) : ").lower()
    if cont == "non":
        break