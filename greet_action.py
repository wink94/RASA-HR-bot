from typing import Text, Dict, Any,  List
import datetime
from random import randint

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, BotUttered
from rasa_sdk.executor import CollectingDispatcher


class ActionTimeGreet(Action):

   def name(self) -> Text:
      return "action_time_greeting"

    #current machine time based greeting
   def timeGreeting(self):

       hour = datetime.datetime.now().hour

       if hour < 12:
           return "Good Morning"
       elif hour >= 12 and hour < 18:
           return "Good Afternoon"
       elif hour >=18 and hour < 20:
           return "Good Evening"
       else:
           return "Good Night"



   def randGreeting(self):

       greetings=["Welcome to Hsenid Mobile","Welcome to Hsenid mobile bot service"
        ,"Greetings from Hsenid Mobile"]

       return greetings[randint(0,2)]


   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

       help_text="How may i help you?"
       greet_msg=''
       if(tracker.current_slot_values()['name'] != None):

           greet_msg=self.timeGreeting()+" !! "+tracker.current_slot_values()['name']+", "+self.randGreeting()

       else:
           greet_msg = self.timeGreeting() +" !!," + self.randGreeting()

       return [BotUttered(text=greet_msg)]



