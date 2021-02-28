from random import randrange, choice as rand_choice, sample
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label

CORRECT = "three"

THAI = "หนังสือ,ระวัง,ตลาด,โรงพยาบาล".split(",")
ENGLISH = "book,beware,market,hospital".split(",")


class MyDisplayWidget(Widget):
    pass






class PootDai(App):

    def build(self):
        parent = Widget()



        self.question = Label(text="")

        self.next_question()

        self.buttons = [Button(text=option) for option in self.options]
        [b.bind(on_release=self.check_answer) for b in self.buttons]



        parent.add_widget(self.question)

        for b in self.buttons:
            parent.add_widget(b)
        return parent

    def next_question(self):
        i = randrange(0, len(THAI))
        w = THAI[i]
        self.correct = ENGLISH[i]
        self.options = [w]
        while w in self.options:
            self.options = sample(ENGLISH, 3)
        self.question.text = "What is the meaning of the word '{}'?".format(w)

    def check_answer(self, button):
        if button.text == self.correct:
            button.text = "change"




if __name__ == '__main__':
    PootDai().run()