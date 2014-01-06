from bs4 import BeautifulSoup
import urllib2

urls = [
    ["http://www.healthcentral.com/rheumatoid-arthritis/c/499724/162236/pt-experience/",
     "http://www.healthcentral.com/schizophrenia/c/120/162330/schizophrenia-august/"], ]


html_header = """
<!DOCTYPE html>
<html>
<body>
"""

html_footer = """
</body>
</html>
"""

html_1 = "<p><font size = '3' color = 'red'>"
html_2 = "</font></p>"

for url in urls:
    print url
    cdata_list = []

    for env in url:

        try:

            page = urllib2.urlopen(env)
            soup = BeautifulSoup(page.read())
            text = soup.script
        except:
            f1 = open("results.html", "a")
            url_error = "Error opening URL %s" % env + "\n"
            html_1 = "<p><font size = '3' color = '#880000'>"
            html_2 = "</font></p>"
            f1.write(html_header + "\n")
            f1.write(html_1 + url_error + html_2 + "\n")
            f1.write(html_footer)
            f1.close()

        cdata_list.append(text)

        for i in range(len(cdata_list) - 1):
            if cdata_list[i] in cdata_list[i + 1]:
                """write results file with errors only"""
                #cdata = "%s and %s" % (cdata_list[i], cdata_list[i + 1])
                #result = "match found. all ok for %s and %s"
                cdata = "OK"
                result = "OK"
            elif cdata_list[i] == cdata_list[i + 1]:
                """write results file with errors only"""
                #result = "match found. all ok for %s and %s"
                #% (cdata_list[i], cdata_list[i + 1])
                cdata = "OK"
                result = "OK"
            else:
                #result = "ERROR!!! no match for %s and %s"
                #% (cdata_list[i], cdata_list[i + 1])
                cdata = "%s %s" % (cdata_list[i], cdata_list[i + 1]) + "\n"
                result = "ERROR for env %s" % url

                f = open("results.html", "a")
                f.write(html_header + "\n")
                f.write(html_1 + result + html_2)
                f.write(html_1 + cdata + html_2)
                f.write(html_footer)
                f.close()

        #f1 = open("results.html", "a")
        #url_error = "Error opening URL %s" % env + "\n"
        #html_1 = "<p><font size = '3' color = '#880000'>"
        #html_2 = "</font></p>"
        #f1.write(html_header + "\n")
        #f1.write(html_1 + url_error + html_2 + "\n")
        #f1.write(html_footer)
        #f1.close()
