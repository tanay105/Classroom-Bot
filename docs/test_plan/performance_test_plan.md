#performance test plan

These tests described below should be done on multiple devices , with different hardware configurations.    

### Memory test plan

* Initially, the testing environment consists of slack without any classroom bot installed.
* The user uses slack for a period of 24 hours and a background daemon keeps track of the memory used by slack in that time frame. 
* The background daemon saves the exact amount of memory that slack is using every minute. So it takes 60 readings in a minute and 720 readings in a day.
* After this , the user goes ahead and installs the classroom bot and uses slack for 24 hours again. 
* The background daemon again takes the reading of memory being used by slack.
* we compare the memory utilised values taken before and after using the bot to figure out if the bot might be hogging more memory than expected.           

Goal of this test is to analyze the following : 
* is there a memory leak when classroom bot is active ?
* how much memory does the classrooom bot take when the user is not interacting with the bot ? 
* how much memory does the classrooom bot take when the user is interacting with the bot ? 

### CPU utilisation test plan

* Initially, the testing environment consists of slack without any classroom bot installed.
* The user uses slack for a period of 24 hours and a background daemon keeps track of the CPU utilisation by slack in that time frame. 
* The background daemon saves the exact metric of  CPU utilisation that slack is using every minute. So it takes 60 readings in a minute and 720 readings in a day.
* After this , the user goes ahead and installs the classroom bot and uses slack for 24 hours again. 
* The background daemon again takes the reading of CPU utilisation being used by slack.

Goal of this test is to analyze the following : 
* Is there a CPU utilisation spike when classroom bot is active? 
* how much CPU cycle does the bot take when the user is not interacting with the bot ? 
* how much CPU cycle does the bot take when the user is interacting with the bot ?
* does the bot work with older CPU's which have less cores ? 
* does the bot work with CPU cores that have hyper threading enabled ?
* we compare the CPU utilisations values taken before and after using the bot to figure out if the bot might be hogging more CPU cycles than expected.   

### mobile device test plan

* We do the above mentioned performance testing , but this time we do the same on smartphones and tablets
* Some OS/devices where we can test are : iPhone ( from 6s till iphone 12 ), Android ( from Android 8 till android 11 )        