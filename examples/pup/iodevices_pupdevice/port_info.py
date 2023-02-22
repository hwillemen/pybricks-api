from pybricks.iodevices import PUPDevice
from pybricks.parameters import Port
from uerrno import ENODEV

# Dictionary of device identifiers along with their name.
# Also check https://github.com/pybricks/technical-info/blob/master/assigned-numbers.md#io-device-type-ids
# for retired/internal
device_names = {
    1: "Wedo 2.0 Medium Motor", #DCMotor, analog ID
    2: "PUP Train Motor",       #DCMotor, analog ID
    8: "PUP Light",             #Light, analog ID
    34: "Wedo 2.0 Tilt Sensor",
    35: "Wedo 2.0 Infrared Sensor", # aka WeDo 2.0 Motion Sensor
    37: "BOOST Color Distance Sensor",
    38: "BOOST Interactive Motor",
    46: "Technic Large Motor",
    47: "Technic Extra Large Motor",
    48: "SPIKE Medium Angular Motor",
    49: "SPIKE Large Angular Motor",
    61: "SPIKE Color Sensor",
    62: "SPIKE Ultrasonic Sensor",
    63: "SPIKE Force Sensor",
	64: "SPIKE 3x3 Color Light Matrix",
	65: "SPIKE Small Angular Motor",
    75: "Technic Medium Angular Motor",
    76: "Technic Large Angular Motor",
}

# Make a list of known ports.
ports = [Port.A, Port.B]

# On hubs that support it, add more ports.
try:
    ports.append(Port.C)
    ports.append(Port.D)
except AttributeError:
    pass

# On hubs that support it, add more ports.
try:
    ports.append(Port.E)
    ports.append(Port.F)
except AttributeError:
    pass

# Go through all available ports.
for port in ports:

    # Try to get the device, if it is attached.
    try:
        device = PUPDevice(port)
    except OSError as ex:
        if ex.args[0] == ENODEV:
            # No device found on this port.
            print(port, ": ---")
            continue
        else:
            raise

    # Get the device id
    id = device.info()["id"]

    # Look up the name.
    try:
        print(port, ":", device_names[id])
    except KeyError:
        print(port, ":", "Unknown device with ID", id)
