from hamcrest import assert_that, is_
from mock import ANY

import quic_version_detector.net as net


def describe_parse_hostname_ip():
    def describe_when_address_info_is_an_empty_array():
        def it_returns_none():
            assert_that(net.parse_hostname_ip([]), is_(None))

    def describe_when_address_info_is_an_array_which_has_address_information_tuple():
        def it_returns_extracted_ip_address_from_that_tuple():
            ip = net.parse_hostname_ip([(ANY, ANY, ANY, ANY, ('1.2.3.4', ANY))])

            assert_that(ip, is_('1.2.3.4'))
