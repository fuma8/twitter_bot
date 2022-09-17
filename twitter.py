import tweepy, openai

api_key = "Siqw1IqeWDCBl3cKfMdgOWPaa"
api_secret = "yHysKjPpWon2iOvHizIn6W1N1URSF5UNM8iVjcrjQqyACAGPtu"
access_key = "1568501320163950592-WCRcOK05mf7nwIvTlLhotIF6eAvQ5t"
access_secret = "s5jRy8GTOyX1i8ZwggWFU4IswvgjgMuhbPUwN2Lym6Glp"
openai_key = "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"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# openai.api_key = openai_key
# response = openai.Completion.create(
#     engine = "text-davinci-001",
#     prompt = "食べ物",
#     max_tokens = 128
# )

# print(response)
api.update_status("hello world")

# def translate(text, s_lang='', t_lang='JA'):
#     headers = {
#         'Content-Type': 'application/x-www-form-urlencoded; utf-8'
#     }
#     params = {
#         'auth_key': AUTH_KEY,
#         'text': text,
#         'target_lang': t_lang
#     }
#     if s_lang != '':
#         params['source_lang'] = s_lang
 
#     req = urllib.request.Request(
#         DEEPL_TRANSLATE_EP,
#         method='POST',
#         data=urllib.parse.urlencode(params).encode('utf-8'),
#         headers=headers
#     )
#     try:
#         with urllib.request.urlopen(req) as res:
#             res_json = json.loads(res.read().decode('utf-8'))
#             print(json.dumps(res_json, indent=2, ensure_ascii=False))
#             return res_json['translations'][0]['text']
#     except urllib.error.HTTPError as e:
#         print(e)