import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Entrées
error = ctrl.Antecedent(np.arange(-4, 4, 1), 'error')
error_names = ['too_hot', 'just_right', 'too_cold']
error_dot = ctrl.Antecedent(np.arange(-10, 10, 1), 'error_dot')
error_dot_names = ['getting_hotter', 'no_change', 'getting_colder']

# Sorties
percent_output = ctrl.Consequent(np.arange(-100, 100, 1), 'percent_output')

# Automf
error.automf(names=error_names)
error_dot.automf(names=error_dot_names)

# Configuration des sorties
percent_output['cool'] = fuzz.trapmf(percent_output.universe, [-100, -100, -50, 0])
percent_output['do_nothing'] = fuzz.trimf(percent_output.universe, [-50, 0, 50])
percent_output['heat'] = fuzz.trapmf(percent_output.universe, [0, 50, 100, 100])

# Définitions des règles
rule1 = ctrl.Rule(error['too_cold'] | error_dot['getting_colder'], percent_output['heat'])
rule2 = ctrl.Rule(error['too_cold'] | error_dot['no_change'], percent_output['heat'])
rule3 = ctrl.Rule(error['too_cold'] | error_dot['getting_hotter'], percent_output['heat'])
rule4 = ctrl.Rule(error['just_right'] | error_dot['getting_colder'], percent_output['heat'])
rule5 = ctrl.Rule(error['just_right'] | error_dot['no_change'], percent_output['do_nothing'])
rule6 = ctrl.Rule(error['too_hot'] | error_dot['getting_colder'], percent_output['cool'])
rule7 = ctrl.Rule(error['too_hot'] | error_dot['no_change'], percent_output['cool'])
rule8 = ctrl.Rule(error['too_hot'] | error_dot['getting_hotter'], percent_output['cool'])
rule9 = ctrl.Rule(error['just_right'] | error_dot['getting_hotter'], percent_output['cool'])

percent_output_ctrl = ctrl.ControlSystem([rule1,
                                        rule2,
                                        rule3,
                                        rule4,
                                        rule5,
                                        rule6,
                                        rule7,
                                        rule8,
                                        rule9])

percent_output_calcul = ctrl.ControlSystemSimulation(percent_output_ctrl)

percent_output_calcul.input['error'] = float(input("Saisir degree : "))
percent_output_calcul.input['error_dot'] = float(input("Saisir type : "))

percent_output_calcul.compute()

print(percent_output_calcul.output['percent_output'])
percent_output.view(sim=percent_output_calcul)

