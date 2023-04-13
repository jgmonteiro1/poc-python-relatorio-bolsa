#Poc especificamente de objetivo educativo, não deve ser utilizada como parâmetro pra nada :D

# import panda as pd
import datetime

import yfinance as yf

from matplotlib import pyplot as plt
import mplcyberpunk
# import smtplib
# from email.message import EmailMessage


listaAtivos = ["MRFG3.SA", "JBSS3.SA", "TAEE11.SA"]

dataAtual = datetime.datetime.now()

anoAnterior = dataAtual - datetime.timedelta(days=365)

dadosMercado = yf.download(listaAtivos, anoAnterior, dataAtual)

dadosFechamento = dadosMercado['Adj Close']
dadosFechamento.columns = ['JBS', 'MAFRIG', 'TAESA']

dadosFechamento = dadosFechamento.dropna()

dadosFechamento.head(50)

dadosFechamentoMensal = dadosFechamento.resample("M").last()
dadosFechamentoAnual = dadosFechamento.resample("Y").last()

retornoAno = dadosFechamentoAnual.pct_change().dropna()
retornoDiario = dadosFechamento.pct_change().dropna()
retornoMensal = dadosFechamentoMensal.pct_change().dropna()

# print(dadosFechamento)
# print(dadosFechamentoMensal)
# print(dadosFechamentoAnual)
# print(retornoAno)
print(retornoDiario)
# print(retornoMensal)

# retornoDiarioJBS = retornoDiario.loc['2023-04-12', 'JBS']
#
# print(retornoDiarioJBS)

# retornoDiario.iloc[nomeDaLinha, nomeDaColuna]

print('----------------------------------------------')

retornoDiarioWithIloc = retornoDiario.iloc[0,0]
# print(retornoDiarioWithIloc)

# Pegando último dia no dataframe
retornoFechamentoDiarioJBS = retornoDiario.iloc[-1, 0]
retornoFechamentoDiarioMarfrig = retornoDiario.iloc[-1, 1]
retornoFechamentoDiarioTaesa = retornoDiario.iloc[-1, 2]

retornoFechamentoDiarioJBS = round(retornoFechamentoDiarioJBS * 100, 2)
retornoFechamentoDiarioMarfrig = round(retornoFechamentoDiarioMarfrig * 100, 2)
retornoFechamentoDiarioTaesa = round(retornoFechamentoDiarioTaesa * 100, 2)



print('-----------DADOS DO FECHAMENTO ABAIXO RENTABILIDADE % DO DIA ANTERIOR---------')

print('Último fechamento JBSS3: ' + str(retornoFechamentoDiarioJBS))
print('Último fechamento MRFG3: ' + str(retornoFechamentoDiarioMarfrig))
print('Último fechamento TAEE11: ' + str(retornoFechamentoDiarioTaesa))


plt.style.use("cyberpunk")

dadosFechamento.plot(y = 'JBS', use_index = True, legend = False)

plt.title("Grafico JBS fechamento")

plt.savefig('JBS.png', dpi = 300)

plt.show()


