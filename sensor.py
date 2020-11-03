#!/usr/bin/env python
# coding: utf-8

import json
import datetime
import random
import testdata
import boto3

client = boto3.client('firehose') 

def getData(iotName, lowVal, highVal):
   data = {}
   data["iotName"] = iotName
   data["iotValue"] = random.randint(lowVal, highVal)
   return data

while 1:
   rnd = random.random()
   if (rnd < 0.01):
      response = client.put_record(
           DeliveryStreamName='sourcestream',
           Record={
                'Data': json.dumps(getData("SensorRecord", 100, 120))
            }
        )

   else:
      response = client.put_record(
           DeliveryStreamName='sourcestream',
           Record={
                'Data': json.dumps(getData("SensorRecord", 10, 20))
            }
        )


