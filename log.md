# #100DaysOfCode Log - Round 1 - Chase Bleyl

The log of my #100DaysOfCode challenge. Started on Monday, January 8th, 2018.

## Log

### [R1D1](#r1-d1)
Created a simple website to upload my log to my personal site at code.100daysof.chasebleyl.com. Next need to configure SSL through a CloudFront distribution, and integrate a Webhook to automatically sync my log from my commits.

### [R1D2](#r1-d2)
Configured HTTPS on subdomain (code.100daysof.chasebleyl.com) and distributed website through Cloudfront. Couldn't get Github to S3 to sync up - the Github to SNS to Lambda to S3 integration is far more complicated than I had originally hoped. Hopefully figure that out tomorrow. 

### [R1D3](#r1-d3)
Configured Travis-CI for automatic deployment on push, but don't like the security compromises. I have to keep the `.travis.yml` file in my Github repository with AWS accessKey and secretAccessKey. There are limited permissions on that user, but I don't want anyone else having the opportunity to deploy to my bucket. Thus, I deleted the AWS user so those credentials are now invalid.

### [R1D4](#r1-d4)
Today was a Capstone workday for me. I updated some existing updates to communicate with a new DynamoDB table, which has been an interesting learning experience. Interacting with AWS' Dynamo API is a little different than anything I am used to, but I am beginning to understand their query/expression language. I was able to get all the updates finished and pushed to our API.

Long term, I would love to learn NoSQL to the point I can be confident in a complete NoSQL database implementation. For our Capstone, the largest costs we are incurring are from our RDS databases, and the required NAT Gateway that comes along with Internet - Lambda - EC2 communication. NoSQL (DynamoDB) would eliminate the RDS instances, which would eliminate the VPC, which would eliminate the NAT Gateway, and with it 90% of our current cost.

In order to gain some experience and exposure with NoSQL, I am writing our transaction data (completion of tasks) to both our MySQL database in RDS and to a new DynamoDB table. I formatted the DynamoDB table to mimic what our analytics portal will need, which should help for lightning fast reads. So far I am really excited in this setup - I think it will make life much easier once we start building out that dashboard.

I am also realizing that the caching from Cloudfront might actually be hurting my website. Since my website's "data" is really just this Log file, it takes hours for Cloudfront to update their edge locations with updates from my S3 bucket. As this is really only a log and requires now client interaction, I might as well remove the Cloudfront distribution, losing the certificate but allowing quick updates to my log data. I'll try to do that tomorrow morning for tomorrow's work!

I will be traveling this weekend up to Idaho, so there is a good chance that I'll have to read instead of code.

### [R1D5](#r1-d5)
Opened up Travis-CI work, trying to work with encrypted variables in my config file. I was able to encrypt the access key and secret access key via `travis encrypt access_key_id=THIS_ID --add`, and then moving that newly created environment variable inside my deploy section. I got a weird `Aws::S3::Errors::AuthorizationHeaderMalformed` error from Travis-CI, which makes me think that the secret key isn't correct (the access key is, but I can't see the decrypted secret key in the console). I have reached out the Travis-CI support to see if they have any insight on what I am doing wrong.

I also removed my Cloudfront distribution and am reverting back to an S3 hosted bucket.

### [R1D6](#r1-d6)
Remote today, so I read from "Clean Code: A Handbook of Agile Software Craftmanship" by Robert C Martin. I specifically read about unit testing and test driven development (TDD). I have been working primarily on web APIs, and I have always justified not writing tests due to the complexity surrounding HTTP protocols and permissions, but reading these chapters on unit tests and previously functions make me realize these are poor excuses. My code should be better organized so that code is broken up into simple, readable chunks that are easily tested. Through Test Driven Development, the tests would be built before the code is ever written. What I have today is a product of not starting with a test driven mindset to development.

Notes and highlights:
*Three Laws of TDD*
1. You may not write production code until you have written a failing unit test.
2. You may not write more of a unit test than is sufficient to fail, and not compiling is failing.
3. You may not write more production code than is sufficient to pass the currently failing test.

