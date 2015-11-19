import threading,time

class ThreadWorker():
    '''
    The basic idea is given a function create an object.
    The object can then run the function in a thread.
    It provides a wrapper to start it,check its status,and get data out the function.
    '''
    def __init__(self,func,func_on_finished=None):
        self.thread = None
        self.data = None
        self.on_finished=func_on_finished
        self.func = self.save_data(func)

    def save_data(self,func):
        '''modify function to save its returned data'''
        def new_func(*args, **kwargs):
            self.data=func(*args, **kwargs)
            if self.on_finished<>None: self.on_finished(self.data)

        return new_func

    def start(self,params):
        self.data = None
        if self.thread is not None:
            if self.thread.isAlive():
                return 'running' #could raise exception here

        #unless thread exists and is alive start or restart it
        self.thread = threading.Thread(target=self.func,args=params)
        self.thread.start()
        return 'started'

    def status(self):
        if self.thread is None:
            return 'not_started'
        else:
            if self.thread.isAlive():
                return 'running'
            else:
                return 'finished'

    def get_results(self):
        if self.thread is None:
            return 'not_started' #could return exception
        else:
            if self.thread.isAlive():
                return 'running'
            else:
                return self.data



if __name__=="__main__":
    
    def add(x,y):
        time.sleep(5)
        return x+y
    
    def then_finished(args):
        print "returned value: ",args
        
    add_worker = ThreadWorker(add,then_finished)
    print add_worker.start((1,2,))
    print add_worker.status()
    print add_worker.get_results()