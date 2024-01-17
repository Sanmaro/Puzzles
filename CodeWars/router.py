class Router(object):
    def __init__(self):
        self.urls = []
    
    def bind(self, url, method, action):
        try:
            for page in self.urls:
                if page["url"] == url and page["method"] == method:
                    page["action"] = action
        except KeyError:
            pass
        else:
            self.urls.append({"url" : url, "method": method, "action": action})
        
    def runRequest(self, url, method):
        for page in self.urls:
            if page["url"] == url and page["method"] == method: 
                return page["action"]()
        return "Error 404: Not Found"
    
router = Router()
router.bind('/login', 'GET', lambda: 'Please log-in.')
router.bind('/login', 'POST', lambda: 'Logging-in.')

print(router.runRequest('/login', 'GET'))
print(router.runRequest('/login', 'POST'))