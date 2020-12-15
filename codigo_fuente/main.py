import kivy
import sqlite3


import ast
from bs4 import BeautifulSoup
from urllib.request import urlopen


from kivy.config import Config
Config.set('graphics','width','425')
Config.set('graphics','height','800')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.modalview import ModalView
from kivy.uix.floatlayout import FloatLayout


class Principal(ScreenManager):
    def __init__(self,**kwarg):
        super(Principal,self).__init__()
        self.Login = Login(self)
        self.Registro = Registro(self)
        self.Comidas = Comidas(self)
        self.Hamburguesas_1 = Hamburguesas_1(self)
        self.Seleccion_ciudad = Seleccion_ciudad(self)

        wid = Screen(name='inicio')
        wid.add_widget(self.Login)
        self.add_widget(wid)

        wid = Screen(name='registro')
        wid.add_widget(self.Registro)
        self.add_widget(wid)

        wid = Screen(name='seleccion_ciudad')
        wid.add_widget(self.Seleccion_ciudad)
        self.add_widget(wid)

        wid = Screen(name='comidas')
        wid.add_widget(self.Comidas)
        self.add_widget(wid)

        wid = Screen(name='hamburguesas')
        wid.add_widget(self.Hamburguesas_1)
        self.add_widget(wid)

        self.goto_inicio()

    def goto_registro(self):
        self.current = 'registro'

    def goto_inicio(self):
        self.current = 'inicio'

    def goto_seleccion_ciudad(self):
        self.current = 'seleccion_ciudad'

    def goto_restaurantes(self):
        self.current = 'restaurantes'

    def goto_comidas(self):
        self.current = 'comidas'

    def goto_hamburguesas(self):
        self.current = 'hamburguesas'




class Login(BoxLayout):
    def __init__(self,Principal,**kwargs):
        super(Login,self).__init__()
        self.Principal = Principal

    def inicio_sesion(self):
        if self.ids.P1_input_usuario.text != '' and self.ids.P1_input_contra.text != '':
            conexion = sqlite3.connect('users.db')
            consulta = conexion.cursor()

            x = self.ids.P1_input_usuario.text
            y = self.ids.P1_input_contra.text

            try:
                consulta.execute("SELECT * FROM Usuarios WHERE Usuario =? AND Contraseña=?", (x, y,))

                z = consulta.fetchall()

                if len(z) != 0:
                    for g in z:

                        pedido.append(['Usuario', x])
                        self.Principal.goto_seleccion_ciudad()
                else:
                    print('Usuario y/o contraseña incorrecto')

                conexion.close()

            except Exception as e:
                print(e)


class Registro(BoxLayout):
    def __init__(self,Principal,**kwargs):
        super(Registro,self).__init__()
        self.Principal = Principal

    def registro_nuevo_usuario(self):
        if self.ids.P3_input_usuario.text != '' and self.ids.P3_input_contra.text != '':
            conexion = sqlite3.connect('users.db')
            consulta = conexion.cursor()

            a = self.ids.P3_input_usuario.text
            b = self.ids.P3_input_contra.text

            sql = "INSERT INTO Usuarios(Usuario,contraseña)VALUES(?,?)"
            datos = (a, b)


            try:
                consulta.execute(sql, datos)
                consulta.close()
                conexion.commit()
                conexion.close()
                self.Principal.goto_inicio()
            except Exception as e:
                print(e)
        else:
            print('vacio')

