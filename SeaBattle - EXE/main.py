from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
#from kivy.properties import StringProperty
#from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
import random
import time

import TABLE as tb

Builder.load_file('my.kv')
Config.set('graphics','resizable', '0')
Config.set('graphics', 'width', '1000')
Config.set('graphics','height', '600')
       

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        
    def run(self, appKek):
        self.appKek = appKek
        
    def start_game(self):
        self.appKek['GameScreen'].reboot_game()
        #self.appKek['GameScreen'].set_ship()
        self.manager.current = 'game_screen'
        
    def exitt(self):
        App.get_running_app().stop()


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.btn_player = [[],[],[],[],[],[],[],[],[],[],[]]
        self.btn_cpu = [[],[],[],[],[],[],[],[],[],[],[]]
        self.mass_ships = []
    
    def destroy_ship(self, search_index):
        for y in range(len(self.appKek['cpu_mass'])):
            if search_index in self.appKek['cpu_mass'][y]:
                return False
        return True
    
    def destroy_ship_CPU(self, search_index):
        for y in range(len(self.appKek['player_mass'])):
            if search_index in self.appKek['player_mass'][y]:
                return False
        return True
                
    
    def run(self, appKek):
        self.appKek = appKek
        
    def kkk(self, kolabs = False, search_index = None):
        if kolabs == True:
            for y in range(len(self.appKek['player_mass'])):
                for x in range(len(self.appKek['player_mass'][y])):
                    if search_index == self.appKek['player_mass'][y][x]:
                        self.CPU_click(self.btn_player[y][x])
        else:
            y = random.randint(1, 10)
            x = random.randint(1, 10)
            self.CPU_click(self.btn_player[y][x])
    
    
    def chek_pobeda(self, mass):
        a = ['41','32','33','21','22','23','11','12','13','14']
        for y in range(11):
            for x in range(11):
                for elem in a:
                    if elem == mass[y][x]:
                        return True
        return False
    
    
    def CPU_click(self, instance):
        
        if self.chek_pobeda(self.appKek['cpu_mass']) == True:
            pass
        else:
            self.manager.current = 'game_screen_win'
        for i in range(len(self.btn_player)):
            if instance in self.btn_player[i]:
                y = self.btn_player.index(self.btn_player[i])
                x = self.btn_player[i].index(instance)
                mAss = self.appKek['player_mass'][y][x]
                if mAss != '--' and mAss != '00' and instance.text != '*' and instance.text != '+':
                    instance.text = '+'
                    instance.background_color = [1,0,0,1]
                    self.appKek['player_mass'][y][x] = 'xx'
                    if self.destroy_ship_CPU(mAss) == False:
                        #self.ids['info_ship_status_CPU'].text = 'Компьютер - Попал !'
                        self.kkk(True, mAss)
                        #self.appKek[GameScreen].ids.info_ship_status(text = 'Попал !!!')
                    else:
                        #self.ids['info_ship_status_CPU'].text = 'Компьютер - Убил !!!'
                        self.kkk(False)
                        #self.appKek[GameScreen].ids.info_ship_status(text = 'Убил !!!')
                    #print('CPU - ',y,x)
                    
                if instance.text == '*':
                    self.kkk(False)
                elif self.appKek['player_mass'][y][x] == '--' or self.appKek['player_mass'][y][x] == '00':
                    #self.ids['info_ship_status_CPU'].text = 'Компьютер - Промахнулся'
                    instance.text = '*'
                    #print('CPU - ',y,x)
                else:
                    pass
        

                
    
    def click(self, instance):
        
        if self.chek_pobeda(self.appKek['cpu_mass']) == True:
            pass
        else:
            self.manager.current = 'game_screen_win'
        for i in range(len(self.btn_cpu)):
            if instance in self.btn_cpu[i]:
                y = self.btn_cpu.index(self.btn_cpu[i])
                x = self.btn_cpu[i].index(instance)
                mAss = self.appKek['cpu_mass'][y][x]
                if mAss != '--' and mAss != '00' and instance.text != '*' and instance.text != '+':
                    instance.text = '+'
                    instance.background_color = [2,4,2,1]
                    self.appKek['cpu_mass'][y][x] = 'xx'
                    if self.destroy_ship(mAss) == False:
                        self.ids['info_ship_status'].text = 'Попал !!!'
                        #self.appKek[GameScreen].ids.info_ship_status(text = 'Попал !!!')
                    else:
                        self.ids['info_ship_status'].text = 'Убил !!!'
                        #self.appKek[GameScreen].ids.info_ship_status(text = 'Убил !!!')
                    #print('Player - ',y,x)
                    
                if instance.text == '*':
                    pass
                elif self.appKek['cpu_mass'][y][x] == '--' or self.appKek['cpu_mass'][y][x] == '00':
                    self.ids['info_ship_status'].text = 'Промах'
                    instance.text = '*'
                    self.kkk(False)
                    #print('Player - ',y,x)
                else:
                    pass
                
        if self.chek_pobeda(self.appKek['player_mass']) == True:
            pass
        else:
            self.manager.current = 'game_screen_defeat'
                

