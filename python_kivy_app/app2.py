#qpy:kivy

from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from kivy.utils import get_color_from_hex


class AutomacaoApp(App):

    LabelBase.register(name='Roboto',
                       fn_regular='font/Roboto-Thin.ttf',
                       fn_bold ='font/Roboto-Medium.ttf')

    LabelBase.register(name='Metro',
                       fn_regular='font/Flaticon.ttf')

    def callback(self,instance):
        if instance.state == "down":
            instance.text=u'[b]L[/b]ampada\n[font=Metro]\uf106[/font]\nON'
        else:
            instance.text=u'[b]L[/b]ampada\n[font=Metro]\uf106[/font]\nOFF'

    def build(self):
        princ = BoxLayout(orientation='vertical')


        titulo = BoxLayout(orientation= 'horizontal',
                           size_hint_y= None,
                           height='70dp');

        titulo.add_widget(Label(text="[b]Tiwhu[/b] Domotica",
                                font_size=40,
                                markup=True))

        princ.add_widget(titulo)

        layout = GridLayout()

        btn1=ToggleButton(
            background_color=get_color_from_hex('#3498db'),
            text=u'[b]L[/b]ampada\n[font=Metro]\uf106[/font]\nON',
            disabled=False)

        btn1.bind(on_press=self.callback)


        btn2=Button(background_color=get_color_from_hex('#e74c3c'),
                    text=u'[font=Metro]\uf101[/font]\n25 C')

        btn3=Button(background_color=get_color_from_hex('#1abc9c'),
                    text=u'[b]P[/b]resenca [font=Metro]\uf104[/font]\n[size=50]+[/size]')

        btn4=Button(background_color=get_color_from_hex('#f1c40f'),
                    text=u'[b]P[/b]orta [font=Metro]\uf103[/font]\nAberta')

        btn5=Button(background_color=get_color_from_hex('#9b59b6'),
                    text=u'[b]L[/b]umin. [font=Metro]\uf105[/font]\n85%')

        btn6=Button(background_color=get_color_from_hex('#2d89ef'),
                    text=u'[b]D[/b]istancia [font=Metro]\uf108[/font]\n 2 M')

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)
        layout.add_widget(btn6)

        dimer = BoxLayout(orientation= 'horizontal',
                           size_hint_y= None,
                           height='70dp');

        dimer.add_widget(Label(text="[b]D[/b]imer",
                                font_size=30,
                                markup=True))

        dimer.add_widget(Slider(size_hint_y= None))


        princ.add_widget(layout)
        # princ.add_widget(dimer)

        return princ

if __name__ == "__main__":
    AutomacaoApp().run()
