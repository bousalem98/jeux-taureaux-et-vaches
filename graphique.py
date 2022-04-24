from tkinter import *
from tkinter import ttk
import random
from time import *
import os


# fonction qui genere un code secret de 4 chiffre, le cs ne doit pas commencer par 0
def generateCodeSecret():
    i = 0
    x = random.randint(1, 9)
    code = str(x)
    while i < 3:
        x = random.randint(0, 9)
        if str(x) in code:
            continue
        else:
            code += str(x)
            i += 1
    return code


# fonction qui retourne les nombre teaureau dans un nombre
def nbTaureaux(code):
    t = 0
    for j in code:
        if j in CS and CS.index(j) == code.index(j):
            t += 1
    return t


# fonction qui retourne les nombre vaches dans un nombre
def nbVaches(code):
    v = 0
    for j in code:
        if j in CS and CS.index(j) != code.index(j):
            v += 1
    return v


# fonction definit pour le bouton "info" qui consiste a creer un nouvel widget en affichant les information de jeu
def infobutton():
    tkinfo = Tk()
    tkinfo.title("Info")
    tkinfo.geometry("520x460")
    tkinfo.configure(background='#FFFAFA')
    Label(tkinfo, bg="#FFFAFA", fg="#333D79", text='Bonjour '
                                                   'Ce ci est un jeu très populaire en Bulgarie, proche et\n'
                                                   'probablement ancètre du célèbre jeu Mastermind -- trouver le\n'
                                                   'nombre auquel pense votre adversaire. D\'habitude on joue avec \n'
                                                   'un crayon et du papier, contre un autre enfant. Le premier à\n'
                                                   'découvrir le nombre secret de l\'autre gagne. Ce programme est '
                                                   'une version simulaire de cette jeu, \n '
                                                   'il faut juste deviner le nombre choisi par l\'ordinateur.\n'
                                                   'Essayez de deviner le nombre secret avec un minimum de questions '
                                                   '(moins de 10).\n '
                                                   ' L\'ordinateur indique le nombre de vos coïncidances.\n'
                                                   'Règles:\n'
                                                   '1. Tous les chiffres dans le nombre secret sont differents.\n'
                                                   '2. Le nombre secret ne peut pas commencer par zéro (dans les '
                                                   'règles officielles).\n '
                                                   '3. Si dans votre proposition il y a des chiffres du nombre '
                                                   'secret,\n '
                                                   'aux bons endroits, ils sont des Taureaux.\n'
                                                   '4. Si dans votre proposition il y a des chiffres du nombre '
                                                   'secret, \n '
                                                   'mais pas aux bons endroits, ils sont des Vaches.\n'
                                                   '5. Une réponse sera affichée dans la boîte en dessous.\n'
                                                   '6. Vous avez 10 essai pour chaque partie\n'
                                                   'Example:\n'
                                                   'n. secret: 2567\n'
                                                   'essai: 6578 : 1 taureau et 2 vaches\n'
                                                   'Il faut d\'abord cliquer sur le bouton Start pour commencer le '
                                                   'jeu\n '
                                                   'puis dans le champs de saisie vous devez taper un nombre de 4 '
                                                   'chiffres distinctes.\n '
                                                   'Apres que tu saisie votre proposition \n'
                                                   'vous pouvez continuer en cliquant sur le bouton Tester le Nombre '
                                                   '.\n '
                                                   'Si vous voulez rejouer sans avoir la bonne solution il faut '
                                                   'cliquer sur Stop puis Start .\n '
                                                   'Si vous trouvez le jeu difficile, vous pouvez demander un '
                                                   '"joker", avec le bouton "Besoin '
                                                   'Aide?"\n '
                                                   'pour voir un chiffre secret dans une aleatoire position\n '
                                                   'Pour voir votre liste des scores appuyer sur Score .'
                                                   ' Si vous decidez de sortir de jeu, cliquer sur Exit .\n '
                                                   'Si vous trouvez le code secret vous pouvez rejouer ou bien sortir.'

          ).place(x=0, y=5)


