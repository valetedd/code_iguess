class ZodiacSign(object):
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def describe(self):
        print(f"{self.name} is a {self.element} sign")
    
    #better version:
    def __str__(self):
        return f"{self.name} is a {self.element} sign"
    
    def is_compatible_with(self, other_sign):
        comp_dict = {
            "Air" : "Fire",
            "Fire" : "Air",
            "Earth" : "Water",
            "Water" : "Earth"
        }
        return other_sign.element == comp_dict[self.element] or other_sign.element == self.element

class ZodiacCircle(ZodiacSign):
    def __init__(self):
        self.signs = list()

    def add_sign(self, zodiac_sign):
        if zodiac_sign not in self.signs:
            self.signs.append(zodiac_sign)

    def find_sign(self, name):
        for obj in self.signs:
            if obj.name == name:
                return obj
            
    def check_compatibility(self, sign_name1, sign_name2):
        obj_1 = self.find_sign(sign_name1)
        obj_2 = self.find_sign(sign_name2)
        return obj_1.is_compatible_with(obj_2)




