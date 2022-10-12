from datetime import date
from house_info import HouseInfo

class TemperatureData(HouseInfo):
    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(int(rec, base=10))
        return recs

    def get_data_by_area(self, rec_area=0):
        field = 'temperature'
        recs = super().get_data_by_area(field, rec_area)
        return recs

    def get_data_by_date(self, rec_date=date.today()):
        field = 'temperature'
        recs = super().get_data_by_date(field, rec_date)
        return self._convert_data(recs)