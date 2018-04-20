# -*- coding: utf-8 -*-
# pylint: disable=F0401,abstract-method,no-member

import sys
import time
import logging
#from google.cloud import language
from googleapiclient import discovery
import httplib2
from googleapiclient.errors import HttpError
from oauth2client.client import GoogleCredentials
from oauth2client.service_account import ServiceAccountCredentials


class NLPUtils():
    """"
    Custom slack hook for sending message to specific slack channal
    """

    def __init__(self,
                 service_account_path=None,
                 scope='https://www.googleapis.com/auth/cloud-platform',
                 *args,
                 **kwargs):
        self.service_account_path =  service_account_path
        self.scope=scope

    def _authorize(self):
        """
        Returns an authorized HTTP object to be used to build a Google cloud
        service hook connection.
        """

        if self.service_account_path is None:
            logging.info('Getting connection using `gcloud auth` user, since no key file '
                         'is defined for hook.')
            credentials = GoogleCredentials.get_application_default()
        else:
            if not self.scope:
                raise Exception('Scope should be defined when using a key file.')
            scopes = [s.strip() for s in self.scope.split(',')]
            if self.service_account_path.endswith('.json'):
                logging.info('Getting connection using a JSON key file.')
                credentials = ServiceAccountCredentials\
                    .from_json_keyfile_name(self.service_account_path, scopes)
            elif self.service_account_path.endswith('.p12'):
                raise Exception('Legacy P12 key file are not supported, '
                                       'use a JSON key file.')
            else:
                raise Exception('Unrecognised extension for key file.')

        http = httplib2.Http()
        return credentials.authorize(http)

    def get_service(self):
        http_authorized = self._authorize()
        return discovery.build('language', 'v1beta1', http=http_authorized)

    def get_native_encoding_type(self):
        """Returns the encoding type that matches Python's native strings."""
        if sys.maxunicode == 65535:
            return 'UTF16'
        else:
            return 'UTF32'

    def analyze_entities(self, text, encoding='UTF32'):
        """analyze the entities in given text"""
        try:
            body = {
                'document': {
                    'type': 'PLAIN_TEXT',
                    "language": "EN",
                    'content': text,
                },
                'encodingType': encoding,
            }

            service = self.get_service()

            request = service.documents().analyzeEntities(body=body)
            response = request.execute()

            return response
        except HttpError, err:
            if err.resp.status in [429]:
                logging.info("====================sleeping============================")
                time.sleep(10)
                return self.analyze_entities(text, encoding)
            else:
                logging.info("-----------------")
                logging.info(err.resp.status)
                raise Exception("%s" % err)

    def analyze_sentiment(self, text):
        """Analyze the sentiments in given text"""
        body = {
            'document': {
                'type': 'PLAIN_TEXT',
                'content': text,
            }
        }

        service = self.get_service()

        request = service.documents().analyzeSentiment(body=body)
        response = request.execute()

        return response

    def analyze_syntax(self, text, encoding='UTF32'):
        """Analyze the syntex in given text"""
        body = {
            'document': {
                'type': 'PLAIN_TEXT',
                'content': text,
            },
            'features': {
                'extract_syntax': True,
            },
            'encodingType': encoding,
        }

        service = self.get_service()

        request = service.documents().annotateText(body=body)
        response = request.execute()

        return response

    # def get_language_client(self):
    #     return language.LanguageServiceClient()
    #
    # def get_text_classify(self, text, verbose=True):
    #     """Classify the input text into categories. """
    #     try:
    #         language_client = language.LanguageServiceClient()
    #
    #         document = language.types.Document(
    #             content=text,
    #             type=language.enums.Document.Type.PLAIN_TEXT)
    #         response = language_client.classify_text(document)
    #         categories = response.categories
    #         return categories
    #     except Exception, e:
    #         logging.info(e)
    #         return [{'category': None, 'confidence': 0}]



