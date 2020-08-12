import threading
import psutil
import time
import schedule
import asyncio
import base64
from asyncio import Future
import struct
from rx import interval
from apscheduler.schedulers.background import BackgroundScheduler

class Nutella(threading.Thread):

    def __init__(self):
        p = psutil.Process()
        loop = asyncio.new_event_loop()

        async def _action(self, controller: str, action: str, args=None, lock=True, allow_in_shutdown=False):
            print("test2")

        def job_action_threadsafe(self, action: str, args=None) -> Future:
            print("test")
            if args is None: args = []
            return asyncio.run_coroutine_threadsafe(_action('job', action, args),loop)

        def on_hardware_metrics(dummy):
            net = psutil.net_io_counters()
            disk = psutil.disk_io_counters()
            data = struct.pack(
                '<BHdHHffff',
                1,
                0,
                time.time(),
                # stretch to max precision of uint16
                min(65535, int(((p.cpu_percent(interval=None) / 100) / psutil.cpu_count(False)) * 65535)),
                # stretch to max precision of uint16
                min(65535, int((p.memory_percent() / 100) * 65535)),
                float(net.bytes_recv),
                float(net.bytes_sent),
                float(disk.write_bytes),
                float(disk.read_bytes),
            )

            job_action_threadsafe('nutellaController',
                                              ['test',
                                               base64.b64encode(data).decode('utf8')])

        self.hardware_subscription = interval(1).subscribe(on_hardware_metrics)
        loop.run_forever()
        print("test7")



    def init(self,modelName=None, projectKey=None, reinit=False):

        self.projectKey=projectKey
        self.modelName=modelName
        self.reinit=reinit


    #def config(self,**configData):
       # self.epochs=epochs
    # self.batchSize=batchSize

   # def log(self,**logData):

a=Nutella()





