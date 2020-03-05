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
       minute = datetime.datetime.now().minute

       if hour < 12:
           print("good morning")
           return "Good Morning"
       elif hour >= 12 and hour < 18:
           return "Good Afternoon"
       elif hour >=18 and hour < 20:
           return "Good Evening"
       else:
           return "Good Night"



   def randGreeting(self):

       greetings=["Hi Welcome to Hsenid Mobile, How may i help you?","Hello Welcome to Hsenid mobile bot service, How can i help You?"
        ,"Greetings from Hsenid Mobile, How may i helps you?"]

       return "".join([self.timeGreeting()," ,",greetings[randint(0,2)]])


   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

       print(tracker)
       return [BotUttered(text=self.randGreeting())]



