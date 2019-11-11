<h2>POEditor API "List Project Terms"</h2>
<a href="https://www.codacy.com/manual/aleksejkov/poeditor_get_tokens?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=aleksejkov/poeditor_get_tokens&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/5494ed37af304648a29dda009f2a8cc8"/></a>
<p>To perform an action using the API, send a request to the API endpoint and a response will then be sent back to you.</p>
<p>The POEditor API consists of a set of callable methods.</p>
<p>The request should be POST.</p>
<p>The response you'll get will be a JSON encoded object.</p>
<p>If the response is not sucessful, the JSON object will contain an error code and a message.</p>

<h4>Returns project's terms and translations if the argument language is provided.</h4>

```python
data = {'api_token' : API_KEY, 
        'id' : API_ID, #<integer>	The id of project
        'language' : language #<string>	The language code
        }
```

<h3>Request example</h3>

```bash
curl -X POST https://api.poeditor.com/v2/terms/list \
     -d api_token="2182c25ea625e2d505e1c233e0a10a48" \
     -d id="7717" \
     -d language="en"
```

<h3>Response example</h3>

```json
{
    "response": {
        "status": "success",
        "code": "200",
        "message": "OK"
    },
    "result": {
        "terms": [
            {
                "term": "app_name",
                "context": "",
                "plural": "",
                "created": "2013-06-10T11:08:54+0000",
                "updated": "",
                "translation": {
                    "content": "TODO List",
                    "fuzzy": 0,
                    "proofread": 1,
                    "updated": "2013-06-12T11:08:54+0000"
                },
                "reference": "",
                "tags": [
                    "first_upload",
                    "second_upload"
                ],
                "comment": "Don't translate the name of the app"
            },
            {
                "term": "mark_as_unread",
                "context": "",
                "plural": "",
                "created": "2013-06-10T11:08:54+0000",
                "updated": "",
                "translation": {
                    "content": "",
                    "fuzzy": 0,
                    "proofread": 0,
                    "updated": ""
                },
                "reference": "",
                "tags": [
                    "second_upload"
                ],
                "comment": ""
            },
            {
                "term": "One Item",
                "context": "",
                "plural": "%d Items",
                "created": "2013-06-10T11:24:12+0000",
                "updated": "",
                "translation": {
                    "content": {
                        "one": "",
                        "other": ""
                    },
                    "fuzzy": 0,
                    "proofread": 0,
                    "updated": ""
                },
                "reference": "",
                "tags": [],
                "comment": ""
            }
        ]
    }
}
```
