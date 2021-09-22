from wsgiref.simple_server import make_server
import falcon
import json
import RPi.GPIO as GPIO


LEDS = {"green": 16, "red": 18}
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDS["green"], GPIO.OUT)
GPIO.setup(LEDS["red"], GPIO.OUT)


def get_led_state(led_colour):

    return json.dumps({
            'active' : GPIO.input(LEDS[led_colour]),
            })

def set_led_state(led_colour, led_new_state):

    state = {'off': 0, 'on': 1}

    if not led_new_state in state:
        return json.dumps({
            'result' : 'error - incorrect state option supplied'
        })

    else:
        GPIO.output(LEDS[led_colour], state[led_new_state])
        return json.dumps({
            'result' : 'success'
        })


class helpPageResource:

    def on_get(self, req, resp):
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = ('Hello! To interact with this API please use GET and PUT requests on:\n\n' +
                     req.url + '<led_colour>\n\n'
                     'Available colours:\n'
                     '    /green, /red\n'
                     'Available PUT operations on the above colours:\n'
                     '   Change of state: active=<on or off>'
                    )


class LedGreenResource:

    def on_get(self, req, resp):
        resp.text = get_led_state('green')

    def on_put(self, req, resp):
        change = json.loads(req.bounded_stream.read())
        resp.text = set_led_state('green', change['active'])


class LedRedResource:

    def on_get(self, req, resp):
        resp.text = get_led_state('red')

    def on_put(self, req, resp):
        change = json.loads(req.bounded_stream.read())
        resp.text = set_led_state('red', change['active'])


app       = falcon.App()
help_page = helpPageResource()
led_green = LedGreenResource()
led_red   = LedRedResource()

app.add_route('/',      help_page)
app.add_route('/green', led_green)
app.add_route('/red',   led_red  )


if __name__ == '__main__':

    with make_server('', 80, app) as httpd:

        print('Serving REST LED controller on Wormhole...')
        httpd.serve_forever()
