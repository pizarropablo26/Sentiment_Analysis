# compute average sentiment value for each tweet
def Single_Tweet_Average_Score(lst,Dict_Keywords):
    countsimilarwords = 0 # to count the # of keywords in each twitter
    happiness_score = 0
    for word in lst: #read list
        for wordlist in Dict_Keywords: # to read the dictionary
            if word == wordlist:
                countsimilarwords += 1 # compound addition,
                happiness_score += Dict_Keywords[wordlist]
                break # break "for wordlist in Dict_Keywords" loop
    if countsimilarwords != 0:
        Average_Tweets_Happy_Score = (happiness_score/countsimilarwords)
    else:
        Average_Tweets_Happy_Score = 0
    return Average_Tweets_Happy_Score

def compute_tweets(Open_file_Twitter, Open_file_Keywords):
    try: # "try" the program
        # 1st parameter print names of files with tweets
        with open(Open_file_Twitter, "r",encoding="utf-8") as inf_Twitter: #open file twitter
        # 2nd parameter names of file with keywords
            with open(Open_file_Keywords, "r",encoding="utf-8") as inf_Keywords: #open file keywords

                Dict_Keywords = {} # to define a dictionary
                Eastern_Tweet = ()
                Sum_Of_Tweet_Happiness_Score_Eastern = 0
                count_of_keyword_tweets_East = 0
                count_of_tweets_East = 0
                # ieo error code

                Central_Tweet = ()
                Sum_Of_Tweet_Happiness_Score_Central = 0
                count_of_keyword_tweets_Central = 0
                count_of_tweets_Central = 0

                Mountain_Tweet = ()
                Sum_Of_Tweet_Happiness_Score_Mountain = 0
                count_of_keyword_tweets_Mountain = 0
                count_of_tweets_Mountain = 0

                Pacific_Tweet = ()
                Sum_Of_Tweet_Happiness_Score_Pacific = 0
                count_of_keyword_tweets_Pacific = 0
                count_of_tweets_Pacific = 0

                for line in inf_Keywords:
                    line = line.lower()
                    keywords, score = line.split(",")
                    score = eval(score)
                    Dict_Keywords[keywords] = score
                for line in inf_Twitter:
                    line = line.lower()
                    lst = line.split()
                    lst[1] = lst[1].strip("]") #strip backward ]
                    lst[0] = lst[0].strip(',[')
                    lst[0] = eval(lst[0])
                    lst[1] = eval(lst[1]) # evaluate change to numeric the coordinate

                #>>> now we are trying to determine the location of tweets within the timezone
                    if lst[0] >= 24.660845  and lst[0] <= 49.189787: # compare latitude
                        if lst[1] >= -125.242264 and lst[1] <= -67.444574: # compare longitude
                            One_Tweet_Score = Single_Tweet_Average_Score(lst,Dict_Keywords)
                            # this is the longitude coordinate comparison
                            # this is to determine the time zone
                            if lst[1] > -87.518395: # this is east region
                                count_of_tweets_East += 1
                                if One_Tweet_Score != 0: # count keyword in each tweet
                                    count_of_keyword_tweets_East += 1
                                # compute total sentiment score for the region
                                Sum_Of_Tweet_Happiness_Score_Eastern += One_Tweet_Score

                            elif lst[1] > -101.998892: # this is central
                                count_of_tweets_Central += 1
                                if One_Tweet_Score != 0:
                                    count_of_keyword_tweets_Central += 1
                                # compute total sentiment score for the region
                                Sum_Of_Tweet_Happiness_Score_Central += One_Tweet_Score

                            elif lst[1] > -115.236428: #this is mountain
                                count_of_tweets_Mountain += 1
                                if One_Tweet_Score != 0:
                                    count_of_keyword_tweets_Mountain += 1
                                # compute total sentiment score for the region
                                Sum_Of_Tweet_Happiness_Score_Mountain += One_Tweet_Score

                            else: # this is pacific
                                count_of_tweets_Pacific += 1
                                if One_Tweet_Score != 0:
                                    count_of_keyword_tweets_Pacific += 1
                                # compute total sentiment score for the region
                                Sum_Of_Tweet_Happiness_Score_Pacific += One_Tweet_Score

        ############### from this point one, we know the total happiness score of every lines of the textfile tweet
# and the total number of keywords in on single line

                #compute timezone average
                if count_of_keyword_tweets_East != 0:
                    Average_Eastern = round(Sum_Of_Tweet_Happiness_Score_Eastern/count_of_keyword_tweets_East, 4)
                else:
                    Average_Eastern = 0
                if count_of_keyword_tweets_Central != 0:
                    Average_Central = round(Sum_Of_Tweet_Happiness_Score_Central/count_of_keyword_tweets_Central, 4)
                else:
                    Average_Central = 0
                if count_of_keyword_tweets_Mountain != 0:
                    Average_Mountain = round(Sum_Of_Tweet_Happiness_Score_Mountain/count_of_keyword_tweets_Mountain, 4)
                else:
                    Average_Mountain = 0
                if count_of_keyword_tweets_Pacific != 0:
                    Average_Pacific = round(Sum_Of_Tweet_Happiness_Score_Pacific/count_of_keyword_tweets_Pacific, 4)
                else:
                    Average_Pacific = 0
                # a. The list should contain the results in a tuple for each of the regions,
                #    in order: Eastern, Central, Mountain, Pacific.
                # b. Each tuple should contain three values:
                #   (average, count_of_keyword_tweets, count_of_tweets),where
                #           average is the average “happiness value” of that region,
                #           count_of_keyword_tweets is the number of tweets found in that region with keywords and
                #           count_of_tweets is the number of tweets found in that region.
                #   These values should be in the order specified.
                Eastern = (Average_Eastern, count_of_keyword_tweets_East, count_of_tweets_East) # to generate a tuple
                Central = (Average_Central, count_of_keyword_tweets_Central, count_of_tweets_Central) # to generate a tuple
                Mountain = (Average_Mountain, count_of_keyword_tweets_Mountain, count_of_tweets_Mountain) # to generate a tuple
                Pacific = (Average_Pacific, count_of_keyword_tweets_Pacific, count_of_tweets_Pacific) # to generate a tuple
                Sentiment_by_Region = [Eastern, Central, Mountain, Pacific]
                return Sentiment_by_Region

# c. Note: if there is an exception from a file name that does not exist,
#    then an empty list should be returned.
    except IOError: #error because the file does not exist
        Sentiment_by_Region = [] # to generate an empty list
        return Sentiment_by_Region # to return a list













