from django.http import HttpResponseRedirect, HttpResponse

STATE = 1


def check_state(request):
    global STATE
    state = STATE
    print("Current State is - {}".format(state))
    return HttpResponse(state)


def set_state(request, state):
    global STATE
    print("Current State: {}".format(STATE))
    print("Incoming desired state is - {} | {}".format(state, len(state)))
    if state not in ["off", "on"]:
        print("Invalid state")
        HttpResponse(500)
    if state == "off":
        print("Changing STATE to 0")
        STATE = 0
    elif state == "on":
        print("Changing STATE to 1")
        STATE = 1
    else:
        print("Undefined incoming state")
        HttpResponse(500)
    return HttpResponse(200)
