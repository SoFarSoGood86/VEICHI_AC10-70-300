from homeassistant.components.switch import SwitchEntity
from .const import REG_RUN_STOP, REG_DIRECTION, DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    hub = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([VeichiRunSwitch(hub), VeichiDirectionSwitch(hub)])

class VeichiRunSwitch(SwitchEntity):
    name = "AC70 Marche"
    def __init__(self, hub): self.hub = hub
    def turn_on(self): self.hub.write(REG_RUN_STOP, 1)
    def turn_off(self): self.hub.write(REG_RUN_STOP, 0)

class VeichiDirectionSwitch(SwitchEntity):
    name = "AC70 Sens Rotation"
    def __init__(self, hub): self.hub = hub
    def turn_on(self): self.hub.write(REG_DIRECTION, 1)
    def turn_off(self): self.hub.write(REG_DIRECTION, 0)
