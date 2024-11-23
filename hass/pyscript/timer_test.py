@time_trigger('period(now, 300s)')
def periodic_test_function():
    auto = input_boolean.airco_controller_on == 'on'
    roomTemperature = float(state.get('sensor.0x842712fffe55c005_temperature'))
    mode = climate.midea_climate
    log.info(f"before: auto={auto}, temp={roomTemperature} mode={mode}")
    if auto:
        if mode == 'heat':
            if roomTemperature > 16.5:
                climate.midea_climate.set_hvac_mode('off')
                log.info("heat off")
        else:
            if roomTemperature < 14.5:
                climate.midea_climate.set_hvac_mode('heat')
                log.info("heat on")

    mode = climate.midea_climate
    log.info(f"after: auto={auto}, temp={roomTemperature} mode={mode}")
