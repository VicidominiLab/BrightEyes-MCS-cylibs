from brighteyes_mcs_cylibs.autocorrelator import Autocorrelator
from brighteyes_mcs_cylibs.fastconverter import (
    convertDataFromAnalogFIFO,
    convertRawDataToCountsDirect,
    convertRawDataToCountsDirect49,
)
from brighteyes_mcs_cylibs.timeBinner import timeBinner


def test_extension_imports():
    assert convertRawDataToCountsDirect.__name__ == "convertRawDataToCountsDirect"
    assert convertRawDataToCountsDirect49.__name__ == "convertRawDataToCountsDirect49"
    assert convertDataFromAnalogFIFO.__name__ == "convertDataFromAnalogFIFO"
    assert Autocorrelator.__name__ == "Autocorrelator"
    assert timeBinner.__name__ == "timeBinner"
