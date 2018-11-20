# userEvents
# in your Tkinter program, you'll configure the specific events that you
# want your program to listen for and respond to. For each event, you need to
# define a handler method to respond to the event.

# When you call the main loop funciton of your top-level Tk object, the
# program enters what is known as the event loop. The program waits here until
# it receives a notice from the OS that an event has occurred.
# It is important to keep in mind when writing handler functions that the
# event loop is not abel to handle multiple events at the same time, it must handle
# them in the order it receives them. It handles one event, then returns to the
# main loop and then handles any events that have been queued in the interim.
# So, main loop --> handle event --> main loop --> handle event --> etc

# It's good to keep your handler code short and efficient to that user will not
# have to wait for your GUI to respond to events-- you don't want a backlog of
# user triggered events sitting in the queue.



