from ag import AlgoritmoGenetico

dados = [
{'item': 'valvula1', 'pressao': 12.53}, {'item': 'valvula2', 'pressao': -33.12},
{'item': 'valvula3', 'pressao': 50.78}, {'item': 'valvula4', 'pressao': -78.99},
{'item': 'valvula5', 'pressao': 25.48}, {'item': 'valvula6', 'pressao': -60.83},
{'item': 'valvula7', 'pressao': 81.81}, {'item': 'valvula8', 'pressao': -20.55},
{'item': 'valvula9', 'pressao': 35.63}, {'item': 'valvula10', 'pressao': -40.51}
]

def funFitness(genes, dados):
    pressaoTotal  = 0
    for i in range(len(genes)):
        if genes[i] == 1:
            pressaoTotal += dados[i]['pressao']
    if 45.28 <= pressaoTotal <= 48.33:
        return 1000
    else:
        return -(pressaoTotal)
   
ag = AlgoritmoGenetico(dados,100,1000,funcaoFitness=funFitness,maiorFitness=True)
ag.executa()

melhorResutado = ag.melhorResultado()

print("Válvulas escolhidas:", melhorResutado['genes'])

pressaoFinal = 0

for i in range(len(melhorResutado['genes'])):
    if melhorResutado['genes'][i] == 1:
        pressaoFinal+= dados[i]['pressao']

print(f"Pressão final: {pressaoFinal:.2f}")
