import motor_fn
import weed
import sprayer_fn
import time

for i in range(0,2):
    x = weed.detect_weed(); time.sleep(3)
    y=weed.detect_weed(); time.sleep(3)
    suma=x+y

    if suma>=1:
     sprayer_fn.sprayer_run()
    
    motor_fn.motorrun()
