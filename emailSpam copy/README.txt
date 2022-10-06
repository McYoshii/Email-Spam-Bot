Hello!
I built this command line tool as somewhat of a basic mockup of a mass-emailing system (or a spam bot, as a intended originally). the full functionality of the email spamming mechanism is fully in tact, and the email content is entirely customizable. Though the current barebones product is designed to send text based emails, the ability to customize this to send more complex entries (i.e- CSS/HTML promotional templates) should be absolutely easy to integrate. I primarily just wanted to build a back end functionality for this tool.

How it works:
The most important thing to know about this tool is regarding the spamList.txt file; as this is what gives the program something to work with. to input new emails to send content to (or spam), input a new email on each line and separate each with a comma. this could probably also work if everything is mashed together on the same line, however I myself ran into some issues inputing the content that way.
as well, the strings in the email that say anything to the effect of "#INPUT STUFF BETWEEN THESE TAGS#" are completely customizable. you could either paste your own messages within these fields, or re define what these variables do. as these variables are representative of he content that the tool sends out, which in this case would be the text based stuff. so in other words, if you were to send an email as is, it would literally send something to the effect of "Subject: #PUT SOMETHING IN BETWEEN THESE TAGS#" and "body: #TAGS#".

As well, there are comments within the source code that are there to try and assist you further within setting up the email spam tool for your specific needs. 

Happy Coding!
