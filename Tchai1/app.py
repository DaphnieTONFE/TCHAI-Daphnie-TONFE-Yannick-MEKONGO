# This Python file uses the following encoding: utf-8
# !/Users/yannickedouard/pythonProject/venv/bin/python
# -*- coding: utf-8 -*-
import hashlib

from flask import *
from operator import itemgetter
from datetime import datetime

from future.backports.urllib import request

app = Flask(__name__)
# app.decode(encoding= 'UTF-8', errors='strict')
enregistrement_t = []
resultSearch = []

# ouverture de mon fichier base de données
with open('bd.txt', encoding="utf8", errors='ignore') as file:
    # lecture des lignes
    for line in file:
        tuple = ()
        for word in line.split():
            tuple = tuple + (str(word),)
        enregistrement_t.append(tuple)
file.close()


# ordre chronologique
@app.route('/')
def tridate():
    # enregistrement_t.sort(key=lambda t: t[3])
    return 'Hello <ul>' + ''.join(
        ['<li>' + format(n) for n in enregistrement_t]
    ) + '</ul>\n', 200


# A3
@app.route('/search')
def PrintSearch():
    resultSearch.sort(key=lambda t: t[3])
    return 'Research give <ul>' + ''.join(
        ['<li>' + format(n) for n in resultSearch]
    ) + '</ul>\n', 200


# enregistrement de la transaction
@app.route('/enregistrement_t', methods=['POST'])
def add():
    if request.method == 'POST':
        P1 = request.values.get('P1')
        P2 = request.values.get('P2')
        d = request.values.get('d')
        a = request.values.get('a')

        fichier = open("bd.txt", "a")
        fichier.write("\n")
        data = str(P1) + " " + str(P2) + " " + str(a) + " " + str(d)

        # hachage
        h = hashlib.sha256(bytes(data, encoding='utf-8')).hexdigest()
        n = len(enregistrement_t)
        h = h + enregistrement_t[n - 1][4]

        fichier.write(data + " " + str(h))

        fichier.close()

        enregistrement_t.append((str(P1), str(P2), str(a), str(d)))
        return redirect(url_for('tridate'))


# enregistrement de la transaction lié à une personne
@app.route('/search/<name>')
def search(name):
    # creation d'une autre liste
    Personne_t = []
    for n in enregistrement_t:
        if name in (n[0], n[1]):
            Personne_t.append(n)
    # affichage dans l'ordre chronologique
    Personne_t.sort(key=lambda t: t[3])
    return 'Transactions que cette personne a déjà effectuée : <ul>' + ''.join(
        ['<li>' + format(n) for n in Personne_t]
    ) + '</ul>\n', 200

#LA
# affiche le solde d une personne
@app.route('/solde/<name>')
def solde(name):
    # on initialise le solde à o
    Solde = 0
    # Si le nom entré est egale à p1 on procéde à un a-solde et si le nom entré est egale à p2 on fait a+solde
    for n in enregistrement_t:
        if name == n[1]:
            Solde = Solde + int(n[2])
        if name == n[0]:
            Solde = Solde - int(n[2])
    affiche = 'Le solde de ' + name + ' est: '
    return affiche + ''.join(
        str(Solde)
    ), 200


# verification de l'integrité
@app.route('/integrite', methods=['POST', 'GET'])
def integrity():
    if request.method == 'POST':
        P1 = request.values.get('P1')
        P2 = request.values.get('P2')
        d = request.values.get('d')
        a = request.values.get('a')

        data = str(P1) + " " + str(P2) + " " + str(a) + " " + str(d)

        # hachage
        h = hashlib.sha256(bytes(data, encoding='utf-8')).hexdigest()

        for i in enregistrement_t:
            if h == i[4]:
                return 'la base de données est intègre'
            if h != i[4]:
                return 'la base de données pas intègre '


# afficher une liste de transaction dans l'ordre chronologique
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
