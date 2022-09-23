from itertools import islice
from youtube_comment_downloader import *
import spacy
downloader = YoutubeCommentDownloader()
text=''
comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=Kr2gj93wT0c', sort_by=SORT_BY_POPULAR)
for comment in islice(comments, 23):
    text+=comment['text']

nlp= spacy.load("en_core_web_sm")
doc= nlp(text)
token_list = [token for token in doc]
filtered_tokens = [token for token in doc if not token.is_stop]
lemmas = [
     f"Token: {token}, lemma: {token.lemma_}"   
     for token in filtered_tokens
     ]
print(filtered_tokens[1].vector)
