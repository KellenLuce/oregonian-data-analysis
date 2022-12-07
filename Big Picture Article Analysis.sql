/* average share count by newspaper source */

SELECT newspaper, avg(share_count) average FROM f_proj.articles_raw
GROUP BY newspaper
ORDER BY average
;

/* average share count by label (ordered by label frequency */

SELECT label, avg(share_count) average, count(label) total_occurences FROM f_proj.articles_raw
GROUP BY label
ORDER BY total_occurences DESC
;
