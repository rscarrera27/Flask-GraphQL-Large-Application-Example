import unittest
from config import dev
from Server import create_app
import json

app = create_app(dev.DevConfig)


class BasicTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

        app.testing = True
        self.tester = app.test_client(self)

    def request(self, type, call, body):
        query = type + " {" + call + "{" + body + "}" + "}"

        response = self.tester.post('/graphql',
                                    data=json.dumps({"query": query}),
                                    content_type='application/json'
                                    )

        print(response.json)
        return dict(response.json)['data']

    def _create_fake_data(self):
        # Create fake data
        pass

    def _get_tokens(self):
        response = self.request(type="mutation",
                                call='auth(id:"{0}", password:"{1}")'.format("fake user's id", "fake user's pw"),
                                body='''
                                     result{
                                     ... on AuthField{
                                     refreshToken
                                     accessToken
                                     message
                                     }
                                     }
                                     ''')

        response = response['auth']
        self.access_token = response['result']['accessToken']
        self.refresh_token = response['result']['refreshToken']

    def setUp(self):
        self._create_fake_data()
        self._get_tokens()

    def tearDown(self):
        # teardown code ex. drop tables
        pass
