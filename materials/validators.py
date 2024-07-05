from rest_framework import serializers


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if 'https://www.youtube.com/' not in tmp_val:
            raise serializers.ValidationError('All the materials have to be videos from youtube')
