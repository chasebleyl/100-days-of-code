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

