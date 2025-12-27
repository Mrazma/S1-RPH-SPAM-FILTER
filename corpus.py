import os

class Corpus:
    def __init__(self,path: str):
        self.path = path

    def emails(self):
        for fname in os.listdir(self.path):
            if fname.startswith('!'):
                continue

            full_path = os.path.join(self.path,fname)

            with open(full_path,"rt",encoding="utf-8") as file:
                yield fname, file.read()

    def emails_paths(self):
        for fname in os.listdir(self.path):
            if fname.startswith('!'):
                continue

            yield os.path.join(self.path,fname), fname