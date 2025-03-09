# Global parameters for the system
M = 1       # Mass (kg)
K = 1       # Spring constant (N/m)
x_o = 1     # Initial displacement (m)
v = 1       # Initial velocity (m/s)

class system_response():
    """
    A class to model different damping scenarios in a mass-spring-damper system.
    
    This class calculates damping coefficients and damping ratios for different
    damping cases (undamped, critically damped, overdamped, underdamped) and
    can be extended to calculate system time responses.
    """
    
    def __init__(self, case=None, C_value=None, Z=None, Sys_time_response=None):
        """
        Initialize the system_response object.
        
        Parameters:
        -----------
        case : str
            The damping case to model ('Not Damped', 'Critically Damped', 
            'Over Damped', or 'Underdamped')
        C_value : float, optional
            Damping coefficient. If None, will be calculated based on the case.
        Z : float, optional
            Damping ratio. If None, will be calculated based on the case.
        Sys_time_response : array-like, optional
            System time response data. Can be populated later.
        """
        self.case = case
        self.C_value = C_value  # Damping coefficient
        self.Z = Z              # Damping ratio (zeta)
        self.Sys_time_response = Sys_time_response 

    def declare_case(self, new_case):
        """
        Set or change the damping case and calculate appropriate C and Z values.
        
        Parameters:
        -----------
        new_case : str
            The damping case to model ('Not Damped', 'Critically Damped', 
            'Over Damped', or 'Underdamped')
        """
        self.case = new_case
        print(f"The case declared is {self.case}, running loop to determine C...")

        if self.case == 'Not Damped':
            # No damping (C=0, Z=0)
            self.C_value = 0
            self.Z = 0

        elif self.case == 'Critically Damped':
            # Critical damping (C=2√(KM), Z=1)
            # System returns to equilibrium without oscillation in minimum time
            self.C_value = 2*np.sqrt(K*M)
            self.Z = 1

        elif self.case == 'Over Damped':
            # Over damping (C>2√(KM), Z>1)
            # System returns to equilibrium without oscillation but slower than critical
            self.C_value = 2*np.sqrt(K*M)
            # For overdamped: C > 2*sqrt(K*M)
            while self.C_value <= 2*np.sqrt(K*M):
                self.C_value += 1
            self.Z = self.C_value / (2*np.sqrt(K*M))

        elif self.case == "Underdamped":
            # Under damping (C<2√(KM), Z<1)
            # System oscillates with decreasing amplitude
            self.C_value = 2*np.sqrt(K*M)
            # For underdamped: C < 2*sqrt(K*M)
            while self.C_value >= 2*np.sqrt(K*M):
                self.C_value -= 1
            self.Z = self.C_value / (2*np.sqrt(K*M))



        print(f"C value: {self.C_value}, Damping ratio: {self.Z}")

critically_damp = system_response()
critically_damp.declare_case("Critically Damped")
