import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stratos.settings')

import django
django.setup()

# Fake populate script
import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topics():
        t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
        t.save()
        return t

def populate(N = 5):
        for entry in range(N):

                # get the topic for the entry
                top = add_topics()

                # Create the fake data for the entry
                fake_url = fakegen.url()
                fake_date = fakegen.date()
                fake_name = fakegen.company()

                # Create the new webpage entry
                webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

                # Create a fake access record for that webpage
                acc_res = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == "__main__":
        print('Populating script')
        populate(N=4)
        print('Populating done')