from Common.DTOs.EventDTO import EventDTO


class NotifierBL:
    @staticmethod
    def notify(event: EventDTO):
        print(f'your event: {event.title} is starting at: {event.date}. \n'
              f'prepare yourself ;)')
