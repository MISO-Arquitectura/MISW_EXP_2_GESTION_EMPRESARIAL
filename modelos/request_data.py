class RequestData:
    def __init__(self, http_method, url_endpoint, client, operating_system, ip_address, access_datetime):
        self.req = {
            "http_method": http_method,
            "url_endpoint": url_endpoint,
            "client": client,
            "operating_system": operating_system,
            "ip_address": ip_address,
            "access_datetime": access_datetime
        }