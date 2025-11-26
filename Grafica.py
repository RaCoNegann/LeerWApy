from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import os
import MensajeDebug as mensajeDebug

def guardar_dato(texto,numeroUsuario,aux):
    ruta_archivo = "mi_archivo"+numeroUsuario+".csv"
    archivo = "Grafica"
    if aux:
        if os.path.exists(ruta_archivo):
            mensajeDebug.mensajeConsola(archivo,f"El archivo '{ruta_archivo}' existe y se llenara con datos de prueba",1)
            datos_lista = [['10/10/25',100], ['18/11/25',213], ['18/11/25',400],['20/11/25',200], ['21/11/25',214], ['22/11/25',500]]
            df = pd.DataFrame(datos_lista, columns=['Fecha', 'Data'])
            mensajeDebug.mensajeConsola(archivo,df,2)#No se porque en local se ve dos veces
            df.to_csv('mi_archivo'+numeroUsuario+'.csv', mode='a', header=False, index=False)
            mensajeDebug.mensajeConsola(archivo,"Escribido",1)
        else:
            mensajeDebug.mensajeConsola(archivo,f"El archivo '{ruta_archivo}' NO existe y se llenara con datos de prueba",1)
            datos_lista = [['10/10/25',100], ['18/11/25',213], ['18/11/25',400],['20/11/25',200], ['21/11/25',214], ['22/11/25',500]]
            df = pd.DataFrame(datos_lista, columns=['Fecha', 'Data'])
            mensajeDebug.mensajeConsola(archivo,df,2)#No se porque en local se ve dos veces
            df.to_csv('mi_archivo'+numeroUsuario+'.csv', mode='a', header=True, index=False)
            mensajeDebug.mensajeConsola(archivo,"Escribido",1)
    else:
        today = date.today()
        formatted_date = today.strftime('%d/%m/%y')
        valor = texto.split()
        df_nuevo = pd.DataFrame({'Fecha': [formatted_date],'Data': [valor[1]]})
        if os.path.exists(ruta_archivo):
            mensajeDebug.mensajeConsola(archivo,"El archivo '{ruta_archivo}' existe y se llena con lo que llego al chat",1)
            df_nuevo.to_csv('mi_archivo'+numeroUsuario+'.csv', mode='a', header=False, index=False)
        else:
            mensajeDebug.mensajeConsola(archivo,f"El archivo '{ruta_archivo}' NO y se llena con lo que llego al chat",1)
            df_nuevo.to_csv('mi_archivo'+numeroUsuario+'.csv', mode='a', header=True, index=False)

def grafica(numeroUsuario):
    archivo = "Grafica"
    mensajeDebug.mensajeConsola(archivo,"Se debe mandar la grafica",1)
    df3 = pd.read_csv('mi_archivo'+numeroUsuario+'.csv')
    df3.plot(x='Fecha', y='Data', kind='bar')
    mensajeDebug.mensajeConsola(archivo,df3,2)
    #Personalizar las etiquetas y el título (opcional)
    plt.xlabel("Fecha")
    plt.ylabel("Valores")
    plt.title(f"Gastos xdd de '{numeroUsuario}'")
    plt.xticks(rotation=45)
    plt.savefig("i_grafico"+numeroUsuario+".png") 
    #plt.show()
