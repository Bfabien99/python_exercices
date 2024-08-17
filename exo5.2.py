import random
from datetime import timedelta

def convert_seconds(total_seconds):
    delta = timedelta(seconds=total_seconds)
    
    # Extraction des composants
    years, remaining_days = divmod(delta.days, 365)
    months, days = divmod(remaining_days, 30)
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return years, months, days, hours, minutes, seconds

# Exemple d'utilisation
total_seconds = random.randint(60, 99999999)
years, months, days, hours, minutes, seconds = convert_seconds(total_seconds)

print(f"{total_seconds} secondes équivalent à :")
print(f"{years} années, {months} mois, {days} jours, {hours} heures, {minutes} minutes, et {seconds} secondes.")
