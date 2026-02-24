from .notificator_interface import NotificatorInterface

class NotificationSms(NotificatorInterface):
     def send_notification(self, message: str) -> None:
          print(f"sending email: {message}")