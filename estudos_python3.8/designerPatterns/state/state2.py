from __future__ import annotations
from abc import ABC, abstractmethod




class Sound:
    def __init__(self):
        self.mode: PlayMode = RadioMode()
        self.playing = 0



class PlayMode(ABC):
    def __init__(self, sound: Sound) -> None:
        self.sound = sound

    @abstractmethod
    def press_next(self) -> None: pass 

    @abstractmethod
    def press_prev(self) -> None: pass 
    





class RadioMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1000

    def press_prev(self) -> None: 
        self.sound.playing += 1000 if self.sound.playing > 0 else 0

