class student:
    def __init__(self, name):
        self.name = name
        print("Constructor Call")

s1 = student ("Riya")
print(s1.name)