` If you don't keep your tests clean, you will lose them. And without them, you lose the very thing that keeps your production code flexible. ... If you have tests, you do not fear making changes to the code!

*F.I.R.S.T. - Five rules for clean tests*
*F*ast. Tests should be fast. If they don't run quickly, you won't want to run them.
*I*ndependent. Tests should not depend on each other. You should be able to run any test you like and in whatever order you like.
*R*epeatable. Tests should be repeatable in any environment (laptop, desktop, Windows, Mac, internet, no internet). If you can't run them, you won't use them.
*S*elf-validating. Tests should have a boolean output - they should pass or fail.
*T*imely. Tests should be written JUST before the production code.

### [R1D7](#r1-d7)
Still remote, so I continued reading from "Clean Code" by Robert C Martin. Today, I read a bit on classes. I SUCK at solid clean class development. I get function and variable sprawl when I should be taking the time to thoughtfully design and implement classes to encapsulate the responsibilities that my code is trying to perform. Reading this chapter helped me recognize that I am weak in OOP, and I decided that I will jump to "Clean Architecture" by the same author to brush up on those principles.

Notes and highlights:
` We want our systems to be composed of many small classes, not a few large ones. Each small class encapsulates a single responsibility (SRP), has a single reason to change, and collaborates with a few others to achieve the desired system behaviors.

### [R1D8](#r1-d8)
Still remote, so I continued reading from "Clean Code" by Robert C Martin. I finished the chapter on classes, and looking through a couple of his example on refactoring large function segments into multiple classes. I need to spend some time doing exercises like these, and I think this would be a valuable use of my future #100DaysOfCode time to build up this kind of expertise.

