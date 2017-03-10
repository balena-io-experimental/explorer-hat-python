import time
import explorerhat

# Flash the lights!
while True:
    explorerhat.light.on()
    time.sleep(1)
    explorerhat.light.off()
    time.sleep(1)
