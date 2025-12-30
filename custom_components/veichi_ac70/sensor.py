from homeassistant.components.sensor import SensorEntity
from .const import *

async def async_setup_entry(hass, entry, async_add_entities):
    hub = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        VeichiSensor(hub, "Fréquence réelle", REG_FREQ_ACTUAL, 0.01, "Hz"),
        VeichiSensor(hub, "Courant moteur", REG_CURRENT, 0.1, "A"),
        VeichiSensor(hub, "Puissance moteur", REG_POWER, 0.1, "kW"),
        VeichiSensor(hub, "Température variateur", REG_TEMPERATURE, 1, "°C"),
    ])

class VeichiSensor(SensorEntity):
    def __init__(self, hub, name, register, scale, unit):
        self.hub = hub
        self._attr_name = f"AC70 {name}"
        self.register = register
        self.scale = scale
        self._attr_native_unit_of_measurement = unit

    def update(self):
        val = self.hub.read(self.register)
        if val is not None:
            self._attr_native_value = val * self.scale
