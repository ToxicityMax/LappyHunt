from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
import csv

class Company(models.Model):
    cname = models.CharField(max_length=25)
    def __str__(self):
        return self.cname


class LaptopSpec(models.Model):
    Company = models.ForeignKey(Company,on_delete=models.CASCADE)
    # slug = models.SlugField(max_length=250, null=True, blank=True)
    Model = models.CharField(max_length=255)
    DisplayName = models.CharField(max_length=256,null=True, blank=True,default="testing")
    #Image = models.ImageField(upload_to="LapImages/", blank=True)
    # Physical info
    Weight = models.CharField(max_length=5)  # "Item Weight"
    Dimensions = models.CharField(max_length=20)  # "Product Dimensions"
    ScreenSize = models.CharField(max_length=4)  #
    ScreenResolution = models.CharField(max_length=10)
    MaxResolution = models.CharField(max_length=10)
    DisplayType = models.BooleanField(
        default=True
    )  # true if LED-backlight ...... false TFTLCD
    Color = models.CharField(max_length=10)
    Speaker = models.CharField(max_length=30, blank=True)
    # Wifi = models.BooleanField(default=True)
    # Bluetooth = models.DecimalField(
    #     default=5, max_digits=3, decimal_places=1
    # )  # Bluetooth-V(integerValue)
    # Infrared = models.BooleanField(default=False)
    # AudioType = models.CharField(max_length=30)
    # KeyboardBacklit = models.BooleanField(default=True)
    # OpticalDriveType = models.BooleanField(default=False)
    # CardReader = models.BooleanField(default=True)

    # PORTS
    PortsUsb2 = models.CharField(max_length=2)
    PortsUsb3 = models.CharField(max_length=2)
    PortsHdmi = models.CharField(max_length=2)
    PortsAudio = models.CharField(max_length=2)
    PortsEthernet = models.CharField(max_length=2)
    PortsMicrophone = models.CharField(max_length=2)
    PortsVga = models.CharField(max_length=2)
    # PortsCtype = models.PositiveIntegerField()     have to loook up for column type

    # RAM Hard drive and SSD info
    Ram = models.CharField(max_length=6)  # In Gb
    RamTechnology = models.CharField(max_length=8)
    # ExtraRam = models.PositiveIntegerField()  # In Gb
    HardDrive = models.CharField(max_length=10, default="512", blank=True)  # In Gb
    HardDriveType = models.CharField(max_length=12, default=None)  # In Gb

    # Battery
    Battery = models.CharField(max_length=15)
    # BatteryAvgLife = models.PositiveIntegerField()
    # BatteryAvgLifeStandby = models.PositiveIntegerField(blank=True)
    # PowerSource = models.CharField(default="Battery Powered", max_length=30, blank=True)

    Os = models.CharField(max_length=20)
    # INTEL = "Intel"
    # AMD = "Amd"
    # ProcCompanies = [
    #     (INTEL, "Intel"),
    #     (AMD, "Amd"),
    # ]
    ProcessorName = models.CharField(max_length=5)
    ProcessorSpeed = models.CharField(max_length=8)  # In ghz
    ProcessorType = models.CharField(max_length=20)
    # GraphicsCard = models.BooleanField(
    #     default=True
    # )  # True if Integrated .... false if Dedicated
    Graphics = models.CharField(max_length=25)

    IncludedComponents = models.TextField()
    SoftwareIncluded = models.TextField()
    DataLinkProtocol = models.CharField(default="IEEE 802.11 a/b/g/n/ac", max_length=20)
    # URL
    # url = models.CharField(max_length=40)
    # file = laptop.csv
    def __str__(self):
        return self.DisplayName


# def rl_pre_save_receiver(sender, instance, *args, **kwargs):
#    if not instance.slug:
#        instance.slug = unique_slug_generator(instance)
#
#
# pre_save.connect(rl_pre_save_receiver, sender=Post)
