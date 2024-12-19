from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.uix.video import Video
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, RoundedRectangle

# Define color scheme and gradients
WHITE_COLOR = [1, 1, 1, 1]
RED_COLOR = [1, 0, 0, 1]
LIGHT_RED_COLOR = [1, 0, 0, 1]
yel = [1, 1, 0, 1]

# Custom widget for gradient and rounded buttons
class GradientButton(Button):
    def __init__(self, **kwargs):
        super(GradientButton, self).__init__(**kwargs)
        with self.canvas.before:
            Color(1, 0, 0, 1)  # Light red at the top
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(pos=self.update_rect, size=self.update_rect)

        # Custom button styling
        self.color = RED_COLOR
        self.font_size = 20
        self.background_normal ='' 
        self.background_down = ''

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

# Custom widget for back button
class BackButton(Button):
    def __init__(self, **kwargs):
        super(BackButton, self).__init__(**kwargs)
        self.text = "< Back"
        self.size_hint = (0.1, 0.1)
        self.pos_hint = {'x': 0, 'y': 0.9}
        self.background_color = WHITE_COLOR
        self.color = RED_COLOR
        self.font_size = 16
        self.background_normal = ''
        self.background_down = ''

# Splash Screen with Video
class SplashScreen(Screen):
    def on_enter(self):
        self.layout = FloatLayout()
        # Load the video (change the path if needed)
        self.video = Video(source='vid.mp4', state='play')
        self.layout.add_widget(self.video)
        self.add_widget(self.layout)

        # Set the duration for splash screen
        Clock.schedule_once(self.switch_to_main, 10)

    def switch_to_main(self, *args):
        self.manager.current = 'menu'


# Home Screen with Navigation
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.layout = layout

        # Set white background
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)
        
        # App title
        title = Label(text="Heart Care App", font_size=40, color=RED_COLOR, bold=True)
        layout.add_widget(title)
        
        # Adding buttons with gradient and curved edges
        layout.add_widget(self.create_menu_button("Facts", self.go_to_facts))
        layout.add_widget(self.create_menu_button("About Us", self.go_to_about))
        layout.add_widget(self.create_menu_button("Blockage Detector", self.go_to_detector))

        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def create_menu_button(self, text, callback):
        button = GradientButton(text=text, size_hint=(0.8, 0.1), pos_hint={"center_x": 0.5}, font_size=24)
        button.bind(on_press=callback)
        return button

    def go_to_facts(self, instance):
        self.manager.current = 'facts'

    def go_to_about(self, instance):
        self.manager.current = 'about_us'

    def go_to_detector(self, instance):
        self.manager.current = 'blockage_detector'


# Facts Screen
class FactsScreen(Screen):
    def __init__(self, **kwargs):
        super(FactsScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20)
        
        # Set white background
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

        # Back button
        back_button = BackButton(on_press=self.go_back)
        self.layout.add_widget(back_button)

        # Placeholder for facts data and images
        fact_label = Label(text="Heart Facts will be displayed here.", font_size=18, color=RED_COLOR)
        fact_image = Image(source='xxx.png')
        
        self.layout.add_widget(fact_label)
        self.layout.add_widget(fact_image)
        self.add_widget(self.layout)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def go_back(self, instance):
        self.manager.current = 'menu'


# About Us Screen
class AboutUsScreen(Screen):
    def __init__(self, **kwargs):
        super(AboutUsScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20)
        
        # Set white background
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

        # Back button
        back_button = BackButton(on_press=self.go_back)
        self.layout.add_widget(back_button)

        # Placeholder for "About Us"
        about_label = Label(text="About Us Information will be added here.", font_size=18, color=RED_COLOR)
        self.layout.add_widget(about_label)
        self.add_widget(self.layout)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def go_back(self, instance):
        self.manager.current = 'menu'


# Blockage Detector Screen
class BlockageDetectorScreen(Screen):
    def __init__(self, **kwargs):
        super(BlockageDetectorScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Set white background
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

        # Back button
        back_button = BackButton(on_press=self.go_back)
        self.layout.add_widget(back_button)

        # Title for Blockage Detector
        title = Label(text="Blockage Detector", font_size=32, color=RED_COLOR, bold=True)
        self.layout.add_widget(title)

        # Add a GridLayout for questions
        self.grid = GridLayout(cols=1, spacing=10, padding=20)
        self.questions = []
        self.answers = []

        # Example of adding questions
        self.add_question("Do you experience chest pain?", ["Yes", "No"])
        self.add_question("Do you have shortness of breath?", ["Yes", "No"])
        self.add_question("Do you have a family history of heart disease?", ["Yes", "No"])

        self.submit_button = GradientButton(text="Submit", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5}, on_press=self.calculate_blockage)
        self.layout.add_widget(self.grid)
        self.layout.add_widget(self.submit_button)
        self.add_widget(self.layout)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def add_question(self, question_text, options):
        self.grid.add_widget(Label(text=question_text, color=RED_COLOR, font_size=18))
        answer = TextInput()
        self.answers.append(answer)
        self.grid.add_widget(answer)

    def calculate_blockage(self, instance):
        risk_score = sum([1 for answer in self.answers if answer.text.lower() == 'yes'])
        progress = ProgressBar(max=100)
        progress.value = risk_score * 33  # Assuming 3 questions, 33% per question for simplicity
        self.layout.add_widget(progress)

        result_popup = Popup(title="Blockage Risk", content=Label(text=f"Your blockage risk is {progress.value}%"), size_hint=(0.8, 0.4))
        result_popup.open()

    def go_back(self, instance):
        self.manager.current = 'menu'


# Managing all screens
class HeartCareApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(FactsScreen(name='facts'))
        sm.add_widget(AboutUsScreen(name='about_us'))
        sm.add_widget(BlockageDetectorScreen(name='blockage_detector'))

        return sm


if __name__ == '__main__':
    HeartCareApp().run()
