### IMPORTAR BIBLIOTECAS
import pandas as pd
import xlrd
import time
import os


### CAMINHO DO ARQUIVO A SER IMPORTADO
caminho_arquivo="Microdados RS\RS\Amostra_Pessoas_43_SAMPLE.txt"

### GRAVAR HORA INICIO
start = time.time()


### DEFINIR DATA FRAME (DF) 
df = pd.read_fwf(caminho_arquivo, widths=[2,5,186,1,1,4,3,10,6], usecols=[0,1,3,4,6,8], header=None, names=['idUF', 'Mun', 'Est', 'Trab', 'Atv','Rend'], converters={'idUF': str, 'Mun': str, 'Est': str, 'Trab': str, 'Atv': str})

### IMPRIMIR PRIMEIRAS LINHAS PARA VER COMO FICOU O DATA FRAME (DF)
print(df.head())

### IMPRIMIR SUMÁRIO DAS ESTATÍSTICAS SOBRE O CAMPO RENDA (Rend)
print (df['Rend'].describe())


### DEFINIR DF CONTENDO DESCRICAO DOS CODIGOS E NOMES DOS ESTADOS
UFInform = [
    [11, 'Rondônia'],
    [12, 'Acre'],
    [13, 'Amazonas'],
    [14, 'Roraima'],
    [15, 'Pará'],
    [16, 'Amapá'],
    [17, 'Tocantins'],
    [21, 'Maranhão'],             
    [22, 'Piauí'],
    [23, 'Ceará'],
    [24, 'Rio Grande do Norte'],
    [25, 'Paraíba'],
    [26, 'Pernambuco'],
    [27, 'Alagoas'],
    [28, 'Sergipe'],
    [29, 'Tocantins'],
    [31, 'Minas Gerais'],             
    [32, 'Espírito Santo'],
    [33, 'Rio de Janeiro'],
    [35, 'São Paulo'],
    [41, 'Paraná'],
    [42, 'Santa Catarina'],             
    [43, 'Rio Grande do Sul'],
    [50, 'Mato Grosso do Sul'],
    [51, 'Mato Grosso'],
    [52, 'Goiás'],
    [53, 'Distrito Federal'],
]
Colunas = ['idUFNum', 'Estado']
UFs = pd.DataFrame(UFInform, columns=Colunas)

### DEFINIR CAMPO idUF COMO STRING
UFs["idUF"] = UFs["idUFNum"].astype(str)

### COMBINAR OS CAMPOS DO DATAFRAME UFs[] ao DATAFRAME df[] 
df = pd.merge(df, UFs, on='idUF')

### EXPORTAR DATAFRAME df[] PARA UM ARQUIVO CSV
df.to_csv('Output.csv')

### IMPORTAR EXCEL COM DESCRICAO DOS MUNICIPIOS
xls_file = pd.ExcelFile('Documentacao\Municipios.xls')
Municipios = xls_file.parse('Município')
#print(Municipios.head())

### CRIAR UM NOVO DATAFRAME MunicipiosRS[] CONTENDO SOMENTE OS MUNICIPIOS DO RS
#MunicipiosRS = Municipios.loc[Municipios['UF'] == 43]
#MunicipiosRS = MunicipiosRS[['Município','Nome_Munic']]
#print(MunicipiosRS.head())


### AGREGAR INFORMACOES DE NOME DO MUNICIPIO NO DATAFRAME df[]
df["Município"] = df["idUF"] + df["Mun"]
df["Município"] = df["Município"].astype(str)
Municipios["Município"] = Municipios["Município"].astype(str)
df = pd.merge(df, Municipios, on='Município')
print(df.head())
### IMPRIMIR TEMPO DECORRIDO
#end = time.time()
#str_c = "Tempo decorrido: " + str(round(end-start,0))
 
#print(str_c)