> #!/usr/bin/env python3
import pkg_resources
pkg_resources.require("PyYAML==3.13")
import yaml
import base64

WHITE = "\033[37m"
GREEN = "\033[32m"
RED = "\033[31m"
BOLD = "\033[1m"

class Config():
  units = None
  propulsion_temp = None
  solar_array_temp = None
  IR_spectrometer_temp = None
  auto_calibration = None

def create_config():
  print(f"\n{GREEN}- Creating new config -{WHITE}")
  config = Config()
  config.units = input("Temperature units (F/C/K): ")
  config.propulsion_temp = input("Propulsion Components Target Temperature : ")
  config.solar_array_temp = input("Solar Array Target Temperature : ")
  config.IR_spectrometer_temp = input("Infrared Spectrometers Target Temperature : ")
  config.auto_calibration = input("Auto Calibration (ON/OFF) : ")
  return config

def serialize(obj):
  x = base64.b64encode(yaml.dump(obj).encode()).decode()
  print(f"\nSerialized config: {x}\n"
        f"{GREEN}Uploading to ship...{WHITE}\n")

def deserialize(x):
  try:
    obj = yaml.load(base64.b64decode(x))
    print(f"{GREEN}** Success **\n"
          f"Uploading to ship...{WHITE}")
  except Exception:
    print(f"\n{RED}Unable to load config!{WHITE}\n")

def TCS():
  inp = input(
    f"\n{GREEN}{BOLD}"
    "<------[TCS]------>\n"
    f"{WHITE}"
    "[1] Create config\n" 
    "[2] Load config\n"
    "[3] Exit\n"
    "> ")
  if inp == "1":
    serialize(create_config())
  elif inp == "2":
    x = input("\nSerialized config to load: ").encode()
    deserialize(x)
  else:
    print(f"\n{RED}Exiting...\n")
    exit()

if __name__ == "__main__":
  while 1: TCS()
