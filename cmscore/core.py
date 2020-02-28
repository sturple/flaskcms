class CmsCore(object):
  def __init__(self):
    ''' Init '''
    self.data = {
      'app': {},
      'plugins': {},
      'add_action': {}
    }
    #print(self.data)
  
  def activate(self, app, plugins):
    self.data['app'] = app
    self.data['plugins'] = plugins

  def deactivate(self):
    pass

  def do_action(self, name, *a, **kwg):
    ''' hooks do_action if no hook, then do defaults or do nothing used with add_action.'''
    found = False
    for key, items in self.data.get('add_action', {}).items():
        if key == name:
            items.sort(key=lambda x: x[0])
            output = []
            for order, action in items:
                found = True
                output.append(action(*a, **kwg))
            return output
    if found == False and kwg.get('default', False):
        default_call = kwg.get('default')
        return default_call(*a, **kwg)

  def add_action(self, name, fnct, order=10):
    ''' used to register add_action, when a do_fucntion is called, it will cycle through the add_action for matches '''
    if self.data.get('add_action').get(name) == None:
        self.data['add_action'][name] =  [(order,fnct)]
    else:
        self.data['add_action'][name].append((order,fnct))

  def logger(self, *msgs, **kw):
    ''' default logger, if no logger plugin is used '''
    for msg in msgs:
        print(msg)



def register():
  return CmsCore()
