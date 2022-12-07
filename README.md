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

-- Some of my conclusions:
   -- Journalist self-promotion does not seem to significantly impact the amount of interactions an article receives (as quantified
      by the number of shares it has received). It is more likely that articles which seemed to be gaining traction were tweeted out
      by their authors (causing these numbers to rise) than that the self-promo itself significantly affected article interaction,
      especially given the usually small amount of interactions (as defined by num of rts, qrts, likes, and replies) these tweets
      get.





