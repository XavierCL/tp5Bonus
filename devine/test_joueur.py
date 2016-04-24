#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Pour partir les tests, on tape:
# python3 -m unittest discover devine

# from unittest import TestCase
import unittest

import mock

import devine.joueur

def identique(donnee):
    return donnee

class TestJoueur_jouer(unittest.TestCase):

    def setUp(self):
        # imp = devine.contact.Contact()

        # Remplace la méthode imprime_reponse
        self.imp = mock.Mock()
        self.imp.imprime_reponse = mock.MagicMock(side_effect=identique)

        # Remplace la méthode entree
        # self.imp.entree.return_value = '11'

        # Remplace la méthode nombre

    def test_jouer_1(self):

        # Nombre à deviner
        alea = mock.Mock()
        alea.nombre.return_value = 50

        # Nombres fournis
        imp = mock.Mock()
        imp.imprime_reponse = mock.MagicMock(side_effect=identique)
        imp.entree.side_effect = ['11']

        joueur_mock2 = devine.joueur.Joueur(alea, imp, 1, "joueur Mock")

        self.assertEqual(joueur_mock2.jouer(), '1: 11 trop bas')


    def test_jouer_2(self):

        # Nombre à deviner
        alea = mock.Mock()
        alea.nombre.return_value = 10

        # Nombres fournis
        imp = mock.Mock()
        imp.imprime_reponse = mock.MagicMock(side_effect=identique)
        imp.entree.side_effect = ['11', '9']

        joueur_mock2 = devine.joueur.Joueur(alea, imp, 2, "joueur Mock")

        self.assertEqual(joueur_mock2.jouer(), '2: 11 trop haut1: 9 trop bas')

    def test_jouer_3(self):

        # Nombre à deviner
        alea = mock.Mock()
        alea.nombre.return_value = 60

        # Nombres fournis
        imp = mock.Mock()
        imp.imprime_reponse = mock.MagicMock(side_effect=identique)
        imp.entree.side_effect = ['70', '50', '55']

        joueur_mock2 = devine.joueur.Joueur(alea, imp, 2, "joueur Mock")

        self.assertEqual(joueur_mock2.jouer(), '2: 70 trop haut1: 50 trop bas')

