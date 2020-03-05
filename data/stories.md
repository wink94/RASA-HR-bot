## welcome to hsenid
* greet
  - action_time_greeting

## job search non specific with greet
* greet
  - action_time_greeting
* job_apply_fresh_non_specific
  - utter_job_apply_fresh_non_specific
  
## job search non specific without greet
* job_apply_fresh_non_specific
  - utter_job_apply_fresh_non_specific

## job search dev with greet
* greet
  - action_time_greeting
* job_apply_dev
  - utter_job_apply_dev
  
## job search dev without greet
* job_apply_dev
  - utter_job_apply_dev
  
## job search dev apply ASE with greet
* greet
  - action_time_greeting
* job_apply_dev
   - utter_job_apply_dev
   
## job search dev apply ASE without greet
* job_apply_dev
   - utter_job_apply_dev
  
## happy hsenid faq path
* greet
  - action_time_greeting
* hsenid_mobile_faq
  - utter_hsenid_mobile_faq


## sad path 2
* greet
  - action_time_greeting
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
