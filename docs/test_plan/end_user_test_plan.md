#End User Test Plan

These tests described below should be done with multiple users.    

### Moderated user testing

* The user is given information about the bot and a member of the dev team will help user set up the slack bot.
* He will also answer any technical question related to the bot, if the user asks it.
* The user will use the bot and the dev team member will observe him
* No diagnostic data ( such as memory reading and other performance metrics ) will be collected during this test

The goals of this test are as to find these outcome: 
* How easily can the user start using this bot if he has some assistance.
* How much time ( in minutes ) does it take for the user to set up the bot. 
* How much time did the user use the bot ? Did the user uninstall the bot ? 
* did the bot crash while the user was using it ? 


### Unmoderated user testing

* The user is given information about the bot and is asked to test it out. The user has no help from any member of the development team.
* The user will install the bot on his own and will use it without any guidance from anyone.
* After the user is done with the testing , the user will fill out the survey form.
* No diagnostic data ( such as memory reading and other performance metrics ) will be collected during this test


The goals of this test are as to find these outcome: 
* How easily can the user start using this bot if he has no assistance.
* How much time ( in minutes ) does it take for the user to set up the bot. 
* How much time did the user use the bot ? Did the user uninstall the bot ? 
* did the bot crash while the user was using it ? 
* Is the user likely to recommend it other users ? 


##### In the above tests the diagnostic data is not collected. we can have another set of tests described as above in which we can collect diagnostic data when moderated and un-moderated testing is going on. The challenge here would be to install diagnostic software ( which will collect metric such as memory usage and other metrics defined in performance_test_plan.md) on the machine owned by user.  