# EstimateImpulse
Used to Estimate the Delta-V, burn time, and Impulse requirements for a given engine characteristic, start mass, TWR.

Impulse.py is dependent on several functions, especially the FCEA.exe program, included in this package. FCEA is NASA's CEA program converted to a handy executable. When run, the executable returns an output file, containing a lot of useful information. Documentation on NASA's CEA program may be found here: https://www.grc.nasa.gov/WWW/CEAWeb/ceaWhat.htm

The next important function is the "engine" class. The engine class creates allows the CEAPython.py file to create the CEA's input file from given engine characteristics. Currently, only one fuel and oxidizer may be added, but I will work on adding more in the future. The engine class is set up as such: AresEngine = engine('300','psi','27.2','CH4','O2(L)','2.0','298','90.17') The definition of the engine class may be found in CEAFunctions.py, located in the CEA/ceaexec folder. As noticed, the inputs to the engine class are strings, since they get written to a text file (ceapy.inp, also located in CEA/ceaexec).

If the file is not running, check the ceapy.out file to make sure any conditions are not incorrect, for example, O2(L) is only defined at 90.17K, and the program will throw an error if the ceapy.out file is not complete. 

The Delta-V calculations come from an orbital mechanics approximation, combined with 1m/s for every 1km for a drag approximation and 0.5m/s for every 1 km for gravity compensation. 

# This program is not 100% accurate!
This program is to be used to provide a starting approximation for the impulse a rocket needs to hit to obtain an altitude (not an orbit!). The bottom of this program includes a spot for starting mass (fully fueled) to be entered. This is where the rocket obtains it's impulse. If this value is unknown, set this value equal to 1, and focus on the burntime required as your starting value. Use tools like OpenRocket to determine final and starting masses of your rocket. If the final mass is known, use the mass ratio given (MR in the  program = EmptyMass/FullMass) to determine the estimated Full Mass requirement for your rocket. A suitable motor, or liquid engine, in this case, may be determined.
