"""
This modules has functions to handle all the supported commands for the
classroom bot.

Author: Adarsh Trivedi
Date: 2020-09-04
"""

from ..slack_client import send_message
from proxy_service.models import CommandRequest
from proxy_service.bot_server_http_calls.assignment import (get_all_assignments_for_team,
                                                            create_new_assignment)
from proxy_service.bot_server_http_calls.student import (register_user_email_id, get_groups_for_user)
from proxy_service.bot_server_http_calls.schedule import (save_lecture_link_user_email_id,
                                                          save_tutor_link_user_email_id,
                                                          get_lecture_link_for_user,
                                                          get_tutor_link_for_user)

supported_group_command_parameters = ('help', 'list')
supported_assignment_command_operations = ('get', 'create')
upported_bookmarks_command_operations = ('get','create')

def is_valid_group_command_request(parameters):
    parameters = parameters.split(" ")

    if parameters[0] in supported_group_command_parameters:
        return True
    return False


def send_command_response(request, response):
    team_id = request["team_id"]
    send_message(team_id=team_id, channel=request["channel_id"], message=response, user_id=request["user_id"])


def parse_group_command_parameters_and_respond(parameters):
    response = ""

    if is_valid_group_command_request(parameters):

        parameters = parameters.split(" ")

        request_id = CommandRequest.objects.create_new_incoming_record(command="group", command_parameter=parameters)

        if request_id != -1:

            if parameters[0] == 'help':
                response = "Supported parameters by /group command are 'help', 'list'.\n" \
                           "Parameter usage:\n" \
                           "1. /group help\n" \
                           "2. /group list group_name or group_number\n"
            CommandRequest.objects.update_request(request_id=request_id, request_parameters={'response': response})

    else:
        request_id = CommandRequest.objects.create_new_incoming_record(
            command="group", command_parameter=parameters,
            is_valid_request=False)

        if request_id != -1:
            response = " The first parameter you passed in incorrect.\n" \
                       "Supported parameters by /group command are 'help', 'list'.\n" \
                       "Parameter usage:\n" \
                       "1. /group help\n" \
                       "2. /group list group_name or group_number\n"
            CommandRequest.objects.update_request(request_id=request_id,
                                                  request_parameters={
                                                      "response": response,
                                                      "request_status": "invalid"
                                                  })

    return response


def group_handler(request: dict) -> None:
    """
    The function handles a request coming from slack for the group command.
    :param request:
    :return: returns a suitable response based on the request
    """
    response_text = parse_group_command_parameters_and_respond(request["text"])
    send_command_response(request, response_text)


# assignment handlers

def is_valid_assignment_command_request(parameters):
    parameters = parameters.split(" ")

    if parameters[0] in supported_assignment_command_operations:

        if len(parameters) == 1 and parameters[0] == 'get':
            return True
        elif parameters[0] == 'create' and len(parameters) == 7:
            supported_create_parameters = ['assignment_name', 'due_by', 'homework_url']
            parameter_fields = [parameters[1], parameters[3], parameters[5]]
            for parameter_field in parameter_fields:
                if parameter_field not in supported_create_parameters:
                    return False
            return True
    else:
        return False


def format_assignment_get_response(response_json):
    response = "Assignment Name    |  Due Date            | Assignment URL\n"

    for assignment in response_json["data"]:
        response += "{} | {} | {}\n".format(assignment["fields"]["assignment_name"],
                                            assignment["fields"]["due_by"],
                                            assignment["fields"]["homework_url"])

    return response


def parse_assignment_command_parameters_and_respond(request, parameters):
    response = ""

    if is_valid_assignment_command_request(parameters):
        parameters = parameters.split(" ")

        if parameters[0] == "get":
            response = get_all_assignments_for_team(team_id=request["team_id"])
            response = format_assignment_get_response(response)
        elif parameters[0] == "create":

            request_parameters = dict()

            request_parameters[parameters[1]] = parameters[2]
            request_parameters[parameters[3]] = parameters[4]
            request_parameters[parameters[5]] = parameters[6]
            request_parameters["team_id"] = request["team_id"]
            request_parameters["created_by"] = request["user_id"]

            response = create_new_assignment(assignment=request_parameters)

    else:
        response = "Invalid command parameters."

    return response


def assignment_handler(request: dict) -> None:
    """
    This function handles a request from the slack for the assignment command.
    :param request:
    :return:
    """
    request_parameters = request["text"].replace("\xa0", " ")
    response_text = parse_assignment_command_parameters_and_respond(request, request_parameters)
    send_command_response(request, response_text)


# code for handling my command from slack to class room environment

supported_my_command_operations = ('register', 'group')


def is_valid_my_command_request(parameters):
    parameters = parameters.split(" ")

    if parameters[0] in supported_my_command_operations:

        if parameters[0] == "register":
            if len(parameters) == 2:
                return True
            else:
                return False
        if parameters[0] == "group":
            if len(parameters) == 1:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def parse_my_command_parameters_and_respond(request, parameters):
    response = ""

    if is_valid_my_command_request(parameters):

        parameters = parameters.split(" ")

        if parameters[0] == "register":
            email = parameters[1]
            team_id = request["team_id"]

            response = register_user_email_id(email_id=email, team_id=team_id, slack_user_id=request["user_id"])
        elif parameters[0] == "group":
            response = get_groups_for_user(request['user_id'])

    else:
        response = "Invalid request format/structure."
    return response


