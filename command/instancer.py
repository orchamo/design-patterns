from invokers.Invoker import Invoker
from commands.LightOnCommand import LightOnCommand


invoker = Invoker(LightOnCommand())

invoker.click()
invoker.click_again()