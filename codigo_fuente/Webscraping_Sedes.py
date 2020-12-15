#----------------Menu1314 - WebScraping - Sedes Disponibles---------

#----------Librerias------------
import ast
from bs4 import BeautifulSoup
from urllib.request import urlopen


#----------------------------------WebScraping - Diccionario de Sedes Por Ciudad---------
def ObtenerSedes():
    url_Sedes = 'https://www.elcorral.com/servicios-restaurantes'
    pagina = urlopen(url_Sedes)
    html = pagina.read().decode("utf-8")
    soup_sedes = BeautifulSoup(html,"html.parser")

    DicSedesCiudades = {}
    Tabla = soup_sedes.find_all('tr')
    for Sede_T in Tabla:
        #-----Extraccion de datos - -----
        Ciudad = Sede_T.find(attrs={"data-label": "Ciudad"})
        Ciudad = Ciudad.get_text()
        Sede = Sede_T.find(attrs={"data-label": "Restaurante"})
        Sede = Sede.get_text()
        Direccion = Sede_T.find(attrs={"data-label": "Dirección"})
        Direccion = Direccion.get_text()
        Horario = Sede_T.find(attrs={"data-label": "Horario restaurante"})
        Horario = Horario.get_text()
        #----Creacion - Actulizacion Diccionario----
        if Ciudad not in list(DicSedesCiudades.keys()):
            DicSedesCiudades[Ciudad] = {}
        if Sede not in list(DicSedesCiudades[Ciudad].keys()):
            DicSedesCiudades[Ciudad][Sede] = {}
        DicSedesCiudades[Ciudad][Sede]['Dirección'] = Direccion
        DicSedesCiudades[Ciudad][Sede]['Horario'] = Horario

    # ---Estructura: Dic = {Ciudad1 : {Sede1:{Direccion,Horario},Sede 2:{Direccion,Horario}....},Ciudad2:{...}...}
    #-----------→→→→DicSedesCiudades←←←--------------

    #--------Guardar Registro-------
    SobreEscribirSedes = open("Sedes.txt","w")
    SobreEscribirSedes.write(str(DicSedesCiudades))
    SobreEscribirSedes.close()

#------------------------Lista- Ciudad---------------------------------------------------------------
def ListaCiudades():
    CopiaCiudades = open("Sedes.txt","r")
    DicSedesCiudades = CopiaCiudades.read()#Consulta Diccionario en String
    DicSedesCiudades = ast.literal_eval(DicSedesCiudades)#Consulta Diccionario en Dict
    ListaCiudades = list(DicSedesCiudades.keys())
    CopiaCiudades.close()
    return ListaCiudades

#------------------------Consulta - Sedes ---------------------------------------------------------------
def ListaSedes(Ciudad):#------------------------Necesita Una CIUDAD - Opcion SELECCIONABLE-------------
    CopiaSedes = open("Sedes.txt","r")
    DicSedesCiudades = CopiaSedes.read()#Consulta Diccionario en String
    DicSedesCiudades = ast.literal_eval(DicSedesCiudades)#Consulta Diccionario en Dict
    ListaSedes = list(DicSedesCiudades[Ciudad].keys())
    CopiaSedes.close()
    return(ListaSedes)

#-----------------------Buscador------------------------------
def BuscarSedes(Ciudad): # ------------------------Necesita Una CIUDAD - OPCION MANUAL del USUARIO-------------
    CopiaSedes = open("Sedes.txt", "r")
    DicSedesCiudades = CopiaSedes.read()  # Consulta Diccionario en String
    DicSedesCiudades = ast.literal_eval(DicSedesCiudades)  # Consulta Diccionario en Dict
    BusquedaSedes = 'No Hay Sede Alli'
    try:
        BusquedaSedes = list(DicSedesCiudades[Ciudad])
        return (BusquedaSedes)
    except:
        return (BusquedaSedes)
    finally:
        CopiaSedes.close()


#-----------------------------------FUNCIONES------------------------------------------------------------------------
ObtenerSedes()#------------------------WebScraping - Diccionario de Sedes Por Ciudad---------

#Ciudad = input()

#ListaCiudades = ListaCiudades()#------------------------Consulta - Ciudad---------
#ListaSedes = ListaSedes(Ciudad)#------------------------Consulta - SEDES - OPCIONES VALIDAS---------
#BusquedaSedes = BuscarSedes(Ciudad)#--------------------Consulta- SEDES - Buscador Abierto--------
#print(ListaCiudades,ListaSedes,BusquedaSedes)
#print(ListaCiudades,BusquedaSedes)
#print(BusquedaSedes)