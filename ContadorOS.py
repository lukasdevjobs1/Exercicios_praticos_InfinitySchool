import matplotlib.pyplot as plt

def plotar_distribuicao_servicos(df):
    contagem = df['tipo_servico'].value_counts()
    contagem.plot(kind='bar', title='Distribuição por Tipo de Serviço')
    plt.show()