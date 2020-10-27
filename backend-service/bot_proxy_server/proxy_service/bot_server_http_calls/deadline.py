import requests
import os


def add_deadline_user_email_id(name, date, team_id, slack_user_id):
    deadline_url = os.getenv("BOT_SERVER_DEADLINE_URL", None)

    if deadline_url:
        req = requests.patch(deadline_url, data={'name': name,
                                                 'date': date,
                                                 'workspace_id': team_id,
                                                 'slack_user_id': slack_user_id})

        res = req.text

        if res == 'true':
            return "Your deadline is saved."
        else:
            return "Something went wrong from our end. We will fix it soon. Sorry for inconvenience."

    return "Our system is wrongly configured. We will fix it soon. Sorry for inconvenience."


def show_deadlines_for_user(slack_id):
    deadline_url = os.getenv("BOT_SERVER_SCHEDULE_URL", None)

    if deadline_url:
        req = requests.get(deadline_url, params={
            "student_id": slack_id
        })

        res = req.json()
        return res["data"]