### [R1D9](#r1-d9)
Back with a decent internet connection! Decided to do some practice with TDD by busting out the Bowling Game Kata. My finished kata has been uploaded to [Github](https://github.com/chasebleyl/100-days-of-code/tree/master/tdd/katas/bowling_game).

I need to become more familiar with Unit Tests and working within unit testing frameworks. I have been severely lacking in this category and I believe I could add a lot of value and quality to my work by taking this more seriously.

Todo: I need to implement auto-scroll based on the URL hash on my site.

### [R1D10](#r1-d10)
Went off on a random project today, but it's one that I have been meaning to get to for quite a while! I am building an image processor that can analyze trail cam photos for game (Elk and Deer) and also extract key quantitative information such as date and time. Later, I will correlate that will weather station data and try to study big game movement patterns based on the images and the camera data.

Today I built the majority of the image processor part. I used the Serverless framework (LOVE this framework) to use S3, Lambda, and Rekognition. Whenever an image is uploaded to an S3 bucket, a Lambda function is triggered which processes that image using AWS Rekognition. [You can see my work so far here](https://github.com/chasebleyl/process-trail-cam-photos). Next, I need to create a DynamoDB table to store that data for quick and easy extraction. Then, finally, I need to create a front-end interface where images can be uploaded to that bucket and then automatically kick off this whole process.

I spent a little more time on this today than I should have, but I just couldn't stop once I got rolling! I can't wait to build out these other components.


### [R1D11](#r1-d11)
Did the [BowlingGame Kata again](https://github.com/chasebleyl/100-days-of-code/tree/master/tdd/katas/bowling_game_2). This time I finished in about 20 minutes given the test cases and checking once for some guidance when I got stuck.

I also read some more from "Clean Architecture" about the balance between *behavior* and *structure*. Often, *structure* is overlooked as business requirements require that *behavior*, or application function, is addressed first. This creates a massive void in simplicity and causes enormous technical debt as the application matures.

I loved this quote from President Eisenhower: "I have two kinds of problems, the urgent and the important. The urgent are not important, and the important are never urgent." This quote and reading from this chapter encouraged my capstone colleague and I to address some core structural issues with our mobile app and address the scope of our project. By focusing on the important aspects now, we hope to be able to move quickly and effeciently later.

Headed out of town this afternoon again. Should be a lot of time for reading. I will update when I can!

### [R1D12](#r1-d12)
Remote for the weekend, more reading from "Clean Architecture" by Robert C Martin. I read about structured programming and object oriented programming. I enjoyed this quote about structured programming; "... software is like a science. We show correctness by failing to prove incorrectness, despite our best efforts." Test Driven Development forces you to write tests before you write code. Thus, when we add more code, our test suite simply ensures that our code is without bugs that we have already created. With this mindset, your code will only ever be as good as your tests.

I need to get better at writing unit tests.

### [R1D13](#r1-d13)
Read some more about object oriented programming and did the Bowling Game Kata again. I need to find a couple other Katas I can do when I am remote like I am today. I did pretty well, but it is probably time to mix it up. Headed back home tomorrow, hopefully I can find an exercise or two to practice when I am offline.

### [R1D14](#r1-d14)
Thanks to a suggestion from Andy Mockler, I found a great site to do some practice driven by unit tests at [exercism.io](http://exercism.io). I [completed 5 exercises](http://exercism.io/chasebleyl) and really like it! They give you all of the tests before you start so I'm not getting much practice writing tests, but it is good to be writing my code based off those tests.

Exercism is really light on bandwidth which is perfect when I am out of town. I am going to use this as the base of my practice when I am up here and continue with my personal projects when I am home.

### [R1D15](#r1-d15)
Finally got a response from Travis-CI and figured out how to properly configure it! My S3 bucket is automatically updated whenever I push to master! Glad that is configured - I was getting tired of manually uploading to S3!

Had some time while watching The Office tonight so I went ahead and configured my log page to jump to whatever hash is included in the URL. Since I am rendering the Markdown HTML after page load the browser can't use the anchor tags like it normally would. I had to manually insert the name attributes on those anchor tags, and then manually invoke the location of the DOM to go to whatever hash is found in the URL. Super hacky, but finally working!

One of these days I'll do a bit more styling. In an oddly nerdy way, I really like the plain text look of my website. It looks a bit cheap, however, so I'll have to mess with the font and some other things.

### [R1D16](#r1-d16)
Not a very productive day today. I tried to make some unit tests for the OCR app for trail cams that I created last week but it went poorly fast. It would have been much easier to start with the tests than to begin them half way through. I need to be more serious about TDD!

### [R1D17](#r1-d17)
Rough day today! Motivation was super low - probably due to a lack of sleep. I got my hour in doing edits to my log and to my personal site (chasebleyl.com). Glad I did something - hopefully tomorrow and the rest of the week will be more productive.

### [R1D18](#r1-d18)
Today I fixed my unit tests! After a few slow and sluggish days I realized that I wasn't storing a JSON object but a string for my test data. I quickly printed out some JSON objects, stored those, and began writing tests.

I was able to write four tests to identify which text we want to parse out of an array of text. Next up we will be manipulating that text string to extract our four key data components: temperature, date, time, and camera. Once we can accurately extract that data, it will be time to write to DynamoDB!

Glad I had a good morning. After a rough couple of days it feels good to get my confidence back with some sweet success.

[Commit from today's work](https://github.com/chasebleyl/process-trail-cam-photos/commit/950c7b577d38069de837dfee4fa9f152058826ea)

### [R1D19](#r1-d19)
A ton of work today for my employer, couldn't get away to code myself. Had to do an EC2 implementation of a CherryPy API. Ran into a bunch of random problems. Will be implementing a Dev/QA version early next week.

### [R1D20](#r1-d20)
Did some Exercism Katas. Got stuck on some advanced cases of the Bowling Game Kata, including validating improper bowls on the 10th frame and improper spares. Need to work through that logic a little better.

### [R1D21](#r1-d21)
Wrote some unit tests for my photo transcription service. Still slow-going as I am working out how the logic will process the images, but we are getting there slowly.

### [R1D22](#r1-d22)
Kept working on the Bowling Game Kata with little success. That one is a doozy that I'm not sure I'm gonna crack. Too much other stuff going on.

### [R1D23](#r1-d23)
Did a ton of work on the photo processing service. I am up to 58 unit tests on my response parsing service. Next, I need to write that parsed response data to DynamoDB, and then we are ready for a React Front end. Getting stuff done!

Had an interesting issue come up when [Google shut down my search](https://twitter.com/chasebleyl/status/958528833774211072). Logged a nice little Twitter rant about that. I have become ridiculously dependent on Google.

### [R1D24](#r1-d24)
Photo transcription service work today! The data extraction and storage components are basically done. I setup a DynamoDB table to store the data and hooked it up to my Lambda function. It is writing properly.

I still need to enable multiple uploads of the same filename. Currently, S3 is just updating the file, and DynamoDB will update the record as well with the same filename. Need to fix that so it creates a unique filename. Could be as easy as listing all the bucket files and then looking up that filename.

Pretty soon I'll be jumping onto the frontend! There is a lot I can do with this frontend - I'm excited to see where it goes in the next 75 days.

### [R1D25](#r1-d25)
Started work on the React app! Found a [pre-built React authentication template](https://github.com/ganezasan/react-cognito-auth) built for AWS Cognito and got my User Pool setup today. I created a User Pool and hooked it all up! Got caught up for a minute on running React on Windows, but got around it soon enough and everything seems to be working fine.

Next, I'll be stripping out some components and learning how to build my own React components! Excited to get into React.

### [R1D26](#r1-d26)
Learned a bit about Redux today. The authentication template that I used yesterday uses Redux to handle the authentication functionality, and I figured it was a good excuse to learn Redux.

I went through the majority of the basics tutorial and really nailed down the core concepts of Actions, Reducers, and the Store. I'm excited to finish the tutorial tomorrow and begin dissecting Redux in my current authentication app.

### [R1D27](#r1-d27)
Finished the Redux tutorial. Tried for a while to configure Redux with React but was getting errors trying to start the React app. Found a couple of example that I am going to use tomorrow to base my app off of to get it up and running.

Once I've got that sample app going, I'm going to take apart my authenticated app to really understand how they implemented Redux, and how I can build on top of that store.

### [R1D28](#r1-d28)
The Super Bowl delayed my coding, but I got it done! I finished up the basic Redux tutorial and got the [Todo app running properly with React](https://github.com/chasebleyl/redux-todo-tutorial). Thankfully, someone had incorporated that logic into a Create-React-App project, so I just had to follow their code and resolve the differences.

Tomorrow I'll be dissecting the authentication app I pulled down to understand how Redux is implemented. Once I get a grasp on how they implemented Redux, I can then begin designing the store to fit the needs of the photo transcription.

The main components necessary for this app will be allowing a user to upload an image, verify that the image has a unique name, change the name of the image if it doesn't, and then upload that image to S3. All transcription is handled by the backend once it is uploaded (Serverless tech is awesome). Eventually, I am going to want to add functionality to view images and their associated data, but that is way down the line.

### [R1D29](#r1-d29)
Went through the authentication app to dissect Redux. I realized that this template uses a ton of libraries which is probably why I was so overwhelmed when I first downloaded the template.

I'm trying to refactor the main authentication reducer to be "pure" Redux, just to gauge my knowledge and ensure that I understand all of these components. This is super slow work, but I think it is valuable to ensure my understanding of these components, the state, and how authentication is working.

This could easily take me 10-20 days. I'll have a better idea of how large a task this is over the next two or three days. I'm guessing it will take me a week to get past the learning curve with Redux!

### [R1D30](#r1-d30)
A rough day working with Redux! I redid the reducers and actions for the authentication template to a "standard" Redux approach, but something broke. This app incorporates a library called `redux-saga` for the actual authentication logic, and I am guessing that is where it blew up. Mapping the authentication state to that "saga" has been difficult since I didn't set it up.

Part of me wonders if I ought to look for another template, or if I should try to build a Cognito authentication library for React/Redux myself. I'm going to do some research tomorrow to see where my time is best spent. I could easily just accept the current authentication logic, but with this much dedicated time, it might be worth the effort in building my own authentication library!

Hopefully I will have more progress to report in the next couple of days.

### [R1D31](#r1-d31)
It has been a long time! I had to take care of some personal stuff, but I am ready to jump back into the 100 day challenge! I am a little bummed because I'm not on track to finish with the semester, but I'm happy to hopefully be back to coding on a more consistent basis.

After a lot of study and conversations with people over the last several weeks, I decided that I don't need to delve into Redux as much as I thought. I found a great authentication tutorial from [Dhruv Kumar Jha](https://dhruvkumarjha.com/user-authentication-using-aws-cognito/setting-up-the-frontend) on setting up a basic React app with Cognito authentication. I tried it out with the user pool I had created a few weeks ago and it seems to be working fine.

I am liking this approach. This will enable me to setup a file upload form and build the upload components into this app. Once this is all setup, I'll then be able to build some advanced features surrounding the image processing.

### [R1D32](#r1-d32)
Today was a capstone work day. I tried to get away from it to do some personal work for #100DaysOfCode, or even some research for work, but I just couldn't put it down.

Our capstone project is being implemented in a store this week, so it has been a little busy. We had some last minute changes to data, so I had to create and use some stored procedures in MySQL in order to manage those changes. I have been diving deep into stored procedures and functions in MySQL the last couple of weeks, and it has been amazing. My work with procedures, functions, and triggers have enabled me to re-work our transaction recording system which should help us a ton when we build out our data analysis API.

I am hoping to get to work on more React stuff tomorrow, but there is a good chance that I am absorbed by my capstone once again. I am having a blast! I just don't want to lose sight of this personal project.
