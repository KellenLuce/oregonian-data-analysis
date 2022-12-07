# oregonian-data-analysis

Various Twitter-Article Analysis:

-- Over the past 7 days, a journalist whose twitter was linked to an article tweeted out a link to an article in the dataset 25 times.

-- Average Shares per Article that was NOT tweeted out by one of the selected journalists is 85.4387755102040816

-- Average Shares per Article that WAS tweeted out by one of the selected journalists is 418.56

   -- However, the article corresponding with the tweet that had the most interactions had a total of 111 shares (at time of collection)
   
   -- Meanwhile, while the article with by far the most shares was tweeted out by the author (one of our journalists), their tweet
      received 0 quantifiable interactions (0 retweets, 0 likes, 0 quote retweets, and 0 replies)
      -- Looking at the articles by this journalist, we see that of the articles by her recorded in the articles dataset, all but one was
         tweeted out (the remaining article not having been tweeted out at all), and yet both of the other two articles had 0 shares
       
-- The journalist who had the most followers on Twitter has not made a relevant tweet over the last 7 days
   -- Relevant meaning linking an article to the Oregonian and affiliates
   
-- The journalist who had the second most followers on Twitter has not made a relevant tweet over the last 7 days

-- The journalist who had the third most followers on Twitter has made 6 tweets over the last 7 days featuring an article found in
   our dataset
   -- Barring one, all of the articles she shared were written by herself
   -- Average share count of the articles she has tweeted links to: 651.8333333333333333
   -- Average share count of HER articles that she has tweeted links to: 782.20
   -- Average share count of HER articles when none of our journalists have linked them: 681.50
   -- Average share count of HER articles when any of our journalists have linked them: 782.20
      (notice that this is the same as when she has linked them herself)
   -- Average share count of her articles in general: 737.4444444444444444
   
   
-- The average share count of the TOP article that was NOT tweeted about by a journalist is 681.50
-- The average share count of the TOP article that WAS tweeted about by a journalist is 1654.00
   -- However, excluding the number one most shared article, which was not tweeted about by another journalist and had 0 quantifiable 
      interactions on twitter, this number drops to 782.20
   -- Notice that these numbers are the same as the numbers for the 3rd most followed journalist on twitter

-- Across all tweets sharing articles, the average number of retweets is 1.24, the avg number of quote retweets is 0.64, the average
   number of replies is 1.36, and the average number of likes is 11.04

-- Articles with the highest average interactions on twitter were labeled Timbers, Beavers, and Travel & Outdoors
-- Articles shared to twitter with the highest average interactions were labeled Real Estate (of course), Public Safety, 
   Portland, and Education

-- Some of my conclusions:
   -- Journalist self-promotion does not seem to significantly impact the amount of interactions an article receives (as quantified
      by the number of shares it has received). It is more likely that articles which seemed to be gaining traction were tweeted out
      by their authors (causing these numbers to rise) than that the self-promo itself significantly affected article interaction,
      especially given the usually small amount of interactions (as defined by num of rts, qrts, likes, and replies) these tweets
      get.



------------------------
Emotional Word Analyses:
Article-specific
-- Meaningfulness scores (dimension 5, how well you understand the meaning of the word) relatively high (average score of 6.2925 for nouns [max score was 6.96] and average score of 6.3839 for adjectives [max score was 7]). Share count seems to increase as meaningfulness score increases in adjectives (no obvious correlation in noun words), possibly inferring articles with easier to understand words get more shares. Words like domineering, obliging, subjective etc. have lower scores and the corresponding articles have lower shares, while words like magical, protected, good, etc. have the max score (7, most accurately understood) with those articles having closer to thousands of shares.

-- The most most used word among all articles is "productive" used 69 times total (only used once in each of the articles it appears in)

Shared articles w/ tweets
-- Noun dimension 3 (imagery, how well you can form picture of word in mind) has higher average score of 5.91 (max score is 6.85). The most shared tweets have headlines like "Goonie's house," gun, museum, criminal, etc. words that are easier to form a picture in the mind. Words easier to imagine might be more effective in getting article shares, but those tweets have lower engagement (might be because tweets don't offer twitter users better visuals, might just be because of the subject matter being more or less interesting to twitter users)
   -- Adjective dimension also has small sample size of 3 different words, but they all score higher (5.403 average with a 6.62 max), twitter         engagement barely exists for those headlines but the share count is middle-of-the-road (not in the thousands, but not the smallest amount       of shares), so more vivid adjective words might help with that increase(?)

-- Noun dimension 5 (meaningfulness scores) very high on average (6.433 with a max score of 6.92). Every emotional word that was used in the tweet headlines has a score above 6, so effective of easy to understand words on share count is hard to determine (words like museum, church, child, transfer, etc. scored highest). Effect on tweet engagement not evident
   -- Again, adjective sample size is 3 different words in 4 articles. Very high scores (average is 6.567 with max of 6.95 and min of 5.74), shares amount similar to adjective dimension 3 results (middle of the road but still in the hundreds)

-- Noun dimension 7 (emotionality, how emotional the meaning of the word is) has average score of 3.21 vs max score of 4.53, relatively low and doesn't seem to have any big effect on the number of shares. However, twitter engagment seemed to be higher with the least emotional-scoring words used in that tweet's headline ("Portland Timbers sign Brazilian midfielder Evander in club-record transfer", using words like record & transfer with two of the lowest scoring words). Could be relavent, or could simply be because of the subject manner (sports)
   -- That same Portland Timbers headline has a low imagery score, and headlines scoring higher in imagery had less tweet interactions, could be       relavent or, again, could just be about sports and its fans engaging with it more.
   
   

-- The other dimensions of the words used didn't correlate to shares or lack thereof, which was surprising to me (I'd assumed that more click-baity headlines and article titles would've caught people's eye more. Which might be the case still, but it doesn't translate into more shares or tweet engagement).
-- The most meaningful relationship I could find was that article shares were higher with more meaningful words used in them. Words that are easier to picture/come up with an image for might effect article shares but not twitter engagement, which might be related or it might just be less engaging to have to imagine whatever's in the headline when other news sources might just post a picture for you, possibly making reading the tweet (and thus the article) less of a hastle
