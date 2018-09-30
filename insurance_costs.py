
def _cost_per_mph(mph,seconds):
    if(mph <= 30):
        return 0
    elif(mph <=60):
        return float((.1/60)*seconds)
    elif(mph<=80):
        return float((.2/60)*seconds)
    else:
        return float((.6/60)*seconds)

def _cost_per_mile(mph,seconds):
    # $1 per mile
    return float(1.0*mph/3600)

def _cost_per_road_type(roadType,mph,seconds):
    #convert to miles per second
    return road_type_rate(roadType)* float(mph/3600*seconds)


def road_type_rate(roadType):
    """Cost per mile
    0 : Freeway
    1 : Ramp
    2 : Primary Street
    3 : Major Highway
    4 : Minor Highway
    """
    if(roadType == 0):
        return 0.2
    elif(roadType == 1):
        return 0.05
    elif(roadType == 2):
        return 0.01
    elif(roadType == 3):
        return 0.5
    else:
        return 0.3