"""
.. module:: pfam_qaqc
   :synopsis: A useful module indeed.
"""

import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import cgitb
cgitb.enable()
from uber import uber_lib

class pfamQaqcPage(webapp.RequestHandler):
    def get(self):
        templatepath = os.path.dirname(__file__) + '/../templates/'
        ChkCookie = self.request.cookies.get("ubercookie")
        html = uber_lib.SkinChk(ChkCookie, "PFAM QA/QC")
        html = html + template.render(templatepath + '02uberintroblock_wmodellinks.html', {
                'site_skin' : os.environ['SITE_SKIN'],
                'model':'pfam',
                'page':'qaqc',})
        html = html + template.render (templatepath + '03ubertext_links_left.html', {})                
        html = html + template.render(templatepath + '04uberinput_start.html', {
                'model':'pfam',
                'model_attributes':'PFAM QAQC'})
#        html = html =
        html = html + template.render(templatepath + '04uberinput_end.html', {'sub_title': ''})
        html = html + template.render(templatepath + '05ubertext_links_right.html', {})
        html = html + template.render(templatepath + '06uberfooter.html', {'links': ''})
        self.response.out.write(html)

app = webapp.WSGIApplication([('/.*', pfamQaqcPage)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()
