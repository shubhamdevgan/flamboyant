Django toast messages
=====================

Link to repository: https://github.com/Arpaso/toastmessage

Provides django template tag for displaying toast message for 10 seconds after window load.

Usage
=====

**template.html**::

    <link rel="stylesheet" href="{{ STATIC_URL }}css/jquery.toastmessage.css">

    <script src="{{ STATIC_URL }}/js/jquery.toastmessage.js"></script>
    <script type="text/javascript">
        $().toastmessage('showSuccessToast', "Hello there! Message is shown.");
    </script>
    {% include "toastmessages_fragment.html" %}



Written by the development team of Arpaso company: http://arpaso.com

Regards to
~~~~~~~~~~

jQuery-powered sexy floating messages - http://akquinet.github.com/jquery-toastmessage-plugin/

