from django.shortcuts import render

import base64
import uuid
from django.core.files.base import ContentFile
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime
from jaundice_api.models import Newborn, ImageModel

# Create your views here.


@api_view(['POST'])
def saveData(request):
    data = request.data

    try: 
        dateOfBirth = data.get('dateOfBirth')
        timeOfBirth = data.get('timeOfBirth')
        birthWeight = data.get('birthWeight')
        gender = data.get('gender')
        fSkinTone = data.get('fSkinTone')
        mSkinTone = data.get('mSkinTone')
        kramer = data.get('kramer')
        jaundice = data.get('jaundice')
        bilirubin = data.get('bilirubin')
        foreheads = data.get('foreheads')
        device = data.get('device')

        dateOfBirth = datetime.strptime(dateOfBirth, '%Y-%m-%d').date()
        timeOfBirth = datetime.strptime(timeOfBirth, '%H:%M').time()

        newborn = Newborn.objects.create(
            dateOfBirth=dateOfBirth,
            timeOfBirth=timeOfBirth,
            birthWeight=birthWeight,
            gender=gender,
            fSkinTone=fSkinTone,
            mSkinTone=mSkinTone,
            kramer=kramer,
            jaundice=jaundice,
            bilirubin=bilirubin,
            device=device
        )

        for f in foreheads:
            img_data = base64.b64decode(f.encode())

            # Save image to model
            image = ImageModel.objects.create()
            image.img.save(f"{uuid.uuid4()}.jpg", ContentFile(img_data))
            newborn.foreheads.add(image)

        newborn.save()
        return Response("Successfully saved.", status=status.HTTP_201_CREATED)

    except Exception as err:
        return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)