def my_handler(request: dict) -> None:
    """
    This function handles a request from the slack for registering a new user using it's email address.
    :param request: slack request
    :return: None
    """

    request_parameters = request["text"].replace("\xa0", " ")
    response_text = parse_my_command_parameters_and_respond(request, request_parameters)
    send_command_response(request, response_text)


# code for handling schedule command from slack to class room environment


supported_schedule_command_operations = ('tutor', 'lecture', 'get_lecture_link', 'get_tutor_link')


def is_valid_schedule_command_request(parameters):
    parameters = parameters.split(" ")

    if parameters[0] in supported_schedule_command_operations:

        if parameters[0] == "tutor":
            if len(parameters) == 2:
                return True
            else:
                return False
        if parameters[0] == "lecture":
            if len(parameters) == 2:
                return True
            else:
                return False
        if parameters[0] == "get_lecture_link":
            if len(parameters) == 1:
                return True
            else:
                return False
        if parameters[0] == "get_tutor_link":
            if len(parameters) == 1:
                return True
            else:
                return False

        else:
            return False
    else:
        return False


supported_deadline_command_operations = ('add', 'show')


def is_valid_deadline_command_request(parameters):
    if parameters[0] in supported_deadline_command_operations:

        if parameters[0] == "add":
            if len(parameters) == 3:
                return True
            else:
                return False
        if parameters[0] == "show":
            if len(parameters) == 1:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def parse_schedule_command_parameters_and_respond(request, parameters):
    response = ""

    if is_valid_schedule_command_request(parameters):

        parameters = parameters.split(" ")
        print("printing parameters")
        print(parameters)

        if parameters[0] == "tutor":
            link = parameters[1]
            team_id = request["team_id"]

            response = save_tutor_link_user_email_id(tutor_link=link, team_id=team_id, slack_user_id=request["user_id"])
        elif parameters[0] == "lecture":
            link = parameters[1]
            team_id = request["team_id"]

            response = save_lecture_link_user_email_id(lecture_link=link, team_id=team_id,
                                                       slack_user_id=request["user_id"])
        elif parameters[0] == "get_tutor_link":
            response = get_tutor_link_for_user(request['user_id'])
        elif parameters[0] == "get_lecture_link":
            response = get_lecture_link_for_user(request['user_id'])

    else:
        response = "Invalid request format/structure."
    return response


def schedule_handler(request: dict) -> None:
    """
    This function handles a request from the slack for registering a new schedule using it's link.
    :param request: slack request
    :return: None
    """

    request_parameters = request["text"].replace("\xa0", " ")
    response_text = parse_schedule_command_parameters_and_respond(request, request_parameters)
    send_command_response(request, response_text)



def is_valid_bookmarks_command_request(parameters):

    parameters = parameters.split(" ")

    if parameters[0] in supported_bookmarks_command_operations:

        if len(parameters) == 1 and parameters[0] == 'get':
            return True
        elif parameters[0] == 'create':
            # create params 
            return True
    else:
        return False


def format_bookmarks_get_response(response_json):
    response = "Bookmark ID   | Bookmark Name     | URL\n"

    for grade in response_json["data"]:
        response += "{} | {} | {}\n".format(bookmarks["fields"]["bookmarkID"],
                                            grade["fields"]["bookmarkName"],
                                            grade["fields"]["URL"])

    return response


def parse_bookmarks_command_parameters_and_respond(request, parameters):

    response = ""

    if is_valid_grade_command_request(parameters):
        parameters = parameters.split(" ")

        if parameters[0] == "get":
            response = get_all_bookmarks(course_id=request["course_id"])
            response = format_bookmarks_get_response(response)
        elif parameters[0] == "create":
            pass


    else:
        response = "Invalid command parameters."
    return response
        
        
def bookmarks_handler(request: dict) -> None:

    """
    This function handles a request from the slack for the assignment command.
    :param request:
    :return:
    """
    request_parameters = request["text"].replace("\xa0", " ")
    response_text = parse_bookmarks_command_parameters_and_respond(request, request_parameters)
    send_command_response(request, response_text)

    
    
    
def parse_daedline_parameters_and_respond(request, parameters):
    response = ""

    if is_valid_deadline_command_request(parameters):

        parameters = parameters.split("")

        if parameters[0] == "add":
            name = parameters[1]
            date = parameters[2]
            team_id = parameters["team_id"]

            response = add_deadline_user_email_id(name=name, date=date,
                                                  team_id=team_id,
                                                  slack_user_id=request["user_id"])

        elif parameters[0] == "show":
            response = show_deadlines_for_user(request["user_id"])

        else:
            response = "Invalid request format or structure"


    return response






def deadline_handler(request: dict) -> None:
    """
    This function handles a request from the slack for adding new deadlines
    and showing the most upcoming deadlines.
    :param request: slack request
    :return: None
    """

    request_parameters = request["text"].replace("\xa0", " ")
    response_text = parse_daedline_parameters_and_respond(request, request_parameters)
    send_command_response(request, response_text)

