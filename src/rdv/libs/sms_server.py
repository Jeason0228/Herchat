
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os, requests, urllib.parse, time
# import contextlib

# class PausingObserver(Observer):
#     def __init__(self, timeout=3):
#         super().__init__(timeout=timeout)
#         # self._is_paused = False

#     def dispatch_events(self, *args, **kwargs):
#         # print(args)
#         if not getattr(self, '_is_paused', False):
#             print("self._is_paused")
#             super(PausingObserver, self).dispatch_events(*args, **kwargs)

#     def pause(self):
#         self._is_paused = True

#     def resume(self):
#         print("resume")
#         time.sleep(5)  # allow interim events to be queued
#         print(self.event_queue.queue)
#         self.event_queue.queue.clear()
#         print(self.event_queue.queue)
#         self._is_paused = False

#     # @contextlib.contextmanager
#     # def ignore_events(self):
#     #     self.pause()
#     #     yield
#     #     self.resume()

class FileModifiedHandler(FileSystemEventHandler):

    def __init__(self, path, file_name, callback):
        self.file_name = file_name
        self.callback = callback

        # set observer to watch for changes in the directory
        self.observer = Observer()
        self.path = path
        self.watch = self.observer.schedule(self, path, recursive=False)
        self.observer.start()
        self.observer.join()

    def on_modified(self, event): 
        # only act on the change that we're looking for
        if not event.is_directory and event.src_path.endswith(self.file_name):
            # self.observer.pause() # stop watching
            # self.observer.unschedule(self.watch)
            self.callback() # call callback
            # time.sleep(1)
            # self.observer.schedule(self, self.path, recursive=False)





from sys import argv, exit

if __name__ == '__main__':

    if not len(argv) == 2:
        print("No file specified")
        exit(1)

    def callback():

        print("New sms")
        with open('/Users/PENGHanyuan/Documents/Programs/Herchat/Herchat/src/rdv/assects/短信接收记录.txt', 'rb') as f:
            try:  # catch OSError in case of a one line file 
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b'\n':
                    f.seek(-2, os.SEEK_CUR)
            except OSError:
                f.seek(0)
            last_line = f.readline().decode()

        print(last_line)
        line_array = last_line.split(",")
        phone_number = urllib.parse.quote_plus(line_array[1].strip())
        port = urllib.parse.quote_plus(line_array[0].strip())
        date_time = urllib.parse.quote_plus(line_array[2].strip())
        send_number = urllib.parse.quote_plus(line_array[3].strip())
        msg = urllib.parse.quote_plus(line_array[4].strip())
        url = f"http://localhost:5000/sms_input/{phone_number}/{msg}/{date_time}/{port}"
        requests.get(url)
        # observer.resume()
        
        

    FileModifiedHandler('/Users/PENGHanyuan/Documents/Programs/Herchat/Herchat/src/rdv/assects', argv[1], callback)