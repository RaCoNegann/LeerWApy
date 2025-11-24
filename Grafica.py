from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger(__name__)
def guardar_dato(texto,numeroUsuario):
    today = date.today()
    formatted_date = today.strftime('%d/%m/%y')
    valor = texto.split()
    df_nuevo = pd.DataFrame({'Fecha': [formatted_date],'Data': [valor[1]]})
    df_nuevo.to_csv('mi_archivo'+numeroUsuario+'.csv', mode='a', header=True, index=False)

def mas_datos(numeroUsuario):
    datos_lista = [['10/10/25',100], ['18/11/25',213], ['18/11/25',400],['20/11/25',200], ['21/11/25',214], ['22/11/25',500]]
    df = pd.DataFrame(datos_lista, columns=['Fecha', 'Data'])
    logger.info(df)
    df.to_csv('mi_archivo'+numeroUsuario+'.csv', index=False)
    logger.info("Escribio")

def grafica(numeroUsuario):
    df3 = pd.read_csv('mi_archivo'+numeroUsuario+'.csv')
    df3.plot(x='Fecha', y='Data', kind='bar')
    logger.warning(df3)
    #Personalizar las etiquetas y el título (opcional)
    plt.xlabel("Fecha")
    plt.ylabel("Valores")
    plt.title("Gastos xdd")
    plt.xticks(rotation=45)
    plt.savefig("i_grafico"+numeroUsuario+".png") 
    #plt.show()
