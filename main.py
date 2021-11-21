#Your main program, main.py, will prompt the user for the name of the two files –
#               the file containing the keywords
#               the file containing the tweets.
# It will then call the function compute_tweets with the two files
# to process the tweets using the given keywords.
#Your main program will get the results from compute_tweets and print the results;
# it should print the results in a readable fashion (i.e., not just numbers).
print("Jiaqi Yuan, 251172679")
print("third assignment, cs1026a")
print("Prof.Michael Bauer")
print("Wed Nov 18th 2020")

def main():
    import sentiment_analysis
    Open_file_Twitter = input("Enter name of Twitter file: ")
    Open_file_Keywords = input("Enter name of keywords file: ")
    Sentiment_of_Region = sentiment_analysis.compute_tweets(Open_file_Twitter, Open_file_Keywords)

    if Sentiment_of_Region:
        print("===================================================================")
        print("Timezone:".ljust(25),"East".ljust(10),"Central".ljust(10),"Mountain".ljust(10),"Pacific")
        print("-------------------------------------------------------------------")
        print("Happiness value".ljust(25), "%-10.4f %-10.4f %-10.4f %-10.4f" %
              (Sentiment_of_Region[0][0], Sentiment_of_Region[1][0],
               Sentiment_of_Region[2][0], Sentiment_of_Region[3][0]))
        print("number of Keyword tweet".ljust(25), "%-10d %-10d %-10d %-10d" %
              (Sentiment_of_Region[0][1], Sentiment_of_Region[1][1],
               Sentiment_of_Region[2][1], Sentiment_of_Region[3][1]))
        print("number of Tweet".ljust(25), "%-10d %-10d %-10d %-10d" %
              (Sentiment_of_Region[0][2], Sentiment_of_Region[1][2],
               Sentiment_of_Region[2][2], Sentiment_of_Region[3][2]))
        print("===================================================================")

    else:
        #i. The “happiness score” for each timezone.
        #ii. The number of tweets found in that timezone


        # if one of two doesn't exit
        # return a [] list
        print("=============================================================")
        print ("Timezone:".ljust(20),"East".ljust(10),"Central".ljust(10),"Mountain".ljust(10),"Pacific")
        print("-------------------------------------------------------------")
        print("Happiness".ljust(20), "%-10s %-10s %-10s %-10s" % ("--", "--", "--", "--"))
        print("Keyword tweet".ljust(20), "%-10s %-10s %-10s %-10s" % ("--", "--", "--", "--"))
        print("Tweet".ljust(20), "%-10s %-10s %-10s %-10s" % ("--", "--", "--", "--"))
        print("=============================================================")

main()

