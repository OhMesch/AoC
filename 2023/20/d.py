from abc import ABC, abstractmethod
from collections import deque
from enum import Enum
import re

from math import lcm

COUNT = 0

class Pulse(Enum):
    LOW = 0
    HIGH = 1

class Module(ABC):
    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.has_broadcast = True
        self.sent_count = False

    def addSubscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def getSubscribers(self):
        return self.subscribers
    
    def hasBroadcast(self):
        return self.has_broadcast
    
    def __repr__(self) -> str:
        return f"{type(self)}: {self.name} -> {[s.name for s in self.subscribers]}"

    @abstractmethod
    def receiveBroadcast(self, origin, pulse):
        pass

    @abstractmethod
    def broadcast(self):
        pass

class BroadcastModule(Module):
    def __init__(self, name):
        super().__init__(name)
        self.repeat_pulse = Pulse.LOW

    def receiveBroadcast(self, _, pulse):
        self.repeat_pulse = pulse

    def broadcast(self):
        return self.repeat_pulse

class FlipFlopModule(Module):
    def __init__(self, name):
        super().__init__(name)
        self.is_on = False

    def receiveBroadcast(self, _, pulse):
        if pulse == Pulse.LOW:
            self.is_on = not self.is_on
            self.has_broadcast = True
        else:
            self.has_broadcast = False

    def broadcast(self):
        return Pulse.HIGH if self.is_on else Pulse.LOW

def printGreen(text):
    print(f"\033[92m{text}\033[00m")

class ConjunctionModule(Module):
    def __init__(self, name):
        super().__init__(name)
        self.subscribed_to = {}
        self.watching = {}

    def addWatch(self, module):
        self.subscribed_to[module] = Pulse.LOW

    def receiveBroadcast(self, origin, pulse):
        global COUNT
        if self.name == "kz" and pulse == Pulse.HIGH:
            if origin not in self.watching:
                self.watching[origin] = COUNT
            if all([k in self.watching for k in self.subscribed_to.keys()]):
                print()
                print(self.watching)
                print(lcm(*self.watching.values()))
                exit()
            printGreen(f"KZ received from {origin.name} at count {COUNT}")
        self.subscribed_to[origin] = pulse

    def broadcast(self):
        self.sent_count = False
        if all([p == Pulse.HIGH for p in self.subscribed_to.values()]):
            if self.name == 'kz':
                self.sent_count = True
            return Pulse.LOW
        else:
            return Pulse.HIGH
        
    def __repr__(self) -> str:
        base_str = super().__repr__()
        return f"{base_str} Watching: {[s.name for s in self.subscribed_to.keys()]}"

class ModuleManager():
    def __init__(self):
        self.broadcast_module = None
        self.modules = {}
        self.queue = deque()

    def getModule(self, name):
        return self.modules.get(name, None)
    
    def printModules(self):
        for mod in self.modules.values():
            print(mod)

    def createBroadcastModule(self, name):
        self.broadcast_module = BroadcastModule(name)
        self.modules[name] = self.broadcast_module

    def createFlipFlopModule(self, name):
        self.modules[name] = FlipFlopModule(name)

    def createConjunctionModule(self, name):
        self.modules[name] = ConjunctionModule(name)

    def pressButton(self):
        global COUNT
        COUNT += 1
        # print()
        # print(f"Button pressed")
        # print(f"button -> Pulse.LOW -> {self.broadcast_module.name}")
        self.queue.append((None, Pulse.LOW, self.broadcast_module))

        rx_count = 0
        while self.queue:
            origin_module, input_pulse, receiving_module = self.queue.popleft()
            receiving_module.receiveBroadcast(origin_module, input_pulse)
            if receiving_module.hasBroadcast():
                output_pulse = receiving_module.broadcast()
                if receiving_module.sent_count:
                    rx_count += 1
                for sub in receiving_module.getSubscribers():
                    # print(f"{receiving_module.name} -> {output_pulse} -> {sub.name}")
                    self.queue.append((receiving_module, output_pulse, sub))
            else:
                pass
                # print(f"{receiving_module.name} -> NO BROADCAST")
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

    print()
    manager.printModules()

    return manager

def printRed(text):
    print(f"\033[91m{text}\033[00m")

def generateSolution(filename):
    manager = createStateModuleManager(filename)
    last = manager.pressButton()
    count = 1
    while last != 1:
        if count % 100000 == 0:
            print(f"Curr: {count}")
        count += 1
        if last > 0:
            printRed(f"Count at btn press: {last} {count}")
        last = manager.pressButton()
    return count
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))