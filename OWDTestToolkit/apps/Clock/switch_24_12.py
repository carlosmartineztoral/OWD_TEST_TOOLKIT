from OWDTestToolkit.global_imports import *
	
class main(GaiaTestCase):

    def switch_24_12(self, p_hour):
        #
        # Returns array "hour" (12 hour format) and "ampm" based on a 24hour "p_hour".
        #
        if p_hour >= 12:
            t_ampm = "PM"
            if p_hour > 12:
                t_hour = p_hour - 12
            else:
                t_hour = p_hour
        else:
            t_hour = p_hour
            t_ampm = "AM"
        
        return (t_hour, t_ampm)
        
