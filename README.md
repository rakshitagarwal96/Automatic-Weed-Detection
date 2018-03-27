# Automatic-Weed-Detection
Automatic Weed Detection And Smart Herbicide Sprayer Robot.

The ordinary method for murdering weeds in a harvest manor is to shower herbicides all through the estate. This outcomes in defilement of the sustenance crops and furthermore the yield turns out to be less as a portion of the product plants pass on alongside the weeds. In this way there is a requirement for a brilliant weed control framework. In this venture, a picture handling calculation is utilized to take pictures of the manor columns at consistent interims and after recognizing the weeds in the picture, the herbicide is showered specifically and just on the weeds. The herbicide is put away in a compartment fitted with water pump engines joined to shower spouts. Once the weeds are recognized, a flag is sent from Raspberry Pi to the engine driver IC controlling the water draw engines to shower the chemicals over the weeds.

Here are the codes for detection of weed(unwanted plants) through Raspberry Pi using Python and OpenCV.

weed_fn.py --> This is the code for detection of weed(broad green leaf) through image processing.

motor_fn --> This is the code for running motors of the Robot.

sprayer_fn --> This is the code for running Sprayer Pump to spray herbicides on detected Weed.

wms_single --> This is the final code for accessing all the above codes by importing them and make the robot work according to our algorithm.
