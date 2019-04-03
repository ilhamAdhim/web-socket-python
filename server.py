import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)

slot = 1000

@sio.on('connect')
def connect(sid, environ):
	print('new client connected ', sid)

@sio.on('trigger_gate')
def trigger_gate(sid, isEnter):
	global slot
	print('is car enter ? ' , isEnter)
	if (isEnter):
		slot = slot - 1
	else:
		slot = slot + 1

	sio.emit("change_slot", slot)


@sio.on('disconnect')
def disconnect(sid):
	print('client disconnect ', sid)

if __name__ == '__main__':
	eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
