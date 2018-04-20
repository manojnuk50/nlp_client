# NLP - entities, sentiment, syntax

Extract entities, sentiment, syntax analyses from given text content using google nlp api


### Prerequisites

What things you need to install the software and how to install them

```
python 2.7
virtualenv==15.1.0
google-api-python-client==1.6.6
```

### Installing

#### Install python virutalenv package
```bash
pip install -U virtualenv
```
Create seperate python virutal environment and install dependancey pacakges

```
git clone https://github.com/manojnuk50/nlp_client.git
cd nlp_client
virtualenv venv
activate venv/bin/activate
pip install -e .
```
##### Linux/Mac:
```bash
virtualenv venv
. venv/bin/activate
pip install -e .
```
##### Windows:
```
python -m virtualenv venv
activate venv/Scripts/activate
python -m pip install -e .
```

-h command will return the help content which contains all the available  options
```
nlp_client -h
```

End with an example of getting some data out of the system or using it for a little demo

## Available option

```bash
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -en, --enities        Provide text content for NLP extraction
  -ca, --catagories     Provide text content for NLP extraction
  -sy, --syntax         Provide text content for NLP extraction
  -se, --sentiment      Provide text content for NLP extraction
  -t TEXT, --text TEXT  Provide text content for NLP extraction
  -tf TEXT, --text-file TEXT
                        Provide text content for NLP extraction
  -sf SERVICE_ACCOUNT_PATH, --service-account-file-path SERVICE_ACCOUNT_PATH
                        provide valid path of service account json file
```


### Entity Extraction

Pass text content or text content file

```
nlp_client --entities -t "hello world"
```
or
 ```bash
nlp_client --entities -tf sample-content.txt
```

### Syntax Extraction

if your query is quite long, you can save it to text file and pass the path of it
```
nlp_client --syntax -t "hello world" -sf service_acc.json
```

### Sentiment Extraction

In default it will substitute current date into template fields. but if you want to change the date value you can pass manually using start date parameter

```
nlp_client --sentiment -t "hello world" -sf service_acc.json
```

