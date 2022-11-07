# pickems
Small python project that helps determine my football picks and (hopefully) win my family pick'em league. Utilizes a free sports odds API, Twilio's SMS service & GitHub actions (w/ GitHub Secrets) to text me my picks every Wednesday night & Sunday morning.

## my strategy:
I've been playing pickems for the last couple years in a small family/friends leauge and usually do well the first couple weeks, then somewhere towards the middle of the season I get busy with work or school and forget to make my picks until halfway through the day Sunday. Making this mistake once or twice virtually guarantees defeat, so the most important (and most challenging) part of my pickems strategy has always been remembering to make my picks. That is why this project was designed to integrate with the Twilio SMS API to text my picks to me once they are generated. That way I can recieve a reminder every week and never forget to make my picks again!

The strategy I use to decide games each week is fairly simple: I average the game odds from an array of bookmakers, and then apply some customized "favor" points to bird teams (i.e. Ravens, Falcons, Cardinals, Eagles, Seahawks) & personal favorites (Saints, Steelers, Chargers, Vikings) in an attempt pick some of the weeks upsets.

## tools used:

* To collect data from bookmakers I used [The Odds API](https://the-odds-api.com) which has a free trail tier allowing for 500 requests 
per month. This is more than enough for my purpose as I query data ~3 times a week (leaving me way under the request per month limit). For more advanced game deciding stategies (e.g. ones that factor in QB stats, injury rosters, home vs aways records for the last three seasons, etc.) data will need to be sourced from a more comprehensive, and likely paid, API. For my purposes, I was happy to stick with this free API and just use the weekly bookmaker spreads.

* In order to send myself SMS reminders with my picks, I integrated with a trail account of the [Twilio SMS API](https://www.twilio.com/go/sms-api-sales-2). This was a breeze to use and if you are okay with a "Sent from your Twilio trial account" prefix to each message, will work for the season at no cost! You can also upgrade to a pay-as-you-go plan & remove the "Sent from ..." prefix from the messages for a few cents per SMS.

* Finally in order to run my python script, I setup a simple [GitHub Actions workflow](https://docs.github.com/en/actions/using-workflows/about-workflows) that will be triggered on certain days (I run my script every Wednesday night, Sunday morning, and Monday afternoon). This of course required me to put my repo on Github so in order to keep my private info secure (i.e. API keys, phone number, etc.) I utilized [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) to store these values. When my workflow runs, it can retrieve these secrets from the workflow environment without revealing them to observers.

## preformance for the 2022 season:

### week 1:
| Game | Spread | My Pick | Result |
| --- | --- | --- | --- |
|Buffalo Bills at Los Angeles Rams | BUF -2.5 | LAR | BUF |
|Cleveland Browns at Carolina Panthers | CAR -2.5 | CLE | CLE |
|New England Patriots at Miami Dolphins	| MIA -3 | MIA | MIA |
|Philadelphia Eagles at Detroit Lions	| PHI -4 | PHI | PHI |
|Baltimore Ravens at New York Jets	| BAL -7	| BAL | BAL |
|San Francisco 49ers at Chicago Bears	| SF -7	| SF | CHI |
|Indianapolis Colts at Houston Texans	| IND -7	| IND | HOU |
|Jacksonville Jaguars at Washington Commanders	| WAH -2.5	| WAS | WAS |
|New Orleans Saints at Atlanta Falcons | NO -5.5	| NO | NO |
|Pittsburgh Steelers at Cincinnati Bengals	| CIN -6.5	|CIN | PIT |
|Kansas City Chiefs at Arizona Cardinals	| KAN -6	| ARI | KAN |
|Green Bay Packers at Minnesota Vikings	| GB -1.5	| MIN | MIN |
|Las Vegas Raiders at Los Angeles Chargers	| LA -3	| LAC | LAC |
|New York Giants at Tennessee Titans	| TEN -5.5	| TEN | NYG |
|Tampa Bay Buccaneers at Dallas Cowboys	| TB -2.5	| TB | TB |
|Denver Broncos at Seattle Seahawks	| DEN -6.5	| DEN | SEA |

### week 2:
| Game | Spread | My Pick | Result |
| --- | --- | --- | --- |
Miami Dolphins at Baltimore Ravens | BAL -3.5| My Pick | Result |
New York Jets at Cleveland Browns | CLE -6.5| My Pick | Result |
Washington Commanders at Detroit Lions | DET -0.5| My Pick | Result |
Indianapolis Colts at Jacksonville Jaguars | IND -3.5| My Pick | Result |
Tampa Bay Buccaneers at New Orleans Saints | TB -2.5| My Pick | Result |
Carolina Panthers at New York Giants | CAR -1.5| My Pick | Result |
New England Patriots at Pittsburgh Steelers | NE -2.5| My Pick | Result |
Atlanta Falcons at Los Angeles Rams | LAR -9.5| My Pick | Result |
Seattle Seahawks at San Francisco 49ers | SF -8.5| My Pick | Result |
Cincinnati Bengals at Dallas Cowboys | CIN -6.5| My Pick | Result |
Houston Texans at Denver Broncos | DEN -10.5| My Pick | Result |
Arizona Cardinals at Las Vegas Raiders | LV -5.5| My Pick | Result |
Chicago Bears at Green Bay Packers | GB -10.5| My Pick | Result |
Tennessee Titans at Buffalo Bills | BUF -9.5| My Pick | Result |
Minnesota Vikings vs. Philadelphia Eagles | PHI -2.5| My Pick | Result |

### week 3: 
| Game | Spread | My Pick | Result |
| --- | --- | --- | --- |
Pittsburgh Steelers at Cleveland Browns | CLE -3.5 | My Pick | Result |
New Orleans Saints at Carolina Panthers | NO -2.5 | My Pick | Result |
Houston Texans at Chicago Bears | CHI -2.5 | My Pick | Result |
Kansas City Chiefs at Indianapolis Colts | KC -5.5 | My Pick | Result |
Buffalo Bills at Miami Dolphins |BUF -4.5 | My Pick | Result |
Detroit Lions at Minnesota Vikings | MIN -6.5 | My Pick | Result |
Baltimore Ravens at New England Patriots | BAL -2.5 | My Pick | Result |
Cincinnati Bengals at New York Jets |CIN -6.5 | My Pick | Result |
Las Vegas Raiders at Tennessee Titans | LV -1.5 | My Pick | Result |
Philadelphia Eagles at Washington Commanders | PHI -6.5 | My Pick | Result |
Jacksonville Jaguars at Los Angeles Chargers | LAC -3.5 | My Pick | Result | 
Los Angeles Rams at Arizona Cardinals | LAR -3.5 | My Pick | Result |
Atlanta Falcons at Seattle Seahawks | SEA -1.5 | My Pick | Result |
Green Bay Packers at Tampa Bay Buccaneers |TB -1.5 | My Pick | Result |
San Francisco 49ers at Denver Broncos | SF -1.5 | My Pick | Result |
Dallas Cowboys at New York Giants | NYG -0.5 | My Pick | Result |


### week 4:
| Game | Spread | My Pick | Result |
| --- | --- | --- | --- |

### week 5:
| Game | Spread | My Pick | Result |
| --- | --- | --- | --- |
