# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
from sqlite3 import Error


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect("firstdb")
        print("connected!...")

        cursor = conn.cursor()
        slot_value = next(tracker.get_latest_entity_values("mood"),None)
        print("here slot value: " , slot_value)
        # cur.execute("select * from music_list where mood=?", slot_value)
        sql_select_query = """select * from music_list where mood = ?"""
        cursor.execute(sql_select_query, (slot_value,))
        rows = cursor.fetchall()
        print("this is result",rows)
        dispatcher.utter_message(text=' '.join(str(i) for i in rows) )

        return []
