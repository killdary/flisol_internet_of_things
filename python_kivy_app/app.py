#qpy:kivy
from random import randint
from time import sleep

import conex
from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex


class AutomacaoApp(App):

    # conn = conex.Conexao("192.168.0.107",5000)

    LabelBase.register(name='Roboto',
                       fn_regular='font/Roboto-Thin.ttf',
                       fn_bold ='font/Roboto-Medium.ttf')

    LabelBase.register(name='Metro',
                       fn_regular='font/Flaticon.ttf')

    def callback(self,instance):
        if instance.state == "down":
            # self.conn.enviar("acender")
            # dadosRecebidos = self.conn.receber()
            #
            # while(dadosRecebidos == "1"):
            #     self.conn.enviar("acender")
            #     dadosRecebidos = self.conn.receber()
            #     sleep(randint(0,9))

            instance.text=u'[b]L[/b]ampada\n[font=Metro]\uf106[/font]\nON'
        else:
            # self.conn.enviar("apagar")
            # dadosRecebidos = self.conn.receber()
            #
            # while(dadosRecebidos == "0"):
            #     self.conn.enviar("apagar")
            #     dadosRecebidos = self.conn.receber()
            #     sleep(randint(0,9))

            instance.text=u'[b]L[/b]ampada\n[font=Metro]\uf106[/font]\nOFF'
    #
    # def update(self,nap):
    #     self.conn.enviar("ler")
    #     dadosRecebidos = self.conn.receber()
    #     dados = dadosRecebidos.split("|")
    #     self.root.ids.termometro.text=u'[font=Metro]\uf101[/font]\n'+dados[0]+u' C'
    #     self.root.ids.luminosidade.text=u'[b]L[/b]umin. [font=Metro]\uf105[/font]\n'+dados[3]+'%'
    #     self.root.ids.distancia.text=u'[b]D[/b]istancia [font=Metro]\uf108[/font]\n '+dados[4]+' M'
    #     if dados[2] == "1":
    #         u'[b]P[/b]orta [font=Metro]\uf103[/font]\nFechada'
    #     else:
    #         u'[b]P[/b]orta [font=Metro]\uf103[/font]\nAberta'
    #
    #     if dados[1] == "1":
    #         self.root.ids.presenca.text=u'[b]P[/b]resenca [font=Metro]\uf104[/font]\n[size=50]+[/size]'
    #     else:
    #         self.root.ids.presenca.text=u'[b]P[/b]resenca [font=Metro]\uf104[/font]\n[size=50]+[/size]'

    # def on_start(self):
    #     Clock.schedule_interval(self.update,5)

    def build(self):
        self.root.ids.lampada.bind(on_press=self.callback)
        pass

if __name__ == "__main__":
    # Window.clearcolor = get_color_from_hex('#ffffff')
    # Window.maximize = True
    # Window.size = (300, 100)
    AutomacaoApp().run()

#
#
# #qpy:kivy
# from random import randint
# from time import sleep
#
# import conex
# from kivy.app import App
# from kivy.clock import Clock
# from kivy.core.text import LabelBase
# from kivy.core.window import Window
# from kivy.utils import get_color_from_hex
#
#
# class AutomacaoApp(App):
#
#     conn = conex.Conexao("192.168.0.107",5000)
#
#     LabelBase.register(name='Roboto',
#                        fn_regular='font/Roboto-Thin.ttf',
#                        fn_bold ='font/Roboto-Medium.ttf')
#
#     LabelBase.register(name='Metro',
#                        fn_regular='font/Flaticon.ttf')
#
#     def callback(self,instance):
#         if instance.state == "down":
#             self.conn.enviar("acender")
#             dadosRecebidos = self.conn.receber()
#
#             while(dadosRecebidos == "1"):
#                 self.conn.enviar("acender")
#                 dadosRecebidos = self.conn.receber()
#                 sleep(randint(0,9))
#
#             instance.text=u'[b]L[/b]ampada\n[font=Metro]\uf106[/font]\nON'
#         else:
#             self.conn.enviar("apagar")
#             dadosRecebidos = self.conn.receber()
#
#             while(dadosRecebidos == "0"):
#                 self.conn.enviar("apagar")
#                 dadosRecebidos = self.conn.receber()
#                 sleep(randint(0,9))
#
#             dadosRecebidos = self.conn.receber()
#             instance.text=u'[b]L[/b]ampada\n[font=Metro]\uf106[/font]\nOFF'
#
#     def update(self,nap):
#         self.conn.enviar("ler")
#         dadosRecebidos = self.conn.receber()
#         dados = dadosRecebidos.split("|")
#         self.root.ids.termometro.text=u'[font=Metro]\uf101[/font]\n'+dados[0]+u' C'
#         self.root.ids.luminosidade.text=u'[b]L[/b]umin. [font=Metro]\uf105[/font]\n'+dados[3]+'%'
#         self.root.ids.distancia.text=u'[b]D[/b]istancia [font=Metro]\uf108[/font]\n '+dados[4]+' M'
#         if dados[2] == "1":
#             u'[b]P[/b]orta [font=Metro]\uf103[/font]\nFechada'
#         else:
#             u'[b]P[/b]orta [font=Metro]\uf103[/font]\nAberta'
#
#         if dados[1] == "1":
#             self.root.ids.presenca.text=u'[b]P[/b]resenca [font=Metro]\uf104[/font]\n[size=50]+[/size]'
#         else:
#             self.root.ids.presenca.text=u'[b]P[/b]resenca [font=Metro]\uf104[/font]\n[size=50]+[/size]'
#
#     def on_start(self):
#         Clock.schedule_interval(self.update,5)
#
#     def build(self):
#         self.root.ids.lampada.bind(on_press=self.callback)
#         pass
#
# if __name__ == "__main__":
#     # Window.clearcolor = get_color_from_hex('#ffffff')
#     AutomacaoApp().run()

