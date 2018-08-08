import pusher

pusher_client = pusher.Pusher(
  app_id='387107',
  key='4f583f43cd134c7376c8',
  secret='10c23c508bdb7870c93f',
  cluster='us2',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
