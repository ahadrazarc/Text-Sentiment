import feedparser
from transformers import pipeline
ticker = 'PROJ'
keyword = 'project'
pipe = pipeline("text-classification", model="ProsusAI/finbert")
#print(pipe('Stocks rallied and the British pound gained'))
res_url = f'https://www.tesla.com/'
feed = feedparser.parse(res_url)
total_score = 0
num_articles = 0

for i, entry in enumerate(feed.entries):
  if keyword.lower() not in entry.summary.lower():
    continue
  print(f'title:{entry.title}')
  print(f'link:{entry.link}')
  print(f'published{entry.published}') 
  print(f'summary:{entry.summary}')

  sentiment = pipe(entry.title)[0]

  print(f'sentiment:{sentiment["label"]}')
  print(f'score:{sentiment["score"]}')
  print('-' * 40)

  if sentiment['label'] == 'positive':
    total_score += sentiment['score']
    num_articles += 1
    # score = pipe(entry.title)[0]['score']
    # total_score += score
  elif sentiment['label'] == 'negative':
    total_score -= sentiment['score']
    num_articles += 1
    # score = pipe(entry.title)[0]['score']
    # total_score += score

# Handle the case when no articles are found
if num_articles == 0:
    final_score = 0  # Or any other default value you prefer
    print("No articles found related to the keyword.")
else:
    final_score = total_score / num_articles
    print(f'Overall Sentiment:{"Positive" if total_score >= 0.15 else "Negative" if total_score <= -0.15 else "Neutral"} {final_score}')