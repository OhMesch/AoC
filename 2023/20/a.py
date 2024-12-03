from abc import ABC, abstractmethod
from collections import deque
from enum import Enum
import re

class Pulse(Enum):
    LOW = 0
    HIGH = 1

class Module(ABC):
    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.has_broadcast = True

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

class ConjunctionModule(Module):
    def __init__(self, name):
        super().__init__(name)
        self.subscribed_to = {}

    def addWatch(self, module):
        self.subscribed_to[module] = Pulse.LOW

    def receiveBroadcast(self, origin, pulse):
        self.subscribed_to[origin] = pulse

    def broadcast(self):
        if all([p == Pulse.HIGH for p in self.subscribed_to.values()]):
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

        self.l_count = 0
        self.h_count = 0

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
        print()
        print(f"Button pressed")
        print(f"button -> Pulse.LOW -> {self.broadcast_module.name}")
        # self.broadcast_module.receiveBroadcast(None, Pulse.LOW)
        self.queue.append((None, Pulse.LOW, self.broadcast_module))

        while self.queue:
            origin_module, input_pulse, receiving_module = self.queue.popleft()
            receiving_module.receiveBroadcast(origin_module, input_pulse)
            if receiving_module.hasBroadcast():
                output_pulse = receiving_module.broadcast()
                if not receiving_module.getSubscribers():
                    if output_pulse == Pulse.LOW:
                        self.l_count += 1
                    else:
                        self.h_count += 1
                for sub in receiving_module.getSubscribers():
                    print(f"{receiving_module.name} -> {output_pulse} -> {sub.name}")
                    self.queue.append((receiving_module, output_pulse, sub))
            else:
                print(f"{receiving_module.name} -> NO BROADCAST")
            if input_pulse == Pulse.LOW:
                self.l_count += 1
            else:
                self.h_count += 1

    def getPulseCount(self):
        return self.l_count*self.h_count

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

def generateSolution(filename):
    manager = createStateModuleManager(filename)
    for _ in range(1000):
        manager.pressButton()
    return manager.getPulseCount()
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))