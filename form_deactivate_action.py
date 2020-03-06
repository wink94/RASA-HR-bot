from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import Form, SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionFormDeactivate(Action):

    def name(self) -> Text:
        return "action_form_deactivate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [Form(None), SlotSet("requested_slot", None)]