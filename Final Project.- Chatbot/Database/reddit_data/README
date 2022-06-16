This is an archive of Reddit comments from October of 2007 until May of 2015 
(complete month).  This reflects 14 months of work and a lot of API calls.  
This dataset includes nearly every publicly available Reddit comment.  
Approximately 350,000 comments out of ~1.65 billion were unavailable due to 
Reddit API issues.  


Q:  How are the files structured?

Each file is compressed with bzip2 compression.  When uncompressed, each file 
is a series of JSON blocks delimited by new lines (\n).  The name of each file 
follows the format RC_yyyy-mm.bz2 where yyyy is the year and mm is the month.  
RC stands for "reddit comments."

Q:  What does Reddit use for comment ids?


Comment ids are in base 36.  If a comment starts with t1_, simply remove that 
piece and convert to base 10 to get an integer representation of the comment.  
Most comments should be in sequential order.

Q:  I noticed 1-5 comments are missing on average for each 100 sequential ids 
-- why?

Those comments were either removed, private or unavailable from the API.  99% 
of the time, it’s due to the comment being posted in a private subreddit.

Q:  I’m doing analysis on scores and need to know when the comments were 
fetched.

Most of the JSONs should have a “retrieved_on” key that I added to reflect 
when that particular comment was pulled from the Reddit API.  There is also an 
“archived” key in each JSON block that will tell you if that comment has 
been archived (meaning that people can no longer vote or reply to that comment).

Q:  I have additional questions and would like to contact you.  What is your 
contact information?

No problem. My e-mail is jason@pushshift.io

