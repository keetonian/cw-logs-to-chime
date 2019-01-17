import pytest
import handlers
import requests
import chime

import test_constants


def test_logs_to_chime(mocker):
    mocker.patch.object(chime, 'post_message')
    handlers.logs_to_chime(test_constants.AWS_LOG_EVENT, None)
    chime.post_message.assert_any_call(test_constants.CHIME_URL, test_constants.EXTRACTED_LOG_EVENTS[0]['message'])
    chime.post_message.assert_any_call(test_constants.CHIME_URL, test_constants.EXTRACTED_LOG_EVENTS[1]['message'])
