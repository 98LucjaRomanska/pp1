class Phone():
 def __init__(self, name, model, number, volume):
    self.name = name
    self.model = model
    self.number = number
    self.volume = 1
    self.apps = []
    self.is_on = True
 def turn_off(self):
    self.is_on = False
 def turn_off(self):
    self.is_on = True
 def turn_up(self):
    self.volume += 1

 def turn_down(self):
    self.volume -= 1
def download_app(self,app):
    self.apps.append(app)

phone1 = Phone("Iphone", "SE", "66644433", 3)
phone2 = Phone("samsung", "5S","443332243", 6)
print(phone1.apps)
print(f'My phone is Iphone')
phone1.download_app("facebook")

