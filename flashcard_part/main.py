from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

# Flashcard Screen Logic
class FlashcardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flashcards = []  # To store flashcards as a list of dictionaries
        self.current_index = 0  # Track the current flashcard

    def add_flashcard(self, question, answer):
        """Add a new flashcard."""
        if question and answer:
            self.flashcards.append({"question": question, "answer": answer})
            self.ids.flashcard_question.text = "Flashcard added!"
        else:
            self.ids.flashcard_question.text = "Please enter both question and answer!"

    def show_flashcard(self):
        """Display the current flashcard's question."""
        if self.flashcards:
            card = self.flashcards[self.current_index]
            self.ids.flashcard_question.text = card["question"]
            self.ids.flashcard_answer.text = ""

    def flip_flashcard(self):
        """Show the answer to the current flashcard."""
        if self.flashcards:
            card = self.flashcards[self.current_index]
            self.ids.flashcard_answer.text = card["answer"]

    def next_flashcard(self):
        """Move to the next flashcard."""
        if self.flashcards:
            self.current_index = (self.current_index + 1) % len(self.flashcards)
            self.show_flashcard()

# Main App
class FlashcardApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FlashcardScreen(name="flashcard"))
        return sm

if __name__ == "__main__":
    FlashcardApp().run()
