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
        print(tracker.current_slot_values())
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
    def validate_name(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value.strip().isalpha():
            return {"name": value}
        else:
            dispatcher.utter_message(text="utter_wrong_input")
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

        if re.search(reg_string, value):
            return {"dob": value}
        else:
            dispatcher.utter_message(text="utter_wrong_input")
            return {"dob": None}

    # phone number validation
    def validate_phone(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        reg_phone="^(?:0|94|\+94|0094)?(?:(11|21|23|24|25|26|27|31|32|33|34|35|36|37|38|41|45|47|51|52|54|55|57|63|65|66|67|81|91)(0|2|3|4|5|7|9)|7(0|1|2|5|6|7|8)\d)\d{6}$"
        if re.search(reg_phone, value):
            return {"phone": value}
        else:
            dispatcher.utter_message(text="utter_wrong_input")
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
            dispatcher.utter_message(text="utter_wrong_input")
            return {"email": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Thanks for getting in touch with Hsenid Mobile \nYou can submit your CV to this link: https://www.hsenidmobile.com/careers/#careers ")
        return [AllSlotsReset()]