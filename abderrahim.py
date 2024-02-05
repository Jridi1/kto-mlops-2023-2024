"""
Count names with more than seven letters
"""
def names(prenoms: list) -> bool:
    more_than_seven = 0
    len_mot = 7
    for prenom in prenoms:
        if len(prenom) > len_mot:
            more_than_seven += 1
            print("Prenom supérieur à 7 : " + prenom)
        else:
            print("Prenom inférieur ou égal à 7 : " + prenom)
    return more_than_seven

prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
print("Nombre de prénoms supérieurs à 7 : " + str(names(prenoms=prenoms)))