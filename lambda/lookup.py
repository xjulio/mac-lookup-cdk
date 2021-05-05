import json

macs = {}


def load_dump():
    with open("resources/macaddress.io-db.csv") as fp:
        line = fp.readline().strip().lower()
        while line:
            if line.startswith("oui"):
                line = fp.readline().strip().lower()
            oui_array = line.split(",")
            macs[oui_array[0]] = oui_array[2].upper().replace('"', "")
            line = fp.readline().strip().lower()


def query(mac: str) -> str:
    if not mac:
        return None

    if not macs:
        load_dump()

    vendor = macs.get(mac.lower())
    if not vendor:
        for x in range(-1, -10, -1):
            vendor = macs.get(mac[:x])
            if vendor:
                return vendor


def handler(event, context):
    print("request: {}".format(json.dumps(event)))

    mac = event.get("pathParameters", {}).get("mac")
    vendor = query(mac)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"mac": f"{mac}", "vendor": f"{vendor}"}),
    }
