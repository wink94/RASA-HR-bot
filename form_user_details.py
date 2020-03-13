from rasa_sdk.events import AllSlotsReset, EventType, SlotSet, BotUttered
from typing import Dict, List, Text, Any, Union, Optional
import re

from rasa_sdk import Action, Tracker, logger
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT


class UserDetailForm(FormAction):
    """Collects  information from user"""

    deactivate_forms=["deactivate","stop form","deactivate form","please stop form","delete form"]
    reactivate_forms=["no","i want to continue","continue","quit"]
    reject_intents=['deactivate','deny','affirm']
    jobs_list=['Associate System Engineer','Associate Software Engineer','intern','ASE']



    def name(self):

        return "user_detail_form"

    @staticmethod
    def required_slots(tracker):
        logger.debug(tracker.current_slot_values())
        print("Slot mappings: ",tracker.current_slot_values())

        return [
            "name",
            "dob",
            "phone",
            "email",
            "job_preference"
        ]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:

        return {
            "name": [self.from_text(),self.from_entity(entity='name')],
            "dob": [self.from_text(),self.from_entity(entity='dob')],
            "phone": [self.from_entity(entity='phone')],
            "email": [self.from_text(),self.from_entity(entity='email')],
            "job_preference": [self.from_text(),self.from_entity(entity='job_preference')]
        }

    def request_next_slot(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> Optional[List[EventType]]:

        #track intent of the input
        intent = tracker.latest_message.get("intent", {}).get("name")
        print(intent)
        #classify deacitvate intent
        if intent =='deactivate':
            return [BotUttered("Do you really want to exit?",tracker)]
        #affirm intent to refill form
        elif intent =='affirm' :
            return [self.deactivate()]
        ## continue filling form but other intents are
        else:
            for slot in self.required_slots(tracker):
                if self._should_request_slot(tracker, slot):
                    logger.debug("Request next slot '{}'".format(slot))
                    dispatcher.utter_template("utter_ask_{}".format(slot),
                                              tracker,
                                              silent_fail=False,
                                              **tracker.slots)
                    return [SlotSet(REQUESTED_SLOT, slot)]


    # first name alphabetical text only validation
    def validate_name(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        intent = tracker.latest_message.get("intent", {}).get("name")
        reg_name_string = "^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$"

        if intent in self.reject_intents:
            return {"name": None}


        if re.search(reg_name_string,value.lower().strip()):
            return {"name": value}

        else:
            dispatcher.utter_message(text="Sorry, i didn't get you.\nPlease provide a valid input")
            return {"name": None}


    # date validation
    def validate_dob(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        reg_string = "^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$"

        intent = tracker.latest_message.get("intent", {}).get("name")

        if re.search(reg_string, value):
            return {"dob": value.strip()}

        elif intent in self.reject_intents:
            return {"dob": None}
        else:
            dispatcher.utter_message(text="Sorry, i didn't get you.\nPlease provide the DOB in valid format")
            return {"dob": None}

    # phone number validation
    def validate_phone(
            self,
            value: List,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        reg_phone="^(?:0|94|\+94|0094)?(?:(11|21|23|24|25|26|27|31|32|33|34|35|36|37|38|41|45|47|51|52|54|55|57|63|65|66|67|81|91)(0|2|3|4|5|7|9)|7(0|1|2|5|6|7|8)\d)\d{6}$"

        intent = tracker.latest_message.get("intent", {}).get("name")
        print(value)
        phone_numbers=[]
        if intent in self.reject_intents:
            return {"phone": None}

        if len(value)==0:
            return {"phone": None}

        elif len(value)==1:
            if re.search(reg_phone, value[0].strip()):
                return {"phone": value[0]}
            else:
                dispatcher.utter_message(text="Sorry, i didn't get you.\nPlease provide a valid phone number")
                return {"phone": None}

        else:
            for number in value:
                if re.search(reg_phone, number.strip()):
                    phone_numbers.append(number)
            print(phone_numbers)
            if len(phone_numbers)>0:
                return {"phone": phone_numbers}
            else:
                return {"phone": None}


    # email validation
    def validate_email(
            self,
            value: Text, ## email list
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        reg_email = "[^@]+@[^@]+\.[^@]+"
        intent = tracker.latest_message.get("intent", {}).get("name")
        print(value)
        if re.search(reg_email, value[0].strip()):
            return {"email": value}
        elif intent in self.reject_intents:
            return {"email": None}
        else:
            dispatcher.utter_message(text="Sorry, i didnt get you.\nPlease provide a valid input for email")
            return {"email": None}

    # email job preference
    def validate_job_preference(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        intent = tracker.latest_message.get("intent", {}).get("name")
        reg_job_string = "^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$"

        if intent in self.reject_intents:
            return {"job_preference": None}

        if re.search(reg_job_string, value.lower().strip()) and value.lower().strip() in self.jobs_list:
            return {"job_preference": value}

        else:
            dispatcher.utter_message(text="Sorry, i didnt get you.\nPlease provide a valid input for job preference")
            return {"job_preference": None}


    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:


        dispatcher.utter_message("Thanks for getting in touch with Hsenid Mobile \nYou can submit your CV to this link: https://www.hsenidmobile.com/careers/#careers ")
        return [AllSlotsReset()]

