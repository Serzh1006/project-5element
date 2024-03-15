from collections import UserDict


class Note(UserDict):
    def __init__(self, id, text):
        super().__init__()
        self['id'] = id
        self['text'] = text

    def edit(self, new_text):
        self['text'] = new_text

    def __str__(self):
        return f'{self["id"]}: {self["text"]}'

    

class Notesbook(UserDict):
    def __init__(self):
        super().__init__()
        self.data = {}
        self.__id = 1


    def add_note(self, text):
        id = self.__id
        note = Note(id, text)
        if len(text) >= 2:
            self[id] = note
            self.__id += 1
            return f'Note # {id} created.'
        else:
            raise ValueError
            

    def delete_note(self, id):
        del self[int(id)]
        return f'Note # {id} deleted.'
     

    def edit_note(self, id, new_text):
    
        note = self[int(id)]
        if len(new_text) >= 2:
            note['text'] = new_text
            return f'Note # {id} edited.'
        else:
            raise ValueError


    def find_note(self, subtext):
        if len(subtext) > 0:
            if len(self) > 0:
                return '\n'.join([f'{str(self[key])}' for key in self if subtext.casefold() in self[key]["text"].casefold()]) 
            else:        
                return "Notebook is empty."
        else:
            raise ValueError


    def __str__(self):
        if len(self) > 0:
            return '\n'.join([f'{str(self[key])}' for key in self])
        else:
            return 'Notebook is empty.'

