import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# ----------------- Antecedentes -----------------
peso = ctrl.Antecedent(np.arange(0, 16+0.5, 0.5), 'peso')
peso['muitoLeve'] = fuzz.trimf(peso.universe, [0, 0, 3])
peso['leve'] = fuzz.trimf(peso.universe, [2, 3.5, 5])
peso['medio'] = fuzz.trimf(peso.universe, [4, 6, 10.5])
peso['pesado'] = fuzz.trimf(peso.universe, [8, 11, 14])
peso['muitoPesado'] = fuzz.trimf(peso.universe, [13, 16, 16])
# peso.view()

sujeira = ctrl.Antecedent(np.arange(0, 10+0.5, 0.5), 'sujeira')
sujeira['quaseLimpa'] = fuzz.trimf(sujeira.universe, [0, 0, 2])
sujeira['pouca'] = fuzz.trimf(sujeira.universe, [1, 2.5, 4])
sujeira['media'] = fuzz.trimf(sujeira.universe, [2, 5, 8])
sujeira['muita'] = fuzz.trimf(sujeira.universe, [6, 10, 10])
# sujeira.view()

delicadeza = ctrl.Antecedent(np.arange(0, 10+0.5, 0.5), 'delicadeza')
delicadeza['muitoFina'] = fuzz.trimf(delicadeza.universe, [0, 0, 2])
delicadeza['fina'] = fuzz.trimf(delicadeza.universe, [1, 2.5, 4])
delicadeza['normal'] = fuzz.trimf(delicadeza.universe, [3, 5, 7])
delicadeza['grossa'] = fuzz.trimf(delicadeza.universe, [6, 7.5, 9])
delicadeza['muitoGrossa'] = fuzz.trimf(delicadeza.universe, [8, 10, 10])
# delicadeza.view()


# ----------------- Consequentes -----------------
detergente = ctrl.Consequent(np.arange(0, 250+1, 1), 'detergente')
detergente['muitoBaixo'] = fuzz.trimf(detergente.universe, [0, 0, 40])
detergente['baixo'] = fuzz.trimf(detergente.universe, [30, 60, 80])
detergente['medio'] = fuzz.trimf(detergente.universe, [70, 100, 120])
detergente['alto'] = fuzz.trimf(detergente.universe, [100, 125, 150])
detergente['exagerado'] = fuzz.trimf(detergente.universe, [140, 170, 230])
detergente['maximo'] = fuzz.trimf(detergente.universe, [220, 250, 250])
# detergente.view()

temperatura = ctrl.Consequent(np.arange(0, 90+1, 1), 'temperatura')
temperatura['ambiente'] = fuzz.trimf(temperatura.universe, [0, 0, 30])
temperatura['baixa'] = fuzz.trimf(temperatura.universe, [25, 35, 45])
temperatura['media'] = fuzz.trimf(temperatura.universe, [40, 55, 75])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [60, 90, 90])
# aquecimento.view()


centrifugacao = ctrl.Consequent(
    np.arange(400, 1600+1, 25), 'centrifugacao')
centrifugacao['mínima'] = fuzz.trimf(centrifugacao.universe, [400, 400, 700])
centrifugacao['leve'] = fuzz.trimf(centrifugacao.universe, [600, 725, 850])
centrifugacao['normal'] = fuzz.trimf(centrifugacao.universe, [800, 950, 1100])
centrifugacao['rápida'] = fuzz.trimf(
    centrifugacao.universe, [1000, 1200, 1400])
centrifugacao['extrema'] = fuzz.trimf(
    centrifugacao.universe, [1250, 1600, 1600])
# centrifugacao.view()


# ----------------- Regras -----------------
rule1 = ctrl.Rule(peso['leve'] & sujeira['quaseLimpa'],
                  detergente['muitoBaixo'])
rule2 = ctrl.Rule(peso['muitoLeve'] & sujeira['muita'], detergente['baixo'])
rule3 = ctrl.Rule(peso['leve'] & sujeira['quaseLimpa'], detergente['baixo'])
rule4 = ctrl.Rule(peso['pesado'] & (delicadeza['muitoGrossa'] |
                  delicadeza['grossa']) & sujeira['muita'], centrifugacao['extrema'])
rule5 = ctrl.Rule((delicadeza['muitoGrossa'] | delicadeza['grossa']) & (
    sujeira['media'] | peso['muitoPesado']), centrifugacao['rápida'])
rule6 = ctrl.Rule(
    (delicadeza['muitoFina'] | delicadeza['fina']), centrifugacao['leve'])
rule7 = ctrl.Rule((delicadeza['muitoFina'] | delicadeza['fina']) & (
    sujeira['pouca'] | peso['leve']), centrifugacao['mínima'])
rule8 = ctrl.Rule(delicadeza['muitoFina'], temperatura['ambiente'])
rule9 = ctrl.Rule(delicadeza['normal'] &
                  sujeira['muita'], temperatura['media'])
rule10 = ctrl.Rule(delicadeza['grossa'] &
                   sujeira['muita'], temperatura['alta'])
rule11 = ctrl.Rule(peso['muitoPesado'] &
                   sujeira['media'], temperatura['media'])
rule12 = ctrl.Rule(sujeira['pouca'], temperatura['ambiente'])
rule13 = ctrl.Rule(sujeira['media'] &
                   delicadeza['normal'], temperatura['baixa'])
rule14 = ctrl.Rule(sujeira['muita'] &
                   peso['muitoPesado'], detergente['maximo'])
rule15 = ctrl.Rule(sujeira['muita'] &
                   peso['pesado'], detergente['exagerado'])
rule16 = ctrl.Rule(sujeira['media'] & peso['medio'], detergente['medio'])


regrasDetergente = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule14, rule15, rule16])
simulacaoDetergente = ctrl.ControlSystemSimulation(regrasDetergente)
simulacaoDetergente.input['peso'] = 9
simulacaoDetergente.input['sujeira'] = 6.8

simulacaoDetergente.compute()
print(f'resultado (detergente): {simulacaoDetergente.output["detergente"]}')
detergente.view(sim=simulacaoDetergente)


regrasCentrifugacao = ctrl.ControlSystem(
    [rule4, rule5, rule6, rule7])
simulacaoCentrifugacao = ctrl.ControlSystemSimulation(regrasCentrifugacao)
simulacaoCentrifugacao.input['peso'] = 9
simulacaoCentrifugacao.input['sujeira'] = 6.8
simulacaoCentrifugacao.input['delicadeza'] = 7

simulacaoCentrifugacao.compute()
print(
    f'resultado (centrifugação): {simulacaoCentrifugacao.output["centrifugacao"]}')
centrifugacao.view(sim=simulacaoCentrifugacao)


regrasTemperatura = ctrl.ControlSystem(
    [rule8, rule9, rule10, rule11, rule12, rule13])
simulacaoTemperatura = ctrl.ControlSystemSimulation(regrasTemperatura)
simulacaoTemperatura.input['peso'] = 7
simulacaoTemperatura.input['sujeira'] = 6
simulacaoTemperatura.input['delicadeza'] = 6

simulacaoTemperatura.compute()
print(
    f'resultado (temperatura): {simulacaoTemperatura.output["temperatura"]}')
temperatura.view(sim=simulacaoTemperatura)

plt.show()
