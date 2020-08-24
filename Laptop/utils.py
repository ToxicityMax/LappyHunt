import random
import string
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
    

def upload():
    import csv

    with open("Laptop/laptop.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        fieldNames = []
        # ['knk_name', 'Brand', 'Model', 'Model Name', 'Item Weight', 'Product Dimensions', 'Batteries:', 'Item model number', 'RAM Size', 'Memory Storage Capacity', 'Flash Memory Installed Size', 'Ram Memory Installed Size', 'Ram Memory Technology', 'Hard Drive Size', 'Hard Disk Technology', 'Operating System', 'Processor Brand', 'Processor Speed', 'Processor Type', 'Graphics Card Description', 'Graphics Coprocessor', 'Included Components', 'Screen Size', 'Display Type', 'Display Resolution Maximum', 'Batteries
        #     Included', 'Batteries Required', 'Battery Cell Composition', 'Connector Type', '\xa0', 'Series', 'Colour', 'Item Height', 'Item Width', 'Maximum Display Resolution', 'Memory Technology', 'Speaker Description', 'Graphics Chipset Brand', 'Connectivity Type', 'Number of USB 2.0 Ports', 'Number of USB 3.0 Ports', 'Number of HDMI Ports', 'Number of Audio-out Ports', 'Number of Ethernet Ports', 'Number of Microphone Ports', 'Number of VGA Ports', 'Lithium Battery Energy Content', 'Number of Lithium Ion Cells', 'Supported Software', 'Optical Drive Type', 'Hard Disk Rotational Speed', 'Lithium battery Weight', 'Number of Lithium Metal
        #     Cells', 'Resolution', 'Power Source', 'Battery Average Life', 'Battery Average Life Standby', 'Wireless Type', 'Data Link Proto 'Form Factor', 'Maximum Memory Supported', 'Card Reader', 'Hardware Platform', 'Model Year', 'Graphics Card Ram Size', 'Audio
        #     Output Type', 'Keyboard Description', 'Notebook Display Technology', 'Screen Resolution', 'Computer Memory Type']
        # obj_list = []
        for row in csv_reader:
            if line_count == 0:
                for item in row:
                    fieldNames.append(item)
                line_count += 1
            else:
                col_num = 0
                obj_map = {}
                for item in row:
                    obj_map[fieldNames[col_num]] = item
                    col_num = col_num + 1
                # obj_list.append(obj_map)
                #
                a = LaptopSpec()
                line_count += 1
                a.Weight = obj_map["Item Weight"]
                a.Dimensions = obj_map["Product Dimensions"]  # "Product Dimensions"
                a.ScreenSize = obj_map["Screen Size"]
                # ScreenResolution
                if obj_map["Display Resolution Maximum"] != "":
                    a.ScreenResolution = obj_map["Display Resolution Maximum"]
                elif obj_map["Maximum Display Resolution"] != "":
                    a.ScreenResolution = obj_map["Maximum Display Resolution"]
                elif obj_map["Resolution"] != "":
                    a.ScreenResolution = obj_map["Resolution"]
                else:
                    a.ScreenResolution = obj_map["Screen Resolution"]

                # MaxResolution = .CharField(max_length=10)
                # DisplayType = models.BooleanField(
                #     default=True
                # )  # true if LED-backlight ...... false TFTLCD

                a.DisplayName = obj_map["knk_name"]
                a.Color = obj_map["Colour"]

                a.Speaker = obj_map["Speaker Description"]
                # Wifi = models.BooleanField(default=True) #delete
                # Bluetooth = models.DecimalField(  #delete
                # default=5, max_digits=3, decimal_places=1
                # )  # Bluetooth-V(integerValue)
                # Infrared = models.BooleanField(default=False)
                # AudioType = models.CharField(max_length=30)
                # KeyboardBacklit = models.BooleanField(default=True)
                # OpticalDriveType = models.BooleanField(default=False)
                # CardReader = models.BooleanField(default=True)

                # PORTS
                a.PortsUsb2 = obj_map["Number of USB 2.0 Ports"]
                a.PortsUsb3 = obj_map["Number of USB 3.0 Ports"]
                a.PortsHdmi = obj_map["Number of HDMI Ports"]

                a.PortsAudio = obj_map["Number of Audio-out Ports"]

                a.PortsEthernet = obj_map["Number of Ethernet Ports"]
                a.PortsMicrophone = obj_map["Number of Microphone Ports"]

                a.PortsVga = obj_map["Number of VGA Ports"]
                # PortsCtype = Sample data needed

                # RAM Hard drive and SSD info
                # In Gb
                if obj_map["RAM Size"] != "":
                    a.Ram = obj_map["RAM Size"]
                elif obj_map["Ram Memory Installed Size"] != "":
                    a.Ram = obj_map["Ram Memory Installed Size"]
                a.RamTechnology = obj_map["Hard Disk Technology"]
                # ExtraRam = models.PositiveIntegerField()  # In Gb no need ig
                a.HardDrive = obj_map["Hard Drive Size"]  # In Gb
                a.HardDriveType = obj_map["Hard Disk Technology"]

                # Battery
                a.Battery = obj_map["Lithium Battery Energy Content"]
                # BatteryAvgLife = models.PositiveIntegerField()
                # BatteryAvgLifeStandby = models.PositiveIntegerField(blank=True)
                # PowerSource = models.CharField(default="Battery Powered", max_length=30, blank=True)

                a.Os = obj_map["Operating System"]

                # INTEL = "Intel"
                # AMD = "Amd"
                # ProcCompanies = [
                #     (INTEL, "Intel"),
                #     (AMD, "Amd"),
                # ]
                a.ProcessorName = obj_map["Processor Brand"]
                a.ProcessorSpeed = obj_map["Processor Speed"]
                a.ProcessorType = obj_map["Processor Type"]  # In ghz
                # True if Integrated .... false if Dedicated
                a.Graphics = (
                    obj_map["Graphics Card Description"]
                    + obj_map["Graphics Coprocessor"]
                    + obj_map["Graphics Card Ram Size"]
                )
                # DataLinkProtocol = models.CharField(default="IEEE 802.11 a/b/g/n/ac", max_length=20)
                a.save()
                print(f"Processed {line_count} lines.")
