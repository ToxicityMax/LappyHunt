from django.db import models


class LaptopSpec(models.Model):
    Model = models.CharField(max_length=70)

    # Physical info
    Weight = models.DecimalField(max_digits=5, decimal_places=3)  # In grams
    Dimensions = models.CharField(max_length=20)
    ScreenSize = models.DecimalField(max_digits=4, decimal_places=2)
    ScreenResolution = models.CharField(max_length=10)
    MaxResolution = models.CharField(max_length=10)
    DisplayType = models.BooleanField(
        default=True
    )  # true if LED-backlight ...... false TFTLCD
    Color = models.CharField(max_length=10)
    Speaker = models.CharField(max_length=30, blank=True)
    Wifi = models.BooleanField(default=True)
    Bluetooth = models.DecimalField(
        default=5, max_digits=3, decimal_places=1
    )  # Bluetooth-V(integerValue)
    Infrared = models.BooleanField(default=False)
    AudioType = models.CharField(max_length=30)
    KeyboardBacklit = models.BooleanField(default=True)
    OpticalDriveType = models.BooleanField(default=False)
    CardReader = models.BooleanField(default=True)

    # PORTS
    PortsUsb2 = models.PositiveIntegerField()
    PortsUsb3 = models.PositiveIntegerField()
    PortsHdmi = models.PositiveIntegerField()
    PortsAudio = models.PositiveIntegerField()
    PortsEthernet = models.PositiveIntegerField()
    PortsMicrophone = models.PositiveIntegerField()
    PortsVga = models.PositiveIntegerField()
    PortsCtype = models.PositiveIntegerField()

    # RAM Hard drive and SSD info
    Ram = models.PositiveIntegerField()  # In Gb
    RamTechnology = models.CharField(max_length=5)
    ExtraRam = models.PositiveIntegerField()  # In Gb
    HddSize = models.PositiveIntegerField()  # In Gb
    SsdSize = models.PositiveIntegerField()  # In Gb

    # Battery
    Battery = models.PositiveIntegerField()
    BatteryAvgLife = models.PositiveIntegerField()
    BatteryAvgLifeStandby = models.PositiveIntegerField(blank=True)
    PowerSource = models.CharField(default="Battery Powered", max_length=30, blank=True)

    Os = models.CharField(max_length=20)
    INTEL = "Intel"
    AMD = "Amd"
    ProcCompanies = [
        (INTEL, "Intel"),
        (AMD, "Amd"),
    ]
    ProcessorName = models.CharField(max_length=5, choices=ProcCompanies)
    ProcessorSpeed = models.DecimalField(max_digits=3, decimal_places=2)  # In ghz
    ProcessorType = models.CharField(max_length=20)
    GraphicsCard = models.BooleanField(
        default=True
    )  # True if Integrated .... false if Dedicated
    Graphics = models.CharField(max_length=25)
    GraphicRamSize = models.PositiveIntegerField()
    IncludedComponents = models.TextField()
    SoftwareIncluded = models.TextField()
    DataLinkProtocol = models.CharField(default="IEEE 802.11 a/b/g/n/ac", max_length=20)

