from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN, DEFAULT_PORT, DEFAULT_SLAVE

class VeichiConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="VEICHI AC70", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("host", default="192.168.1.254"): str,
                vol.Required("port", default=DEFAULT_PORT): int,
                vol.Required("slave", default=DEFAULT_SLAVE): int,
            })
        )
