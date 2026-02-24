from .notificator_interface import NotificatorInterface

class NotificationEmail(NotificatorInterface):
     def send_notification(self, message: str) -> None:
          print(f"sending email: {message}")