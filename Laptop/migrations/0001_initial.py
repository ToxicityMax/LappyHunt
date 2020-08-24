# Generated by Django 3.0.9 on 2020-08-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaptopSpecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model', models.CharField(max_length=70)),
                ('Weight', models.DecimalField(decimal_places=3, max_digits=5)),
                ('Dimensions', models.CharField(max_length=20)),
                ('ScreenSize', models.DecimalField(decimal_places=2, max_digits=4)),
                ('ScreenResolution', models.CharField(max_length=10)),
                ('MaxResolution', models.CharField(max_length=10)),
                ('DisplayType', models.BooleanField(default=True)),
                ('Color', models.CharField(max_length=10)),
                ('Speaker', models.CharField(blank=True, max_length=30)),
                ('Wifi', models.BooleanField(default=True)),
                ('Bluetooth', models.DecimalField(decimal_places=1, default=5, max_digits=3)),
                ('Infrared', models.BooleanField(default=False)),
                ('AudioType', models.CharField(max_length=30)),
                ('KeyboardBacklit', models.BooleanField(default=True)),
                ('OpticalDriveType', models.BooleanField(default=False)),
                ('CardReader', models.BooleanField(default=True)),
                ('PortsUsb2', models.PositiveIntegerField()),
                ('PortsUsb3', models.PositiveIntegerField()),
                ('PortsHdmi', models.PositiveIntegerField()),
                ('PortsAudio', models.PositiveIntegerField()),
                ('PortsEthernet', models.PositiveIntegerField()),
                ('PortsMicrophone', models.PositiveIntegerField()),
                ('PortsVga', models.PositiveIntegerField()),
                ('PortsCtype', models.PositiveIntegerField()),
                ('Ram', models.PositiveIntegerField()),
                ('RamTechnology', models.CharField(max_length=5)),
                ('ExtraRam', models.PositiveIntegerField()),
                ('HddSize', models.PositiveIntegerField()),
                ('SsdSize', models.PositiveIntegerField()),
                ('Battery', models.PositiveIntegerField()),
                ('BatteryAvgLife', models.PositiveIntegerField()),
                ('BatteryAvgLifeStandby', models.PositiveIntegerField(blank=True)),
                ('PowerSource', models.CharField(blank=True, default='Battery Powered', max_length=30)),
                ('Os', models.CharField(max_length=20)),
                ('ProcessorName', models.CharField(choices=[('Intel', 'Intel'), ('Amd', 'Amd')], max_length=5)),
                ('ProcessorSpeed', models.DecimalField(decimal_places=2, max_digits=3)),
                ('ProcessorType', models.CharField(max_length=20)),
                ('GraphicsCard', models.BooleanField(default=True)),
                ('Graphics', models.CharField(max_length=25)),
                ('GraphicRamSize', models.PositiveIntegerField()),
                ('IncludedComponents', models.TextField()),
                ('SoftwareIncluded', models.TextField()),
                ('DataLinkProtocol', models.CharField(default='IEEE 802.11 a/b/g/n/ac', max_length=20)),
            ],
        ),
    ]