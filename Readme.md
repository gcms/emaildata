# Welcome

[emaildata](https://pypi.python.org/pypi/emaildata/ "View emaildata in pypi")
is a python package for extracting content from email messages. It is
a fork of the [emailcontent](https://pypi.python.org/pypi/emailcontent/ "View emailcontent in pypi")
package but adds from features.

## emaildata features

[emaildata](https://pypi.python.org/pypi/emaildata/ "View emaildata in pypi")
extracts this types of contents from emails:

* Extract metadata.
* Extract text (plain text and html).
* Extract attachements.

## Extracting metadata

This feature was included from the *metadata* module of the 
[emailcontent](https://pypi.python.org/pypi/emailcontent/ "View emailcontent in pypi"). This module was
copied module, few methods of is *MetaData* class were removed, and the module was made more pylint friendly.

To extract metadata from an email message headers you create an instance of the *MetaData* class
passing a message to the constructor. You can retrieve the metadata with the method *to_dict*.
This can also be done using the method *set_message*:

```
#!python

import email
from emailcontent.metadata import MetaData

message = email.message_from_file(open('message.eml'))
extractor = MetaData(message)
data = extractor.to_dict()
print data.keys()

message2 = email.message_from_file(open('message2.eml'))
extractor.set_message(message2)
data2 = extractor.to_dict()
```

## Extracting text

Comming soon...

## Extracting attachements

Comming soon...

## Changelog

### Version 0.1 (2015-03-15)

* Initial version.
* Support for metadata extraction.
