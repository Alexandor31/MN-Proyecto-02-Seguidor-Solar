#----------Método para calcular los ángulos de elevación y azimutal y resolver el sistema que se obtiene al rotar un vector director---------

from pysolar.solar import get_altitude, get_azimuth
import matplotlib.image as mpimg
from datetime import datetime, timedelta
from pytz import timezone
import numpy as np
from BackEndSeguidorSolar import src

def calculate_solar_positions(
    start_date: datetime,
    start_hour: int = 10,
    end_hour: int = 17,
    latitude: float = -0.2105367,
    longitude: float = -78.491614
):
    """Calcula posiciones solares y ángulos para una fecha específica y rango de horas.

    ## Parameters
    - start_date: Fecha y hora de inicio para la simulación (se usa solo la fecha, hora se define con start_hour).
    - start_hour: Hora de inicio del cálculo.
    - end_hour: Hora de fin del cálculo.
    - latitude: Latitud para la posición geográfica.
    - longitude: Longitud para la posición geográfica.

    ## Return
    - times: Lista de tiempos de simulación.
    - azimuths: Lista de ángulos azimutales.
    - elevations: Lista de ángulos de elevación.
    - beta: Lista de ángulos de rollo calculados.
    - phi: Lista de ángulos de inclinación calculados.
    """
    times = []
    azimuths = []
    elevations = []
    beta = []
    phi = []

    time_interval = timedelta(hours=0.33)

    # Crear el rango de tiempos basado en la hora de inicio y fin
    start_time = start_date.replace(hour=start_hour, minute=0, second=0, microsecond=0)
    end_time = start_date.replace(hour=end_hour, minute=0, second=0, microsecond=0)

    current_time = start_time
    while current_time <= end_time:
        az = get_azimuth(latitude, longitude, current_time)
        el = get_altitude(latitude, longitude, current_time)

        # Convertir a radianes para los cálculos
        az_rad = (az * np.pi) / 180
        el_rad = (el * np.pi) / 180

        val = np.cos(el_rad) * np.sin(az_rad)
        beta_rad = np.arcsin(val)
        beta_deg = (beta_rad * 180) / np.pi

        val_fi1 = -(np.cos(el_rad) * np.cos(az_rad)) / np.cos(beta_rad)
        x_rad = np.arcsin(val_fi1)
        x_deg = (x_rad * 180) / np.pi

        times.append(current_time)
        azimuths.append(az)
        elevations.append(el)
        beta.append(beta_deg)
        phi.append(x_deg)  # Asumiendo que phi corresponde a x_deg; ajusta si es necesario

        current_time += time_interval

    return times, azimuths, elevations, beta, phi