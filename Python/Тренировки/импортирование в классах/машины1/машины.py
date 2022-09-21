from electric_car import Electricalcar
from car import Car

waitan = Electricalcar('УРАЛ', 'К-110', 1976)
Kpaz = Car('КРАЗ', 'У-800', 1966)
print(Kpaz.description_name())
Kpaz.update_odometer(124)
Kpaz.read_odometer()
print(waitan.description_name())
waitan.battery.description_battery()
waitan.battery.discharge(100)
waitan.battery.rangee()
waitan.battery.zaridka()
waitan.battery.upgrade_battery()

