from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, DictProperty

# Временные данные для демонстрации
temp_users = {
    'admin': {
        'password': 'admin123',
        'email': 'admin@university.com',
        'name': 'Администратор',
        'group': 'ADM-01',
        'grades': {'Математика': 5, 'Физика': 5}
    },
    'student': {
        'password': 'student123',
        'email': 'student@university.com',
        'name': 'Иванов Иван',
        'group': 'ПИ-21-1',
        'grades': {'Математика': 4, 'Физика': 3}
    }
}

class ScreenManagement(ScreenManager):
    pass

# Основные экраны
class WelcomeScreen(Screen):
    pass


class LoginScreen(Screen):
    login = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_user(self):
        username = self.login.text
        password = self.password.text
        app = MDApp.get_running_app()

        if username in temp_users and temp_users[username]['password'] == password:
            print(f"Успешный вход как {username}!")
            # Обновляем данные текущего пользователя
            app.current_user = temp_users[username]
            self.manager.current = 'main'
        else:
            print("Ошибка: Неверный логин или пароль")


class RegisterScreen(Screen):
    reg_login = ObjectProperty(None)
    reg_password = ObjectProperty(None)
    reg_email = ObjectProperty(None)

    def register_user(self):
        username = self.reg_login.text
        password = self.reg_password.text
        email = self.reg_email.text

        if username in temp_users:
            print("Ошибка: Пользователь уже существует")
            return

        temp_users[username] = {
            'password': password,
            'email': email,
            'name': 'Новый пользователь',
            'group': 'Группа не указана',
            'grades': {}
        }
        print(f"Пользователь {username} успешно зарегистрирован!")


# Новые экраны главного меню
class MainScreen(Screen):
    def show_profile(self):
        self.manager.current = 'profile'

    def show_schedule(self):
        self.manager.current = 'schedule'

    def show_grades(self):
        self.manager.current = 'grades'

class ProfileScreen(Screen):
    pass

class ScheduleScreen(Screen):
    pass

class GradesScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class ScheduleScreen(Screen):
    pass

class GradesScreen(Screen):
    pass

Builder.load_string('''
<ScreenManagement>:
    WelcomeScreen:
        name: 'welcome'
    LoginScreen:
        name: 'login'
    RegisterScreen:
        name: 'register'
    MainScreen:
        name: 'main'
    ProfileScreen:
        name: 'profile'
    ScheduleScreen:
        name: 'schedule'
    GradesScreen:
        name: 'grades'

<WelcomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20

        MDLabel:
            text: 'Добро пожаловать в Университетский Помощник!'
            halign: 'center'
            font_style: 'H4'

        MDRaisedButton:
            text: 'Войти'
            on_press: root.manager.current = 'login'

        MDRaisedButton:
            text: 'Регистрация'
            on_press: root.manager.current = 'register'

<LoginScreen>:
    login: login_input
    password: password_input

    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15

        MDLabel:
            text: 'Авторизация'
            halign: 'center'
            font_style: 'H5'

        MDTextField:
            id: login_input
            hint_text: 'Логин'

        MDTextField:
            id: password_input
            hint_text: 'Пароль'
            password: True

        MDRaisedButton:
            text: 'Войти'
            on_press: root.login_user()

        MDRectangleFlatButton:
            text: 'Нет аккаунта? Зарегистрируйтесь'
            on_press: root.manager.current = 'register'

<RegisterScreen>:
    reg_login: reg_login_input
    reg_password: reg_password_input
    reg_email: reg_email_input

    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15

        MDLabel:
            text: 'Регистрация'
            halign: 'center'
            font_style: 'H5'

        MDTextField:
            id: reg_login_input
            hint_text: 'Придумайте логин'

        MDTextField:
            id: reg_password_input
            hint_text: 'Придумайте пароль'
            password: True

        MDTextField:
            id: reg_email_input
            hint_text: 'Ваш email'

        MDRaisedButton:
            text: 'Зарегистрироваться'
            on_press: root.register_user()

        MDRectangleFlatButton:
            text: 'Назад к авторизации'
            on_press: root.manager.current = 'login'

<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15

        MDLabel:
            text: 'Главное меню'
            halign: 'center'
            font_style: 'H4'
            size_hint_y: 0.2

        MDRaisedButton:
            text: 'Личный кабинет'
            on_press: root.show_profile()
            icon: 'account'
            size_hint_y: 0.2

        MDRaisedButton:
            text: 'Расписание занятий'
            on_press: root.show_schedule()
            icon: 'calendar'
            size_hint_y: 0.2

        MDRaisedButton:
            text: 'Зачётная книжка'
            on_press: root.show_grades()
            icon: 'book-open'
            size_hint_y: 0.2

        MDRectangleFlatButton:
            text: 'Выйти из системы'
            on_press: root.manager.current = 'welcome'
            size_hint_y: 0.2

<ProfileScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        
        MDLabel:
            text: 'Личный кабинет'
            halign: 'center'
            font_style: 'H4'
        
        MDLabel:
            text: f"Пользователь: {app.current_user['name']}"
        
        MDLabel:
            text: f"Группа: {app.current_user['group']}"
        
        MDRectangleFlatButton:
            text: 'Назад'
            on_press: root.manager.current = 'main'

<ScheduleScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        MDLabel:
            text: 'Расписание занятий'
            halign: 'center'
            font_style: 'H4'
        
        ScrollView:
            MDList:
                id: schedule_list
                OneLineListItem:
                    text: "Понедельник: Математика (9:00-10:30)"
                OneLineListItem:
                    text: "Вторник: Физика (10:45-12:15)"
        
        MDRectangleFlatButton:
            text: 'Назад'
            on_press: root.manager.current = 'main'

<GradesScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        MDLabel:
            text: 'Зачётная книжка'
            halign: 'center'
            font_style: 'H4'
        
        ScrollView:
            MDList:
                id: grades_list
                OneLineListItem:
                    text: f"Математика: {app.current_user['grades'].get('Математика', 'нет оценки')}"
                OneLineListItem:
                    text: f"Физика: {app.current_user['grades'].get('Физика', 'нет оценки')}"
        
        MDRectangleFlatButton:
            text: 'Назад'
            on_press: root.manager.current = 'main'
''')


class DigitalHelperApp(MDApp):
    current_user = DictProperty()  # Теперь current_user - свойство приложения

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.current_user = {  # Инициализируем здесь
            'name': 'Гость',
            'group': 'Не указана',
            'grades': {}
        }
        return ScreenManagement()

if __name__ == '__main__':
    DigitalHelperApp().run()