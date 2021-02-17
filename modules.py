from ContextScreen import Clue, ContextScreen
import abc, time
import pyautogui as auto

class Module(abc.ABC):
    @abc.abstractmethod
    def run():
        pass
    
class ContinueAutoSearch(Module):
    def __init__(self):
        pass

    def run(self):
        c1 = Clue((811, 274))
        c2 = Clue((599, 817))
        c3 = Clue((1268, 819))
        stageClear = ContextScreen("Autosearch stage clear", [c1, c2, c3])
        
        while True:
            screen = auto.screenshot()
            print(screen.getpixel((1214, 781)))
            if stageClear.match(screen):
                print('wow')
                auto.leftClick(1250, 790)
            else:
                print("Sadge")
            time.sleep(10)

if __name__ == "__main__":
    test = ContinueAutoSearch()
    test.run()