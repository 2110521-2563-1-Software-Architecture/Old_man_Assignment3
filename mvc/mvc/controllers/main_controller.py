from mvc.models.repositories.note_repository import NoteRepository
class MainController:
    def __init__(self):
        # Create note repository here
        # Your code here
        self.noteRepository = NoteRepository()
        # self.notes.append(NoteRepository.get_all_notes(self))
        return
    
    def get_all_notes(self):
        # Return all notes
        # Your code here
        return self.noteRepository.get_all_notes()

    def add_note(self, note: str):
        # Add note
        # Your code here
        self.noteRepository.add_note(note)
        return

    def clear_all(self):
        # Clear all note
        # Your code here
        self.noteRepository.clear_all_notes()
        return
