from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager 
from kivy.properties import  StringProperty
#first window
class OpenWindow(Screen):
   pass
#second window
class LoginWindow(Screen):
    # we use StringProperty  because to change screen if username and password is true
    current_window = StringProperty("login") 
    user_name = "cvs"
    password =  "12345"
    # this func takes username and password what user wrote, we put this func here because passwords and usernames are in this screen
    def get_names(self):
        if self.ids.user.text == self.user_name and self.ids.password.text == self.password:
            # to change the window, current_window
            self.current_window = "work"
# third window to make work somethings...
class WorkingWindow(Screen):
    def start(self):
        pass
    def stop(self):
        pass
# Window manager necessery
class ManagerWindow(ScreenManager):
    pass
class MainApp(MDApp):
    def build(self):
        # themes

        kv = Builder.load_file('login.kv')
        return kv

if __name__ == '__main__':
    # we may use myapp later
    myapp = MainApp()
    myapp.run()