class SaveText:
    def __init__(self):
        pass

    def save(self, filename, content):
        with open(f"{filename}.txt", "w") as file:
            file.write(content)
