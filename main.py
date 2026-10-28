import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.checkbox import CheckBox
from Questions import questions_c1
from Questions import questions_c2
from Questions import questions_c3
from Questions import questions_c4
from Questions import questions_c5
from Questions import questions_c6
from Questions import questions_c7
from Questions import questions_c8
from Questions import questions_c9
from Questions import questions_c10


# Define our different screens
class MainMenu(Screen):
    pass


# Second window
class Section1(Screen, Widget):
    def __init__(self, **kwargs):
        super(Section1, self).__init__(**kwargs)
        self.correct_answer = None
        self.questions_c1 = questions_c1
        self.indicator = 0
        self.amount_questions = 0
        Clock.schedule_once(self.questions_section_1)
        self.answers = []
        self.count_false = 0

        random.shuffle(self.questions_c1)

    def questions_section_1(self, dt=0):
        for child in reversed(self.ids.grid.children):
            if isinstance(child, CheckBox):
                child.active = False

        if self.amount_questions > len(self.questions_c1) - 1:
            self.ids.QuestionLabel.text = f"You answered {self.amount_questions - self.count_false} question(s) correctly out of {self.amount_questions}.\n" + f"You have {round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2)} %"
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelA.text = ""
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelB.text = ""
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelC.text = ""
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.LabelD.text = ""
            self.ids.Next.disabled = True
            if round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2) >= 75:
                self.ids.QuestionLabel.color = (0, 1, 0, 1)
            else:
                self.ids.QuestionLabel.color = (1, 0, 0, 1)
            return

        self.ids.AmountLabel.text = f"Question {self.amount_questions + 1} of {len(self.questions_c1)}"

        self.ids.LabelA.color = (1, 1, 1, 1)
        self.ids.LabelB.color = (1, 1, 1, 1)
        self.ids.LabelC.color = (1, 1, 1, 1)
        self.ids.LabelD.color = (1, 1, 1, 1)

        self.ids.QuestionLabel.text = self.questions_c1[self.amount_questions][0]

        self.ids.LabelA.text = self.questions_c1[self.amount_questions][1]

        self.ids.LabelB.text = self.questions_c1[self.amount_questions][2]

        self.ids.LabelC.text = self.questions_c1[self.amount_questions][3]

        self.ids.LabelD.text = self.questions_c1[self.amount_questions][4]

        self.correct_answer = self.questions_c1[self.amount_questions][-1]
        self.ids.Next.disabled = True

    def next_click(self):
        self.amount_questions += 1
        self.questions_section_1()

    # Collect answer from checkbox

    def checkbox_answer(self, instance, value, letter):

        if value is True:
            self.answers.append(letter)
            self.ids.Next.disabled = False

        else:
            self.answers.remove(letter)
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.Next.disabled = False
            return

        if self.answers[-1] == self.correct_answer:
            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)

            elif self.correct_answer == "b":
                self.ids.LabelB.color = (0, 1, 0, 1)

            elif self.correct_answer == "c":
                self.ids.LabelC.color = (0, 1, 0, 1)

            elif self.correct_answer == "d":
                self.ids.LabelD.color = (0, 1, 0, 1)
            else:
                return

        else:
            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "b":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (0, 1, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "c":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (0, 1, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "d":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (0, 1, 0, 1)
                self.count_false += 1

            else:
                return


class Section2(Screen, Widget):
    def __init__(self, **kwargs):
        super(Section2, self).__init__(**kwargs)
        self.correct_answer = None
        self.questions_c2 = questions_c2
        self.indicator = 0
        self.amount_questions = 0
        Clock.schedule_once(self.questions_section_2)
        self.answers = []
        self.count_false = 0

        random.shuffle(self.questions_c2)

    def questions_section_2(self, dt=0):
        for child in reversed(self.ids.grid.children):
            if isinstance(child, CheckBox):
                child.active = False

        if self.amount_questions > len(self.questions_c2) - 1:
            self.ids.QuestionLabel.text = f"You answered {self.amount_questions - self.count_false} question(s) correctly out of {self.amount_questions}.\n" + f"You have {round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2)} %"
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelA.text = ""
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelB.text = ""
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelC.text = ""
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.LabelD.text = ""
            self.ids.Next.disabled = True
            if round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2) >= 75:
                self.ids.QuestionLabel.color = (0, 1, 0, 1)
            else:
                self.ids.QuestionLabel.color = (1, 0, 0, 1)
            return

        self.ids.AmountLabel.text = f"Question {self.amount_questions + 1} of {len(self.questions_c2)}"

        self.ids.LabelA.color = (1, 1, 1, 1)
        self.ids.LabelB.color = (1, 1, 1, 1)
        self.ids.LabelC.color = (1, 1, 1, 1)
        self.ids.LabelD.color = (1, 1, 1, 1)

        self.ids.QuestionLabel.text = self.questions_c2[self.amount_questions][0]

        self.ids.LabelA.text = self.questions_c2[self.amount_questions][1]

        self.ids.LabelB.text = self.questions_c2[self.amount_questions][2]

        self.ids.LabelC.text = self.questions_c2[self.amount_questions][3]

        self.ids.LabelD.text = self.questions_c2[self.amount_questions][4]

        self.correct_answer = self.questions_c2[self.amount_questions][-1]
        self.ids.Next.disabled = True

    def next_click(self):
        self.amount_questions += 1
        self.questions_section_2()

    # Collect answer from checkbox

    def checkbox_answer(self, instance, value, letter):

        if value is True:
            self.answers.append(letter)
            self.ids.Next.disabled = False
        else:
            self.answers.remove(letter)
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.Next.disabled = False
            return

        if self.answers[-1] == self.correct_answer:
            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)

            elif self.correct_answer == "b":
                self.ids.LabelB.color = (0, 1, 0, 1)

            elif self.correct_answer == "c":
                self.ids.LabelC.color = (0, 1, 0, 1)

            elif self.correct_answer == "d":
                self.ids.LabelD.color = (0, 1, 0, 1)

            else:
                return

        else:

            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "b":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (0, 1, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "c":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (0, 1, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "d":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (0, 1, 0, 1)
                self.count_false += 1

            else:
                return


class Section3(Screen, Widget):
    def __init__(self, **kwargs):
        super(Section3, self).__init__(**kwargs)
        self.correct_answer = None
        self.questions_c3 = questions_c3
        self.indicator = 0
        self.amount_questions = 0
        Clock.schedule_once(self.questions_section_3)
        self.answers = []
        self.count_false = 0

        random.shuffle(self.questions_c3)

    def questions_section_3(self, dt=0):
        for child in reversed(self.ids.grid.children):
            if isinstance(child, CheckBox):
                child.active = False

        if self.amount_questions > len(self.questions_c3) - 1:
            self.ids.QuestionLabel.text = f"You answered {self.amount_questions - self.count_false} question(s) correctly out of {self.amount_questions}.\n" + f"You have {round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2)} %"
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelA.text = ""
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelB.text = ""
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelC.text = ""
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.LabelD.text = ""
            self.ids.Next.disabled = True
            if round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2) >= 75:
                self.ids.QuestionLabel.color = (0, 1, 0, 1)
            else:
                self.ids.QuestionLabel.color = (1, 0, 0, 1)
            return

        self.ids.AmountLabel.text = f"Question {self.amount_questions + 1} of {len(self.questions_c3)}"

        self.ids.LabelA.color = (1, 1, 1, 1)
        self.ids.LabelB.color = (1, 1, 1, 1)
        self.ids.LabelC.color = (1, 1, 1, 1)
        self.ids.LabelD.color = (1, 1, 1, 1)

        self.ids.QuestionLabel.text = self.questions_c3[self.amount_questions][0]

        self.ids.LabelA.text = self.questions_c3[self.amount_questions][1]

        self.ids.LabelB.text = self.questions_c3[self.amount_questions][2]

        self.ids.LabelC.text = self.questions_c3[self.amount_questions][3]

        self.ids.LabelD.text = self.questions_c3[self.amount_questions][4]

        self.correct_answer = self.questions_c3[self.amount_questions][-1]
        self.ids.Next.disabled = True

    def next_click(self):
        self.amount_questions += 1
        self.questions_section_3()

    # Collect answer from checkbox

    def checkbox_answer(self, instance, value, letter):

        if value is True:
            self.answers.append(letter)
            self.ids.Next.disabled = False
        else:
            self.answers.remove(letter)
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.Next.disabled = False
            return

        if self.answers[-1] == self.correct_answer:
            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)

            elif self.correct_answer == "b":
                self.ids.LabelB.color = (0, 1, 0, 1)

            elif self.correct_answer == "c":
                self.ids.LabelC.color = (0, 1, 0, 1)

            elif self.correct_answer == "d":
                self.ids.LabelD.color = (0, 1, 0, 1)

            else:
                return

        else:

            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "b":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (0, 1, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "c":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (0, 1, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "d":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (0, 1, 0, 1)
                self.count_false += 1

            else:
                return


class Section4(Screen, Widget):
    def __init__(self, **kwargs):
        super(Section4, self).__init__(**kwargs)
        self.correct_answer = None
        self.questions_c4 = questions_c4
        self.indicator = 0
        self.amount_questions = 0
        Clock.schedule_once(self.questions_section_4)
        self.answers = []
        self.count_false = 0

        random.shuffle(self.questions_c4)

    def questions_section_4(self, dt=0):
        for child in reversed(self.ids.grid.children):
            if isinstance(child, CheckBox):
                child.active = False

        if self.amount_questions > len(self.questions_c4) - 1:
            self.ids.QuestionLabel.text = f"You answered {self.amount_questions - self.count_false} question(s) correctly out of {self.amount_questions}.\n" + f"You have {round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2)} %"
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelA.text = ""
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelB.text = ""
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelC.text = ""
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.LabelD.text = ""
            self.ids.Next.disabled = True
            if round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2) >= 75:
                self.ids.QuestionLabel.color = (0, 1, 0, 1)
            else:
                self.ids.QuestionLabel.color = (1, 0, 0, 1)
            return

        self.ids.AmountLabel.text = f"Question {self.amount_questions + 1} of {len(self.questions_c4)}"

        self.ids.LabelA.color = (1, 1, 1, 1)
        self.ids.LabelB.color = (1, 1, 1, 1)
        self.ids.LabelC.color = (1, 1, 1, 1)
        self.ids.LabelD.color = (1, 1, 1, 1)

        self.ids.QuestionLabel.text = self.questions_c4[self.amount_questions][0]

        self.ids.LabelA.text = self.questions_c4[self.amount_questions][1]

        self.ids.LabelB.text = self.questions_c4[self.amount_questions][2]

        self.ids.LabelC.text = self.questions_c4[self.amount_questions][3]

        self.ids.LabelD.text = self.questions_c4[self.amount_questions][4]

        self.correct_answer = self.questions_c4[self.amount_questions][-1]
        self.ids.Next.disabled = True

    def next_click(self):
        self.amount_questions += 1
        self.questions_section_4()

    # Collect answer from checkbox

    def checkbox_answer(self, instance, value, letter):

        if value is True:
            self.answers.append(letter)
            self.ids.Next.disabled = False
        else:
            self.answers.remove(letter)
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.Next.disabled = False
            return

        if self.answers[-1] == self.correct_answer:
            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)

            elif self.correct_answer == "b":
                self.ids.LabelB.color = (0, 1, 0, 1)

            elif self.correct_answer == "c":
                self.ids.LabelC.color = (0, 1, 0, 1)

            elif self.correct_answer == "d":
                self.ids.LabelD.color = (0, 1, 0, 1)

            else:
                return

        else:

            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "b":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (0, 1, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "c":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (0, 1, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "d":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (0, 1, 0, 1)
                self.count_false += 1

            else:
                return


class Section5(Screen, Widget):
    def __init__(self, **kwargs):
        super(Section5, self).__init__(**kwargs)
        self.correct_answer = None
        self.questions_c5 = questions_c5
        self.indicator = 0
        self.amount_questions = 0
        Clock.schedule_once(self.questions_section_5)
        self.answers = []
        self.count_false = 0

        random.shuffle(self.questions_c5)

    def questions_section_5(self, dt=0):
        for child in reversed(self.ids.grid.children):
            if isinstance(child, CheckBox):
                child.active = False

        if self.amount_questions > len(self.questions_c5) - 1:
            self.ids.QuestionLabel.text = f"You answered {self.amount_questions - self.count_false} question(s) correctly out of {self.amount_questions}.\n" + f"You have {round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2)} %"
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelA.text = ""
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelB.text = ""
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelC.text = ""
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.LabelD.text = ""
            self.ids.Next.disabled = True
            if round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2) >= 75:
                self.ids.QuestionLabel.color = (0, 1, 0, 1)
            else:
                self.ids.QuestionLabel.color = (1, 0, 0, 1)
            return

        self.ids.AmountLabel.text = f"Question {self.amount_questions + 1} of {len(self.questions_c5)}"

        self.ids.LabelA.color = (1, 1, 1, 1)
        self.ids.LabelB.color = (1, 1, 1, 1)
        self.ids.LabelC.color = (1, 1, 1, 1)
        self.ids.LabelD.color = (1, 1, 1, 1)

        self.ids.QuestionLabel.text = self.questions_c5[self.amount_questions][0]

        self.ids.LabelA.text = self.questions_c5[self.amount_questions][1]

        self.ids.LabelB.text = self.questions_c5[self.amount_questions][2]

        self.ids.LabelC.text = self.questions_c5[self.amount_questions][3]

        self.ids.LabelD.text = self.questions_c5[self.amount_questions][4]

        self.correct_answer = self.questions_c5[self.amount_questions][-1]
        self.ids.Next.disabled = True

    def next_click(self):
        self.amount_questions += 1
        self.questions_section_5()

    # Collect answer from checkbox

    def checkbox_answer(self, instance, value, letter):

        if value is True:
            self.answers.append(letter)
            self.ids.Next.disabled = False
        else:
            self.answers.remove(letter)
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.Next.disabled = False
            return

        if self.answers[-1] == self.correct_answer:
            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)

            elif self.correct_answer == "b":
                self.ids.LabelB.color = (0, 1, 0, 1)

            elif self.correct_answer == "c":
                self.ids.LabelC.color = (0, 1, 0, 1)

            elif self.correct_answer == "d":
                self.ids.LabelD.color = (0, 1, 0, 1)

            else:
                return

        else:

            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "b":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (0, 1, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "c":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (0, 1, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "d":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (0, 1, 0, 1)
                self.count_false += 1

            else:
                return


class Section6(Screen, Widget):
    def __init__(self, **kwargs):
        super(Section6, self).__init__(**kwargs)
        self.correct_answer = None
        self.questions_c6 = questions_c6
        self.indicator = 0
        self.amount_questions = 0
        Clock.schedule_once(self.questions_section_6)
        self.answers = []
        self.count_false = 0

        random.shuffle(self.questions_c6)

    def questions_section_6(self, dt=0):
        for child in reversed(self.ids.grid.children):
            if isinstance(child, CheckBox):
                child.active = False

        if self.amount_questions > len(self.questions_c6) - 1:
            self.ids.QuestionLabel.text = f"You answered {self.amount_questions - self.count_false} question(s) correctly out of {self.amount_questions}.\n" + f"You have {round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2)} %"
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelA.text = ""
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelB.text = ""
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelC.text = ""
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.LabelD.text = ""
            self.ids.Next.disabled = True
            if round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2) >= 75:
                self.ids.QuestionLabel.color = (0, 1, 0, 1)
            else:
                self.ids.QuestionLabel.color = (1, 0, 0, 1)
            return

        self.ids.AmountLabel.text = f"Question {self.amount_questions + 1} of {len(self.questions_c6)}"

        self.ids.LabelA.color = (1, 1, 1, 1)
        self.ids.LabelB.color = (1, 1, 1, 1)
        self.ids.LabelC.color = (1, 1, 1, 1)
        self.ids.LabelD.color = (1, 1, 1, 1)

        self.ids.QuestionLabel.text = self.questions_c6[self.amount_questions][0]

        self.ids.LabelA.text = self.questions_c6[self.amount_questions][1]

        self.ids.LabelB.text = self.questions_c6[self.amount_questions][2]

        self.ids.LabelC.text = self.questions_c6[self.amount_questions][3]

        self.ids.LabelD.text = self.questions_c6[self.amount_questions][4]

        self.correct_answer = self.questions_c6[self.amount_questions][-1]
        self.ids.Next.disabled = True

    def next_click(self):
        self.amount_questions += 1
        self.questions_section_6()

    # Collect answer from checkbox

    def checkbox_answer(self, instance, value, letter):

        if value is True:
            self.answers.append(letter)
            self.ids.Next.disabled = False
        else:
            self.answers.remove(letter)
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.Next.disabled = False
            return

        if self.answers[-1] == self.correct_answer:
            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)

            elif self.correct_answer == "b":
                self.ids.LabelB.color = (0, 1, 0, 1)

            elif self.correct_answer == "c":
                self.ids.LabelC.color = (0, 1, 0, 1)

            elif self.correct_answer == "d":
                self.ids.LabelD.color = (0, 1, 0, 1)

            else:
                return

        else:

            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "b":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (0, 1, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "c":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (0, 1, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "d":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (0, 1, 0, 1)
                self.count_false += 1

            else:
                return


class Section7(Screen, Widget):
    def __init__(self, **kwargs):
        super(Section7, self).__init__(**kwargs)
        self.correct_answer = None
        self.questions_c7 = questions_c7
        self.indicator = 0
        self.amount_questions = 0
        Clock.schedule_once(self.questions_section_7)
        self.answers = []
        self.count_false = 0

        random.shuffle(self.questions_c7)

    def questions_section_7(self, dt=0):
        for child in reversed(self.ids.grid.children):
            if isinstance(child, CheckBox):
                child.active = False

        if self.amount_questions > len(self.questions_c7) - 1:
            self.ids.QuestionLabel.text = f"You answered {self.amount_questions - self.count_false} question(s) correctly out of {self.amount_questions}.\n" + f"You have {round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2)} %"
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelA.text = ""
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelB.text = ""
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelC.text = ""
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.LabelD.text = ""
            self.ids.Next.disabled = True
            if round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2) >= 75:
                self.ids.QuestionLabel.color = (0, 1, 0, 1)
            else:
                self.ids.QuestionLabel.color = (1, 0, 0, 1)
            return

        self.ids.AmountLabel.text = f"Question {self.amount_questions + 1} of {len(self.questions_c7)}"

        self.ids.LabelA.color = (1, 1, 1, 1)
        self.ids.LabelB.color = (1, 1, 1, 1)
        self.ids.LabelC.color = (1, 1, 1, 1)
        self.ids.LabelD.color = (1, 1, 1, 1)

        self.ids.QuestionLabel.text = self.questions_c7[self.amount_questions][0]

        self.ids.LabelA.text = self.questions_c7[self.amount_questions][1]

        self.ids.LabelB.text = self.questions_c7[self.amount_questions][2]

        self.ids.LabelC.text = self.questions_c7[self.amount_questions][3]

        self.ids.LabelD.text = self.questions_c7[self.amount_questions][4]

        self.correct_answer = self.questions_c7[self.amount_questions][-1]
        self.ids.Next.disabled = True

    def next_click(self):
        self.amount_questions += 1
        self.questions_section_7()

    # Collect answer from checkbox

    def checkbox_answer(self, instance, value, letter):

        if value is True:
            self.answers.append(letter)
            self.ids.Next.disabled = False
        else:
            self.answers.remove(letter)
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.Next.disabled = False
            return

        if self.answers[-1] == self.correct_answer:
            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)

            elif self.correct_answer == "b":
                self.ids.LabelB.color = (0, 1, 0, 1)

            elif self.correct_answer == "c":
                self.ids.LabelC.color = (0, 1, 0, 1)

            elif self.correct_answer == "d":
                self.ids.LabelD.color = (0, 1, 0, 1)

            else:
                return

        else:

            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "b":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (0, 1, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "c":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (0, 1, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "d":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (0, 1, 0, 1)
                self.count_false += 1

            else:
                return


class Section8(Screen, Widget):
    def __init__(self, **kwargs):
        super(Section8, self).__init__(**kwargs)
        self.correct_answer = None
        self.questions_c8 = questions_c8
        self.indicator = 0
        self.amount_questions = 0
        Clock.schedule_once(self.questions_section_8)
        self.answers = []
        self.count_false = 0

        random.shuffle(self.questions_c8)

    def questions_section_8(self, dt=0):
        for child in reversed(self.ids.grid.children):
            if isinstance(child, CheckBox):
                child.active = False

        if self.amount_questions > len(self.questions_c8) - 1:
            self.ids.QuestionLabel.text = f"You answered {self.amount_questions - self.count_false} question(s) correctly out of {self.amount_questions}.\n" + f"You have {round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2)} %"
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelA.text = ""
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelB.text = ""
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelC.text = ""
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.LabelD.text = ""
            self.ids.Next.disabled = True
            if round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2) >= 75:
                self.ids.QuestionLabel.color = (0, 1, 0, 1)
            else:
                self.ids.QuestionLabel.color = (1, 0, 0, 1)
            return

        self.ids.AmountLabel.text = f"Question {self.amount_questions + 1} of {len(self.questions_c8)}"

        self.ids.LabelA.color = (1, 1, 1, 1)
        self.ids.LabelB.color = (1, 1, 1, 1)
        self.ids.LabelC.color = (1, 1, 1, 1)
        self.ids.LabelD.color = (1, 1, 1, 1)

        self.ids.QuestionLabel.text = self.questions_c8[self.amount_questions][0]

        self.ids.LabelA.text = self.questions_c8[self.amount_questions][1]

        self.ids.LabelB.text = self.questions_c8[self.amount_questions][2]

        self.ids.LabelC.text = self.questions_c8[self.amount_questions][3]

        self.ids.LabelD.text = self.questions_c8[self.amount_questions][4]

        self.correct_answer = self.questions_c8[self.amount_questions][-1]
        self.ids.Next.disabled = True

    def next_click(self):
        self.amount_questions += 1
        self.questions_section_8()

    # Collect answer from checkbox

    def checkbox_answer(self, instance, value, letter):

        if value is True:
            self.answers.append(letter)
            self.ids.Next.disabled = False
        else:
            self.answers.remove(letter)
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.Next.disabled = False
            return

        if self.answers[-1] == self.correct_answer:
            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)

            elif self.correct_answer == "b":
                self.ids.LabelB.color = (0, 1, 0, 1)

            elif self.correct_answer == "c":
                self.ids.LabelC.color = (0, 1, 0, 1)

            elif self.correct_answer == "d":
                self.ids.LabelD.color = (0, 1, 0, 1)

            else:
                return

        else:

            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "b":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (0, 1, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "c":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (0, 1, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "d":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (0, 1, 0, 1)
                self.count_false += 1

            else:
                return


class Section9(Screen, Widget):
    def __init__(self, **kwargs):
        super(Section9, self).__init__(**kwargs)
        self.correct_answer = None
        self.questions_c9 = questions_c9
        self.indicator = 0
        self.amount_questions = 0
        Clock.schedule_once(self.questions_section_9)
        self.answers = []
        self.count_false = 0

        random.shuffle(self.questions_c9)

    def questions_section_9(self, dt=0):
        for child in reversed(self.ids.grid.children):
            if isinstance(child, CheckBox):
                child.active = False

        if self.amount_questions > len(self.questions_c9) - 1:
            self.ids.QuestionLabel.text = f"You answered {self.amount_questions - self.count_false} question(s) correctly out of {self.amount_questions}.\n" + f"You have {round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2)} %"
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelA.text = ""
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelB.text = ""
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelC.text = ""
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.LabelD.text = ""
            self.ids.Next.disabled = True
            if round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2) >= 75:
                self.ids.QuestionLabel.color = (0, 1, 0, 1)
            else:
                self.ids.QuestionLabel.color = (1, 0, 0, 1)
            return

        self.ids.AmountLabel.text = f"Question {self.amount_questions + 1} of {len(self.questions_c9)}"

        self.ids.LabelA.color = (1, 1, 1, 1)
        self.ids.LabelB.color = (1, 1, 1, 1)
        self.ids.LabelC.color = (1, 1, 1, 1)
        self.ids.LabelD.color = (1, 1, 1, 1)

        self.ids.QuestionLabel.text = self.questions_c9[self.amount_questions][0]

        self.ids.LabelA.text = self.questions_c9[self.amount_questions][1]

        self.ids.LabelB.text = self.questions_c9[self.amount_questions][2]

        self.ids.LabelC.text = self.questions_c9[self.amount_questions][3]

        self.ids.LabelD.text = self.questions_c9[self.amount_questions][4]

        self.correct_answer = self.questions_c9[self.amount_questions][-1]
        self.ids.Next.disabled = True

    def next_click(self):
        self.amount_questions += 1
        self.questions_section_9()

    # Collect answer from checkbox

    def checkbox_answer(self, instance, value, letter):

        if value is True:
            self.answers.append(letter)
            self.ids.Next.disabled = False
        else:
            self.answers.remove(letter)
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.Next.disabled = False
            return

        if self.answers[-1] == self.correct_answer:
            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)

            elif self.correct_answer == "b":
                self.ids.LabelB.color = (0, 1, 0, 1)

            elif self.correct_answer == "c":
                self.ids.LabelC.color = (0, 1, 0, 1)

            elif self.correct_answer == "d":
                self.ids.LabelD.color = (0, 1, 0, 1)

            else:
                return

        else:

            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "b":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (0, 1, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "c":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (0, 1, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "d":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (0, 1, 0, 1)
                self.count_false += 1

            else:
                return


class Section10(Screen, Widget):
    def __init__(self, **kwargs):
        super(Section10, self).__init__(**kwargs)
        self.correct_answer = None
        self.questions_c10 = questions_c10
        self.indicator = 0
        self.amount_questions = 0
        Clock.schedule_once(self.questions_section_10)
        self.answers = []
        self.count_false = 0

        random.shuffle(self.questions_c10)

    def questions_section_10(self, dt=0):
        for child in reversed(self.ids.grid.children):
            if isinstance(child, CheckBox):
                child.active = False

        if self.amount_questions > len(self.questions_c10) - 1:
            self.ids.QuestionLabel.text = f"You answered {self.amount_questions - self.count_false} question(s) correctly out of {self.amount_questions}.\n" + f"You have {round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2)} %"
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelA.text = ""
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelB.text = ""
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelC.text = ""
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.LabelD.text = ""
            self.ids.Next.disabled = True
            if round(((self.amount_questions - self.count_false) / self.amount_questions) * 100, 2) >= 75:
                self.ids.QuestionLabel.color = (0, 1, 0, 1)
            else:
                self.ids.QuestionLabel.color = (1, 0, 0, 1)
            return

        self.ids.AmountLabel.text = f"Question {self.amount_questions + 1} of {len(self.questions_c10)}"

        self.ids.LabelA.color = (1, 1, 1, 1)
        self.ids.LabelB.color = (1, 1, 1, 1)
        self.ids.LabelC.color = (1, 1, 1, 1)
        self.ids.LabelD.color = (1, 1, 1, 1)

        self.ids.QuestionLabel.text = self.questions_c10[self.amount_questions][0]

        self.ids.LabelA.text = self.questions_c10[self.amount_questions][1]

        self.ids.LabelB.text = self.questions_c10[self.amount_questions][2]

        self.ids.LabelC.text = self.questions_c10[self.amount_questions][3]

        self.ids.LabelD.text = self.questions_c10[self.amount_questions][4]

        self.correct_answer = self.questions_c10[self.amount_questions][-1]
        self.ids.Next.disabled = True

    def next_click(self):
        self.amount_questions += 1
        self.questions_section_10()

    # Collect answer from checkbox

    def checkbox_answer(self, instance, value, letter):

        if value is True:
            self.answers.append(letter)
            self.ids.Next.disabled = False
        else:
            self.answers.remove(letter)
            self.ids.LabelA.color = (1, 1, 1, 1)
            self.ids.LabelB.color = (1, 1, 1, 1)
            self.ids.LabelC.color = (1, 1, 1, 1)
            self.ids.LabelD.color = (1, 1, 1, 1)
            self.ids.Next.disabled = False
            return

        if self.answers[-1] == self.correct_answer:
            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)

            elif self.correct_answer == "b":
                self.ids.LabelB.color = (0, 1, 0, 1)

            elif self.correct_answer == "c":
                self.ids.LabelC.color = (0, 1, 0, 1)

            elif self.correct_answer == "d":
                self.ids.LabelD.color = (0, 1, 0, 1)

            else:
                return

        else:

            if self.correct_answer == "a":
                self.ids.LabelA.color = (0, 1, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "b":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (0, 1, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "c":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (0, 1, 0, 1)
                self.ids.LabelD.color = (1, 0, 0, 1)
                self.count_false += 1

            elif self.correct_answer == "d":
                self.ids.LabelA.color = (1, 0, 0, 1)
                self.ids.LabelB.color = (1, 0, 0, 1)
                self.ids.LabelC.color = (1, 0, 0, 1)
                self.ids.LabelD.color = (0, 1, 0, 1)
                self.count_false += 1

            else:
                return


class WindowManager(ScreenManager):
    pass


# Basic Classes for the layout
class MainWidget(Widget):
    pass


class IFIA_quizApp(App):
    pass


IFIA_quizApp().run()