#???????????????????????????????????????????????????????
    def set_ship(self,appKek ,i ,n):
        if appKek[i][n] == '00' or appKek[i][n] == '++':
            return ''
        else:
            return appKek[i][n]

    def reboot_game(self):

        try:
            for child in self.appKek['GameScreen'].ids.gridplayer_game_screen.children:
                self.appKek['GameScreen'].ids.gridplayer_game_screen.children.remove_widget(child)
                
            for child in self.appKek['GameScreen'].ids.gridcpu_game_screen.children:
                self.appKek['GameScreen'].ids.gridcpu_game_screen.children.remove_widget(child)
        except AttributeError:
            pass
        
        self.btn_player = [[],[],[],[],[],[],[],[],[],[],[]]
        self.btn_cpu = [[],[],[],[],[],[],[],[],[],[],[]]
        
        for i in range(11):
            for n in range(11):
                if i == 0 and n != 0:
                    self.btn_player[i].append(Label(text = str(n)))
                if i == 0 and n == 0:
                    self.btn_player[i].append(Label(text = ''))
                if n == 0 and i != 0:
                    self.btn_player[i].append(Label(text = str(i)))
                if n != 0 and i != 0:
                    #self.btn_player[i].append(Button(on_press = self.click))
                    self.btn_player[i].append(Button(background_color = [0,1,2,1]))
                    
                    kek = self.set_ship(self.appKek['player_mass'], i, n)
                    if kek != '' and kek != '--':
                        self.btn_player[i][n].background_color = [4,4,4,1]

                self.appKek['GameScreen'].ids.gridplayer_game_screen.add_widget(self.btn_player[i][n])
                
                
        for i in range(11):
            self.appKek['GameScreen'].ids.lable_game_screen.add_widget(Label(text = '|'))
        
        for i in range(11):
            for n in range(11):
                if i == 0 and n != 0:
                    self.btn_cpu[i].append(Label(text = str(n)))
                if i == 0 and n == 0:
                    self.btn_cpu[i].append(Label(text = ''))
                if n == 0 and i != 0:
                    self.btn_cpu[i].append(Label(text = str(i)))
                if n != 0 and i != 0:
                    self.btn_cpu[i].append(Button(on_press = self.click,))
                    
                    kek = self.set_ship(self.appKek['cpu_mass'], i, n)
                    # if kek != '' and kek != '--':
                    #     self.btn_player[i][n].text = kek
                    #     self.btn_cpu[i][n].background_color = [1,4,4,1]
                    
                self.appKek['GameScreen'].ids.gridcpu_game_screen.add_widget(self.btn_cpu[i][n])
                
            
    def exitt(self):
        App.get_running_app().stop()
        # self.appKek['GameScreen'].ids.gridcpu_game_screen.clear_widgets()
        # print(self.get_root_window())
        
        # self.manager.current = 'menu_screen'
        
        # for i in range(0,100):
        #     self.btn.append(Button(on_press = self.click))
        #     self.appKek['GameScreen'].ids.gridplayer_game_screen.add_widget(self.btn[i])

        # for i in range(0,100):
        #     self.btn2.append(Button(on_press = self.click))
        #     self.appKek['GameScreen'].ids.gridcpu_game_screen.add_widget(self.btn2[i])

    
class GameScreenWin(Screen):
    def __init__(self, **kwargs):
        super(GameScreenWin, self).__init__(**kwargs)
    def exitt(self):
        App.get_running_app().stop()
    def run(self, appKek):
        self.appKek = appKek

class GameScreenDefeat(Screen):
    def __init__(self, **kwargs):
        super(GameScreenDefeat, self).__init__(**kwargs)
    def exitt(self):
        App.get_running_app().stop()
    def run(self, appKek):
        self.appKek = appKek

class MainApp(App):
    def build( self ):
        
        player_mass = tb.start_game()
        cpu_mass = tb.start_game()
        
        for i in range(1,11):
            for n in range(1,11):
                print(player_mass[i][n], end = ' ')
            print()
        print('-----------------------------')
        for i in range(1,11):
            for n in range(1,11):
                print(cpu_mass[i][n], end = ' ')
            print()
        
        appKek = {'MenuScreen' : MenuScreen(), 
                  'GameScreen' : GameScreen(), 
                  'GameScreenWin' : GameScreenWin(),
                  'GameScreenDefeat': GameScreenDefeat(),
                  'player_mass': player_mass,
                  'cpu_mass' : cpu_mass}
                
        appKek['MenuScreen'].run(appKek)
        appKek['GameScreen'].run(appKek)
        appKek['GameScreenWin'].run(appKek)
        appKek['GameScreenDefeat'].run(appKek)
        
        sm = ScreenManager()
        sm.add_widget(appKek['MenuScreen'])
        sm.add_widget(appKek['GameScreen'])
        sm.add_widget(appKek['GameScreenWin'])
        sm.add_widget(appKek['GameScreenDefeat'])
        
        sm.current = 'menu_screen'
        #sm.current = 'game_screen_defeat'
        #sm.current = 'game_screen_win'
        return sm

if __name__ == '__main__':

    
    MainApp().run()