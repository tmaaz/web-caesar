#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar

def pageSetup(enc_content):
    up_content = '''
        <html>
        <head><title>STLCC - LC101 - Web Caesar</title></head>
        <body>
        <h2>Web Caesar - STLCC LC101</h2>
        <strong>Please enter some text for conversion:</strong><br />
    '''
    text_content = '<textarea name="content" style="height: 125px; width: 350px;">' + enc_content + '</textarea><br />'
    code_content = '''
        <br /><strong>Please enter your encryption code:</strong><br />
        <input type="number" name="code" />
        <br />
    '''
    button_content = '<br /><input type="submit" value="Submit" />'
    down_content = '</body></html>'
    form_start = '<form method="post">'
    form_end = '</form>'
    form = form_start + text_content + code_content + button_content + form_end
    form_content = up_content + form + down_content

    return form_content


class MainHandler(webapp2.RequestHandler):

    def get(self):
        the_content = pageSetup("")
        self.response.write(the_content)


    def post(self):
        enc_content = caesar.encrypt(self.request.get("content"), self.request.get("code"))
        the_content = pageSetup(enc_content)
        self.response.write(the_content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
