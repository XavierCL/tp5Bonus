#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

import devine.joueur

import devine.aleatoire
import devine.contact

# python3 -m unittest discover devine

import unittest

def load_tests(loader, tests, pattern):
    return loader.discover('.')

if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        testsuite = unittest.TestLoader().discover('devine/devine')
        unittest.TextTestRunner(verbosity=2).run(testsuite)
        sys.exit(0)

    imp = devine.contact.Contact()

    alea = devine.aleatoire.Aleatoire()

    # Initialisation des deux joueurs
    j1 = devine.joueur.Joueur(alea, imp, 10, "joueur 1")
    j2 = devine.joueur.Joueur(alea, imp, 10, "joueur 2")

    # j1 et j2 jouent
    j1.jouer()
    j2.jouer()


    # Nombre de vies restantes à chaque joueur
    imp.imprime_reponse("Nombre de vies restantes à chaque joueur")
    imp.imprime_reponse(j1.pseudo  + " : " + str(j1.vies) + " restantes")
    imp.imprime_reponse(j2.pseudo  + " : " + str(j2.vies) + " restantes")

    # Résultat de la partie
    imp.imprime_reponse("Résultat de la partie: ")
    if j1.vies < j2.vies:
        imp.imprime_reponse(j1.pseudo + " a gagné la partie")
    elif j1.vies == j2.vies:
        imp.imprime_reponse("match nul")
    else: imp.imprime_reponse(j2.pseudo + " a gagné la partie")



