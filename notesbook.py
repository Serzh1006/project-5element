class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text


    def update_text(self, new_text):
        self.text = new_text


    def __str__(self):
        return f"Title: {self.title}\nText: {self.text}\n"
    

class Notesbook:

    def __init__(self):
        self.notes = []


    def add_note(self, title, text):
        note = Note(title, text)
        self.notes.append(note)


    def edit_note(self, title, new_text):
        for note in self.notes:
            if note.title == title:
                note.update_text(new_text)
                break

            
    def search_note(self, title):
        for note in self.notes:
            if note.title == title:
                return note
  

    def delete_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)

    def __str__(self):
        pass

