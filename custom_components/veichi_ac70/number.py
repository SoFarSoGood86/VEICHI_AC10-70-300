from homeassistant.components.number import NumberEntity
from .const import REG_FREQ_SET, DEFAULT_MAX_FREQ, DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    hub = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([VeichiFrequency(hub)])

class VeichiFrequency(NumberEntity):
    name = "AC70 Fréquence"
    native_min_value = 0
    native_max_value = DEFAULT_MAX_FREQ
    native_step = 0.1
    unit_of_measurement = "Hz"

    def __init__(self, hub): self.hub = hub
    def set_native_value(self, value): self.hub.write(REG_FREQ_SET, int(value * 100))
