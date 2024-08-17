from pysolar.solar import get_altitude, get_azimuth
from datetime import datetime, timedelta
from pytz import timezone


#-----------------Método para obtener el ángulo azimuth y elevation de la posición del sol-------------------
def getSolarPosition(
    latitude: float = -0.2105367, 
    longitude: float = -78.491614,
    date: datetime = datetime.now(tz=timezone("America/Guayaquil")),
):
    """Calcula el ``azimuth`` y la ``elevation`` para una posición geográfica (por defecto la EPN) y la fecha ``date``.

    ## Parameters

    ## Return
    ``azimuth``: ángulo en grados desde el norte hasta la projección en la tierra [0 -> 360).
    ``elevation``: ángulo del sol hacia la proyección en la tierra [-90 -> 90].

    """

    az = get_azimuth(latitude, longitude, date)
    el = get_altitude(latitude, longitude, date)

    return az, el