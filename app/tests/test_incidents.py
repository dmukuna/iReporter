"""import unittesting module"""
from flask import json
from app.tests.base import BaseTestCase


class TestIncidents(BaseTestCase):
    """class for implementing incident tests"""

    def test_redflag_creation(self):
        """method to test for red-flag creation"""
        response = self.client().post('/api/v1/red-flags',
                                      data=json.dumps(self.incident),
                                      content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['data'][0]["message"], 'Created red-flag record')

    def test_get_redflag_with_id(self):
        """method to test for getting a specific red-flag"""
        response_post = self.client().post('/api/v1/red-flags',
                                           data=json.dumps(self.incident),
                                           content_type='application/json')
        #result_post = json.loads(response_post.data)
        self.assertEqual(response_post.status_code, 201)
        response_get = self.client().get('/api/v1/red-flags/1')
        self.assertEqual(response_get.status_code, 200)

    def test_get_all_redflags(self):
        """method to test for getting a specific red-flag"""
        response_post = self.client().post('/api/v1/red-flags',
                                           data=json.dumps(self.incident),
                                           content_type='application/json')
        self.assertEqual(response_post.status_code, 201)
        response_post = self.client().post('/api/v1/red-flags',
                                           data=json.dumps(self.incident2),
                                           content_type='application/json')
        self.assertEqual(response_post.status_code, 201)
        response_get = self.client().get('/api/v1/red-flags')
        self.assertEqual(response_get.status_code, 200)

    def test_comment_edit(self):
        """method to test for editing a specific comment of a red-flag"""
        response_post = self.client().post('/api/v1/red-flags',
                                           data=json.dumps(self.incident),
                                           content_type='application/json')
        self.assertEqual(response_post.status_code, 201)
        response_patch = self.client().patch('/api/v1/red-flags/1/comment',
                                             data=json.dumps(self.comment),
                                             content_type='application/json')
        self.assertEqual(response_patch.status_code, 200)
        result_patch = json.loads(response_patch.data)
        self.assertEqual(result_patch['data'][0]["message"], 'updated red-flag record comment')

    def test_location_edit(self):
        """method to test for editing a specific location of a red-flag"""
        response_post = self.client().post('/api/v1/red-flags',
                                           data=json.dumps(self.incident),
                                           content_type='application/json')
        self.assertEqual(response_post.status_code, 201)
        response_patch = self.client().patch('/api/v1/red-flags/1/location',
                                             data=json.dumps(self.location),
                                             content_type='application/json')
        self.assertEqual(response_patch.status_code, 200)
        result_patch = json.loads(response_patch.data)
        self.assertEqual(result_patch['data'][0]["message"], 'updated red-flag record location')

    def test_404_not_found(self):
        """method to test for non-existing red-flag"""
        response_post = self.client().post('/api/v1/red-flags',
                                           data=json.dumps(self.incident),
                                           content_type='application/json')
        self.assertEqual(response_post.status_code, 201)
        response_get = self.client().get('/api/v1/red-flags/4')
        self.assertEqual(response_get.status_code, 404)
        result_get = json.loads(response_get.data)
        self.assertEqual(result_get['error'], 'The specified red-flag does not exist')