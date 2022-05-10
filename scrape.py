import twint 


TEMPLATE_TWEET = "Also, work ethic expectations would be extreme, but much less than I demand of myself"

c = twint.Config()

def validate(username):
    global TEMPLATE_TWEET
    tList = list()
    c.Username = username
    c.Limit = 20
    c.Store_object = True
    c.Store_object_tweets_list = tList
    c.Hide_output = True

    twint.run.Search(c)
    tweets = twint.output.tweets_list
    return True
    # for data in tList:
    #     if data.tweet == TEMPLATE_TWEET:
    #         return True
    # return False

if __name__ == "__main__":
    print(validate("elonmusk"))
    print(validate("sunosuporno"))