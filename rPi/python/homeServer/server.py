#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET
from light_start import light_start

urls = (
    '/light/start/<employee_id>', 'light_start',
    '/light/stop', 'light_stop'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()