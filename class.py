# Base Class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        return f"The {self.brand} {self.model} is now ON."

    def power_off(self):
        return f"The {self.brand} {self.model} is now OFF."


# Derived Class: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model) 
        self.storage = storage 
        self.camera_megapixels = camera_megapixels  # Camera resolution

    def take_photo(self):
        return f"Taking a photo with the {self.camera_megapixels}MP camera."

    def install_app(self, app_name):
        return f"Installing {app_name} on your {self.brand} {self.model}."

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.camera_megapixels}MP camera."


# Using the Classes
my_phone = Smartphone("Apple", "iPhone 14", 128, 48)

print(my_phone)  
print(my_phone.power_on())
print(my_phone.take_photo())
print(my_phone.install_app("Instagram"))
