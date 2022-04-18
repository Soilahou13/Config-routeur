# Config-routeur
interface de configurations des routeurs Linux
Interface graphique d’utilisateur (GUI) qui permet la configuration des routeurs linux dans un réseau.
Cela a pour but d’éviter les configurations via ligne de commande, 
en offrant une interface plus intuitive à l’utilisateur, qui, en théorie,
n’aurait plus besoin de connaître les commandes spécifiques des configurations.

Interface graphique d’utilisateur (GUI) qui permettant la
configuration des routeurs Linux dans un réseau. Cela a pour but d’éviter les configurations
via ligne de commande, en offrant une interface plus intuitive à l’utilisateur, qui, en théorie,
n’aurait plus besoin de connaître les commandes spécifiques des configurations.

###1) Fonctionnalités de configuration :
   1) L’utilisateur a le choix du routeur qu’il désire configurer. 
   2) Une fois sélectionné, les caractéristiques suivantes seront accessibles :
      1) Configuration de l’interface de communication (fe1/0, ge0/0, …). Cela implique
      les adresses IP, les masques des sous-réseaux et les passerelles par défaut. 
      2) Le nom du routeur. 
      3) La table de routage s’il le faut. 
   3) L’ajout/suppression d’un routeur.

###2) Fonctionnalités d’affichage :
   1) L’affichage de toutes les configurations (accessibles dans le logiciel) d’un routeur : @IP, masques, table de routage.
   2) Des consignes : des labels ou des textes qui apparaissent pour expliquer le
fonctionnement d’un champ/bouton.
###3) Éléments de la GUI :
   1) Barre de menus :
      1) Fonction « quitter ». 
      2) Fonction enregistrer. Une fois
      cliqué, toutes les informations saisies seront stockées dans un fichier. 
      3) Fonction lire : on récupère un fichier de configuration. 
   2) Affichage d’un écran d’introduction : le panneau de configuration ne sera affiché
   qu’après la clique sur un bouton

##Technologies utilisées :
- QtDesigner + PyQT
- Paramiko