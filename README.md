# hn notifier

HN is a distraction source so it's a good idea to block it in order to stay productive, but I don't want to lose any of the top news. 

I wrote this small script that groups the stories that get into the top `x` rank. A second script uses `mailgun` to send me an email every day with the recap. 

I use github actions itogether with google drive to have this system working and persisting data without need to run any servers, and no maintainance. In case the scripts fail for any reason I'll start getting emails so no need to worry about monitoring either.
