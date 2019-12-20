from pyDatalog import pyDatalog
from easygui import *

pyDatalog.clear()

pyDatalog.create_terms('plus_urgent, moins_urgent, physique, electrique, chaleur, asphyxie, saigne, etouffement, malaise, brulure,  X')

plus_urgent(X) <= physique(X)
plus_urgent(X) <= electrique(X)
plus_urgent(X) <= chaleur(X)
plusUrgent(X) <= asphyxie(X)

moins_urgent(X) <= saigne(X)
moins_urgent(X) <= etouffement(X)
moins_urgent(X) <= brulure(X)
moins_urgent(X) <= malaise(X)

+etouffement('main_a_la_gorge')


message = "Quelle est la raison de votre appel ?"
title = "IHM"

