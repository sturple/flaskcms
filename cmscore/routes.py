class CmsRouter(object):
  def __init__(self):
    ''' Init '''
    self.data = {
      'app': {},
      'plugins': {}
    }
    #print(self.data)
  
  def activate(self, app, plugins):
    self.data['app'] = app
    self.data['plugins'] = plugins
    self.data['app'].add_url_rule('/', "index", self.index )

  def deactivate(self):
    pass
    
  def index(self):
    return 'Home page from the router'

def register():
  return CmsRouter()






