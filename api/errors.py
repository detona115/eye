from datetime import datetime
from django.utils import timezone
from rest_framework.exceptions import APIException


class InvalidDate(APIException):
    status_code = 400
    default_detail = 'Future date is not allowed'
    default_code = 'Prohibited future date'


def check_date(date: str) -> None:
    user_datetime = datetime.fromisoformat(str(date))
    now = timezone.now()

    if user_datetime > now:
        raise InvalidDate()