-----------------------------------------------------
MD5 checksums
-----------------------------------------------------
d30072432caed49e2c7c4d88cdbbf34e *2007/RC_2007-10.bz2
3a2065c3e755a5595a3b5014cdd5a68e *2007/RC_2007-11.bz2
d9dc852590e1d97d386095b140f08655 *2007/RC_2007-12.bz2
7bc71500bb9de4dcfec435d362c365f1 *2008/RC_2008-01.bz2
c84db2b82a6b9a3eccb35d7b53882cc5 *2008/RC_2008-02.bz2
0c8ae50d4919ced310302752b065a1e5 *2008/RC_2008-03.bz2
ed3b59d7cc2605693e3a49d9aaa74233 *2008/RC_2008-04.bz2
cb436ca8c80c6847ea7bbf6c08174bef *2008/RC_2008-05.bz2
beecbc94a0db951624708ce2b987b531 *2008/RC_2008-06.bz2
d5ba70f1fabd7b7c55f9f0e4042de97d *2008/RC_2008-07.bz2
ab9455f47d47f08e022acdde09eba89b *2008/RC_2008-08.bz2
020f511447abe9de2fae566bd4e73a9f *2008/RC_2008-09.bz2
30daa6cf49931bda5c055a32af676013 *2008/RC_2008-10.bz2
45a9ccfd17e55178e63b385baa63c920 *2008/RC_2008-11.bz2
a5293328786bae818801c4ae44ba5719 *2008/RC_2008-12.bz2
c2da0bc800b1d46e363c6a7d0e232e9e *2009/RC_2009-01.bz2
da4a687b72732b1c51bf17ec1919fdf9 *2009/RC_2009-02.bz2
1907b1073813aa8a62de41e26ae506b9 *2009/RC_2009-03.bz2
05bafb4745b99c9b12f50dc4a0e523ed *2009/RC_2009-04.bz2
d09b2e1cb2820963da232820dfdd7a62 *2009/RC_2009-05.bz2
6247c5a8f0e12c14c75c441ead58c918 *2009/RC_2009-06.bz2
9b01fa6f3d09c45a019f25588c761c62 *2009/RC_2009-07.bz2
55ebb5f1762dc8c483099ce54b54ad10 *2009/RC_2009-08.bz2
571e0af58f9c33c901653603ea897983 *2009/RC_2009-09.bz2
35be68da0856bf6875a0c8a0f1272af4 *2009/RC_2009-10.bz2
529f64cb43e71ca15ddec1dc9f02fa3d *2009/RC_2009-11.bz2
68b753c09f3d9f4070a24abfd3ed58f0 *2009/RC_2009-12.bz2
fce1ee5a6c9e4c11427c696ca2d8838d *2010/RC_2010-01.bz2
857acf30d03ad0cf10c866615b32bc98 *2010/RC_2010-02.bz2
a7ca334476fedcceafea43d79f277e46 *2010/RC_2010-03.bz2
43d307e3b7b78af0e324872283227dc6 *2010/RC_2010-04.bz2
c98ff7d9fddb14de017f346eafd91bfb *2010/RC_2010-05.bz2
cd8da56086a2f0c16cbff3d28eaaf5aa *2010/RC_2010-06.bz2
42716abe9de51b2615e34592116505ec *2010/RC_2010-07.bz2
b24304fcc8b626224c98c5dda818dd37 *2010/RC_2010-08.bz2
294bac92b15d4fdf8203354a747d3533 *2010/RC_2010-09.bz2
555d7e12659486a24d0832f6dd90def9 *2010/RC_2010-10.bz2
63d353dcabfe3cdc6d9e56f8217433f4 *2010/RC_2010-11.bz2
bbd484c543e7924fabea8096b07ed379 *2010/RC_2010-12.bz2
52c212a3f83e2460a0adffbfc70a9f04 *2011/RC_2011-01.bz2
07e22a1d908daa12f227146fbdc19707 *2011/RC_2011-02.bz2
db4f533baca0c8e642c35e8598a9131c *2011/RC_2011-03.bz2
d796e1fd2e52b0a4faedbed6610a4628 *2011/RC_2011-04.bz2
18592bab63963397822f3665fc2f1385 *2011/RC_2011-05.bz2
f5ec443f6cb900fb4975a90a3192dda0 *2011/RC_2011-06.bz2
99de0a6a3b364e527f104a989b1414cf *2011/RC_2011-07.bz2
69c8195bc6f7edf1c653869bd549f8c7 *2011/RC_2011-08.bz2
b0c3f6a0d031e9dcb20c0513a0319f53 *2011/RC_2011-09.bz2
fad695a03da84debaa1e28c60ce067b9 *2011/RC_2011-10.bz2
fb21e1d1491bda7d3074519842b5a6b8 *2011/RC_2011-11.bz2
dbd7e5b5aa35bf5d64626e25522127e7 *2011/RC_2011-12.bz2
8ec1c04b862a15ef547ef5f6699f4ad5 *2012/RC_2012-01.bz2
99b29279aee99997f72717cb1d8a008f *2012/RC_2012-02.bz2
cb8499cfc932f46b6d79f78d9cc2a7c2 *2012/RC_2012-03.bz2
6fcb0dee19b9dc2639bec485c8350293 *2012/RC_2012-04.bz2
c7c77bd17acf9e177799397f01076457 *2012/RC_2012-05.bz2
63a5c3c28a88fa37f23ff10ad382c2e7 *2012/RC_2012-06.bz2
85b17c87fe80eb8333ec3fa61a6f3dfe *2012/RC_2012-07.bz2
4134a0698ce2bb686431fa1df8ba1ac8 *2012/RC_2012-08.bz2
8ee6b6f1068b368647e4300fa5f623d0 *2012/RC_2012-09.bz2
b56e99c836ebda43b894d6b907b3e950 *2012/RC_2012-10.bz2
541c95bffc47008e6a84ba3bcd24b271 *2012/RC_2012-11.bz2
ab3041fbd6afdabb67904b2f13363cb3 *2012/RC_2012-12.bz2
636ba48ad1134f5bb56d056dd7ec1019 *2013/RC_2013-01.bz2
a04a6479ce4e93d674edc88fb530d885 *2013/RC_2013-02.bz2
7cd57b8f3f0e52869a34f2a5dcf09560 *2013/RC_2013-03.bz2
7a2a49abcd981ebaf4d3478975ea6425 *2013/RC_2013-04.bz2
2e9caf274c3c70608f4832ce5a0ffbcb *2013/RC_2013-05.bz2
86535b87016a2e39dcfddb4a1e80ef21 *2013/RC_2013-06.bz2
9eafe6b5a21fdbe5391d5dcac61f5583 *2013/RC_2013-07.bz2
d957a92b6343b695ab940bb9b938c347 *2013/RC_2013-08.bz2
44ebbd85af1686667aa99ad2de79b00f *2013/RC_2013-09.bz2
1fa44ca0436f67aa6314a6daf5a61162 *2013/RC_2013-10.bz2
c7302bd19718efd8b027124512c49b7e *2013/RC_2013-11.bz2
2f4298204b4f1baafd80b5395c834d4d *2013/RC_2013-12.bz2
b2ac01347ecda92bb896df4b69d93630 *2014/RC_2014-01.bz2
b6621d6852c133a0543a725d1539d9c8 *2014/RC_2014-02.bz2
fbab66c9de4993361bf9c177249add10 *2014/RC_2014-03.bz2
c460ea9904e851d7bfd8b6e15f33f3e0 *2014/RC_2014-04.bz2
0b7bc4b44f25008bc1c16220a407b5f1 *2014/RC_2014-05.bz2
4ec8f322e79afb25c3694e7416c122d6 *2014/RC_2014-06.bz2
d83a0e09350c91d7eb3ff97da2f239a9 *2014/RC_2014-07.bz2
8beaa85ae0827be86fd2a0c92274e14a *2014/RC_2014-08.bz2
36c9ce9dfa12f0ebaa48169ace2df979 *2014/RC_2014-09.bz2
6d58301634ca3879177edc3042aae80b *2014/RC_2014-10.bz2
6b2f6f2f9cffc42b2d458f26ee079a35 *2014/RC_2014-11.bz2
ca38783a0c3f6709b4d9fd1f23dbe1c1 *2014/RC_2014-12.bz2
a3fc3d9db18786e4486381a7f37d08e2 *2015/RC_2015-01.bz2
7d18ae5a39d4ae85c62b5227b2e4adc2 *2015/RC_2015-02.bz2
19af6bee3a461f944f53e5466c98e668 *2015/RC_2015-03.bz2
6c6c06edbd0ae1ddd0b1d5b94d474644 *2015/RC_2015-04.bz2
04ead3861f2f0c79b42574d72b3e01f4 *2015/RC_2015-05.bz2
