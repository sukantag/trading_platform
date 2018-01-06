import requests
import json


class OrderApiClient:

    def __init__(self, account_id, access_token):
        self.access_token = access_token
        self.account_id = account_id
        self.domain = 'api-fxpractice.oanda.com'

    def create_new_order(self, units, instrument, stop_loss=None, take_profit=None):
        """
        :type units: int
        :type instrument: str
        :type stop_loss: float
        :type take_profit: float
        """
        s = requests.Session()
        url = 'https://{}/v3/accounts/{}/orders'.format(self.domain, self.account_id)
        headers = {
            'Authorization': 'Bearer {}'.format(self.access_token),
            'Content-Type': 'application/json'
        }

        data_order = {
            'units': units,
            'instrument': instrument,
            'timeInForce': 'FOK',
            'type': 'MARKET',
            'positionFill': 'DEFAULT'
        }

        if stop_loss is not None:
            data_order['stopLossOnFill'] = {'price': stop_loss}

        if take_profit is not None:
            data_order['takeProfitOnFill '] = {'price': stop_loss}

        data = {'order': data_order}

        try:
            req = requests.Request('POST', url, headers=headers, data=json.dumps(data))
            pre = req.prepare()
            response = s.send(pre, stream=True, verify=True)

            return json.loads(response.content)

        except Exception as e:
            s.close()
            raise Exception('Caught exception when connecting to API\n' + str(e))