class Seleccion_ciudad(BoxLayout):

    def __init__(self, Principal, **kwargs):
        super(Seleccion_ciudad, self).__init__()
        self.Principal = Principal

    """def ObtenerSedes():
        url_Sedes = 'https://www.elcorral.com/servicios-restaurantes'
        pagina = urlopen(url_Sedes)
        html = pagina.read().decode("utf-8")
        soup_sedes = BeautifulSoup(html, "html.parser")

        DicSedesCiudades = {}
        Tabla = soup_sedes.find_all('tr')
        for Sede_T in Tabla:
            # -----Extraccion de datos - -----
            Ciudad = Sede_T.find(attrs={"data-label": "Ciudad"})
            Ciudad = Ciudad.get_text()
            Sede = Sede_T.find(attrs={"data-label": "Restaurante"})
            Sede = Sede.get_text()
            Direccion = Sede_T.find(attrs={"data-label": "Dirección"})
            Direccion = Direccion.get_text()
            Horario = Sede_T.find(attrs={"data-label": "Horario restaurante"})
            Horario = Horario.get_text()
            # ----Creacion - Actulizacion Diccionario----
            if Ciudad not in list(DicSedesCiudades.keys()):
                DicSedesCiudades[Ciudad] = {}
            if Sede not in list(DicSedesCiudades[Ciudad].keys()):
                DicSedesCiudades[Ciudad][Sede] = {}
            DicSedesCiudades[Ciudad][Sede]['Dirección'] = Direccion
            DicSedesCiudades[Ciudad][Sede]['Horario'] = Horario

        # ---Estructura: Dic = {Ciudad1 : {Sede1:{Direccion,Horario},Sede 2:{Direccion,Horario}....},Ciudad2:{...}...}
        # -----------→→→→DicSedesCiudades←←←--------------

        # --------Guardar Registro-------
        SobreEscribirSedes = open("Sedes.txt", "w")
        SobreEscribirSedes.write(str(DicSedesCiudades))
        SobreEscribirSedes.close()

    ObtenerSedes()"""



    def Sedes(self,ciudad):  # ------------------------Necesita Una CIUDAD - Opcion SELECCIONABLE-------------

        CopiaSedes = open("Sedes.txt", "r")
        DicSedesCiudades = CopiaSedes.read()  # Consulta Diccionario en String
        DicSedesCiudades = ast.literal_eval(DicSedesCiudades)  # Consulta Diccionario en Dict
        ListaSedes = list(DicSedesCiudades[ciudad].keys())
        CopiaSedes.close()
        """xu = ListaSedes
        print(xu)"""
        self.ids['spinner_inicio'].values=ListaSedes


    def cidad_elegida(self,sede,ciudad):
        CopiaSedes = open("Sedes.txt", "r")
        DicSedesCiudades = CopiaSedes.read()  # Consulta Diccionario en String
        DicSedesCiudades = ast.literal_eval(DicSedesCiudades)  # Consulta Diccionario en Dict
        for ubicacion in list(DicSedesCiudades.keys()):
            if ciudad == (list(DicSedesCiudades[ubicacion].keys())):

                pedido.append([ubicacion,sede])
        CopiaSedes.close()



    def ciudadbar(self):
        ciudad = self.ids.barranquilla.text
        self.Sedes(ciudad)



    def ciudadbog(self):
        ciudad = self.ids.bogota.text
        if ciudad == 'Bogota':
            ciudad = 'Bogotá'
        self.Sedes(ciudad)

    def ciudadcar(self):
        ciudad = self.ids.cartagena.text
        self.Sedes(ciudad)

    def ciudadmed(self):
        ciudad = self.ids.medellin.text
        self.Sedes(ciudad)


class Comidas(BoxLayout):
    def __init__(self,Principal,**kwargs):
        super(Comidas,self).__init__()
        self.Principal = Principal

class Hamburguesas_1(BoxLayout):
    def __init__(self,Principal,**kwargs):
        super(Hamburguesas_1,self).__init__()
        self.Principal = Principal

    global pedido
    pedido = []

    def pan(self,pano,porcion):
        pedido.append('-------Pedido-------')
        pedido.append([pano,porcion])


    def queso(self,quezo,porcion):

        pedido.append([quezo, porcion])


    def carne (self,carnu,porcion):

        pedido.append([carnu, porcion])


    def topping (self,topp,porcion):

        pedido.append([topp, porcion])


    def vegetales (self,vege,porcion):

        pedido.append([vege, porcion])


    def salsa (self,sal,porcion):

        pedido.append([sal, porcion])


    def bebida (self,bebi,porcion):

        pedido.append([bebi, porcion])


    def adiciones (self,adi,porcion):

        pedido.append([adi, porcion])


    def finalizar(self):
        cadena = ''
        for sublista in pedido:
            sublista = ' : '.join(sublista)
            cadena = cadena+str(sublista)+'\n'

        self.ids['label_fin'].text=str(cadena+'\n'+'Tu pedido se está preparado'+'\n'+'Gracias por elegirnos')






class MainApp(App):
    title = 'Menu 1314 v2.0'
    def build(self):
        return Principal()

if __name__ == '__main__':
    MainApp().run()
