
#******************************************************************************************************************#

# 6-MVC.py

#******************************************************************************************************************#

# 2021-01-04 06:14:01

# This is the code used in '5-MVC-Model_View_Controller'

# This is the model compoenent - Device
# This stores the data.
class Device:
    
    ipaddress = ""
    port = ""
    
    # Thsi will fill up the list (devices) of Device objects
    @staticmethod
    def finddevices():
        devices = []
        
        d = Device()
        d.ipaddress = "192.168.1.1"
        d.port = "2001"
        
        devices.append(d)
        
        d = Device()
        d.ipaddress = "192.168.1.50"
        d.port = "7091"
        
        devices.append(d)
        
        d = Device()
        d.ipaddress = "192.168.1.100"
        d.port = "80"
        
        devices.append(d)
        
        return devices
    

# This will display the devices in the list
# This doesnt care how many devices are in the list. It will just iterate thru the list.
class DevicesView:

    def showdevices(self, devices):
        for d in devices:
            print("------------------------------")
            print("IP Address: " + d.ipaddress)
            print("Port: " + str(d.port))
            print("------------------------------")


class DevicesController:
    
    def __init__(self):
        
        # Calls finddevices to populate the devices list.
        # It then creates a new instance of the view
        devices = Device.finddevices()
        
        v = DevicesView()
        v.showdevices(devices)
        

# Creating an instance of the controller
c = DevicesController()