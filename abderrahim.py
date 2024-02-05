import unittest
"""
Count names with more than seven letters
"""
def count_names(prenoms: list) -> bool:
    more_than_seven = 0
    len_mot = 7
    for prenom in prenoms:
        if len(prenom) > len_mot:
            more_than_seven += 1
            print("Prenom supérieur à 7 : " + prenom)
        else:
            print("Prenom inférieur ou égal à 7 : " + prenom)
    return more_than_seven

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = count_names(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()