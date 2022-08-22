class Point():

    def __init__(self, name, latitude, longitude) -> None:
        self.name = name

        if not(-90 <= latitude <=90) or not (-180 <= longitude <=180):
            raise ValueError ("Invalid latitude, longitude combination")
        self.longitude = longitude
        self.latitude = latitude
    
    def get_lat_long(self):
        return(self.latitude, self.longitude)