from copy import deepcopy
import time

import json

class Notes:
    def __init__(self, path: str = 'item2.json'):
        self.path = 'item2.json'
        self.notes2 = {}
        self.original_notes2 = {} 

    def open_file(self):
        with open("item2.json", "r",encoding='ascii') as read_content: 
            aList = json.load(read_content)
        
        for i, note in enumerate(aList):
	        self.notes2[i] = note
        self.original_notes2 = deepcopy(self.notes2)

    def save_file(self):

        data2 = []
        for note in self.notes2.values():
            data2.append(note)

        with open("item2.json", "w",encoding='ascii') as read_content: 
            json.dump(data2, read_content)  

    def add_note(self, new_note):
        c_id = max(self.notes2) + 1
        curr_time = time.strftime("%d %b %Y %H:%M:%S", time.localtime())
        self.notes2[c_id] = {"Title" : new_note[0],"Body" : new_note[1], "TimeStamp": curr_time}

    def edit_note(self, c_id: int, new_note):
        note = []
        for i in range(len(new_note)):
            note.append(new_note[i])
            self.notes2[c_id] = note
        note.append(time.strftime("%d %b %Y %H:%M:%S", time.localtime()))
        self.notes2[c_id] = {"Title" : note[0],"Body" : note[1], "TimeStamp": note[2]}
        return note[0]

    def delete_note(self, c_id: int) -> str:
        return self.notes2.pop(c_id)
    