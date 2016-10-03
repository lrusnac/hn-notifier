# hn notifier

HN is a distraction source so it's a good idea to block it in order to stay productive, but I don't want to lose any of the top news. 

I wrote this small script that groups the stories that get into the top `x` rank. A second script uses `mailgun` to send me an email every 2 hours with the recap. 

An example of the mail_sender script is available, I did not include the actual mail sender since you can use whathever you want, a direct mail from python, a third party like mailgun, pushbulet or whathever you like.

