# band.py
class Band:
    def __init__(self, name, hometown):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(hometown, str) or len(hometown) == 0:
            raise ValueError("Hometown must be a non-empty string.")
        
        self._name = name
        self._hometown = hometown
        self._concerts = []
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    @property
    def hometown(self):
        return self._hometown

    def concerts(self):
        return self._concerts

    def venues(self):
        return list(set(concert.venue for concert in self._concerts))

    def play_in_venue(self, venue, date):
        # Create and return a new concert
        concert = Concert(date, self, venue)
        self._concerts.append(concert)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts]




# venue.py
class Venue:
    def __init__(self, name, city):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(city, str) or len(city) == 0:
            raise ValueError("City must be a non-empty string.")
        
        self._name = name
        self._city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("City must be a non-empty string.")
        self._city = value

    def concerts(self):
        return self._concerts

    def bands(self):
        return list(set(concert.band for concert in self._concerts))

    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None



# concert.py
class Concert:
    all = []

    def __init__(self, date, band, venue):
        if not isinstance(date, str) or len(date) == 0:
            raise ValueError("Date must be a non-empty string.")
        if not isinstance(band, Band):
            raise TypeError("Band must be an instance of Band.")
        if not isinstance(venue, Venue):
            raise TypeError("Venue must be an instance of Venue.")
        
        self._date = date
        self._band = band
        self._venue = venue
        self._band._concerts.append(self)
        self._venue._concerts.append(self)
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Date must be a non-empty string.")
        self._date = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise TypeError("Band must be an instance of Band.")
        self._band = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise TypeError("Venue must be an instance of Venue.")
        self._venue = value

    def hometown_show(self):
        return self._venue.city == self._band.hometown

    def introduction(self):
        return f"Hello {self._venue.city}!!!! We are {self._band.name} and we're from {self._band.hometown}"
