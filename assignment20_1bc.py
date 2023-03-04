# Sarah Grobe
# POCS Assignment 20
# Due 3/3


from labMTsimple.storyLab import emotionFileReader, emotion, stopper, emotionV
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec



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
    # set window size using z
    window_size = int(10**z)
    
    # initialize variables
    words = data.copy()       # copy of list of 1-grams
    sentiments = []           # holds h_avg values (the y-coordinates for the plot)
    sentiment_window = []     # holds sentiments of all 1-grams in the current window
        
    
    # set up the initial window (the first window_size 1-grams in the data set)
    for i in range(window_size):
        raw_sent, vec = emotion(words[0], labMT, shift=True, happsList=labMTvector)
        temp = stopper(vec, labMTvector, labMTwordList, stopVal=delta_h)
        
        # add each word's sentiment to the sentiment_window list
        sentiment_window.append(emotionV(temp,labMTvector))
        
        # once a word has been added to the window, remove it from our list of 1-grams
        words.pop(0)
    
    # get the avg of all sentiments in the list and add to the list "sentiments"
    sentiments.append(list_avg(sentiment_window))
    
    # slide window by one word until we run out of words
    while len(words) > 0:
        # same procedure as above to get sentiment of the word in question
        raw_sent, vec = emotion(words[0], labMT, shift=True, happsList=labMTvector)
        temp = stopper(vec, labMTvector, labMTwordList, stopVal=delta_h)
        sentiment_window.append(emotionV(temp,labMTvector))
        
        # remove the current word from the data set
        words.pop(0)
        
        # remove first value in sentiment_window (to slide the window by 1)
        sentiment_window.pop(0)
        
        # add the average to the appropriate list
        sentiments.append(list_avg(sentiment_window))
        

    
    # starting x value = midpoint of the window
    start_x = int(window_size/2)
    
        
    # set up x values running from midpoint of first window to midpoint of last window
    x = list(range(start_x, len(data)-start_x+1))
    

    return x, sentiments
    

    
    
    
    
    
delta_h_list = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
z_list = [1, 1.5, 2, 2.5, 3, 3.5, 4]
 

# Testing
# sentiment_plot(z=4, delta_h=1.5)



# 1b
x_list = []
y_list = []
for i in range(len(z_list)):
    x, y = sentiment_plot(z=z_list[i])
    x_list.append(x)
    y_list.append(y)
    
    
# build the figure of 7 plots
gs = gridspec.GridSpec(7,1)
fig = plt.figure(figsize=(14, 28))

xlab = 'Word number i'
ylab = 'h_avg'

# first plot
ax = fig.add_subplot(gs[0])
ax.plot(x_list[0],y_list[0])
ax.set_xlabel(xlab)
ax.set_ylabel(ylab)
title = "Stranger Things Subtitles, T = 10^" + str(z_list[0])
ax.set_title(title)

# subsequent plots
for i in range(1,len(z_list)):
    if len(x_list[i]) != len(y_list[i]):
        x_list[i] = x_list[i][:-1]
    ax = fig.add_subplot(gs[i], sharex=ax)
    ax.plot(x_list[i],y_list[i])
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    title = "Stranger Things Subtitles, T = 10^" + str(z_list[i])
    ax.set_title(title)
    
fig.tight_layout(h_pad=1)
    
plt.show()



# 1c

# move forward using z = 3.5
z = 3.5

x_list = []
y_list = []
for i in range(len(delta_h_list)):
    x, y = sentiment_plot(z=z, delta_h=delta_h_list[i])
    x_list.append(x)
    y_list.append(y)


# build the figure of 7 plots
gs = gridspec.GridSpec(7,1)
fig = plt.figure(figsize=(14, 28))

xlab = 'Word number i'
ylab = 'h_avg'

# first plot
ax = fig.add_subplot(gs[0])
ax.plot(x_list[0],y_list[0])
ax.set_xlabel(xlab)
ax.set_ylabel(ylab)
title = "Stranger Things Subtitles, T = 10^" + str(z) + ", delta_h = " + str(delta_h_list[0])
ax.set_title(title)

# subsequent plots
for i in range(1,len(delta_h_list)):
    if len(x_list[i]) != len(y_list[i]):
        x_list[i] = x_list[i][:-1]
    ax = fig.add_subplot(gs[i], sharex=ax)
    ax.plot(x_list[i],y_list[i])
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    title = "Stranger Things Subtitles, T = 10^" + str(z) + ", delta_h = " + str(delta_h_list[i])
    ax.set_title(title)
    
fig.tight_layout(h_pad=1)
    
plt.show()






















