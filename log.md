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
