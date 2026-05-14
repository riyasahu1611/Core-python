class Doctor:
    def __init__(self, ent, nephrologist, orthopedic):
        self.ent = ent
        self.nephrologist = nephrologist
        self.orthopedic = orthopedic

    def set_ent(self, E):
        self.ent = E

    def get_ent(self):
        return self.ent

    def set_nephrologist(self, N):
        self.nephrologist = N

    def get_nephrologist(self):
        return self.nephrologist

    def set_orthopedic(self, orthopedic):
        self.orthopedic = O

    def get_orthopedic(self):
        return self.orthopedic

D = Doctor("Specialization in ear,nose and throat","Specialization in Kidney","Specialization in Bones")
print("Ent Doctor:",D.get_ent())
print("Nephrologist Doctor:",D.get_nephrologist())
print("Orthopedic Doctor:",D.get_orthopedic())


