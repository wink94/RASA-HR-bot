from typing import Text, Dict, Any,  List
import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionTimeGreet(Action):

   def name(self) -> Text:
      return "action_time_greeting"

    #current machine time based greeting
   def timegreeting(self):

       hour = datetime.datetime.now().hour
       minute = datetime.datetime.now().minute

       if hour < 12:
           return "Good Morning"
       elif hour >= 12 and hour < 18:
           return "Good Afternoon"
       elif hour >=18 and hour < 20:
           return "Good Evening"
       else:
           return "Good Night"




   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


      return [SlotSet("matches", result if result is not None else [])]



