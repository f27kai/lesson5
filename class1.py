class Hello:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hello World {self.name}"

class Hi(Hello):
    pass

hel = Hello("Asan")
print(hel)