from rest_framework import serializers
from .errors import check_date
from .models import Event, Form, Data

class FormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Form
        fields = ['first_name', 'last_name']

    def create(self, validated_data):
        form = None
        for i in validated_data:
            first_name = i['first_name']
            last_name = i['last_name']
            data = i['data']
            form = Form.objects.create(first_name=first_name, last_name=last_name, data=data)
        return form



class DataSerializerAll(serializers.ModelSerializer):
    form = FormSerializer(many=True)
    class Meta:
        model = Data
        fields = ['host', 'path', 'element', 'form']

class DataSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['host', 'path']

    def create(self, validated_data):
        host = validated_data.get('host')
        path = validated_data.get('path')
        event = validated_data.get('event')
        return Data.objects.create(host=host, path=path, event=event)


class DataSerializerForm(serializers.ModelSerializer):
    form = FormSerializer(many=True)
    class Meta:
        model = Data
        fields = ['host', 'path', 'form']


class DataSerializerElement(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ['host', 'path', 'element']

    def create(self, validated_data):
        host = validated_data.get('host')
        path = validated_data.get('path')
        element = validated_data.get('element')
        event = validated_data.get('event')
        return Data.objects.create(host=host, path=path, element=element, event=event)

class EventSerializerAll(serializers.ModelSerializer):
    data = DataSerializerAll(many=True)
    class Meta:
        model = Event
        fields = ['id', 'session_id', 'category', 'name', 'data', 'timestamp']


class EventSerializer(serializers.ModelSerializer):
    data = DataSerializer2(many=True)

    class Meta:
        model = Event
        fields = ['session_id', 'category', 'name', 'data', 'timestamp']


    def create(self, validated_data):
        session_id = validated_data.get('session_id')
        category = validated_data.get('category')
        name = validated_data.get('name')
        timestamp = validated_data.get('timestamp')
        check_date(timestamp)
        event = Event.objects.create(session_id=session_id, category=category, name=name, timestamp=timestamp)
        datas = validated_data.get('data')
        host = datas[0]['host']
        path = datas[0]['path']
        data = Data.objects.create(host=host, path=path, event=event)

        return event

class EventElementSerializer(serializers.ModelSerializer):
    data = DataSerializerElement(many=True)

    class Meta:
        model = Event
        fields = ['session_id', 'category', 'name', 'data', 'timestamp']


    def create(self, validated_data):
        session_id = validated_data.get('session_id')
        category = validated_data.get('category')
        name = validated_data.get('name')
        timestamp = validated_data.get('timestamp')
        check_date(timestamp)
        event = Event.objects.create(session_id=session_id, category=category, name=name, timestamp=timestamp)
        datas = validated_data.get('data')
        host = datas[0]['host']
        path = datas[0]['path']
        element = datas[0]['element']
        data = Data.objects.create(host=host, path=path, element=element, event=event)

        return event

class EventFormSerializer(serializers.ModelSerializer):
    data = DataSerializerForm(many=True)

    class Meta:
        model = Event
        fields = ['session_id', 'category', 'name', 'data', 'timestamp']


    def create(self, validated_data):
        session_id = validated_data.get('session_id')
        category = validated_data.get('category')
        name = validated_data.get('name')
        timestamp = validated_data.get('timestamp')
        check_date(timestamp)
        event = Event.objects.create(session_id=session_id, category=category, name=name, timestamp=timestamp)
        datas = validated_data.get('data')
        host = datas[0]['host']
        path = datas[0]['path']
        forms = datas[0]['form']
        first_name = forms[0]['first_name']
        last_name = forms[0]['last_name']
        data = Data.objects.create(host=host, path=path, event=event)
        form = Form.objects.create(first_name=first_name, last_name=last_name, data=data)

        return event
