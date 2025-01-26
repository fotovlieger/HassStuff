import datetime
def todayAt (hr, min=0, sec=0, micros=0):
    now = datetime.datetime.now()
    return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)    

@state_trigger("binary_sensor.motion1_occupancy", state_hold=0, state_check_now=True)
def door_motion():
    strip1 = "light.door_led_strip"
    strip2 = "light.cv_led_strip"
    if binary_sensor.motion1_occupancy == 'on':
        now = datetime.datetime.now()
        if now>todayAt(7) and now<todayAt(23):
        # Day
            light.turn_on(entity_id=strip1, rgb_color=[255,190, 110], brightness=255)
            light.turn_on(entity_id=strip2, rgb_color=[255,190, 110], brightness=255)
        else:
          # Night
            light.turn_on(entity_id=strip1, rgb_color=[255,190, 110], brightness=160)
            light.turn_on(entity_id=strip2, rgb_color=[255,190, 110], brightness=160)
    else:
        light.turn_off(entity_id=strip1)
        light.turn_off(entity_id=strip2)

log.info("doormotion")
