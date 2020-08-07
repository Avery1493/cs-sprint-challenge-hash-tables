#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        # link tickets
        self.next = None


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # place each ticket in cache with next
    cache = {}
    for ticket in tickets:
        ticket.next = ticket.destination
        cache[ticket.source] = ticket.next
    
    route = []
    # loop list
    current = cache["NONE"]
    # append to route list
    for i in range(length):
        # append route
        route.append(current)
        # increment next
        current = cache[current]

    # return route
    return route

if __name__ == "__main__":
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")

    tickets = [ticket_1, ticket_2, ticket_3]

    print(reconstruct_trip(tickets, 3))
