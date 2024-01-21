from celery import shared_task

from habits.management.commands.send_message import Command


@shared_task
def start_mailing():
    Command.handle(Command())
