## The Effects of Nuclear Weapons Calculator 

Calculations are based on the equations and plots in the book The Effects of Nuclear Weapons. PDF version of the book can be found from 
[https://www.fourmilab.ch/etexts/www/effects/](https://www.fourmilab.ch/etexts/www/effects/), and the digital version of the slide rule accompaning the book can be found from [https://www.fourmilab.ch/bombcalc/](https://www.fourmilab.ch/bombcalc/). 

The aim of this project is to calculate all of the properties that are available in the slide rule. Currently, only some of these calculations are available. At the moment, calculations are available only in US customary units (feet, psi, etc) as in the original slide rule. 

The file `calc_pressures.py` can be run to calculate maximum overpressure (psi), maximum dynamic pressure (psi), and maximum velocity (ft/s) of both surface burst and burst at optimal burst height after giving distance (ft) and yield (kt) of burst as inputs. 

Runnig the file `calc_time.py` calculates positive phase duration (s) on the ground of overpressure, and arrival time (s) on the ground of blast wave using distance (ft), height (ft) and yield (kt) of burst as inputs. 

The folder `Data sources` includes all the data points collected from the pictures of the book (.txt files), and all the codes used to fit curves based on these data points (.py files). These fitted curves are then used when calculating pressures and times with files `calc_pressures.py` and `calc_time.py`. 

