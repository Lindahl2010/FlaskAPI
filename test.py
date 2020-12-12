#!/usr/bin/env python3
import unittest
import app

# Class for unit tests.
class TestHello(unittest.TestCase):

    # Initializes app
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    # Tests route for index.html located at http://<ip addr>:5000/
    # Also checks that the app returns a 200 OK status
    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    #add two more tests please
    # Tests route /get_one_temp_api that returns JSON object of one temp from MongoDB
    # Also checks that the app returns a 200 OK status
    def test_onetemp(self):
        rv = self.app.get('/get_one_temp_api')
        self.assertEqual(rv.status, '200 OK')

    # Tests route /get_ten_temps_api that returns JSON object of ten temps from MongoDB
    # Also checks that the app returns a 200 OK status
    def test_tentemps(self):
        rv = self.app.get('/get_ten_temps_api')
        self.assertEqual(rv.status, '200 OK')

    # Tests route /recent_temps that returns the temps.html layout 
    # Also checks that the app returns a 200 OK status
    def test_recenttemps(self):
        rv = self.app.get('/recent_temps')
        self.assertEqual(rv.status, '200 OK')

if __name__ == '__main__':
    unittest.main()
