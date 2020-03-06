## user asking about company good path
* greet
  - action_time_greeting
* hsenid_mobile_faq
  - utter_hsenid_mobile_faq
* thank
  - utter_noworries
* bye
  - utter_services
  
## user asking about company without greeting
* hsenid_mobile_faq
  - action_time_greeting
  - utter_hsenid_mobile_faq
* thank
  - utter_noworries
  - utter_goodbye

## user ask about biz and mobile
* hsenid_mobile_and_hsenid_biz_faq
  - action_time_greeting
  - utter_hsenid_mobile_biz_faq
  
##user ask help
* help
  - action_time_greeting
  - utter_help
  
## job finding intern
* undergrad OR 
## user introduction with name
* greet
  - action_time_greeting 
  
  

## job search non specific with greet
* greet
  - action_time_greeting
* job_apply_fresh_grad

  
## job search non specific without greet
* job_apply_fresh_grad


## job search dev with greet
* greet
  - action_time_greeting
* job_apply_dev
  - utter_job_apply_dev
  
## job search dev without greet
* job_apply_dev
  - action_time_greeting
  - utter_job_apply_dev
  
## job search dev apply ASE with greet
* greet
  - action_time_greeting
* job_apply_dev
   - utter_job_apply_dev
* ASE_dev
   - utter_ASE_dev
* trigger_apply
   - user_detail_form
   - form{"name":"user_detail_form"}
   - form{"name": null}
   - slot{"name": "saman"}
   - slot{"name": "akmal perera"}
   - slot{"dob": "12/12/1995"}
   - slot{"phone": "0714562589"}
   - slot{"email": "test@test.com"}

   
## job search dev apply ASE without greet
* job_apply_dev
   - action_time_greeting
   - utter_job_apply_dev
  
## happy hsenid faq path
* greet
  - action_time_greeting
* hsenid_mobile_faq
  - utter_hsenid_mobile_faq

## user detail form
* trigger_apply
  - user_detail_form
  - form{"name":"user_detail_form"}
  - form{"name": null}
  
## getting company details


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
