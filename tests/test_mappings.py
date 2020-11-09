from auto_labeling_pipeline.mappings import AmazonComprehendSentimentTemplate, GCPEntitiesTemplate


def test_amazon_comprehend_sentiment():
    response = {
        'Sentiment': 'POSITIVE',
        'SentimentScore': {
            'Positive': 0,
            'Negative': 0,
            'Neutral': 0,
            'Mixed': 0
        }
    }
    mapping_template = AmazonComprehendSentimentTemplate()
    annotations = mapping_template.render(response)
    expected = [{'label': 'POSITIVE'}]
    assert annotations == expected


def test_gcp_entities():
    response = {
        "entities": [
        {
          "name": "Trump",
          "type": "PERSON",
          "metadata": {
            "mid": "/m/0cqt90",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Donald_Trump"
          },
          "salience": 0.7936003,
          "mentions": [
            {
              "text": {
                "content": "Trump",
                "beginOffset": 10
              },
              "type": "PROPER"
            },
            {
              "text": {
                "content": "President",
                "beginOffset": 0
              },
              "type": "COMMON"
            }
          ]
        },
        {
          "name": "White House",
          "type": "LOCATION",
          "metadata": {
            "mid": "/m/081sq",
            "wikipedia_url": "https://en.wikipedia.org/wiki/White_House"
          },
          "salience": 0.09172433,
          "mentions": [
            {
              "text": {
                "content": "White House",
                "beginOffset": 36
              },
              "type": "PROPER"
            }
          ]
        },
        {
          "name": "Pennsylvania Ave NW",
          "type": "LOCATION",
          "metadata": {
            "mid": "/g/1tgb87cq"
          },
          "salience": 0.085507184,
          "mentions": [
            {
              "text": {
                "content": "Pennsylvania Ave NW",
                "beginOffset": 65
              },
              "type": "PROPER"
            }
          ]
        },
        {
          "name": "Washington, DC",
          "type": "LOCATION",
          "metadata": {
            "mid": "/m/0rh6k",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Washington,_D.C."
          },
          "salience": 0.029168168,
          "mentions": [
            {
              "text": {
                "content": "Washington, DC",
                "beginOffset": 86
              },
              "type": "PROPER"
            }
          ]
        },
        {
          "name": "1600 Pennsylvania Ave NW, Washington, DC",
          "type": "ADDRESS",
          "metadata": {
            "country": "US",
            "sublocality": "Fort Lesley J. McNair",
            "locality": "Washington",
            "street_name": "Pennsylvania Avenue Northwest",
            "broad_region": "District of Columbia",
            "narrow_region": "District of Columbia",
            "street_number": "1600"
          },
          "salience": 0,
          "mentions": [
            {
              "text": {
                "content": "1600 Pennsylvania Ave NW, Washington, DC",
                "beginOffset": 60
              },
              "type": "TYPE_UNKNOWN"
            }
          ]
        },
        {
          "name": "1600",
           "type": "NUMBER",
           "metadata": {
               "value": "1600"
           },
           "salience": 0,
           "mentions": [
             {
              "text": {
                  "content": "1600",
                  "beginOffset": 60
               },
               "type": "TYPE_UNKNOWN"
            }
         ]
         },
         {
           "name": "October 7",
           "type": "DATE",
           "metadata": {
             "day": "7",
             "month": "10"
           },
           "salience": 0,
           "mentions": [
             {
               "text": {
                 "content": "October 7",
                 "beginOffset": 105
                },
               "type": "TYPE_UNKNOWN"
             }
           ]
         },
         {
          "name": "7",
          "type": "NUMBER",
          "metadata": {
            "value": "7"
          },
          "salience": 0,
          "mentions": [
            {
              "text": {
                "content": "7",
                "beginOffset": 113
              },
              "type": "TYPE_UNKNOWN"
            }
          ]
        }
      ],
      "language": "en"
    }
    mapping_template = GCPEntitiesTemplate()
    annotations = mapping_template.render(response)
    expected = [
        {
            'label': 'PERSON',
            'start_offset': 10,
            'end_offset': 15
        },
        {
            'label': 'LOCATION',
            'start_offset': 36,
            'end_offset': 47
        },
        {
            'label': 'LOCATION',
            'start_offset': 65,
            'end_offset': 84
        },
        {
            'label': 'LOCATION',
            'start_offset': 86,
            'end_offset': 100
        },
        {
            'label': 'ADDRESS',
            'start_offset': 60,
            'end_offset': 100
        },
        {
            'label': 'NUMBER',
            'start_offset': 60,
            'end_offset': 64
        },
        {
            'label': 'DATE',
            'start_offset': 105,
            'end_offset': 114
        },
        {
            'label': 'NUMBER',
            'start_offset': 113,
            'end_offset': 114
        },
    ]
    assert annotations == expected
