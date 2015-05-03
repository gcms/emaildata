# -*- coding: utf-8 -*-
import email
import cStringIO
import mimetools


class Text(object):
    """Utility class for decoding content of messages, convert text enconding to utf-8 and
    extracting text of html from messages.
    """
    @staticmethod
    def decode_content(message):
        """Decode the content of a message. This method do not checks if the message is
        multipart or if the message mime type is plain text or html.

        Parameters
        ----------
        message: email.message.Message
            Message to decode.

        Returns
        -------
        content: str
            Decoded content of the message

        Raises
        ------
        TypeError
            If the parameter is not an instance of :class:`email.message.Message`.
        """
        if not isinstance(message, email.message.Message):
            raise TypeError("Expected a message object.")
        encoding = message['Content-Transfer-Encoding']
        if encoding and encoding.strip() == 'quoted-printable':
            result = message.get_payload()
            stream = cStringIO.StringIO(result)
            output = cStringIO.StringIO()
            mimetools.decode(stream, output, 'quoted-printable')
            return output.getvalue()
        return message.get_payload(decode=True)

    @staticmethod
    def decode_text(message):
        """Extracts the text of the message and try to convert it to utf-8. This method
        do not checks if the message is multipart or if the message mime type is plain
        text or html. Maybe you want to use the methods :class:`Text.text` and
        :class:`Text.html`.

        Parameters
        ----------
        message: email.message.Message
            Message to extract its text.

        Returns
        -------
        content: str
            Text of the message encoded to utf-8. If it cannot encode the text to utf-8
            the text will be returned as ascii.

        Raises
        ------
        TypeError
            If the parameter is not an instance of :class:`email.message.Message`.
        """
        def utf8(text):
            try:
                charset = message.get_content_charset()
                if charset:
                    return text.decode(charset).encode('utf-8')
            except LookupError:
                return text
            except (UnicodeDecodeError, UnicodeEncodeError):
                return text
            return text
        try:
            return utf8(Text.decode_content(message))
        except (UnicodeDecodeError, UnicodeEncodeError):
            return message.get_payload().encode('ascii')

    @staticmethod
    def text(message):
        """Returns the plain text of the message. If the message is multipart search
        for an attachment with no filename and with mimetype `text/plain` and returns
        it.

        Parameters
        ----------
        message: email.message.Message
            Message to decode.

        Returns
        -------
        message_text: str
            Returns the plain text of the message. This method will try return the text
            encoded to `utf-8`. If it can't, returns it with its original encoding. If
            it can't find the text returns `None`.

        Raises
        ------
        TypeError
            If the parameter is not an instance of :class:`email.message.Message`.
        """
        if not isinstance(message, email.message.Message):
            raise TypeError("Expected a message object.")
        if not message.is_multipart():
            if message.get_filename():
                return None
            if message.get_content_type() == 'text/plain':
                return Text.decode_text(message)
            return None
        for sub_message in message.get_payload():
            text = Text.text(sub_message)
            if text:
                return text
        return None

    @staticmethod
    def html(message):
        """Returns the html of the message. If the message is multipart search for an
        attachment with no filename and with mimetype `text/html` and returns it.

        Parameters
        ----------
        message: email.message.Message
            Message to decode.

        Returns
        -------
        message_text: str
            Returns the html of the message. This method will try return the html
            encoded to `utf-8`. If it can't, returns it with its original encoding. If
            it can't find the text returns `None`.

        Raises
        ------
        TypeError
            If the parameter is not an instance of :class:`email.message.Message`.
        """
        if not isinstance(message, email.message.Message):
            raise TypeError("Expected a message object.")
        if not message.is_multipart():
            if message.get_filename():
                return None
            if message.get_content_type() == 'text/html':
                return Text.decode_text(message)
            return None
        for sub_message in message.get_payload():
            text = Text.html(sub_message)
            if text:
                return text
        return None

    @staticmethod
    def undecoded(message, allowed_mimetypes=None):
        if allowed_mimetypes is None:
            allowed_mimetypes = ('text/plain', 'text/html')
        wrong_mime_types = frozenset(allowed_mimetypes).difference(['text/plain', 'text/html'])
        if wrong_mime_types:
            raise ValueError("Wrong mime types: {0}".format(list(wrong_mime_types)))
        if not isinstance(message, email.message.Message):
            raise TypeError("Expected a message object.")
        if not message.is_multipart():
            if message.get_filename():
                return None
            if message.get_content_type() in allowed_mimetypes:
                return message.get_payload()
            return None
        for sub_message in message.get_payload():
            text = Text.undecoded(sub_message)
            if text:
                return text
        return None

    @staticmethod
    def undecoded_text(message):
        return Text.undecoded(message, ['text/plain'])

    @staticmethod
    def undecoded_html(message):
        return Text.undecoded(message, ['text/html'])




