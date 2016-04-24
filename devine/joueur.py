#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Joueur:
    def __init__(self, aleatoire, contact, vies, pseudo):

        self.vies = vies

        self.pseudo = pseudo

        self.alea = aleatoire

        self.contact = contact


    def jouer(self):
        appreciation = "?"

        reponses = ''

        nombre_a_deviner = self.alea.nombre(100)

        while self.vies > 0:
            nombre_fourni =  self.contact.entree(appreciation + " -- " +
                    self.pseudo + " : " +
                    str(self.vies) +
                    " vies restantes. Nombre choisi : ")

            if int(nombre_fourni) < nombre_a_deviner :
                appreciation = "trop bas"
                reponses += self.contact.imprime_reponse(str(self.vies) + ': ' + nombre_fourni + ' ' + appreciation)

            elif int(nombre_fourni) > nombre_a_deviner :
                appreciation = "trop haut"

                reponses += self.contact.imprime_reponse(str(self.vies) + ': ' + nombre_fourni + ' ' + appreciation)
            else :
                appreciation = "bravo !"

                reponses += self.contact.imprime_reponse(str(self.vies) + ': ' + nombre_fourni + ' ' + appreciation)
                break

            self.vies -= 1

        return reponses

