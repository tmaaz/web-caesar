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

class MainHandler(webapp2.RequestHandler):

    def get(self):
        up_content = '''
            <html>
            <head><title>STLCC - LC101 - Web Caesar</title></head>
            <body>
            <h2>Please enter some text for conversion:</h2>
        '''
        text_content_start = '<textarea name="content" style="height: 125px; width: 350px;">'
        text_content_end = '</textarea><br />'
        code_content = '''
            <h5>Please enter your encryption code:</h5>
            <input type="text" name="code" />
            <br />
        '''
        button_content = '<input type="submit" value="Submit" />'
        down_content = '</body></html>'
        form_start = '<form method="post">'
        form_end = '</form>'
        form = form_start + text_content_start + text_content_end + code_content + button_content + form_end
        raw_content = up_content + form + down_content

        self.response.write(raw_content)


    def post(self):
        enc_content = caesar.encrypt(self.request.get("content"), self.request.get("code"))
        up_content = '''
            <html>
            <head><title>STLCC - LC101 - Web Caesar</title></head>
            <body>
            <h2>Please enter some text for conversion:</h2>
        '''
        text_content_start = '<textarea name="content" style="height: 125px; width: 350px;">'
        text_content_end = '</textarea><br />'
        code_content = '''
            <h5>Please enter your encryption code:</h5>
            <input type="text" name="code" />
            <br />
        '''
        button_content = '<input type="submit" value="Submit" />'
        down_content = '</body></html>'
        form_start = '<form method="post">'
        form_end = '</form>'
        form = form_start + text_content_start + enc_content + text_content_end + code_content + button_content + form_end
        encrypted_content = up_content + form + down_content

        self.response.write(encrypted_content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
