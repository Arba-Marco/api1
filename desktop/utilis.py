import requests

def get_people_in_space():

    url = "http://api.open-notify.org/astros.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["message"] == "success":
            return data["people"]  # Restituisce un elenco di persone nello spazio
        else:
            return []
    except requests.RequestException as e:
        print(f"Errore nel recupero dei dati dall'API: {e}")
        return []
