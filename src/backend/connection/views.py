from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.authentication import TokenAuthentication

from account.models import Student
from account.LISTS import *
from account.serializer import StudentSerializer
from api.serializers import *
from .models import *
from .helpers import redis_get_student

import random
import ujson
import time
import redis

# from numba import jit
from multiprocessing import Pool


# Create your views here.

class GetInfo(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        start_time = time.time()

        r = redis.Redis("132.249.242.203")
        pipe = r.pipeline()

        if (request.user.is_authenticated):
            print("--- %s seconds ---" % (time.time() - start_time))
            #
            return Response(redis_get_student(r, pipe, request.user.id))
        else:
            return Response({})


# 地図: AddKarmaView API
class AddKarmaView(APIView):
    def post(self, request):
        request_content = ujson.loads(request.body)

<<<<<<< HEAD
        # print("**\nAddKarmaView has been called\n")

        # Get the user id so we can use to find the User object 
        request_user_id = request_content["user_id"]
        # print("request user id:")
        # print(request_content["user_id"])

        # Find Student with specified request_user_id
        temp = Student.objects.get(id=request.user.id)

        # print("test to see if we got the right user, user_college:")
        # print(temp.user_college)

        # print("user_karma before set:")
        # print(temp.user_karma)
        # print("\n")

        # Call set_karma and pass in amnt of karma to be added
        temp.set_karma(request_content['add_karma'])
        # print("user_karma after set: ")
        # print(temp.user_karma)
        # print("\n")

        temp.save()

        # print("**\n")

=======
        # Get the user id so we can use to find the User object
        request_user_id = request_content.get("user_id")

        #Find Student with specified request_user_id
        temp = Student.objects.get(id=request_user_id)

        #Call set_karma and pass in amnt of karma to be added
        temp.set_karma(request_content.get("add_karma"))

        temp.save()

>>>>>>> b2ee87c8853691d27dca6e0085b7b5a3b324f0c0
        return Response({})


# Placeholder before we have a real matching algo


'''
    Tons of room for optimization, but will do for now.
'''

'''
    GET: Fetches all Matching that has been sent out.
'''


class MatchingSentView(APIView):
    # print("MatchingSentView has been called");

    authentication_classes = [TokenAuthentication]

    def get(self, request):
        start_time = time.time()
        matching_sent = list(PendingMatching.objects.filter(id_sender=request.user.id))

        toReturn = []
<<<<<<< HEAD
        r = redis.Redis("132.249.242.203")
        pipe = r.pipeline()

=======
>>>>>>> b2ee87c8853691d27dca6e0085b7b5a3b324f0c0
        for i in matching_sent:
            # No longer needed now that we have Student as wrapper model
            # temp = helpers.conn_wrapper(User.objects.get(pk=i.id_receiver), Student.objects.get(pk=i.id_receiver))

<<<<<<< HEAD
            temp = redis_get_student(r, pipe, i.id_receiver)
=======
            r = redis.Redis("132.249.242.203")
            temp = None

            if (not r.exists(f"student_{i.id}")):
                temp = StudentSerializer(Student.objects.get(pk=i.id_receiver)).data
                r.set(f"student_{i.id}", ujson.dumps(temp))
            else:
                temp = ujson.loads(r.get(f"student_{i.id}"))

>>>>>>> b2ee87c8853691d27dca6e0085b7b5a3b324f0c0
            temp.update({'isDenied': i.isDenied})

            toReturn.append(temp)

        pipe.execute()

        #print("--- %s seconds ---" % (time.time() - start_time))
        return Response(toReturn)


'''
    GET: Fetches all Matching that has been received.
'''


# TODO: try out multi-threading
class MatchingReceivedView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        matching_received = list(PendingMatching.objects.filter(id_receiver=request.user.id))

<<<<<<< HEAD
        r = redis.Redis("132.249.242.203")
        pipe = r.pipeline()
        toReturn = []

        for i in matching_received:
            temp = redis_get_student(r, pipe, i.id_sender)
            # temp.update({'isDenied': i.isDenied})
=======
        toReturn = []
        for i in matching_sent:
            temp = StudentSerializer(Student.objects.get(pk=i.id_sender)).data
            temp.update({'isDenied': i.isDenied})
>>>>>>> b2ee87c8853691d27dca6e0085b7b5a3b324f0c0

            toReturn.append(temp)

        pipe.execute()

        return Response(toReturn)


'''
    GET: Fetches all Matching that has been sent out.
    POST: Sends out a request for the matching generated
'''


class GenerateMatchingView(APIView):
    authentication_classes = [TokenAuthentication]

    #TO-DO: User shown before and after request do not match (match request is sent to user shown before, but a different user is shown when match is pending )
    # If front end makes a GET request to url associated to generate_match,
    # the func below executes
    def get(self, request):
        # Make sure the match is not the user itself

        print("hello from get")
        temp = generate_match(request)
        print(generate_match(request))

        # Send the information about the match back to the front end
        
        return Response(StudentSerializer(Student.objects.get(pk=temp.id)).data)

    # If front end makes a POST request to url associated to generate_match,
    # the func below executes
    def post(self, request):
        print("hello from post")
        print(request.user)

        # Extract
        request_content = ujson.loads(request.body)

        # Create a new PendingMatching object, where the sender and receivers are as specified by our input
        m = PendingMatching(
            id_sender=request.user.id,
            id_receiver=request_content.get("id_receiver"))

        # Insert the new PendingMatching object into database by calling .save()
        m.save()

        return Response({})


'''
    GET: Fetches all Matching that has been finalized.
'''


class MatchingFinalized(APIView):
    authentication_classes = [TokenAuthentication]

    # We may be able to optimize this by introducing a hashing mechanism.
    def get(self, request):
        finalized_matching = []

<<<<<<< HEAD
        r = redis.Redis("132.249.242.203")
        pipe = r.pipeline()

=======
>>>>>>> b2ee87c8853691d27dca6e0085b7b5a3b324f0c0
        temp = FinalizedMatching.objects.filter(id_user_1=request.user.id)

        # our user is either user_1 or user_2, so we go through both lists
        for i in temp:
<<<<<<< HEAD
            finalized_matching.append(redis_get_student(r, pipe, i.id_user_2))

        temp = FinalizedMatching.objects.filter(id_user_2=request.user.id)
        for i in temp:
            finalized_matching.append(redis_get_student(r, pipe, i.id_user_1))

        pipe.execute()
        return Response(finalized_matching)
=======
            finalized_matching.append(Student.objects.get(pk=i.id_user_2))

        temp = FinalizedMatching.objects.filter(id_user_2=request.user.id)
        for i in temp:
            finalized_matching.append(Student.objects.get(pk=i.id_user_1))

        toReturn = []
        for i in finalized_matching:
            toReturn.append(StudentSerializer(i).data)

        return Response(toReturn)
>>>>>>> b2ee87c8853691d27dca6e0085b7b5a3b324f0c0


'''
    POST: Modify a pending matching by either:
        1. Accepting it and pushing it to the finalized table (mode: 'y')
        2. Denying it and marking it as denied (mode: 'n')
        3. Pulling it back / removing it at the user's discretion e.g. already denied (mode: 'd')
'''


class ModifyPending(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        request_content = ujson.loads(request.body);

        #print("request_content: ")
        #print(request_content)

        # If yes, push the matching into finalized matching
        # Only receiver could make this call, so request.user.id = id_receiver
        if (request_content.get("mode") == 'y'):
            #print("_____YAY_____");
            FinalizedMatching(id_user_1=request_content.get("id_sender"),
            id_user_2=request.user.id).save()

            PendingMatching.objects.get(id_sender=request_content.get("id_sender"),
            id_receiver=request.user.id).delete()

        # If no, mark as denied. Only show to sender.
        # Only receiver could make this call, so request.user.id = id_receiver
        elif (request_content.get("mode") == 'n'):
            #print("_____NAY_____");
            p = PendingMatching.objects.get(id_sender=request_content.get("id_sender"),
            id_receiver=request.user.id)
            p.isDenied = True
            p.save()

        # Should we allow people to pullback pending matching?
        # Assuming we do, then this is visible to both sender and receiver
        # So we need to determine what request.user.id is.
        elif (request_content.get("mode") == 'd'):
            # Let front end supply only one id, and we can guess the other
            if (request_content.get("id_sender")):
                PendingMatching.objects.get(id_sender=request_content.get("id_sender"),
                id_receiver=request.user.id).delete()
            else:
                PendingMatching.objects.get(id_sender=request.user.id,
                id_receiver=request_content.get("id_receiver")).delete()

        return Response({})


# Placeholder before we have a real matching algo
# TODO: Conditions for matching
def generate_match(request):
    pending_matching = get_pending_matching_id(request)

    tot_users = Student.objects.exclude(pk__in=pending_matching)

<<<<<<< HEAD
    # for i in tot_users:
    #     print(i.id)

=======
    #for i in tot_users:
        #print(i.id)
    
>>>>>>> b2ee87c8853691d27dca6e0085b7b5a3b324f0c0
    matched_user = random.choice(tot_users)
    while (matched_user.id == request.user.id):
        matched_user = random.choice(tot_users)

    return matched_user


# Helper functions

# returns tuple of the form (matching_sent, matching_received)
def get_pending_matching(request):
    matching_sent_id = PendingMatching.objects.filter(id_sender=request.user.id)
    matching_sent = []
    for i in matching_sent_id:
        matching_sent.append(Student.objects.get(pk=i.id_receiver))

    matching_received_id = PendingMatching.objects.filter(id_receiver=request.user.id)
    matching_received = []
    for i in matching_received_id:
        matching_received.append(Student.objects.get(pk=i.id_sender))

    return matching_sent, matching_received


# returns id of all pending matching a user has
def get_pending_matching_id(request):
    temp = []

    for i in PendingMatching.objects.filter(id_sender=request.user.id):
        temp.append(i.id_receiver)

    for i in PendingMatching.objects.filter(id_receiver=request.user.id):
        temp.append(i.id_sender)

    return temp
