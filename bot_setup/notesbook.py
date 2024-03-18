from collections import UserDict
import os
import json


class Note(UserDict):
    def __init__(self, id, text):
        super().__init__()
        self['id'] = id
        self['text'] = text
        self['tags'] = []

    def edit(self, new_text):
        self['text'] = new_text

    def __str__(self):
        if len(self["tags"]) > 0:
            return f'{self["id"]}: {self["text"]}{". Tags: " + ", ".join([tag for tag in self["tags"]])}'
        else:
            return f'{self["id"]}: {self["text"]}'

    

class Notesbook(UserDict):
    def __init__(self, file_path):
        super().__init__()
        self.data = {}
        self.__id = 1
        self.file_path = file_path
        # self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save_notes(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f)


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
        # self.save_notes()
        return f'Note # {id} deleted.'
     

    def edit_note(self, id, new_text):
    
        note = self[int(id)]
        if len(new_text) >= 2:
            note['text'] = new_text
            # self.save_notes()
            return f'Note # {id} edited.'
        else:
            raise ValueError
        

    def find_note(self, subtext):
        if len(subtext) > 0:
            if len(self) > 0:
                return '\n'.join([f'{str(self[key])}' for key in self if subtext.casefold() in self[key]["text"].casefold()]) 
            else:        
                return "\nKodi>> Notebook is empty."
        else:
            raise ValueError
        

    def add_tags(self, id, tags):
        note = self[int(id)]
        for tag in tags:
            for index, item in enumerate(note['tags']):
                if item.casefold() == tag.casefold():
                    note['tags'].pop(index)
                    break
            note['tags'].append(tag)
        return f'\nKodi>> I added tag(s) to the note # {id}.'
      
          
    def delete_tag(self, id, tag):
        note = self[int(id)]
        for index, item in enumerate(note['tags']):
            if item.casefold() == tag.casefold():
                note['tags'].pop(index)
                return f'\nKodi>> I removed tag(s) from the note # {id}.'
        return '\nKodi>> Oops... This tag doesn`t exist.'
        

    def find_note_by_tags(self, tags):
        result = []
        for note in self.values():
            tags_lower = [tag.lower() for tag in note["tags"]]
            if any(tag.casefold() in tags_lower for tag in tags):
                result.append(str(note))
        if len(result) > 0:
            return '\n'.join(result)
        else:
            return '\nKodi>> Oops... I can`t find notes with these tags'


    def __str__(self):
        if len(self) > 0:
            return '\n'.join([f'{str(self[key])}' for key in self])
        else:
            return '\nKodi>> Notebook is empty.'