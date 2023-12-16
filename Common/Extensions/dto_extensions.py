from Common.DTOs.EventDTO import EventDTO
from Common.DTOs.UserDTO import UserDTO
from Common.DTOs.VenueDTO import VenueDTO
from Common.Entities.Event import Event
from Common.Entities.User import User
from Common.Entities.Venue import Venue


def event_to_dto(event: Event) -> EventDTO:
    return EventDTO(event.title, event.date,
                    event.organizer, event.guests,
                    event.location, event.venue, event.link,
                    event.notifications, event.description, event.created_on)


def user_to_dto(user: User) -> UserDTO:
    return UserDTO(user.username, user.role, user.created_on)


def venue_to_dto(venue: Venue) -> VenueDTO:
    return VenueDTO(venue.room_name, venue.notes, venue.created_on)
