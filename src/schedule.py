from __future__ import print_function

import datetime
import os.path

from datetime import datetime, timedelta
import pytz
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from parser import Parser

SCOPES = ['https://www.googleapis.com/auth/calendar']
TOKEN_PATH = 'resources/token.json'
CREDENTIALS_PATH = 'resources/credentials.json'
SCHEDULE_PATH = 'upload/schedule.xls'

NOMINATOR = 'nominator'
DENOMINATOR = 'denominator'


def process(course, group, subgroup):
    creds = None
    if os.path.exists(''):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('calendar', 'v3', credentials=creds)
        create_schedule(service, course, group, subgroup)
    except HttpError as error:
        print('An error occurred: %s' % error)


def create_schedule(service, course, group, subgroup):
    if SCHEDULE_PATH.title() != "":
        parser = Parser(SCHEDULE_PATH)
    else:
        return "Error! File not exists!"
    denom_shchedule = parser.parse_denominator_schedule(course, group, subgroup)
    nom_shchedule = parser.parse_nominator_schedule(course, group, subgroup)
    for el in denom_shchedule:
        day_index = el[0]
        start_time = el[1][0]
        end_time = el[1][1]
        summary = el[2]
        create_events(service, start_time, end_time, day_index, summary, DENOMINATOR)
    for el in nom_shchedule:
        day_index = el[0]
        start_time = el[1][0]
        end_time = el[1][1]
        summary = el[2]
        create_events(service, start_time, end_time, day_index, summary, NOMINATOR)


def create_events(service, start_time, end_time, day_index, summary, weektype):
    timezone = pytz.timezone('Europe/Moscow')
    today = datetime.today().weekday()
    day_offset = 7 - today  # Нужен для того, чтобы расписание начиналось с пн
    if weektype == "nominator":
        start_date = timedelta(days=day_offset) + datetime.now(tz=timezone).date()
    else:
        start_date = timedelta(days=day_offset + 7) + datetime.now(tz=timezone).date()
    day = "MO"

    while start_date.weekday() != day_index:
        start_date += timedelta(days=1)
        day = get_day_name_by_index(day_index)

    event = {
        'summary': f'{summary}',
        'location': 'VSU',
        'description': '',
        'start': {
            'dateTime': datetime.combine(start_date, start_time).isoformat(),
            'timeZone': timezone.zone,
        },
        'end': {
            'dateTime': datetime.combine(start_date, end_time).isoformat(),
            'timeZone': timezone.zone,
        },
        'recurrence': [
            f'RRULE:FREQ=WEEKLY;INTERVAL=2;COUNT={2};BYDAY={day}'
        ],
        'reminders': {
            'useDefault': False,
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))


# Мктод проверки на числитель/знаминатель
def get_week_type() -> str:
    today = datetime.today().date()
    week_number = today.isocalendar()[1]
    if week_number % 2 == 0:
        return 'denominator'
    else:
        return 'nominator'


# Замина интов на строки (Нужно для создания ивента)
def get_day_name_by_index(index) -> str:
    match index:
        case 0:
            day = "MO"
        case 1:
            day = "TU"
        case 2:
            day = "WE"
        case 3:
            day = "TH"
        case 4:
            day = "FR"
        case 5:
            day = "SA"
        case _:
            day = "None"
    return day
