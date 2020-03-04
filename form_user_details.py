from rasa_sdk.events import AllSlotsReset
from typing import Dict, List, Text, Any, Union
import re

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction



class UserDetailForm(FormAction):
    """Collects  information from user"""

    def name(self):
        return "user_detail_form"

    @staticmethod
    def required_slots(tracker):
        print(tracker)
        return [
            "name",
            "dob",
            "phone",
            "email",
        ]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:

        return {
            "name": [self.from_text()],
            "dob": [self.from_text()],
            "phone": [self.from_text()],
            "email": [self.from_text()]
        }

    # first name alphabetical text only validation
    def validate_first_name(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value.strip().isalpha():
            return {"first_name": value}
        else:
            dispatcher.utter_message(template="utter_wrong_input")
            return {"first_name": None}


    # date validation
    def validate_dob(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        reg_string = "^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$"

        if re.search(reg_string, value):
            return {"dob": value}
        else:
            dispatcher.utter_message(template="utter_wrong_input")
            return {"dob": None}

    # phone number validation
    def validate_phone(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value.strip().isdigit() and len(value.strip()) == 10:
            return {"phone": value}
        else:
            dispatcher.utter_message(template="utter_wrong_input")
            return {"phone": None}

    # email validation
    def validate_email(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        reg_email = "[^@]+@[^@]+\.[^@]+"

        if re.search(reg_email, value):
            return {"email": value}
        else:
            dispatcher.utter_message(template="utter_wrong_input")
            return {"email": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Thanks for getting in touch with Hsenid Mobile \nYou can submit your CV to this link: https://www.hsenidmobile.com/careers/#careers ")
        return [AllSlotsReset()]