class FishingPlugin(object):
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

  def deactivate(self):
    pass

  def test(self): 
    return 'hello world from fishing test'

def register():
  return FishingPlugin()

