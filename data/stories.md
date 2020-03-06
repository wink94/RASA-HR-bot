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
  - utter_services
  
## user introduction with name
* greet
  - action_time_greeting 
  - utter_services
  
## job finding intern with help
* help
  - action_time_greeting
  - utter_services
* undergraduate OR job_apply_intern
  - utter_intern_job_apply
* trigger_apply
  - user_detail_form
  - form{"name":"user_detail_form"}
  - form{"name": null}
  - slot{"name": "saman"}
  - slot{"name": "akmal perera"}
  - slot{"dob": "12/12/1995"}
  - slot{"phone": "0714562589"}
  - slot{"email": "test@test.com"}
  - slot{"job_preference":"intern software engineer"}

## job finding intern with greet + help
*greet
  - action_time_greeting
* help
  - utter_services
* undergraduate OR job_apply_intern
  - utter_intern_job_apply
* trigger_apply
  - user_detail_form
  - form{"name":"user_detail_form"}
  - form{"name": null}
  - slot{"name": "saman"}
  - slot{"name": "akmal perera"}
  - slot{"dob": "12/12/1995"}
  - slot{"phone": "0714562589"}
  - slot{"email": "test@test.com"}
  - slot{"job_preference":"intern software engineer"}
  
## job finding intern with greet 
*greet
  - action_time_greeting
* undergraduate OR job_apply_intern
  - utter_intern_job_apply
* trigger_apply
  - user_detail_form
  - form{"name":"user_detail_form"}
  - form{"name": null}
  - slot{"name": "saman"}
  - slot{"name": "akmal perera"}
  - slot{"dob": "12/12/1995"}
  - slot{"phone": "0714562589"}
  - slot{"email": "test@test.com"}
  - slot{"job_preference":"intern software engineer"}
  
  
## job finding fresh grad with help
* help
  - action_time_greeting
  - utter_services
* job_apply_fresh_grad
  - utter_fresh_grad_job_list
* trigger_apply
  - user_detail_form
  - form{"name":"user_detail_form"}
  - form{"name": null}
  - slot{"name": "saman"}
  - slot{"name": "akmal perera"}
  - slot{"dob": "12/12/1995"}
  - slot{"phone": "0714562589"}
  - slot{"email": "test@test.com"}
  - slot{"job_preference":"intern software engineer"}
  
##direct job ask intern from bot
* undergraduate OR job_apply_intern
  - utter_intern_job_apply
* trigger_apply
  - user_detail_form
  - form{"name":"user_detail_form"}
  - form{"name": null}
  - slot{"name": "saman"}
  - slot{"name": "akmal perera"}
  - slot{"dob": "12/12/1995"}
  - slot{"phone": "0714562589"}
  - slot{"email": "test@test.com"}
  - slot{"job_preference":"intern software engineer"}
  
##direct job ask fresh grad from bot
* job_apply_fresh_grad
  - utter_fresh_grad_job_list
* trigger_apply
  - user_detail_form
  - form{"name":"user_detail_form"}
  - form{"name": null}
  - slot{"name": "saman"}
  - slot{"name": "akmal perera"}
  - slot{"dob": "12/12/1995"}
  - slot{"phone": "0714562589"}
  - slot{"email": "test@test.com"}
  - slot{"job_preference":"intern software engineer"}
 
## job finding non specific with help
* help
  - action_time_greeting
  - utter_services
* job_apply_non_specific
  - utter_job_apply_non_specific
* apply_impl_support OR apply_development OR apply_project_management OR apply_intern
  - utter_thank_for_job_apply_non_specific
* affirm OR help
  - user_detail_form
  - form{"name":"user_detail_form"}
  - form{"name": null}
  - slot{"name": "saman"}
  - slot{"name": "akmal perera"}
  - slot{"dob": "12/12/1995"}
  - slot{"phone": "0714562589"}
  - slot{"email": "test@test.com"}
  - slot{"job_preference":"intern software engineer"} 
  
##direct job ask fresh grad from bot
* job_apply_non_specific
  - utter_job_apply_non_specific
* apply_impl_support OR apply_development OR apply_project_management OR apply_intern
  - utter_thank_for_job_apply_non_specific
* affirm OR help
  -utter_ask_details
* affirm OR help
  - user_detail_form
  - form{"name":"user_detail_form"}
  - form{"name": null}
  - slot{"name": "saman"}
  - slot{"name": "akmal perera"}
  - slot{"dob": "12/12/1995"}
  - slot{"phone": "0714562589"}
  - slot{"email": "test@test.com"}
  - slot{"job_preference":"intern software engineer"} 
  
## happy hsenid faq path
* greet
  - action_time_greeting
* hsenid_mobile_faq
  - utter_hsenid_mobile_faq

  
## getting company details

##user detail form deactivate
* deactivate
  - utter_ask_form_continue
* deny
  - action_deactivate_form

## user ask a joke
* telljoke
 - utter_joke
* thank OR affirm OR mood_great
 - utter_services
   
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
