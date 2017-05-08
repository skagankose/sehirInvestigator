import tweepy
import json
import sys

# Load API
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

API = tweepy.API(auth)

# Return certain informations about given user
def analyzeUser(user):

	followersCount = user.followers_count
	tweetsCount = user.statuses_count
	memberListCount = user.listed_count
	followingCount = user.friends_count
	likesCount = user.favourites_count

	return (followersCount, tweetsCount, memberListCount,
			followingCount, likesCount)

# Return certain informations about given tweets
def analyzeTweets(tweets):

	isReplyCount = 0
	isRetweetCount = 0
	mentionCount = 0
	hashtagCount = 0
	gotRetweet = 0
	gotLike = 0

	for tweet in tweets:

		if tweet.in_reply_to_user_id:
			isReplyCount += 1

		if isRetweet(tweet.text):
			isRetweetCount += 1
		else:
			gotRetweet += tweet.retweet_count
			gotLike += tweet.favorite_count
			hashtagCount += len(tweet.entities["hashtags"])
			mentionCount += len(tweet.entities["user_mentions"])


	return (isReplyCount, isRetweetCount, mentionCount,
			hashtagCount, gotRetweet, gotLike)

# Check if given tweet is a retweet
def isRetweet(tweet): return (True if tweet[:4] == "RT @" else False)

# Return certain informations about a user given her username
def currencyValue(userName, lastTweets=100, returnType="each"):

	user = API.get_user(screen_name=userName)
	tweets = API.user_timeline(screen_name=userName, count=lastTweets)

	(followersCount, tweetsCount, memberListCount,
			followingCount, likesCount) = analyzeUser(user)

	(isReplyCount, isRetweetCount, mentionCount,
			hashtagCount, gotRetweet, gotLike) = analyzeTweets(tweets)

	print("---------------------")
	print(" " * int(((21 - len(str(user.screen_name))) / 2))
			+ str(user.screen_name)
			+ " " * int(((21 - len(str(user.screen_name))) / 2)))
	print("---------------------")
	print("- general Information")
	print("| Followers     [+] " + str(followersCount))
	print("| Tweets        [+] " + str(tweetsCount))
	print("| Entered Lists [+] " + str(memberListCount))
	print("| Following     [-] " + str(followingCount))
	print("| Likes         [*] " + str(likesCount))
	print("- last " + str(len(tweets)) + " Tweets")
	print("| got Retweet   [+] " + str(gotRetweet))
	print("| got Like      [+] " + str(gotLike))
	print("| Replies       [*] " + str(isReplyCount))
	print("| Retweets      [*] " + str(isRetweetCount))
	print("| Mentions      [*] " + str(mentionCount))
	print("| Hashtags      [?] " + str(hashtagCount)) # Not Used


	totalValue = (- followingCount
				  + followersCount
				  + tweetsCount
				  + memberListCount
				  + gotRetweet
				  + gotLike)

	if likesCount: likeValue = totalValue / float(likesCount)
	else: likeValue = 0.

	if mentionCount: mentionValue = totalValue / float(mentionCount)
	else: mentionValue = 0.

	if isReplyCount: replyValue = totalValue / float(isReplyCount)
	else: replyValue = 0.

	if isRetweetCount: retweetValue = totalValue / float(isRetweetCount)
	else: retweetValue = 0.

	print("- response Values")
	print("| a Like worth      %.2f" % (float('Inf') if float(likeValue) == 0. else float(likeValue)))
	print("| a Mention worth   %.2f" % (float('Inf') if float(mentionValue) == 0. else float(mentionValue)))
	print("| a Reply worth     %.2f" % (float('Inf') if float(replyValue) == 0. else float(replyValue)))
	print("| a Retweet worth   %.2f" % (float('Inf') if float(retweetValue) == 0. else float(retweetValue)))
	print()

	if returnType == "each":
		return likeValue, mentionValue, replyValue, retweetValue

	elif returnType == "total":
		return totalValue

	elif returnType == "both":
		return totalValue, likeValue, mentionValue, replyValue, retweetValue

# Print the usage of the program
def printUsage():
	print("Usage:")
	print("	python3 testTweepy.py <userName> [options] <number>\n")
	print("Options:")
	print("	-f      Get response values of followers")
	print("	-r      Get response values of following\n")
	print("	Number:")
	print("		<10>     Limit user requests to <10>")
	print("		inf      Don't limit user requests\n")
	print("	-u      Get response values of the user")
	print("	-v      Get the total value of the user obtained from followers")
	return

# Overcomplicated for fun, you don't need to understand that part, just read printUsage()
def main():

	if len(sys.argv) < 3:
		return printUsage()

	userName = sys.argv[1]
	option = sys.argv[2]

	try:
		user = API.get_user(screen_name=userName)
	except:
		print("No Such User: %s" % userName)
		return

	if option == "-f" or option == "-r":
		if len(sys.argv) < 4:
			return printUsage()

		requestNumber = float(sys.argv[3])
		retrievedUser = 1

	if option == "-f":

		for user in tweepy.Cursor(API.followers, screen_name=userName).items():
			if retrievedUser <= requestNumber:
				try: currencyValue(user.screen_name)
				except: pass
				retrievedUser += 1

			else: break

	elif option == "-v":

		totalTotal, likesTotal, mentionTotal, replyTotal, retweetTotal = 0,0,0,0,0

		for user in tweepy.Cursor(API.followers, screen_name=userName).items():
			try:
				totalCurrent, likeCurrent, mentionCurrent, replyCurrent, retweetCurrent =\
					currencyValue(user.screen_name, returnType="both")
				totalTotal += totalCurrent
				likesTotal += likeCurrent
				mentionTotal += mentionCurrent
				replyTotal += replyCurrent
				retweetTotal += retweetCurrent

			except: pass

		print("\n#####################")
		print(" " * int(((21 - len(str(userName))) / 2))
				+ str(userName)
				+ " " * int(((21 - len(str(userName))) / 2)))
		print("#####################")
		print("- got Values")
		print("| Total             %.2f" % float(totalTotal))
		print("| Likes             %.2f" % float(likesTotal))
		print("| Mentions          %.2f" % float(mentionTotal))
		print("| Replies           %.2f" % float(replyTotal))
		print("| Retweets          %.2f" % float(retweetTotal))

	elif option == "-r":
		for userID in tweepy.Cursor(API.friends_ids, screen_name=userName).items():

			if retrievedUser <= requestNumber:
				user = API.get_user(user_id=userID)
				try: currencyValue(user.screen_name)
				except: pass
				retrievedUser += 1
			else: break

	elif option == "-u":
		currencyValue(userName)

	elif option == "-help":
		return printUsage()

if __name__ == "__main__":
	main()
