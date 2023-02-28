# Sarah Grobe
# POCS Assignment 20
# Due 3/3


from labMTsimple.storyLab import emotionFileReader, emotion, stopper, emotionV
import matplotlib.pyplot as plt



# set up the analyzer
labMT,labMTvector,labMTwordList = emotionFileReader(stopval=0.0,lang='english', returnVector=True)


# read in the data
# with open('data/one_grams.txt') as f:
#     data = f.readlines()

with open('data/one_grams_clean.txt') as f:
    data = f.readlines()



# Question 1 B

def list_avg(l):
    return sum(l) / len(l)


def sentiment_plot(z, delta_h = 0):
    window_size = 10**z
    
    words = data.copy()
    sentiments = []
    count = 0
    
    sentiment_window = []
        
    
    # set up the initial window
    for i in range(window_size):
        # window.append(words[0])
        # words.pop(0)
       
        raw_sent, vec = emotion(words[0], labMT, shift=True, happsList=labMTvector)
        temp = stopper(vec, labMTvector, labMTwordList, stopVal=delta_h)
        sentiment_window.append(emotionV(temp,labMTvector))
        
        words.pop(0)
    
    sentiments.append(list_avg(sentiment_window))
    
    # slide window by one word until we run out of words
    while len(words) > 0:
        raw_sent, vec = emotion(words[0], labMT, shift=True, happsList=labMTvector)
        temp = stopper(vec, labMTvector, labMTwordList, stopVal=delta_h)
        sentiment_window.append(emotionV(temp,labMTvector))
        
        words.pop(0)
        sentiment_window.pop(0)
    
        sentiments.append(list_avg(sentiment_window))
        
    
    
    # plot the results
    start_x = int(window_size/2)
    
    title = "Stranger Things Subtitle Sentiment, T = " + str(window_size)
    if delta_h > 0:
        title += ", delta_h = " + str(delta_h)
        
    x = list(range(start_x, len(data)-start_x+1))
    
    plt.plot(x, sentiments)
    plt.title(title)
    
    plt.show()

    
    
    
    
    
delta_h_list = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
z_list = [1, 1.5, 2, 2.5, 3, 3.5, 4]
 
s = sentiment_plot(z=1)