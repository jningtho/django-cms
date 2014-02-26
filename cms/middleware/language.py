# -*- coding: utf-8 -*-
import datetime

from django.utils.translation import get_language
from django.conf import settings


class LanguageCookieMiddleware(object):
    def process_response(self, request, response):
        language = get_language()
        if settings.LANGUAGE_COOKIE_NAME in request.COOKIES and \
                        request.COOKIES[settings.LANGUAGE_COOKIE_NAME] == language:
            return response
        max_age = 365 * 24 * 60 * 60  # 10 years
        expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                             "%a, %d-%b-%Y %H:%M:%S GMT")
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language, expires=expires, max_age=max_age)
        return response