# fonction definit pour le bouton "start"
def btnstart():
    global CS, tbegin, nbe
    CS = generateCodeSecret()
    # initialise le nombre d'essai a 10
    nbe = 10
    print(CS)
    nbech = str(nbe)
    # affichage des nombre d'essai
    chaine_sorti4.configure(text=nbech)
    # activation et desactivation de status des boutons et labels
    bouton_tester["state"] = NORMAL
    bouton_stop["state"] = NORMAL
    tchaine["state"] = NORMAL
    bouton_aide["state"] = NORMAL
    bouton_start["state"] = DISABLED
    historique["state"] = NORMAL
    historique.delete('1.0', END)
    chaine_sorti2.configure(text="")
    tchaine.delete(0, 10)
    # debut de compteur de temps
    tbegin = time()


# fonction definit pour le bouton "stop"
def btnstop():
    # activation et desactivation de status des boutons et labels
    bouton_tester["state"] = DISABLED
    bouton_stop["state"] = DISABLED
    tchaine["state"] = NORMAL
    tchaine.delete(0, 10)
    tchaine["state"] = DISABLED
    bouton_start["state"] = NORMAL
    bouton_aide["state"] = DISABLED
    chaine_sorti4.configure(text="")
    chaine_sorti2.configure(text="")
    historique.delete('1.0', END)
    historique["state"] = DISABLED


# fonction retourne faux si user entrer des chiffres differentes
# sinon retourne faux
def difference(code):
    test = []
    dff = False
    for j in code:
        if j in test:
            dff = True
        else:
            test.append(j)
    return dff


# fonction definit pour le bouton "Tester le nombre"
def btntester():
    global nbe
    # si le nombre d'essai supperieur a 0 (0 < nombre d'essai =< 10 )
    if nbe > 0:
        # recupere ce qui entrer par l'utilisateur
        c = str(tchaine.get())
        # si l'utilisateur donne un nombre valide (qui contient 4 chiffre differents)
        if len(c) == 4 and (c.isdigit()) and not difference(c):
            textError.configure(text="")
            v = str(nbTaureaux(c)) + " T , " + str(nbVaches(c)) + " V"
            v2 = "\tEssai " + str(11 - nbe) + ": " + c + " : " + str(nbTaureaux(c)) + " T , " + str(
                nbVaches(c)) + " V\n"
            # si le nombre donner n'est pas juste
            if nbTaureaux(c) < 4:
                # decrimentation de nombres d'essai
                nbe = nbe - 1
                # afficher les resultats
                chaine_sorti2.configure(text=v)
                historique.insert(END, v2)
                nbech = str(nbe)
                chaine_sorti4.configure(text=nbech)
            # si le nombre donner est juste
            else:
                # fin de compteur de temps
                tend = time()
                # calcule les nombres des secondes ecouler pour trouver la solution
                temps = tend - tbegin
                # convertir ce nombre de secondes en minutes et secondes  avec "gmtime"
                tm = strftime("%M minute et %S secondes ", gmtime(temps))
                v3 = "\tBRAVO ! vous avez gagné\n \tSolution trouver dans " + tm + "\n  "
                # affichage des resultats
                chaine_sorti2.configure(text=v)
                historique.insert(END, v2)
                # decrimentation de nombres d'essai
                nbech = str(nbe - 1)
                # affichage et desactivation necessaire
                chaine_sorti4.configure(text=nbech)
                historique.insert(END, v3)
                bouton_tester["state"] = DISABLED
                bouton_aide["state"] = DISABLED
                tchaine["state"] = DISABLED
                bouton_stop["state"] = DISABLED
                bouton_start["state"] = NORMAL
                # tm doit etre contient temps ecouler et le nombre d'essai
                tm = tm + str(11 - nbe) + " Essais"
                # sauvegardage des scores de utilisatur dans un fichier "Score.txt"
                # cible : le lien de fichier "Score" dans le disque
                cible = "Score.txt"
                # si le fichier est existe on va sauter un ligne et on va inserer le nouveau score
                if os.path.exists(cible):
                    with open(cible, "a", encoding="utf-8") as score:
                        score.write("\n" + tm)
                # sinon on va inserer le nouveau score directement
                else:
                    with open(cible, "a", encoding="utf-8") as score:
                        score.write(tm)

        # si l'utilisateur donne un nombre non valide
        else:
            # affichage d'erreur
            textError.configure(text="Erreur! N'entrez que 4 chiffres , tous différents.")
    # si l'utilisatur ne trouve pas le nombre secret et le nombre d'essai = 0
    if nbe == 0:
        # affichage necessaire
        nbech = str(nbe)
        chaine_sorti4.configure(text=nbech)
        v3 = "\tVous avez perdu  le code secret est : " + CS + "\n"
        historique.insert(END, v3)
        bouton_tester["state"] = DISABLED
        bouton_aide["state"] = DISABLED
        tchaine["state"] = DISABLED
        bouton_stop["state"] = DISABLED
        bouton_start["state"] = NORMAL

    # vider le champs d'insertion des chiffres apres le click sur le bouton "tester le nombre"
    tchaine.delete(0, 10)


