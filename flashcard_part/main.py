from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# Flashcard Screen Logic
class FlashcardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flashcards = []
        self.current_index = 0

    def add_flashcard(self, question, answer):
        if question and answer:
            self.flashcards.append({"question": question, "answer": answer})
            self.ids.flashcard_question.text = "Flashcard added!"
            self.ids.flashcard_answer.text = ""
        else:
            self.ids.flashcard_question.text = "Please enter both question and answer."

    def show_flashcard(self):
        if self.flashcards:
            card = self.flashcards[self.current_index]
            self.ids.flashcard_question.text = card["question"]
            self.ids.flashcard_answer.text = ""
        else:
            self.ids.flashcard_question.text = "No flashcards available."

    def flip_flashcard(self):
        if self.flashcards:
            card = self.flashcards[self.current_index]
            self.ids.flashcard_answer.text = card["answer"]
        else:
            self.ids.flashcard_answer.text = "No flashcards to flip."

    def next_flashcard(self):
        if self.flashcards:
            self.current_index = (self.current_index + 1) % len(self.flashcards)
            self.show_flashcard()

class QuizFlashcardApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FlashcardScreen(name="flashcard"))
        return sm

if __name__ == "__main__":
    QuizFlashcardApp().run()

