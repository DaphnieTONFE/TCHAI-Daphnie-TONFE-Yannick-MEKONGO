# TCHAI-Daphnie-TONFE-Yannick-MEKONGO

_`blibliothèque Flask utilisée, Pycharm comme IDE, Github via pycharm pour les requêtes git`_


#### AUTEURS:
 **`- MEKONGO ABANDA Yannick :` mekongoabanda21@gmail.com**
 
 **`- TONFE TCHATAT Daphnie :` daphnietonfe@gmail.com**
 
##EXERCICE 3
(A1) l'enregistrement d'une transaction se fait via la méthode: def add ().

- `Pour le faire , nous lançons sur le navigateur le fichier enregistrement.HTML. on entre les données et on clique sur SUBMIT`

(A2) l'affichage d'une liste de toutes les transactions dans l’ordre chronologique se fait avec def tridate():

- `On a qu'à exécuter app.py puis lancer le localhost`

(A3) Afficher une liste des transactions dans l’ordre chronologique liées à une personne donnée : def search() :

- http://localhost:5000/search/name --> name c'est le nom de la personne
 
(A4) Afficher le solde du compte de la personne donnée: def solde():

##EXERCICE 4
Attaque en changeant le montant d'une transaction
- `Pour le faire , nous avons ecrit un script shell qui permet de modifier les valeurs des transactions directement sur le fichier bd.txt qui est notre data set`

##EXERCICE 5
Integration de la nouvelle structure
-  `à l'aide de la bibliothèque hashlib , nous avons intégré le hachage dans la methode enregistrement.La valeur du hash est ensuite sauvegardé dans notre base de données  `

##EXERCICE 6
Verification de l'integrité
`Pour la vérification de l'integrité , nous avons procéde à une comparaison des hash d'une transaction deja présente dans la base de données avec le nouveau hach de cette meme transaction`
##EXERCICE 7
Verification que l'attaque précedente 
`Lorsqu'on refait une attaque , on constate qu'on peut desormais remarqué toutes modifications au niveau de la base de données. Ceci grâce à l'integrité`
##EXERCICE 8
Attaque en supprimant une transaction
- `Pour le faire , nous avons ecrit un script shell qui permet de supprimer (attaque2) des transactions directement sur le fichier bd.txt qui est notre data set`
##EXERCICE 9
Modification de la methode du calcul
- `Pour cela, nous avons prit la valeur du hash precédent additionné avec le hash obtenu pour obtenir le hi+1`
##EXERCICE 10
- ``