# fonction definit pour le bouton "besoin aide?"
def btnaide():
    # desactivation de status de bouton
    bouton_aide["state"] = DISABLED
    # on doit choisi un numero de code secret par hasard et en l'affiche a l'utilisateur comme suit
    # par exemple le code secret est : 4529 le systeme affiche: **2*
    i = random.randint(0, 3)
    ad = CS[i]
    ch = ["*", "*", "*", "*"]
    ch[i] = ad
    ch2 = ' '.join([str(elem) for elem in ch])
    ch3 = "\taide   : " + ch2 + "\n"
    historique.insert(END, ch3)


# fonction definit pour le bouton "score"
def btnscore():
    # cree un nouvel widget
    # afficher un tableau contient 3 colonne : Ordre,Temps Ecoulé,Nb des essais
    # et on affiche les scores de l'utilisateur
    root = Tk()
    root.title("Score")
    root.geometry("500x200")
    root.configure(background='#FFFAFA')
    Label(root, bg="#FFFAFA", fg="#333D79", text="Liste des scores", font='Relaway').place(x=180, y=12)
    tree = ttk.Treeview(root, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=50, y=50, width=400)
    scroll = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    scroll.place(x=450, y=50, width=20, height=130)
    tree.configure(yscrollcommand=scroll.set)
    # === dimension des colonnes ===
    tree.column(1, width=20)
    tree.column(2, width=150)
    tree.column(3, width=70)
    # === Création de l ’ entête ===
    tree.heading(1, text="Ordre")
    tree.heading(2, text="Temps Ecoulé")
    tree.heading(3, text="Nb des essais")
    # le lien de fichier score dans le disque
    cible = "Score.txt"
    # on va lire de fichier score (contient tous les scores realiser par l'utilisateur)
    # si le fichier score n'existe pas il affiche un tableau vide sinon il affiche les scores
    if os.path.exists(cible):
        with open(cible, "r", encoding="utf-8") as scoref:
            # on lire de fichier score et on mettre le contenue dans la chaine "contenu"
            contenu = scoref.read()
        # on coupe la chaine obtenu en sous chaine separent par \n et en mettre ces sous chaine dans une liste
        lignes_contenu = contenu.split("\n")
        # creer un dictionnaire, en utilisant les items de liste comme cle de dict (pour eviter la duplication des
        # scores)
        lignes_contenu = list(dict.fromkeys(lignes_contenu))
        lignes_contenu.sort()
        for j in range(len(lignes_contenu)):
            tpecoule = str(lignes_contenu[j])
            pos2 = tpecoule.find('Essais')
            pos1 = pos2 - 3
            pos2 = pos2 + len('Essais')
            nbessai = tpecoule[pos1:pos2]
            tpecoule = tpecoule.replace(nbessai, "")
            tree.insert('', 'end', values=(j + 1, tpecoule, nbessai))


