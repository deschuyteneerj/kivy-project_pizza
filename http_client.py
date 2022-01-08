from kivy.network.urlrequest import UrlRequest
import json


class HttpClient:
    def get_pizzas(self, on_complete, on_error):
        url = 'https://pizzamamadjangopython.herokuapp.com/api/GetPizzas'

        def data_received(req, result):
            data = json.loads(result)
            pizzas_dict = []
            for i in data:
                pizzas_dict.append(i['fields'])
            print('data_received')
            if on_complete:
                on_complete(pizzas_dict)

        def data_error(req, error):
            print('data_error')
            if on_error:
                on_error(error)

        def data_failure(req, result):
            print('data_failure')
            if on_error:
                on_error("Server Error: " + str(req.resp_status))

        req = UrlRequest(url, on_success=data_received, on_error=data_error, on_failure=data_failure)
