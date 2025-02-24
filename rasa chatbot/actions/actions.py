import mysql.connector
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionFetchHighestMark(Action):
    def name(self):
        return "action_fetch_highest_mark"

    def run(self, dispatcher, tracker, domain):
        db = mysql.connector.connect(host="localhost", user="root", password="", database="student_db")
        cursor = db.cursor()
        
        cursor.execute("SELECT name, marks FROM marks ORDER BY marks DESC LIMIT 1")
        result = cursor.fetchone()
        
        if result:
            response = f"The highest mark is {result[1]}, scored by {result[0]}."
        else:
            response = "No data available."
        
        dispatcher.utter_message(text=response)
        db.close()
        return []

class ActionFetchStudentMarks(Action):
    def name(self):
        return "action_fetch_student_marks"

    def run(self, dispatcher, tracker, domain):
        db = mysql.connector.connect(host="localhost", user="root", password="", database="student_db")
        cursor = db.cursor()

        name = None
        subject = None

        for entity in tracker.latest_message.get("entities", []):
            if entity.get("entity") == "name":
                name = entity.get("value")
            if entity.get("entity") == "subject":
                subject = entity.get("value")

        if name and subject:
            query = "SELECT marks FROM marks WHERE name=%s AND subject=%s"
            cursor.execute(query, (name, subject))
        elif name:
            query = "SELECT subject, marks FROM marks WHERE name=%s"
            cursor.execute(query, (name,))
        else:
            dispatcher.utter_message(text="I need a student name to fetch marks.")
            db.close()
            return []

        results = cursor.fetchall()
        if results:
            response = ", ".join([f"{sub}: {m}" for sub, m in results])
        else:
            response = "No records found."

        dispatcher.utter_message(text=response)
        db.close()
        return []
