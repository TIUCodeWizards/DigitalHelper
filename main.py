from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, DictProperty
from kivymd.uix.fitimage import FitImage
from kivy.metrics import dp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout

# Временные данные для демонстрации
temp_users = {
    'student': {
        'password': 'student123',
        'email': 'student@university.com',
        'name': 'Иванов Иван',
        'group': 'ПИ-21-1',
        'phone': '+79991234567',
        'birthDate': '01.01.2000',
        'gender': 'Мужской',
        'grades': {'Математика': 4, 'Физика': 3}
    },
    'teacher': {
        'password': 'teacher123',
        'email': 'teacher@university.com',
        'name': 'Петрова Мария',
        'department': 'Кафедра информатики',
        'phone': '+79998765432',
        'birthDate': '15.05.1985',
        'gender': 'Женский',
        'subjects': ['Математика', 'Программирование']
    },
    'admin': {
        'password': 'admin123',
        'email': 'admin@university.com',
        'name': 'Администратор',
        'group': 'ADM-01',
        'grades': {'Математика': 5, 'Физика': 5}
    }
}

class ScreenManagement(ScreenManager):
    pass

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
            app.current_user = temp_users[username]
            if 'group' in temp_users[username]:
                self.manager.current = 'student_profile'
            else:
                self.manager.current = 'teacher_profile'
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

class MainScreen(Screen):
    def logout(self):
        app = MDApp.get_running_app()
        app.current_user = {
            'name': 'Гость',
            'group': 'Не указана',
            'grades': {}
        }
        self.manager.current = 'welcome'

class StudentProfileScreen(Screen):
    def on_enter(self):
        app = MDApp.get_running_app()
        user = app.current_user
        
        container = self.ids.student_container
        container.clear_widgets()
        
        
        container.add_widget(
            MDLabel(
                text='Профиль студента',
                halign='center',
                font_style='H4',
                size_hint_y=None,
                height=dp(50)))
        
        
        avatar = FitImage(
            source='assets/male-profile.png' if user.get('gender') == 'Мужской' else 'assets/female-profile.png',
            size_hint=(None, None),
            size=(dp(150), dp(150)),
            pos_hint={'center_x': 0.5},
            radius=[dp(75)],  
            mipmap=True  
)
        container.add_widget(avatar)
        
        
        info_card = MDCard(
            orientation='vertical',
            size_hint=(0.9, None),
            height=dp(400),
            pos_hint={'center_x': 0.5},
            padding=[dp(20), dp(25), dp(20), dp(20)],
            spacing=dp(10),
            elevation=3,
            md_bg_color=[1, 1, 1, 1],
            radius=[15]
        )
        
        student_fields = [
            ('Тип профиля', 'Студент'),
            ('ФИО', user.get('name', 'Не указано')),
            ('Почта', user.get('email', 'Не указано')),
            ('Телефон', user.get('phone', 'Не указано')),
            ('Группа', user.get('group', 'Не указана')),
            ('Дата рождения', user.get('birthDate', 'Не указана')),
            ('Пол', user.get('gender', 'Не указан'))
        ]
        
        for label, value in student_fields:
            field_box = MDBoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height=dp(40),
                spacing=dp(2)
            )
            field_box.add_widget(
                MDLabel(
                text=label,
                
                size_hint_y=None,
                height=dp(25),  
                bold=True,      
                
    )
)
            field_box.add_widget(
                MDLabel(
                    text=value,
                    size_hint_y=None,
                    height=dp(20)))
            info_card.add_widget(field_box)
        
        container.add_widget(info_card)
        
        
        buttons = [
            ('На главную', 'main'),
            ('Расписание', 'schedule'),
            ('Оценки', 'grades'),
            ('Выйти', 'welcome')
        ]
        
        for text, screen in buttons:
            btn = MDRaisedButton(
                text=text,
                size_hint=(None, None),
                size=(dp(200), dp(50)),
                pos_hint={'center_x': 0.5}
            )
            btn.bind(on_press=lambda x, s=screen: setattr(self.manager, 'current', s))
            container.add_widget(btn)

