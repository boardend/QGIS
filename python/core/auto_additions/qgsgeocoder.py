# The following has been generated automatically from src/core/geocoding/qgsgeocoder.h
# monkey patching scoped based enum
QgsGeocoderInterface.Flag.GeocodesStrings.__doc__ = "Can geocode string input values"
QgsGeocoderInterface.Flag.GeocodesFeatures.__doc__ = "Can geocode QgsFeature input values"
QgsGeocoderInterface.Flag.__doc__ = """Capability flags for the geocoder.

* ``GeocodesStrings``: Can geocode string input values
* ``GeocodesFeatures``: Can geocode QgsFeature input values

"""
# --
try:
    QgsGeocoderInterface.__virtual_methods__ = ['geocodeFeature', 'appendedFields', 'wkbType', 'geocodeString']
    QgsGeocoderInterface.__abstract_methods__ = ['flags']
    QgsGeocoderInterface.__group__ = ['geocoding']
except (NameError, AttributeError):
    pass
