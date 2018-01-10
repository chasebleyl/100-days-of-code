# #100DaysOfCode Log - Round 1 - Chase Bleyl

The log of my #100DaysOfCode challenge. Started on Monday, January 8th, 2018.

## Log

### [R1D1](#r1-d1)
Created a simple website to upload my log to my personal site at code.100daysof.chasebleyl.com. Next need to configure SSL through a CloudFront distribution, and integrate a Webhook to automatically sync my log from my commits.

### [R1D2](#r1-d2)
Configured HTTPS on subdomain (code.100daysof.chasebleyl.com) and distributed website through Cloudfront. Couldn't get Github to S3 to sync up - the Github to SNS to Lambda to S3 integration is far more complicated than I had originally hoped. Hopefully figure that out tomorrow. 

### [R1D3](#r1-d3)
Configured Travis-CI for automatic deployment on push, but don't like the security compromises. I have to keep the `.travis.yml` file in my Github repository with AWS accessKey and secretAccessKey. There are limited permissions on that user, but I don't want anyone else having the opportunity to deploy to my bucket. Thus, I deleted the AWS user so those credentials are now invalid.