class TeacherProfileScreen(Screen):
    def on_enter(self):
        app = MDApp.get_running_app()
        user = app.current_user
        
        container = self.ids.teacher_container
        container.clear_widgets()
        
        
        container.add_widget(
            MDLabel(
                text='Профиль преподавателя',
                halign='center',
                font_style='H4',
                size_hint_y=None,
                height=dp(50)))
        
        avatar = FitImage(
            source='assets/male-profile.png' if user.get('gender') == 'Мужской' else 'assets/female-profile.png',
            size_hint=(None, None),
            size=(dp(150), dp(150)),
            pos_hint={'center_x': 0.5},
            radius=[dp(75)],  
            mipmap=True  
        )
        container.add_widget(avatar)
        
        
        info_card = MDCard(
            orientation='vertical',
            size_hint=(0.9, None),
            height=dp(450),
            pos_hint={'center_x': 0.5},
            padding=[dp(20), dp(25), dp(20), dp(20)],
            spacing=dp(10),
            elevation=3,
            md_bg_color=[1, 1, 1, 1],
            radius=[15]
        )
        
        teacher_fields = [
            ('Тип профиля', 'Преподаватель'),
            ('ФИО', user.get('name', 'Не указано')),
            ('Почта', user.get('email', 'Не указано')),
            ('Телефон', user.get('phone', 'Не указано')),
            ('Кафедра', user.get('department', 'Не указана')),
            ('Дата рождения', user.get('birthDate', 'Не указана')),
            ('Пол', user.get('gender', 'Не указан')),
            ('Преподаваемые предметы', ', '.join(user.get('subjects', [])))
        ]
        
        for label, value in teacher_fields:
            field_box = MDBoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height=dp(40),
                spacing=dp(2)
            )
            field_box.add_widget(
                MDLabel(
                text=label,
                
                size_hint_y=None,
                height=dp(25),
                bold=True,
                
    )
)
            field_box.add_widget(
                MDLabel(
                    text=value,
                    size_hint_y=None,
                    height=dp(20)))
            info_card.add_widget(field_box)
        
        container.add_widget(info_card)
        
        
        buttons = [
            ('На главную', 'main'),
            ('Расписание', 'schedule'),
            ('Выйти', 'welcome')
        ]
        
        for text, screen in buttons:
            btn = MDRaisedButton(
                text=text,
                size_hint=(None, None),
                size=(dp(200), dp(50)),
                pos_hint={'center_x': 0.5}
            )
            btn.bind(on_press=lambda x, s=screen: setattr(self.manager, 'current', s))
            container.add_widget(btn)

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
    StudentProfileScreen:
        name: 'student_profile'
    TeacherProfileScreen:
        name: 'teacher_profile'
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
            on_press: 
                root.manager.current = 'student_profile' if 'group' in app.current_user else 'teacher_profile'
            icon: 'account'
            size_hint_y: 0.2

        MDRaisedButton:
            text: 'Расписание занятий'
            on_press: root.manager.current = 'schedule'
            icon: 'calendar'
            size_hint_y: 0.2

        MDRaisedButton:
            text: 'Зачётная книжка'
            on_press: root.manager.current = 'grades'
            icon: 'book-open'
            size_hint_y: 0.2
            disabled: 'group' not in app.current_user

        MDRectangleFlatButton:
            text: 'Выйти из системы'
            on_press: root.logout()
            size_hint_y: 0.2

<StudentProfileScreen>:
    ScrollView:
        BoxLayout:
            id: student_container
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(20)
            size_hint_y: None
            height: self.minimum_height

<TeacherProfileScreen>:
    ScrollView:
        BoxLayout:
            id: teacher_container
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(20)
            size_hint_y: None
            height: self.minimum_height

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
    current_user = DictProperty()

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.current_user = {
            'name': 'Гость',
            'group': 'Не указана',
            'grades': {}
        }
        return ScreenManagement()

if __name__ == '__main__':
    DigitalHelperApp().run() 