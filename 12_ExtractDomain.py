def domain_name(url):
    i = url.find("www.")
    if i != -1:
        url_new = url[i+4:]
    else:
        i = url.find("://")
        if i != -1:
            url_new = url[i+3:]
        else:
            url_new = url[0:]
    domain = url_new.split(".")
    return domain[0]

# return url.split("//")[-1].split("www.")[-1].split(".")[0]

import codewars_test as test
test.assert_equals(domain_name("http://google.com"), "google")
test.assert_equals(domain_name("http://google.co.jp"), "google")
test.assert_equals(domain_name("www.xakep.ru"), "xakep")
test.assert_equals(domain_name("https://youtube.com"), "youtube")