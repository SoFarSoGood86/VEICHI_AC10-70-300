from .const import DOMAIN
from .hub import VeichiHub

PLATFORMS = ["sensor", "switch", "number"]

async def async_setup_entry(hass, entry):
    hub = VeichiHub(entry.data["host"], entry.data["port"], entry.data["slave"])
    hub.connect()
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = hub
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True
