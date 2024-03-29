# NFL Pickems
### 2022 season: 173 of 271 correct (63.8%)

Small python project that helps determine my football picks and (hopefully) win my family pick'em league. Utilizes a free sports odds API, Twilio's SMS service & GitHub actions (w/ GitHub Secrets) to text me my picks every Wednesday night & Sunday morning.

## my strategy:
I've been playing pickems for the last couple years in a small family/friends leauge and usually do well the first couple weeks, then somewhere towards the middle of the season I get busy with work or school and forget to make my picks until halfway through the day Sunday. Making this mistake once or twice virtually guarantees defeat, so the most important (and most challenging) part of my pickems strategy has always been remembering to make my picks. That is why this project was designed to integrate with the Twilio SMS API to text my picks to me once they are generated. That way I can recieve a reminder every week and never forget to make my picks again!

The strategy I use to decide games each week is fairly simple: I average the game odds from an array of bookmakers, and then apply some customized "favor" points to bird teams (i.e. Ravens, Falcons, Cardinals, Eagles, Seahawks) & personal favorites (Saints, Steelers, Chargers, Vikings) in an attempt pick some of the weeks upsets.

## tools used:

* To collect data from bookmakers I used [The Odds API](https://the-odds-api.com) which has a free trail tier allowing for 500 requests 
per month. This is more than enough for my purpose as I query data ~3 times a week (leaving me way under the request per month limit). For more advanced game deciding stategies (e.g. ones that factor in QB stats, injury rosters, home vs aways records for the last three seasons, etc.) data will need to be sourced from a more comprehensive, and likely paid, API. For my purposes, I was happy to stick with this free API and just use the weekly bookmaker spreads.

* In order to send myself SMS reminders with my picks, I integrated with a trail account of the [Twilio SMS API](https://www.twilio.com/go/sms-api-sales-2). This was a breeze to use and if you are okay with a "Sent from your Twilio trial account" prefix to each message, will work for the season at no cost! You can also upgrade to a pay-as-you-go plan & remove the "Sent from ..." prefix from the messages for a few cents per SMS.

* Finally in order to run my python script, I setup a simple [GitHub Actions workflow](https://docs.github.com/en/actions/using-workflows/about-workflows) that will be triggered on certain days (I run my script every Wednesday night, Sunday morning, and Monday afternoon). This of course required me to put my repo on Github so in order to keep my private info secure (i.e. API keys, phone number, etc.) I utilized [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) to store these values. When my workflow runs, it can retrieve these secrets from the workflow environment without revealing them to observers.

### this week (week 18): 11-5
| Game | Spread | My Pick | Result |
| --- | --- | --- | --- |
KC @ LV | KC -8.5 | KC | W | 
TEN @ JAC | JAC -6 | JAC | W |
TB @ ATL | ATL -4 | ATL | W |
BAL @ CIN | CIN -7 | CIN | W |
NE @ BUF | BUF -7 | BUF | W | 
CAR @ NO | NO -3.5 | NO | L |
MIN @ CHI | MIN -7.5 | MIN | W | 
CLE @ PIT | PIT -2.5 | PIT | W | 
HOU @ IND | IND -2.5 | IND | L |
NYJ @ MIA | NYJ -1| MIA | W |
ARI @ SF | SF -14 | SF | W |
DAL @ WAS | DAL -8 | DAL | L | 
LAC @ DEN | DEN -2 | LAC | L | 
LAR @ SEA | SEA -6.5 | SEA | W |
NYG @ PHI | PHI -14 | PHI | W |
DET @ GB | GB -4.5 | GB | L |
