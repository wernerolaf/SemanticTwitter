import nltk
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

example_text = "Governor @BrianKempGA and his puppet @GeoffDuncanGA, together with the Secretary of State of Georgia " \
               "are very slow on Signature Verification, and won’t allow Fulton County to be examined. What are these " \
               " RINOS hiding? We will easily win Presidential State race. @KLoeffler and @sendavidperdue will not be " \
               "able to win on January 5th. unless these people allow Signature Verification in presidential race.K & " \
               "D need it for their race also, & Georgia spirit will rise to such a high that they will easily bring " \
               "home a great victory. Move fast @BrianKempGA "

score = SentimentIntensityAnalyzer().polarity_scores(example_text)
neg = score['neg']
neu = score['neu']
pos = score['pos']

if neg > pos and neg > neu:
    print("negative")
elif pos > neu:
    print("positive")
else:
    print("neutral")