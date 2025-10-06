'''Travail autour des sets'''

#### Imports et définition des variables globales ###

import csv

FILENAME = "corpus.txt"
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
VOYELLES = list("aeiouy")
CONSONNES = list("bcdfghjklmnpqrstvwxz")

#### Fonctions secondaires ###

def read_data(filename):
    '''Place tous les mots d'un fichier dans une liste'''

    with open(filename, 'r', encoding='utf-8') as f:
        r = csv.reader(f)
        l = [word.strip() for row in r for word in row]
    return l

def ensemble_mots(filename):
    '''Place les mots d'un fichier dans un set'''

    with open(filename, 'r', encoding='utf-8') as f:
        r = csv.reader(f)
        l = [word for row in r for word in row]

    mot = set(l)
    return mot

def mots_de_n_lettres(mots, n):
    '''Retourne dans un set les mots de n lettre(s)'''

    l = []
    for mot in mots :
        if len(mot) == n :
            l.append(mot)
        else :
            continue
    m = set(l)
    return m



def mots_avec(mots, s):
    '''Retourne dans un set les mots de contenat certaines lettres'''

    l = []
    for mot in mots :
        if s in mot :
            l.append(mot)
        else :
            continue
    ma = set(l)
    return ma

def cherche1(mots, start, stop, n):
    '''Retourne dans un set les mots répondant à certaines caractéristiques'''

    l = []
    l4 = []

    for mot in mots:
        if len(mot) < len(start) or len(mot) < len(stop):
            continue  # trop court pour matcher

        if mot.startswith(start) and mot.endswith(stop):
            l.append(mot)

    for mot in l:
        if len(mot) == n:
            l4.append(mot)

    return set(l4)


def cherche2(mots, lstart, lmid, lstop, nmin, nmax):
    '''Retourne dans un set les mots répondant à certaines caractéristiques'''

    resultats = set()

    for mot in mots:
        taille = len(mot)

        if taille < nmin:
            continue
        if taille > nmax:
            continue

        commence_bien = False
        for debut in lstart:
            if mot.startswith(debut):
                commence_bien = True
                break
        if not commence_bien:
            continue

        finit_bien = False
        for fin in lstop:
            if mot.endswith(fin):
                finit_bien = True
                break
        if not finit_bien:
            continue

        milieu_ok = False
        milieu_texte = mot[1:-1]
        for milieu in lmid:
            if milieu in milieu_texte:
                milieu_ok = True
                break
        if not milieu_ok:
            continue

        resultats.add(mot)

    return resultats


def main():
    '''Appel des fonctions secondaires'''

    # mots = read_data(FILENAME)
    # print( [ mots[i] for i in [24499, 28281, 57305, 118091, 199316, 223435, 336455] ])
    ens = ensemble_mots(FILENAME)
    print (ens)
    # m17 = mots_de_n_lettres(ens, 7)
    # print (m17)
    # print(len(m17))
    # print( random.sample(list(m17), 10) )
    # mk = mots_avec(ens, 'k')
    # print(len(mk))
    # print( random.sample(list(mk), 5) )
    # moo = mots_avec(ens, 'oo')
    # print(len(moo))
    # print( random.sample(list(moo), 5) )
    # mz14 = cherche1(ens, 'z', '', 14)
    # print(mz14)
    # m21z = cherche1(ens, '', 'z', 18)
    # print(m21z)
    # m_z = cherche1(ens, 'z', 'z', 7)
    # print(m_z)
    # mab17ez = mots_avec(cherche1(ens, 'sur', 'ons', 17), 'x')
    # print(mab17ez)
    # mab17ez = cherche2(ens, 'a', 'b', 'z', 16, 16)
    # print(mab17ez)



if __name__ == "__main__":
    main()
