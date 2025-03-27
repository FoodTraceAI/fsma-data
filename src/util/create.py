import os
import requests
import colorama as clr

clr.init(autoreset=True)

BASE_URL = os.getenv("LOCAL_URL")

CTE1 = {
    "sscc": "sscc1",
    "logSerialNo": "LOG001",
    "supCteStatus": "Pending",
    "ftlItem": "Bivalves",
    "variety": "Standard",
    "tlcId": 1,
    "quantity": 100,
    "unitOfMeasure": "Bin",
    "prodDesc": "Fresh Bivalves",
    "shipToLocationId": 1,
    "shipFromLocationId": 2,
    "shipDate": "2025-03-27",
    "tlcSourceId": 3,
    "tlcSourceReference": "SRC001",
    "referenceDocumentType": "ASN",
    "referenceDocumentNum": "DOC001",
}

CTE2 = {
    "sscc": "sscc2",
    "logSerialNo": "LOG002",
    "supCteStatus": "Pending",
    "ftlItem": "Bivalves",
    "variety": "Organic",
    "tlcId": 2,
    "quantity": 250,
    "unitOfMeasure": "Bin",
    "prodDesc": "Fresh Bivalves",
    "shipToLocationId": 3,
    "shipFromLocationId": 2,
    "shipDate": "2025-03-27",
    "tlcSourceId": 3,
    "tlcSourceReference": "SRC002",
    "referenceDocumentType": "ASN",
    "referenceDocumentNum": "DOC002",
}

CTE3 = {
    "sscc": "sscc3",
    "logSerialNo": "LOG003",
    "supCteStatus": "Pending",
    "ftlItem": "Bivalves",
    "variety": "Standard",
    "tlcId": 3,
    "quantity": 400,
    "unitOfMeasure": "Bin",
    "prodDesc": "Fresh Bivalves",
    "shipToLocationId": 3,
    "shipFromLocationId": 2,
    "shipDate": "2025-03-27",
    "tlcSourceId": 3,
    "tlcSourceReference": "SRC003",
    "referenceDocumentType": "ASN",
    "referenceDocumentNum": "DOC003",
}

ctes = [CTE1, CTE2, CTE3];

def supship(accessToken: str):
    headers = {
        "Authorization": f"Bearer {accessToken}",
        "Content-Type": "application/json",
    }

    for cte in ctes:
        try:
            res = requests.post(url=BASE_URL+"/supshipcte", json=cte, headers=headers)
            res.raise_for_status()

            print(f"""{clr.Fore.GREEN}Successfully created CTE with- SSCC: {cte['sscc']}""")
        except Exception as ex:
            print(ex);
