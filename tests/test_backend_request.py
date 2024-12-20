import requests

def test_getBackendResponse():
    try:
        response = requests.get("http://localhost:3000/tasks")
                
    # except requests.exceptions.RequestException as e:
    #     assert False, f"Erreur de connexion au backend : {str(e)}"