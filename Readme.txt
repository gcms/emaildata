Welcome
=======

`emaildata <https://pypi.python.org/pypi/emaildata/>`__ is a python
package for extracting content from email messages. It is a fork of the
`emailcontent <https://pypi.python.org/pypi/emailcontent/>`__ package
but adds from features.

emaildata features
------------------

`emaildata <https://pypi.python.org/pypi/emaildata/>`__ extracts this
types of contents from emails:

-  Extract metadata.
-  Extract text (plain text and html).
-  Extract attachments.

Extracting metadata
-------------------

This feature was included from the *metadata* module of the
`emailcontent <https://pypi.python.org/pypi/emailcontent/>`__. This
module was copied module, few methods of is *MetaData* class were
removed, and the module was made more pylint friendly.

To extract metadata from an email message headers you create an instance
of the *MetaData* class passing a message to the constructor. You can
retrieve the metadata with the method *to\_dict*. This can also be done
using the method *set\_message*::

    import email
    from emaildata.metadata import MetaData

    message = email.message_from_file(open('message.eml'))
    extractor = MetaData(message)
    data = extractor.to_dict()
    print data.keys()

    message2 = email.message_from_file(open('message2.eml'))
    extractor.set_message(message2)
    data2 = extractor.to_dict()

Extracting text
---------------

The class `Text` in the `text` module have static methods for extracting
text and html from messages::

    import email
    from emaildata.text import Text

    message = email.message_from_file(open('message.eml'))
    text = Text.text(message)
    html = Text.html(message)

Extracting attachments
-----------------------

The method `extract` in the Attachment class returns an iterator with the decoded
contents of the attachments of a message::

    import email
    from emaildata.attachment import Attachment

    message = email.message_from_file(open('message.eml'))
    for content, filename, mimetype, message in Attachment.extract(message):
        print filename
        with open(filename, 'w') as stream:
            stream.write(content)
        # If message is not None then it is an instance of email.message.Message
        if message:
            print "The file {0} is a message with attachments.".format(filename)

By default this method only iterates by the attachments with a filename. To retrieve all
attachments you have to pass `False` as the second parameter (`only_with_filename`)::

    import email
    import mimetypes
    import uuid
    from emaildata.attachment import Attachment

    message = email.message_from_file(open('message.eml'))
    for content, filename, mimetype, message in Attachment.extract(message, False):
        if not filename:
            filename = str(uuid.uuid1()) + (mimetypes.guess_extension(mimetype) or '.txt')
        print filename
        with open(filename, 'w') as stream:
            stream.write(content)
        # If message is not None then it is an instance of email.message.Message
        if message:
            print "The file {0} is a message with attachments.".format(filename)

Changelog
---------

Version 0.3 (2015-05-3)
~~~~~~~~~~~~~~~~~~~~~~~~

- Implemented class for extracting attachments from messages.

Version 0.2 (2015-05-3)
~~~~~~~~~~~~~~~~~~~~~~~~

-  Implemented class for extracting plain text and html from messages.

Version 0.1 (2015-03-15)
~~~~~~~~~~~~~~~~~~~~~~~~

-  Initial version.
-  Support for metadata extraction.

