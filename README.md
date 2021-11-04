This is a project about simulating a DC motor with Python.

The calculation of the K_feedback matrix is yet to be implemented.

About the files:
	- init_conditions.py specifies the values of the initial contidions of the signals.
	- constants.py specifies the DC motor constant values (J, b, K, R & L).
	- model_DC_motor.py encapsulates the relationship between the input (Voltage) and outputs (Angular speed and current) using differential equations.
	- state_space_model.py contains a State Space model of the DC motor, necessary for regulator calculations.
	- regulator.py contains the control laws. This module calculates the control action.
	- simulation_[whatever].py is the executable file with the simulation and results visualization. 
