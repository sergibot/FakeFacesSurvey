from django.core.management.base import BaseCommand, CommandError
from surveyapp.models import Image

class Command(BaseCommand):
    help = 'Fills database with relevant images'

    def _input_imgs(self):
        for i in range(1,101):
            if not Image.objects.filter(image_id="image"+str(i), filename="person("+str(i)+").jpg").exists():
                image = Image(image_id="image"+str(i),
                              filename="person("+str(i)+").jpg")
                image.save()
        print(Image.objects.all())


    def handle(self, *args, **options):
        self._input_imgs()


