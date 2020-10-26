import requests
import os


def save_tutor_link_user_email_id(team_id, tutor_link, slack_user_id):

    schedule_url = os.getenv("BOT_SERVER_SCHEDULE_URL", None)

    if schedule_url:
        req = requests.patch(schedule_url,
                             data={'tutor_link': tutor_link,
                                   'workspace_id': team_id,
                                   'slack_user_id': slack_user_id})

        res = req.text
        if res == 'true':
            return "You are registered in your classroom space. " \
                   "Now you can access and use all supported /my command operations."
        else:
            return "Something went wrong from our end. We will fix it soon. Sorry for inconvenience."

    return "Our system is wrongly configured. We will fix it soon. Sorry for inconvenience."


def save_lecture_link_user_email_id(team_id, lecture_link, slack_user_id):

    schedule_url = os.getenv("BOT_SERVER_SCHEDULE_URL", None)

    if schedule_url:
        req = requests.patch(schedule_url,,
                             data={'lecture_link': lecture_link,
                                   'workspace_id': team_id,
                                   'slack_user_id': slack_user_id})

        res = req.text
        if res == 'true':
            return "You are registered in your classroom space. " \
                   "Now you can access and use all supported /my command operations."
        else:
            return "Something went wrong from our end. We will fix it soon. Sorry for inconvenience."

    return "Our system is wrongly configured. We will fix it soon. Sorry for inconvenience."


def get_tutor_link_for_user(slack_id):

    schedule_url = os.getenv("BOT_SERVER_SCHEDULE_URL", None)

    if schedule_url:
        req = requests.get(schedule_url, params={
            "student_id": slack_id
        })

        res = req.json()
        return res["data"]


def get_lecture_link_for_user(slack_id):

    schedule_url = os.getenv("BOT_SERVER_SCHEDULE_URL", None)

    if schedule_url:
        req = requests.get(schedule_url, params={
            "student_id": slack_id
        })

        res = req.json()
        return res["data"]
