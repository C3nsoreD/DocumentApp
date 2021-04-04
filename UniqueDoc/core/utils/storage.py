from django.core.files.storage import FileSystemStorage

from ..models import Document

class CustomStorage(FileSystemStorage):
    def __init__(self):
        super.__init__()
        # self.file_obj = file_obj

        # self._fs = FileSystemStorage()
        pass
        
    def get_meta_data(self):
        file_meta = {}
        file_meta['name'] = self.file_obj.name
        file_meta['content_type'] = self.file_obj.context_type
        file_meta['size'] = self.file_obj.size
        return file_meta

    def _populate_model(self):
        pass

    def check_duplicates(self):
        pass
