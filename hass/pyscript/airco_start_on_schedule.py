#import asyncio
#NOTE: delays are needed, airco does not accept quit succession of commands...
#NOTE: start_check_now does trigger function at restart !?!?

FanMode = 'high'
SwingMode = 'horizontal'
Temperature = 23

@state_trigger("schedule.heating_schedule", state_hold=5, state_check_now=True)
def airco_state_monitor():
    if schedule.heating_schedule == 'On':
        climate.midea_climate.set_hvac_mode('heat')
        task.sleep(6)
        climate.midea_climate.set_swing_mode(SwingMode)
        task.sleep(4)
        climate.midea_climate.set_fan_mode(FanMode)
        task.sleep(4)
        climate.midea_climate.set_temperature(temperature=Temperature)
        task.sleep(4)
        log.info(f"airco: {climate.midea_climate.temperature}, {climate.midea_climate.swing_mode}, {climate.midea_climate.fan_mode}")
