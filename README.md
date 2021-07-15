# TwitterScrapper
A tweet streaming service for discord using twitters version 2 api

## Goal
The goal of this project is to create a bot that will cross post any tweets specified by users in realtime to a discord channel. 

## How it works... so far...
Three services are needed to run TwitterReadr.
The first is the discord bot. It must be added to discord channels and told where to post via the postHere command. After being told where to post, it will begin listening for add commands. Usere will use add commands to add twitter handles or their own custom rules laid out by twitters stream api.k

Next is the Twitter Filtered Stream. This is the stream from twitter that listens for posts according to a given set of rules. The rules can be large and complex, but there are limitations becasue i'm currently using the free version.

Lastly, there is the internal web server. It acts as the inbetween for twitter and discord. This way, the twitter stream has somewhere that is always listening for POST requests while discord can do it own thing. The discord bot will check every two seconds for any data in the stream, and if some is found, it will post it!


TODO: improve documentation with links to twitter filtered stream api

TODO: improve documentation with pics of how to set up discord bot.


