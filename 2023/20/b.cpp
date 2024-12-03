
from collections import deque
import re

LOW_PULSE = 0
HIGH_PULSE = 1

class BroadcastModule():
    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.has_broadcast = True
        self.sent_count = False
        self.repeat_pulse = LOW_PULSE

    def addSubscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def getSubscribers(self):
        return self.subscribers
    
    def hasBroadcast(self):
        return self.has_broadcast

    def receiveBroadcast(self, _, pulse):
        self.repeat_pulse = pulse

    def broadcast(self):
        return self.repeat_pulse

class FlipFlopModule():
    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.has_broadcast = True
        self.sent_count = False
        self.is_on = False

    def addSubscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def getSubscribers(self):
        return self.subscribers
    
    def hasBroadcast(self):
        return self.has_broadcast

    def receiveBroadcast(self, _, pulse):
        if pulse == LOW_PULSE:
            self.is_on = not self.is_on
            self.has_broadcast = True
        else:
            self.has_broadcast = False

    def broadcast(self):
        return HIGH_PULSE if self.is_on else LOW_PULSE

class ConjunctionModule():
    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.has_broadcast = True
        self.sent_count = False
        self.subscribed_to = {}

    def addSubscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def getSubscribers(self):
        return self.subscribers
    
    def hasBroadcast(self):
        return self.has_broadcast

    def addWatch(self, module):
        self.subscribed_to[module] = LOW_PULSE

    def receiveBroadcast(self, origin, pulse):
        self.subscribed_to[origin] = pulse

    def broadcast(self):
        self.sent_count = False
        if all([p == HIGH_PULSE for p in self.subscribed_to.values()]):
            if self.name == 'kz':
                self.sent_count = True
            return LOW_PULSE
        else:
            return HIGH_PULSE

class ModuleManager():
    def __init__(self):
        self.broadcast_module = None
        self.modules = {}
        self.queue = deque()

    def getModule(self, name):
        return self.modules.get(name, None)

    def createBroadcastModule(self, name):
        self.broadcast_module = BroadcastModule(name)
        self.modules[name] = self.broadcast_module

    def createFlipFlopModule(self, name):
        self.modules[name] = FlipFlopModule(name)

    def createConjunctionModule(self, name):
        self.modules[name] = ConjunctionModule(name)

    def pressButton(self):
        self.queue.append((None, LOW_PULSE, self.broadcast_module))

        rx_count = 0
        while self.queue:
            origin_module, input_pulse, receiving_module = self.queue.popleft()
            receiving_module.receiveBroadcast(origin_module, input_pulse)
            if receiving_module.hasBroadcast():
                output_pulse = receiving_module.broadcast()
                if receiving_module.sent_count:
                    rx_count += 1
                for sub in receiving_module.getSubscribers():
                    self.queue.append((receiving_module, output_pulse, sub))
        return rx_count

def createStateModuleManager(filename):
    modules_to_process = []
    with open(filename, "r") as f:
        for line in f:
            modules_to_process.append(re.search(r"(%|&)?(\w+) -> ([\w\s,]+)", line.strip()).groups())
    
    manager = ModuleManager()
    for mod_type, mod_name, _ in modules_to_process:
        if mod_type == "%":
            manager.createFlipFlopModule(mod_name)
        elif mod_type == "&":
            manager.createConjunctionModule(mod_name)
        else:
            manager.createBroadcastModule(mod_name)

    for mod_type, mod_name, subscribers in modules_to_process:
        curr_module = manager.getModule(mod_name)
        for subscriber in subscribers.split(", "):
            subscriber_module = manager.getModule(subscriber)
            if subscriber_module:
                curr_module.addSubscriber(subscriber_module)
                if isinstance(subscriber_module, ConjunctionModule):
                    subscriber_module.addWatch(curr_module)

    return manager

def printRed(text):
    print("\033[91m%s\033[00m"%text)

def generateSolution(filename):
    manager = createStateModuleManager(filename)
    last = manager.pressButton()
    count = 1
    while last != 1:
        if count % 1000000 == 0:
            print("Curr: %d" % count)
        count += 1
        if last > 0:
            printRed("Count at btn press: %d %d" % (count, last))
        last = manager.pressButton()
    return count
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))