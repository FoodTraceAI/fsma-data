import os
import requests
import colorama as clr

clr.init(autoreset=True)

BASE_URL = os.getenv("LOCAL_URL")


def receive(accessToken: str):
    headers = {
        "Authorization": f"Bearer {accessToken}",
        "Content-Type": "application/json",
    }
    res = requests.get(url=BASE_URL + "/cte/receive/findAll", headers=headers)

    print(f"Found {len(res.json())} CTEs")
    if len(res.json()):
        print("Deleting...")

    for cte in res.json():
        try:
            deleted = requests.delete(
                url=f"{BASE_URL}/cte/receive/{cte['id']}", headers=headers
            )
            deleted.raise_for_status()
            print(f"{clr.Fore.GREEN}Successfully deleted CTE with ID: {cte['id']}")
        except Exception as ex:
            print(f"{clr.Fore.RED}An occured while deleting CTE with ID: {cte['id']}")


def supship(accessToken: str):
    headers = {
        "Authorization": f"Bearer {accessToken}",
        "Content-Type": "application/json",
    }

    res = requests.get(url=BASE_URL + "/supshipcte/findAll", headers=headers)

    print(f"Found {len(res.json())} CTEs")
    if len(res.json()):
        print("Deleting...")

    for cte in res.json():
        try:
            deleted = requests.delete(
                url=f"{BASE_URL}/supshipcte/{cte['id']}", headers=headers
            )
            deleted.raise_for_status()
            print(f"{clr.Fore.GREEN}Successfully deleted CTE with ID: {cte['id']}; SSCC: {cte['sscc']};")
        except Exception as ex:
            print(f"{clr.Fore.RED}An occured while deleting CTE with ID: {cte['id']}; SSCC: {cte['sscc']};")
