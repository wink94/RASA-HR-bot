## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- Hallo
- Hei
- Hellllooooooo
- Hello
- Hello Bot
- Hi!
- Hi'
- Hi,
- Hi, bot
- Hieee
- Hieeeeeeeeeeeee
- Hola
- hello im, [Windula Kularatne](name)
- hi im [vinushan](name)
- hello my name is [Adam Sandler](name)
- im [Lihini Perera](name)
- hi im [chathura desilva](name)

## intent: hsenid_mobile_faq
- what is [Hsenid mobile](company)?
- what is [Hsenid](company)?
- what is [hsenid](company)?
- can you please explain about [hsenid mobile](company)?
- i need to know about [hsenid mobile](company)
- i need to know about [hsenid](company)
- tell me about [hsenid](company)

##intent: hsenid_mobile_and hsenid_biz_faq
- what is the difference between [hsenid mobile](company) and [hsenid biz](company)?
- is [hsenid mobile](company) seperate from [hsenid biz](company)?

## intent: job_apply_fresh_ASE
- Hi im [windula](name). i'm looking for a ASE vacancy. what are the available positions?
- Are there any Associate Software Engineer vacancies available
- Hello im [Pavani Perera](name), i'm [25](age) years old. I studied at [university of moratuwa](university), [computer science](study_stream) stream.
currently im looking for a Associate Software Engineer position.
- im [Alan Fernando](name), my age [20](age) years. my university is [IIT](university),i studied in [information technology](study_stream) stream
currently im looking for a Associate Software Engineer position.
- Hi what are the current available openings for ASE
- Hi what are the current available openings for Associate Software eng


## intent: job_apply_fresh_non_specific
- Hi what are the current available openings?
- Hi im [Charith](name). what are are available openings at [hsenid mobile](company).
- hi im a fresh graduate. can you tell me what are the openings available.
- Hi im [Hasitha](name), i'm [23](age) years old. I studied at [university of colombo](university), [software engineering](study_stream) stream.
can you tell me what are the available options.
- what are the available openings
- what are vacancies available
- i want to apply for a job
- can you show all the jobs
- show me all the jobs
- jobs
- openings
- job openings
- Hi im [Nuwan](name), i'm [23](age) years old. I studied at [university of colombo](university), [software engineering](study_stream) stream.
can you tell me what are the available options.

## intent: job_apply_dev
- what are the [development](job_category) vacancies available
- are there any [development](job_category) openings available
- im looking for a [development](job_category) job. are there any openings available
- im looking for a [dev](job_category:Development) job. are there any openings available
- what are the [dev](job_category:Development) vacancies available
- are there any [dev](job_category:Development) openings available
- hello im [Amith](name),im looking for a [development](job_category) opening. my phone number is [0714442225](phone) 
and my email is [amith@gmail.com](email) are there any vacancies available.
- hello im [Amith](name),im looking for a [dev](job_category:Development) opening. my telephone number is [0774472865](phone) 
and my email is [amith@gmail.com](email) are there any vacancies available.
- Hi im [piumal](name), i'm [23](age) years old. I studied at [university of colombo](university), [software engineering](study_stream) stream.
can you tell me what are the available options. currently im looking for a [development](job_category) job. 
- Hello im [piumal](name), i'm [23](age) years old. I studied at [university of colombo](university), [software engineering](study_stream) stream.
can you tell me what are the available options. currently im looking for a [dev](job_category:Development) job. 
- im [piumal](name), im [19](age) years old. I studied at [university of colombo](university), [software engineering](study_stream) stream.
im looking for a [dev](job_category:Development) job. can you tell me what are the available options. 

##intent: ASE_dev
- /ASE_dev
- ASE_dev

##intent: trigger_apply
- /trigger_apply
- trigger_apply


##intent: job_apply_impl_support
- what are the [implementation](job_category) vacancies available
- are there any [implementation](job_category) openings available
- what are the [support](job_category:implementation) vacancies available
- are there any [support](job_category) openings available
- hello im [Nimal Perera](name),im looking for a [implementation](job_category) opening. my telephone number is [0714561237](phone) 
and my email is [nimal@hotmail.com](email) are there any vacancies available.

##intent: job_apply_intern
- what are the [internship](job_category) vacancies available
- are there any [internship](job_category) openings available
- what are the [intern](job_category:internship) vacancies available
- are there any [intern](job_category) openings available
- hello im [saduni nadeesha](name),im looking for a [internship](job_category) at [hsenid mobile](company). my telephone number is [0714412254](phone) 
and my email is [saduni@yahoo.com](email) are there any vacancies available.


## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

##intent: name
- im [windula](name)
- im [tiran](name)
- im [charith  wickrama](name)
- im [pasan](name)
- im [harsha](name)
- im [vinushan selvaraj](name)
- im [shamil](name)
- im [nipuni](name)
- im [gowrishankar](name)
- im [harsha sanjeewa](name)
- im [udaya](name)
- hi im [bandu samarasingha](name)
- hello this is [ahmed mubhash](name)
- hey im [thilini](name)


## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## regex:email
- [^@]+@[^@]+\.[^@]+

## regex:phone
- [0-9]{10}