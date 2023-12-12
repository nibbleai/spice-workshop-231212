from spice import Registry
from spice import config
config.set_credentials("cead0e44-a639-4388-ae35-ca0ba0f468a6", "9ZjF4ADOYdU/uFhSXC8NulVcfzqlpyuiJVBIK/hP")

registry = Registry("NYC taxi")

@registry.register(depends=["pickuptime"])
def pickup_hour(pickuptime):
    return pickuptime.dt.hour

@registry.register(depends=["pickuptime"])
def weekday(pickuptime):
    return pickuptime.dt.day

@registry.register(name="pickuptime")
def pickuptime(data):
    return data['pickup_datetime']