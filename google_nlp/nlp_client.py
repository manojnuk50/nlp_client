import argparse
import sys
import logging
from nlp import NLPUtils

logging.basicConfig(stream=sys.stdout, level=logging.ERROR)


def main():
    try:
        parser = argparse.ArgumentParser(version="0.1", description="NLP utils")
        parser.add_argument("-en", "--entities", dest="entities", action="store_true", default=False, help="NLP entity analyze")
        parser.add_argument("-ca", "--catagories", dest="catagories", action="store_true", default=False, help="NLP categories analyze")
        parser.add_argument("-sy", "--syntax", dest="syntax", action="store_true", default=False, help="NLP syntax analyze")
        parser.add_argument("-se", "--sentiment", dest="sentiment", action="store_true", default=False, help="NLP sentiment analyze")
        parser.add_argument("-t", "--text", dest="text", help="Provide text content for NLP extraction")
        parser.add_argument("-tf", "--text-file", dest="text", help="Provide text file path for NLP extraction")
        parser.add_argument("-sf", "--service-account-file-path", dest="service_account_path", help="provide valid path of service account json file")
        args = parser.parse_args()

        if len(sys.argv) <= 1:
            parser.print_help()
            exit()

        nlp_utils = NLPUtils(service_account_path=args.service_account_path) if args.service_account_path else NLPUtils()

        if not args.text and not args.text_file:
            logging.info("Please provide either text content or text file path")

        if args.entities:
            if args.text:
                print nlp_utils.analyze_entities(text=args.text)
            else:
                with open(args.text_file) as file_cursor:
                    print nlp_utils.analyze_entities(text=file_cursor.readlines())

        if args.syntax:
            if args.text:
                print nlp_utils.analyze_syntax(text=args.text)
            else:
                with open(args.text_file) as file_cursor:
                    print nlp_utils.analyze_syntax(text=file_cursor.readlines())

        if args.sentiment:
            if args.text:
                print nlp_utils.analyze_sentiment(text=args.text)
            else:
                with open(args.text_file) as file_cursor:
                    print nlp_utils.analyze_sentiment(text=file_cursor.readlines())
    except Exception as e:
        logging.info(e)
        raise Exception(e)

    # if args.catagories:
    #     if args.text:
    #         print nlp_utils.get_text_classify(text=args.text)
    #     else:
    #         with open(args.text_file) as file_cursor:
    #             print nlp_utils.get_text_classify(text=file_cursor.readlines())