# creation de l'interface graphique
window = Tk()
window.title("Taureaux et vaches")
window.geometry("700x520")
window.configure(background='#FFFAFA')

# les styles
style = ttk.Style()
style.configure("TButton", foreground="#333D79", background="#333D79")
style.configure("TLabel", foreground="#333D79", background="#FFFAFA")
style.configure("TEntry", foreground="#333D79", background="#333D79")

# les bouttons
bouton_info = ttk.Button(window, text="Info", style="TButton", command=infobutton)
bouton_start = ttk.Button(window, text="Start", style="TButton", command=btnstart)
bouton_exit = ttk.Button(window, text="Exit", style="TButton", command=window.destroy)
bouton_stop = ttk.Button(window, text="Stop", style="TButton", command=btnstop)
bouton_aide = ttk.Button(window, text="Besoin Aide?", style="TButton", command=btnaide)
bouton_tester = ttk.Button(window, text="Tester le nombre", style="TButton", command=btntester)
bouton_score = ttk.Button(window, text="Score", style="TButton", command=btnscore)

# champs text et labels
ttk.Label(window, text='Tester votre intelligence', style="TLabel").place(x=320, y=60)
chaine = ttk.Label(window, text=" Tapez votre Essai de 4 chiffres différents :", style="TLabel")
tchaine = ttk.Entry(window, style="TEntry")
textError = Label(window, fg='red', bg="#FFFAFA", font="Helvetica 10 bold")
tchaine.bind('<Return>', btntester)
chaine_sorti1 = ttk.Label(window, text="Votre Nombre se constitue de: ", style="TLabel")
chaine_sorti2 = ttk.Label(window, font='Helvetica 9 bold', style="TLabel")
chaine_sorti3 = ttk.Label(window, text="==> Le Nombre totale d'essai restant est: ", style="TLabel")
chaine_sorti4 = ttk.Label(window, font='Helvetica 9 bold', style="TLabel")
historique = Text(window, fg="#333D79")

# scroll bar
scbar = ttk.Scrollbar(window, orient="vertical", command=historique.yview)
historique.configure(yscrollcommand=scbar.set)

# places des boutons et labels dans le widget
bouton_info.place(x=170, y=10, width=70, height=25)
bouton_start.place(x=270, y=10, width=70, height=25)
bouton_stop.place(x=370, y=10, width=70, height=25)
bouton_exit.place(x=470, y=10, width=70, height=25)
chaine.place(x=50, y=100, width=320, height=25)
tchaine.place(x=300, y=100, width=320, height=25)
textError.place(x=320, y=130, width=320,height=25)
bouton_aide.place(x=180, y=170, width=150, height=25)
bouton_tester.place(x=380, y=170, width=150, height=25)
chaine_sorti1.place(x=220, y=220, width=190, height=25)
chaine_sorti2.place(x=400, y=220, width=100, height=25)
chaine_sorti3.place(x=185, y=260, width=230, height=25)
chaine_sorti4.place(x=420, y=260, width=50, height=25)
bouton_score.place(x=640, y=270, width=50, height=25)
historique.place(x=25, y=300, height=200)
scbar.place(x=672, y=300, width=20, height=200)

# intialisation (desactivation des boutons non utiliser au debut de jeux)
bouton_tester["state"] = DISABLED
bouton_stop["state"] = DISABLED
tchaine["state"] = DISABLED
bouton_aide["state"] = DISABLED
historique["state"] = DISABLED
#
window.mainloop()
