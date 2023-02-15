from transformers import pipeline


class Lyrics():
    def __init__(self, len):
        self.len = len

    def from_huggingartists(self):
        generator = pipeline(task='text-generation', model='huggingartists/eminem')
        return generator("", num_return_sequences=self.len)
